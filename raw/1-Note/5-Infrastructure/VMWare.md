# VMware 虚拟机 · DevOps 实验环境

在 VMware 虚拟机（示例网段 `192.168.5.x`）上搭建 Docker、Harbor、GitLab、Jenkins、KubeSphere / K8s、Traefik 等组件的操作笔记。

> **说明**：文件名沿用 VMWare；内容为 **Linux 虚拟机内 DevOps 部署**，非 VMware 产品手册。详细 K8s 概念见同目录 `K8s.md`。

## 目录

| 章节 | 内容 |
| --- | --- |
| [DevOps 环境搭建](#devops-环境搭建) | 网络、Docker、Compose、CA、GitLab/Harbor、语言运行时、Jenkins |
| [Kubernetes](#kubernetes-kubekey--kubesphere) | KubeKey、KubeSphere、Harbor Secret |
| [服务账号与 URL](#服务账号与-url-速查) | 控制台地址与默认账号 |
| [KpCloud](#kpcloud) | MySQL / RabbitMQ / Jenkins 源 |
| [Nginx](#nginx) | 卸载重装 |
| [Traefik](#traefik-ingress) | CRD、RBAC、DaemonSet、IngressRoute |
| [GitLab Docker 单机](#gitlab-docker-单机部署) | 容器方式安装 |

---

## DevOps 环境搭建

### 配置 IP（静态）

```bash
vi /etc/sysconfig/network-scripts/ifcfg-ens33
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=ens33
UUID=1cd9ad26-696f-40d4-8e14-dc102681372e
DEVICE=ens33
ONBOOT=yes
IPADDR=192.168.5.24
GATEWAY=192.168.5.2
NETMASK=255.255.255.0
DNS1=114.114.114.114
DNS2=8.8.8.8
```

### 系统初始化（防火墙 / SELinux / 时区）

```bash
yum install -y wget vim
yum -y install curl socat conntrack chrony

# 关闭防火墙（原笔记为 stop 后 enable；若需长期关闭请改为 disable）
sudo systemctl stop firewalld
sudo systemctl disable firewalld
sudo setenforce 0
sudo sed -i s/SELINUX=enforcing/SELINUX=disabled/g /etc/selinux/config
sudo iptables -F
# 查看SELinux的状态
getenforce
# 设置时区
timedatectl
timedatectl set-timezone Asia/Shanghai
chronyc -n sources -v
chronyc tracking
timedatectl status 

yum install unzip -y 
```

### Docker 安装

```bash
wget https://download.docker.com/linux/static/stable/x86_64/docker-20.10.8.tgz 
tar -xzvf docker-20.10.8.tgz
sudo mv docker/* /usr/local/bin/
# 设置权限
sudo groupadd docker || true
sudo usermod -aG docker $USER
#systemd
################################################
cat << EOF | sudo tee /etc/systemd/system/docker.service
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network.target

[Service]
Type=notify
ExecStart=/usr/local/bin/dockerd
ExecReload=/bin/kill -s HUP $MAINPID
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
TimeoutStartSec=0
Delegate=yes
KillMode=process
Restart=always


[Install]
WantedBy=multi-user.target
EOF





#验证
docker --version

#检查Docker服务状态：
sudo systemctl status docker
sudo systemctl start docker
#并且为了确保Docker在系统启动时自动运行  开机自动启动
sudo systemctl enable docker
sudo usermod -aG docker $USER # 添加到docker 组 

ls -l /var/run/docker.sock
srw-rw---- 1 root docker 0 Jun 22 14:58 /var/run/docker.sock
systemctl daemon-reload
sudo systemctl edit docker.service
sudo systemctl enable docker
journalctl -u docker
journalctl -xeu docker.service

```

### jenkins-docker

```bash
ubantu:
apt --fix-broken install
apt-get update
apt-get install iptables
apt-get install -y libdevmapper1.02.1
apt purge docker-ce
docker info
chmod +x /usr/sbin/policy-rc.d
vim /usr/sbin/policy-rc.d
#!/bin/sh
# For most Docker users, "apt-get install" only happens during "docker build",
# where starting services doesn't work and often fails in humorous ways. This
# prevents those failures by stopping the services from attempting to start.

exit 101

next 0 
192.168.5.24  k8sworker2.cluster.local k8sworker2
192.168.5.21  k8smaster.cluster.local k8smaster
192.168.5.24  dockerhub.kubekey.local
192.168.5.21  lb.kubesphere.local
echo "next 0" >> /usr/sbin/policy-rc.d
echo "192.168.5.24  dockerhub.kubekey.local" >> /etc/hosts
 docker login -u admin -p Harbor12345  dockerhub.kubekey.local
sudo dpkg -i containerd.io_1.4.12-1_amd64.deb
sudo dpkg -i docker-ce-cli_20.10.12~3-0~ubuntu-focal_amd64.deb
sudo dpkg -i docker-ce_20.10.12~3-0~ubuntu-focal_amd64.deb
https://zhuanlan.zhihu.com/p/458172588
service docker start
```



### docker-compose

```bash
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-linux-x86_64" -o docker-compose
sudo mv docker-compose /usr/local/bin/
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

### CA证书

```bash
mkdir  ./cert
1. 创建自签名CA证书
# 生成CA私钥
openssl genrsa -out ca.key 4096
# 根据私钥创建自签名的CA证书，有效期3650天（十年）
openssl req -x509 -new -nodes -key ca.key -sha512 -days 3650 -subj "/C=CN/ST=YourState/L=YourCity/O=YourOrganization/CN=YourRootCA" -out ca.crt
2. 生成服务器证书请求（CSR）
#生成服务器证书请求（CSR）
openssl genrsa -out harbor-server.key 4096
# 根据服务器私钥创建CSR文件
openssl req -new -key harbor-server.key -sha512 -days 3650 -out harbor-server.csr -subj "/C=CN/ST=YourState/L=YourCity/O=YourOrg/CN=<your-harbor-domain-or-ip>"
3. 使用CA为服务器签发证书
# 创建v3.ext扩展配置文件（包含如Subject Alternative Name等额外信息）
cat <<EOF > v3.ext
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = dockerhub.kubekey.local
DNS.2 = dockerhub.kubekey.local
IP.1 = 192.168.5.24
EOF

openssl x509 -req -in harbor-server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out harbor-server.crt -days 3650 -sha512 -extfile v3.ext

# 生成文件
ca.crt  ca.key  ca.srl  harbor-server.crt  harbor-server.csr  harbor-server.key  v3.ext

```

### gitlab

```yaml
version: '3.1'
services:
  gitlab:
    image: gitlab/gitlab-ce:15 # 使用最新的社区版镜像
    container_name: gitlab
    privileged: true
    restart: always
    ulimits:
      sigpending: 62793 # 设置挂起信号数限制为10000个
      nproc: 131072
      nofile:
        soft: 60000
        hard: 60000
    environment:
      GITLAB_OMNIBUS_CONFIG: |
          external_url 'http://192.168.5.24:8929'
          gitlab_rails['gitlab_shell_ssh_port'] = 2224
    ports:
      - '8929:8929'
      - '2224:2224'
    volumes:
      - './config:/etc/gitlab'
      - './logs:/var/log/gitlab'
      - './data:/var/opt/gitlab'
networks:
  default:
    name: gitlab_network
```



### harbor

```bash
wget https://your-repo-url/harbor-offline-installer-v2.5.3.tgz 
tar -xzvf harbor-offline-installer-v2.5.3.tgz
cd harbor
cp harbor.yml.tmpl harbor.yml
vim harbor.yml

#配置
hostname: dockerhub.kubekey.local
# http related config
http:
  # port for http, default is 80. If https enabled, this port will redirect to https port
  port: 80
# https related config
https:
  port: 443
  certificate: /home/softs/cert/harbor-server.crt
  private_key: /home/softs/cert/harbor-server.key
harbor_admin_password: Harbor12345
# Harbor DB configuration
database:
  # The password for the root user of Harbor DB. Change this before any production use.
  password: root123
  # The maximum number of connections in the idle connection pool. If it <=0, no idle connections are retained.
  max_idle_conns: 100
  # The maximum number of open connections to the database. If it <= 0, then there is no limit on the number of open connections.
  # Note: the default number of connections is 1024 for postgres of harbor.
  max_open_conns: 900
# The default data volume
data_volume: /data

```

### Miniconda3

```bash
chmod +x Miniconda3-py38_4.11.0-Linux-x86_64.sh
./Miniconda3-py38_4.11.0-Linux-x86_64.sh
export PATH="/root/miniconda3/bin:$PATH"
source ~/.bashrc
conda --version
python --version
```

### Go

```bash
wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
curl -O https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
tar -C /usr/local/ -xzf go1.21.5.linux-amd64.tar.gz
#配置环境变量： 更新系统环境变量以包含Go的bin目录路径。打开或编辑您的bash shell配置文件，通常是 ~/.bashrc 或 ~/.bash_profile：
echo 'export GOROOT=/usr/local/go' >> ~/.bashrc
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOROOT/bin:$GOPATH/bin' >> ~/.bashrc
source ~/.bashrc

#env 
go env -w GOPROXY=https://goproxy.cn,direct
go env -w GO111MODULE=on

```

### NodeJs

```bash
wget https://nodejs.org/dist/v18.19.0/node-v18.19.0-linux-x64.tar.xz
sudo tar -xJf node-v18.19.0-linux-x64.tar.xz -C /usr/local/
sudo ln -s /usr/local/node-v13.14.0-linux-x64/bin/node /usr/local/bin/node
sudo ln -s /usr/local/node-v13.14.0-linux-x64/bin/npm /usr/local/bin/npm
export PATH="/usr/local/node-v13.14.0-linux-x64/bin:$PATH"
source ~/.bashrc
source /etc/profile
node --version
npm --version
# 卸载
sudo rm /usr/local/bin/node
sudo rm /usr/local/bin/npm
# 删除这一行
#/.bash_profile
export PATH="/usr/local/node-v18.19.0-linux-x64/bin:$PATH"
source ~/.bashrc
sudo rm -rf /usr/local/node-v18.19.0-linux-x64
#https://nodejs.org/en/blog/release/v16.13.0
 unlink /usr/local/bin/node
```

### jenkins

```yaml
version: '3'
services:
  jenkins:
    image: jenkins/jenkins:2.176.2-jdk11
    container_name: jenkins
    restart: unless-stopped
    privileged: true
    user: root
    volumes:
     #挂载宿主机本地的maven环境
      - /home/softs/jenkins/maven_home:/var/maven_home
      - /home/softs/jenkins/java_home:/var/java_home
      - /home/softs/jenkins/jenkins_home:/var/jenkins_home
       # 让容器使用宿主的docke
      - /var/run/docker.sock:/var/run/docker.sock
      - /usr/bin/docker:/usr/bin/docker
      - /etc/docker:/etc/docker
    ports:
      - 50000:50000
      - 9999:8080
    environment: 
      TZ: Asia/Shanghai
    networks:
      - shanhy-ci
networks:
  shanhy-ci:
    driver: bridge

```

https://blog.csdn.net/fly910905/article/details/117254938

http://192.168.5.24:9999//api/json/api/json?tree=useCrumbs

{"_class":"hudson.security.csrf.DefaultCrumbIssuer","crumb":"a2bb843144b65f4199ea3f13a9e48eb6727c1ced50f92fcaa86a75290d4c3eb0","crumbRequestField":"Jenkins-Crumb"

插件：

1. ```markdown
   Build With Parameters
   active choice 
   http://192.168.5.24:9999/job/test/api/xml
   http://192.168.5.24:9999/job/test/config.xml
   ```



## Kubernetes（KubeKey / KubeSphere）

```bash
# yum install 
yum update -y
sudo yum install -y yum-utils
sudo yum makecache fast
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
sudo systemctl start docker

# hostname
hostnamectl set-hostname k8smaster
hostnamectl set-hostname k8sworker1
hostnamectl status
echo "127.0.0.1   $(hostname)" >> /etc/hosts
# 免密登录配置
ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.5.24

#3： 关闭防火墙, selinux,iptables 
sudo systemctl stop firewalld
sudo  systemctl enable firewalld
sudo setenforce 0
sudo sed -i s/SELINUX=enforcing/SELINUX=disabled/g /etc/selinux/config
sudo iptables -F

# 查看SELinux的状态
getenforce

# install 
yum -y install curl socat conntrack chrony
# 设置时区
timedatectl
timedatectl set-timezone Asia/Shanghai
chronyc -n sources -v
chronyc tracking
timedatectl status 
# 登录harbor
docker login https://dockerhub.kubekey.local -u admin -p Harbor12345

./kk init registry -a kubesphere-artifact-k8s.tar.gz -f config-sample.yaml
./kk artifact image push -f config-sample.yaml -a kubesphere-artifact-k8s.tar.gz

#在dockerhub 中新建 kubesphereio 空间
./kk delete cluster -f config-sample.yaml
./kk create cluster -f config-sample.yaml -a k8s-kubesphere.tar.gz  --with-kubernetes v1.23.6 --with-kubesphere v3.3.1 --with-package 



Console: http://192.168.5.21:30880
Account: admin
Password: P@88w0rd

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
export KUBECONFIG=/etc/kubernetes/admin.conf
kubeadm join lb.kubesphere.local:6443 --token q5v37f.sxh7hzkrlukhs3xd \
        --discovery-token-ca-cert-hash sha256:51510e85b6d91f2ce6f56d4c4e6e3f8d838667621ef1560c1b66f55fb8e7bb12 \
        --control-plane



```



创建harbor secret：

```bash
kubectl create secret docker-registry harbor-secret \
  --docker-email=tiger@acme.example \ 
  --docker-username=admin \
  --docker-password=Harbor12345 \ 
  --docker-server=dockerhub.kubekey.local:443 \
kubectl create secret docker-registry harbor-secret --docker-email=tiger@acme.example --docker-username=admin  --docker-password=Harbor12345 --docker-server=dockerhub.kubekey.local:443
  
kubectl get secret

```

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

```



## 服务账号与 URL 速查

| 服务 | 地址 | 账号 / 密码 |
| --- | --- | --- |
| KubeSphere | http://192.168.5.21:30880 | admin / P@88w0rd（Harbor12345 见原笔记） |
| Harbor | https://dockerhub.kubekey.local 或 192.168.5.24 | admin / Harbor12345 |
| Jenkins | http://192.168.5.21:30180 、http://192.168.5.24:9999 | admin / P@88w0rd |
| GitLab | http://192.168.5.24:8929 | root / asdf123456 |
| RabbitMQ | http://192.168.5.24:15672 | 见 KpCloud 节 |
| KpCloud 前台 | http://192.168.5.24:8080 | kplcloud@nsini.com / admin |

MinIO 发布包参考：`RELEASE.2019-08-07T01-59-21Z`





## KpCloud

```bash
docker-compse -up

mysql:
host: 192.168.5.24 root pwd:admin db:kplcloud
rabbitMQ:
http://localhost:15672
1:在admin: 添加virtual host :kplcloud 
2: 设置权限
3：登录：http://192.168.5.24:8080/
kplcloud@nsini.com
admin

kplcloud/hello.git

jenkins 清华源
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
```

## Nginx

```
sudo systemctl stop nginx
sudo yum remove nginx
sudo rm -rf /etc/nginx/ /var/log/nginx/ /var/cache/nginx/
sudo yum makecache
```



## Traefik Ingress

部署步骤概览：① CRD → ② RBAC → ③ ConfigMap → ④ 节点 Label → ⑤ DaemonSet → ⑥ IngressRoute。  
文档：[Traefik v2](https://docs.traefik.io/v2.0/)（默认部署在 `kube-system`）。

```yaml
kubectl apply -f https://raw.githubusercontent.com/traefik/traefik/v2.7/docs/content/routing/providers/kubernetes-crd/quickstart/crd.yaml
# 1、创建 CRD 资源
2、创建 RBAC 权限
3、创建 Traefik 配置文件
4、节点设置 Label 标签
5、Kubernetes 部署 Traefik
1、配置 HTTP 路由规则 （Traefik Dashboard 为例）
2、配置 HTTPS 路由规则（Kubernetes Dashboard 为例）
https://docs.traefik.io/v2.0/
Traefik 是部署在 Kube-system Namespace 下，如果不是需要修改下面部署文件中的 Namespace 属性

1: 创建crd 资源：  
kubectl apply -f traefik-crd.yaml
## IngressRoute
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: ingressroutes.traefik.containo.us
spec:
  scope: Namespaced
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: IngressRoute
    plural: ingressroutes
    singular: ingressroute
---
## IngressRouteTCP
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: ingressroutetcps.traefik.containo.us
spec:
  scope: Namespaced
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: IngressRouteTCP
    plural: ingressroutetcps
    singular: ingressroutetcp
---
## Middleware
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: middlewares.traefik.containo.us
spec:
  scope: Namespaced
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: Middleware
    plural: middlewares
    singular: middleware
---
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: tlsoptions.traefik.containo.us
spec:
  scope: Namespaced
  group: traefik.containo.us
  version: v1alpha1
  names:
    kind: TLSOption
    plural: tlsoptions
    singular: tlsoption
    
    
2：创建 RBAC 权限
kubectl apply -f traefik-rbac.yaml -n kube-system

apiVersion: v1
kind: ServiceAccount
metadata:
  namespace: kube-system
  name: traefik-ingress-controller
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: traefik-ingress-controller
rules:
  - apiGroups: [""]
    resources: ["services","endpoints","secrets"]
    verbs: ["get","list","watch"]
  - apiGroups: ["extensions"]
    resources: ["ingresses"]
    verbs: ["get","list","watch"]
  - apiGroups: ["extensions"]
    resources: ["ingresses/status"]
    verbs: ["update"]
  - apiGroups: ["traefik.containo.us"]
    resources: ["middlewares"]
    verbs: ["get","list","watch"]
  - apiGroups: ["traefik.containo.us"]
    resources: ["ingressroutes"]
    verbs: ["get","list","watch"]
  - apiGroups: ["traefik.containo.us"]
    resources: ["ingressroutetcps"]
    verbs: ["get","list","watch"]
  - apiGroups: ["traefik.containo.us"]
    resources: ["tlsoptions"]
    verbs: ["get","list","watch"]
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: traefik-ingress-controller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: traefik-ingress-controller
subjects:
  - kind: ServiceAccount
    name: traefik-ingress-controller
    namespace: kube-system
    
    
3：创建 Traefik 配置文件
traefik-config.yaml 文件
kubectl apply -f traefik-config.yaml -n kube-system
kind: ConfigMap
apiVersion: v1
metadata:
  name: traefik-config
data:
  traefik.yaml: |-
    serversTransport:
      insecureSkipVerify: true
    api:
      insecure: true
      dashboard: true
      debug: true
    metrics:
      prometheus: ""
    entryPoints:
      web:
        address: ":80"
      websecure:
        address: ":443"
    providers:
      kubernetesCRD: ""
    log:
      filePath: ""
      level: error
      format: json
    accessLog:
      filePath: ""
      format: json
      bufferingSize: 0
      filters:
        retryAttempts: true
        minDuration: 20
      fields:
        defaultMode: keep
        names:
          ClientUsername: drop
        headers:
          defaultMode: keep
          names:
            User-Agent: redact
            Authorization: drop
            Content-Type: keep

4：节点设置 Label 标签
由于是 Kubernetes DeamonSet 这种方式部署 Traefik，所以需要提前给节点设置 Label，这样当程序部署时 Pod 会自动调度到设置 Label 的点上。
kubectl label nodes k8s-node-2-12 IngressProxy=true
 kubectl label nodes k8s-node-2-12 IngressProxy-   # 删除标签
 
5、Kubernetes 部署 Traefik
kubectl apply -f traefik-deploy.yaml -n kube-system

apiVersion: v1
kind: Service
metadata:
  name: traefik
spec:
  ports:
    - name: web
      port: 80
    - name: websecure
      port: 443
    - name: admin
      port: 8080
  selector:
    app: traefik
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: traefik-ingress-controller
  labels:
    app: traefik
spec:
  selector:
    matchLabels:
      app: traefik
  template:
    metadata:
      name: traefik
      labels:
        app: traefik
    spec:
      serviceAccountName: traefik-ingress-controller
      terminationGracePeriodSeconds: 1
      containers:
        - image: traefik:latest
          name: traefik-ingress-lb
          ports:
            - name: web
              containerPort: 80
              hostPort: 80           #hostPort方式，将端口暴露到集群节点
            - name: websecure
              containerPort: 443
              hostPort: 443          #hostPort方式，将端口暴露到集群节点
            - name: admin
              containerPort: 8080
          resources:
            limits:
              cpu: 2000m
              memory: 1024Mi
            requests:
              cpu: 1000m
              memory: 1024Mi
          securityContext:
            capabilities:
              drop:
                - ALL
              add:
                - NET_BIND_SERVICE
          args:
            - --configfile=/config/traefik.yaml
          volumeMounts:
            - mountPath: "/config"
              name: "config"
      volumes:
        - name: config
          configMap:
            name: traefik-config 
      tolerations:              #设置容忍所有污点，防止节点被设置污点
        - operator: "Exists"
      nodeSelector:             #设置node筛选器，在特定label的节点上启动
        IngressProxy: "true"
        
        
Traefik 路由规则配置
$ kubectl apply -f traefik-dashboard-route.yaml -n kube-system

raefik 应用已经部署完成，但是想让外部访问 Kubernetes 内部服务，还需要配置路由规则，这里开启了 Traefik Dashboard 配置，所以首先配置 Traefik Dashboard 看板的路由规则，使外部能够访问 Traefik Dashboard。
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: traefik-dashboard-route
spec:
  entryPoints:
    - web
  routes:
    - match: Host(`traefik.mydlq.club`)
      kind: Rule
      services:
        - name: traefik
          port: 8080
```





## GitLab Docker 单机部署

```bash
docker pull gitlab/gitlab-ce:15.3.1-ce.0

docker pull 镜像名称 -–registry-mirror=国内镜像源地址
https://docker-practice.github.io/zh-cn/cloud/alicloud.html
asdf123456


mkdir -p /docker/gitlab/{config,data,logs}
docker pull gitlab/gitlab-ce:15.3.1-ce.0
docker run -d \
-p 8888:80 \
-p 2222:22 \
-v /docker/gitlab/config:/etc/gitlab \
-v /docker/gitlab/data:/var/opt/gitlab \
-v /docker/gitlab/logs:/var/log/gitlab \
-e GITLAB_OMNIBUS_CONFIG="external_url 'http://192.168.2.110'; gitlab_rails['gitlab_shell_ssh_port'] = 2222; gitlab_rails['time_zone'] = 'Asia/Shanghai'" \
-e TZ=Asia/Shanghai \
--memory 16G \
--cpus=8 \
--restart always \
--name gitlab \
gitlab/gitlab-ce:15.3.1-ce.0

docker exec -it gitlab grep "Password": /etc/gitlab/initial_root_password


```



<!-- URL 与账号已合并至「服务账号与 URL 速查」 -->

