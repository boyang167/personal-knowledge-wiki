# PubMed
## 简介

-   PubMed支持检索和获取生物医学和生命科学领域文献，包含超过 3700 万条生物医学文献的引用和摘要。
-   PubMed中的引用主要来自生物医学和健康领域，以及生命科学、行为科学、化学科学、生物工程学等相关领域。
-   一般情况下，PubMed`不包括文献的全文`，当其他来源（如出版商网站或 PubMed Central（PMC））提供全文链接时，PubMed会收录这些链接。

-   PubMed支持对以下NLM文献资源的搜索：
    -   MEDLINE：MEDLINE 是 PubMed 的最大组成部分，主要包括MEDLINE指定期刊中文献。这些文献使用 MeSH（医学主题词）进行索引，包含funding、遗传、化学和其他metadata。（[MEDLINE指定期刊列表](https://www.ncbi.nlm.nih.gov/nlmcatalog?term=currentlyindexed)）
    -   PubMed Central（PMC）：一个包含经过NLM审查和选择的期刊文献的`全文存档`，还收录了一些根据资助方政策进行存档的文献。
    -   Bookshelf：一个与生物医学、健康和生命科学相关的书籍、报告、数据库和其他文档的`全文存档`。

## 数据下载

-   [基准数据](https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/)
-   [每日更新](https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/)


## 数据组织形式
-   [XML DTD](PubMed/pubmed_240101.dtd)
-   [DTD文档: elements and attributes](https://dtd.nlm.nih.gov/ncbi/pubmed/doc/out/240101/index.html)

-   [附录：PubMed XML举例](#附录pubmed-xml举例)

-   常用字段解析：
	-  title
	-  issue*
	-  pages*
	-  abstract
	-  journal
	-  authors
	-  pubdate
	-  pmid
	-  mesh_terms
	-  publication_types
	-  chemical_list
	-  keywords
	-  doi
	-  references(reference)
	-  delete
	-  languages
	-  vernacular_title
	-  affiliations*
	-  pmc
	-  other_id
	-  medline_ta
	-  nlm_unique_id
	-  issn_linking
	-  country
	-  grant_ids

## 数据更新
### 基准数据+每日更新
- 基准数据：NLM每年以XML格式生成一组基线PubMed引用记录供下载。年度基线数据在每年的十二月发布。2024年的完整的基线数据包括文件pubmed24n0001.xml到pubmed24n1219.xml（实际上是2024年前的所有数据）。
- 每日更新文件：NLM每天生成包括新的、修订过的和已删除的引用的更新文件。在加载完2024年度PubMed基线文件集之后，需要加载的第一个更新文件是pubmed24n1220.xml。

## schema


## metadata
| column              | dtype   | description                                                                                                               |   |
|---------------------|---------|---------------------------------------------------------------------------------------------------------------------------|---|
| c_title             | text    | title of the article                                                                                                      |   |
| c_issue             | text    | issue                                                                                                                     |   |
| c_pages             | text    | pages                                                                                                                     |   |
| c_abstract          | text    | abstract of the article                                                                                                   |   |
| c_journal           | text    | journal of the given paper                                                                                                |   |
| c_authors           | text    | authors, each separated by ;                                                                                              |   |
| c_pubdate           | text    | publication date                                                                                                          |   |
| c_pmid              | integer | PubMed ID                                                                                                                 |   |
| c_mesh_terms        | text    | list of MeSH terms with corresponding MeSH ID, each separated by ; e.g. 'D000161:Acoustic Stimulation; D000328:Adult; ... |   |
| c_publication_types | text    | list of publication type list each separated by ; e.g. 'D016428:Journal Article'                                          |   |
| c_chemical_list     | text    | list of chemical terms, each separated by ;                                                                               |   |
| c_keywords          | text    | list of keywords, each separated by ;                                                                                     |   |
| c_doi               | text    | DOI                                                                                                                       |   |
| c_references        | text    | string of PMID each separated by ; or list of references made to the article                                              |   |
| c_delete            | boolean | boolean if False means paper got updated                                                                                  |   |
| c_languages         | text    | list of languages, separated by ;                                                                                         |   |
| c_vernacular_title  | text    | vernacular title. Defaults to empty string whenever non-available.                                                        |   |
| c_affiliations      | text    | affiliations                                                                                                              |   |
| c_pmc               | text    | PubMed Central ID                                                                                                         |   |
| c_other_id          | text    | Other IDs found, each separated by ;                                                                                      |   |
| c_medline_ta        | text    | the abbreviation of the journal name                                                                                      |   |
| c_nlm_unique_id     | text    | NLM unique identification                                                                                                 |   |
| c_issn_linking      | text    | ISSN linkage, typically use to link with Web of Science dataset                                                           |   |
| c_country           | text    | Country extracted from journal information field                                                                          |   |
| c_grant_ids         | text    | Grant ID, Acronym of grant, Country where grant funding from and agency                                                   |   |


## 入库情况
2024年的baseline + updatefiles中到pubmed24n1407.xml.gz的XML已解析完毕，由于202服务器卡顿暂时未入库。

## 附录：PubMed XML一例

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE PubmedArticleSet SYSTEM "http://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_240101.dtd">
<PubmedArticleSet>
  <PubmedArticle>
    <MedlineCitation Status="MEDLINE" Owner="NLM">
      <PMID Version="1">3444263</PMID>
      <DateCompleted>
        <Year>1988</Year>
        <Month>04</Month>
        <Day>22</Day>
      </DateCompleted>
      <DateRevised>
        <Year>2015</Year>
        <Month>11</Month>
        <Day>19</Day>
      </DateRevised>
      <Article PubModel="Print">
        <Journal>
          <JournalIssue CitedMedium="Print">
            <Issue>12</Issue>
            <PubDate>
              <Year>1987</Year>
            </PubDate>
          </JournalIssue>
          <Title>Klinicheskaia khirurgiia</Title>
          <ISOAbbreviation>Klin Khir (1962)</ISOAbbreviation>
        </Journal>
        <ArticleTitle>[Effect of endotracheal and epidural anesthesias on the incidence of acute postoperative erosions and ulcers of the digestive organs].</ArticleTitle>
        <Pagination>
          <MedlinePgn>26-8</MedlinePgn>
        </Pagination>
        <AuthorList CompleteYN="Y">
          <Author ValidYN="Y">
            <LastName>Chepkiĭ</LastName>
            <ForeName>L P</ForeName>
            <Initials>LP</Initials>
          </Author>
          <Author ValidYN="Y">
            <LastName>Khokholia</LastName>
            <ForeName>V P</ForeName>
            <Initials>VP</Initials>
          </Author>
          <Author ValidYN="Y">
            <LastName>Blikhar</LastName>
            <ForeName>T E</ForeName>
            <Initials>TE</Initials>
          </Author>
          <Author ValidYN="Y">
            <LastName>Kopev</LastName>
            <ForeName>Iu A</ForeName>
            <Initials>IuA</Initials>
          </Author>
          <Author ValidYN="Y">
            <LastName>Buryĭ</LastName>
            <ForeName>A N</ForeName>
            <Initials>AN</Initials>
          </Author>
        </AuthorList>
        <Language>rus</Language>
        <PublicationTypeList>
          <PublicationType UI="D003160">Comparative Study</PublicationType>
          <PublicationType UI="D004740">English Abstract</PublicationType>
          <PublicationType UI="D016428">Journal Article</PublicationType>
        </PublicationTypeList>
        <VernacularTitle>Vliianie éndotrakhealnogo narkoza i épiduralnoĭ anestezii na chatotu ostrykh posleoperatsionnykh éroziĭ i iazv organov pishchevaritelnogo apparata.</VernacularTitle>
      </Article>
      <MedlineJournalInfo>
        <Country>Ukraine</Country>
        <MedlineTA>Klin Khir (1962)</MedlineTA>
        <NlmUniqueID>0376360</NlmUniqueID>
      </MedlineJournalInfo>
      <CitationSubset>IM</CitationSubset>
      <MeshHeadingList>
        <MeshHeading>
          <DescriptorName UI="D000770" MajorTopicYN="Y">Anesthesia
 Endotracheal</DescriptorName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName UI="D000767" MajorTopicYN="Y">Anesthesia
 Epidural</DescriptorName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName UI="D005773" MajorTopicYN="N">Gastroscopy</DescriptorName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName UI="D006439" MajorTopicYN="N">Hemodynamics</DescriptorName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName UI="D006801" MajorTopicYN="N">Humans</DescriptorName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName UI="D010437" MajorTopicYN="N">Peptic Ulcer</DescriptorName>
          <QualifierName UI="Q000503" MajorTopicYN="N">physiopathology</QualifierName>
          <QualifierName UI="Q000517" MajorTopicYN="Y">prevention &amp; control</QualifierName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName UI="D010528" MajorTopicYN="N">Peristalsis</DescriptorName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName UI="D011183" MajorTopicYN="N">Postoperative Complications</DescriptorName>
          <QualifierName UI="Q000503" MajorTopicYN="N">physiopathology</QualifierName>
          <QualifierName UI="Q000517" MajorTopicYN="Y">prevention &amp; control</QualifierName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName UI="D011300" MajorTopicYN="N">Preoperative Care</DescriptorName>
        </MeshHeading>
        <MeshHeading>
          <DescriptorName UI="D012307" MajorTopicYN="N">Risk Factors</DescriptorName>
        </MeshHeading>
      </MeshHeadingList>
    </MedlineCitation>
    <PubmedData>
      <History>
        <PubMedPubDate PubStatus="pubmed">
          <Year>1987</Year>
          <Month>1</Month>
          <Day>1</Day>
        </PubMedPubDate>
        <PubMedPubDate PubStatus="medline">
          <Year>1987</Year>
          <Month>1</Month>
          <Day>1</Day>
          <Hour>0</Hour>
          <Minute>1</Minute>
        </PubMedPubDate>
        <PubMedPubDate PubStatus="entrez">
          <Year>1987</Year>
          <Month>1</Month>
          <Day>1</Day>
          <Hour>0</Hour>
          <Minute>0</Minute>
        </PubMedPubDate>
      </History>
      <PublicationStatus>ppublish</PublicationStatus>
      <ArticleIdList>
        <ArticleId IdType="pubmed">3444263</ArticleId>
      </ArticleIdList>
    </PubmedData>
  </PubmedArticle>
```