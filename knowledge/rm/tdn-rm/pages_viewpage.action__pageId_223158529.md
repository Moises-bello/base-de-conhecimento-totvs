---
content_hash: c8704837e0694f839ebec32a91fbaeeece13a7295d23bc8d2700ec481137ef93
fetched_at: '2026-06-29T00:06:20.864286+00:00'
page_id: '223158529'
product: rm
source: tdn-rm
title: SAU0061_Como_realizar_Importação_de_Tabelas_do_SUS_ImportaSUS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223158529
version: 118
---

# Como realizar a importação de tabelas do SUS?

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Hospitalar |
| **Versões:** | Todas |
| **Ocorrência:** | Como realizar a importação de tabelas do SUS? |
| **Passo a passo:** | 1. Realize o download da competência atual do arquivo ImportaSUS através do link: <ftp://ftp.poa.totvs.com.br/rm/lotes/ImportaSUS/> 2. Na pasta do **ImportaSUS** configure o arquivo **alias.dat** com (no seguinte diretório do **TOTVS Gestão Hospitalar** C:\totvs\CorporeRM\RM.Net) os dados referentes a base em que é utilizado o **TOTVS Gestão Hospitalar**.   SQL:  <?xml version="1.0" standalone="yes"?>  <RMSAliasData xmlns="<http://tempuri.org/RMSAliasData.xsd>">      <DbConfig>      <Alias>TISS 3</Alias>      <DbType>SqlServer</DbType>      <DbProvider>SqlClient</DbProvider>      <DbServer>10.51.0.47</DbServer>      <DbName>RM\_TISS3\_SUST</DbName>      <UserName>rm</UserName>      <Password>rm</Password>      <RunService>false</RunService>      <JobServerEnabled>false</JobServerEnabled>      <JobServerMaxThreads>3</JobServerMaxThreads>      <JobServerLocalOnly>true</JobServerLocalOnly>      <JobServerPollingInterval>10</JobServerPollingInterval>      <ChartAlertEnabled>false</ChartAlertEnabled>      <ChartAlertPollingInterval>20</ChartAlertPollingInterval>      <ChartHistoryEnabled>false</ChartHistoryEnabled>      <ChartHistoryPollingInterval>20</ChartHistoryPollingInterval>      <RSSReaderMailEnabled>false</RSSReaderMailEnabled>      <RSSReaderMailPollingInterval>10</RSSReaderMailPollingInterval>    </DbConfig>     </RMSAliasData>    Oracle:  <?xml version="1.0" standalone="yes"?>  <RMSAliasData xmlns="<http://tempuri.org/RMSAliasData.xsd>">      <DbConfig>                  <Alias>FATIMA</Alias>                  <DbType>Oracle</DbType>                  <DbProvider>OracleClient</DbProvider>                  <DbServer>POA01/POAD0009</DbServer>                  <DbName>FATIMA</DbName>                  <UserName>rm</UserName>                  <Password>rm</Password>                  <RunService>false</RunService>                  <JobServerEnabled>false</JobServerEnabled>                  <JobServerMaxThreads>3</JobServerMaxThreads>                  <JobServerLocalOnly>true</JobServerLocalOnly>                  <JobServerPollingInterval>10</JobServerPollingInterval>                  <ChartAlertEnabled>false</ChartAlertEnabled>                  <ChartAlertPollingInterval>20</ChartAlertPollingInterval>                  <ChartHistoryEnabled>false</ChartHistoryEnabled>                  <ChartHistoryPollingInterval>20</ChartHistoryPollingInterval>                  <RSSReaderMailEnabled>false</RSSReaderMailEnabled>                  <RSSReaderMailPollingInterval>10</RSSReaderMailPollingInterval>    </DbConfig>  </RMSAliasData>      2. Abra o **ImportaSUS.exe**, selecione o arquivo **Alias.dat** criado, conforme exemplos.    3. Informe os mesmos dados de acesso a base(Login e Senha).      4. Clique em “**Diretório dos Arquivos TXT:**”.    5. Selecione qualquer arquivo .txt da pasta do **ImportaSUS** e marque a opção “**Importar Tabela de CEPs**”.    6. Clique em **Importar** para concluir a importação. |

divs
