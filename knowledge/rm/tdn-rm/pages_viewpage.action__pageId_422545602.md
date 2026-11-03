---
content_hash: c3fda74c2014718e566a42077dcd24e4307bfd85886735f95f820d45141bea94
fetched_at: '2026-06-29T00:09:19.532658+00:00'
page_id: '422545602'
product: rm
source: tdn-rm
title: Layout de Importação de Lançamentos via WebService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545602
version: 13
---

#f5f5f5#363636noneImportação de Lançamentos via WebService

## **Conteúdo**



## **01. Visão GeralVisaoGeral**

A Inclusão/Alteração de Lançamento Fiscal através de WebService é um processo no qual o cliente passa a integrar diretamente com o módulo  [TOTVS Gestão Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=198948859) através de WebService, onde este processo tem como objetivo incluir ou alterar Lançamentos Fiscais utilizando os novos serviços .NET.

Atualmente o aplicativo RM.Host.exe ou RM.Host.Service.exe funciona como um publicador de serviços, para isto basta acrescentar algumas parametrizações em seus arquivos de configurações.  Veja abaixo em Como Fazer, o link de configuração do arquivos .config.

## **02. WebService e Integraçãowebservice**

Depois de configurar os arquivos e iniciar o RM.Host.exe, o cliente poderá acionar em seu sistema através do WebService wsDataServer o serviço de inclusão/alteração do lançamento através do método SaveRecord do DataServer criado para está funcionalidade "FisLanFiscalImportacaoData".

Existem ferramentas em versão free no mercado (internet) onde é possível buscar o schema XSD do DataSet ligado a este DataServer, a TOTVS também disponibiliza uma ferramenta para esta integração via WebService o "TotvsWSTest.exe", onde além do schema e do XML dos Lançamentos que estão na Base você ainda tem acesso a uma documentação gerada em HTML para melhor compreensão das informações do DataSet do Lançamento Fiscal. Veja abaixo em "Recursos Adicionais" como obter o aplicativo disponibilizado pela TOTVS.

O serviço de WebService receberá um XML contendo um lançamento por vez, ou seja, para cada inclusão/alteração de um lançamento o serviço deverá ser acionado. Esta regra deve ser respeitada, pois o DATASERVER inicia uma transação para cada acionamento, e neste caso se for enviados vários lançamentos em um único XML e houver alguma regra violada nenhum lançamento será importado. Este cenário também implica em perda de performance já que a transação tem que ficar aberta até a conclusão de toda a importação, portanto o serviço ficará disponível para que possa ser incluído/alterado um lançamento por vez.

Com esta nova integração visamos diminuir o tempo de importação dos arquivos e deixar o processo mais dinâmico e mais consistente além de que está funcionará de forma direta entre o aplicativo desenvolvido pelo cliente e o modulo Fiscal da TOTVS, através do WebService, deixando a necessidade de utilização de arquivos.

## **02. Regras de preenchimento e informações do XMLxml**

**Regras para o preenchimento do arquivo XML para inclusão/Alteração de Lançamentos**

O arquivo devera ser preenchido de acordo com o .xsd referente ao DataServer do Lançamento Fiscal "FisLanFiscalImportacaoData" disponibilizado para ser consumido o serviço do WebServer.

**Agrupamento de Itens**

A Tag <AGRUPAITENS> da tabela <DLAFAGRUP> deverá ser preenchida com 1 para "Sim" ou 0 Zero para "Não" para informar se os itens iguais na mesma parcela deverão ser agrupados ou não. Este agrupamento será feito referentes aos Itens iguais da mesma Situação Tributária, estes itens deverão ter mesma Coligada, Identificador da Situação Tributária, Produto e Cupom Fiscal. Obs.: Todas as suas referencias filhas serão agrupadas também neste processo como por exemplo os Tributos de Itens.

**Campos do Item a serem agrupados**: "QTDEPRD", "DESCONTOITEM", "BASEIPI", "VALORIPI", "ISENTOIPI", "OUTROSIPI", "BASEICMSPRD", "BASEICMSSTPRD", "VLRDIFALIQUOTA", "VLRICMSPRD", "VLRICMSSTPRD", "VLRFRETE", "VALORIPISEMCREDITO", "VALORICMSFRETE", "VALORSEGURO", "VALORDESPESA", "OUTROSICMS", "ISENTOICMS", "BASESUBSTCOMPL", "VALORSUBSTCOMPL", "VALORMERC", "QTDECONTRATADA", "VLRICMSDESONERADO"

**Campos do Tributo do Item a serem agrupados:**"BASETRB", "VALORTRB", "VLRISENTO", "DEDUCAOTRB"

**Campo do Lote do Produto a ser agrupado:** "QUANTIDADE"

**Campo do Patrimônio do Item a ser agrupado:**"VALORUTILIZ"

**Campo da Referência do Item a ser agrupado:**"QTDEPRD"

***Observação:*** Agrupamento dos Itens e uma opção interessante para diminuir o volume de dados (registros) na Base de dados, como por exemplo na tabela DITEM e DTRBITEM que são tabelas que contém muitos registros na Base agrupando os itens iguais por Lançamento e Situação Tributaria evita o crescimento da Base.

**Regras de Preenchimento dos Identificadores**

* A Tag <**IDLAFAGRUP**> em todas as tabelas em que ela existir como por exemplo nas tabelas <DLAFAGRUP> ou <SITUACAOTRIBUTARIA> deverá ser preenchida com valor -1 para inclusão de novos Lançamentos ou com o identificador do Lançamento da Base quando for alteração de um determinado Lançamento Fiscal.
* A Tag <**IDLAF**> da tabela <**DLAF**> deverá ser preenchida com o mesmo valor da Tag <IDLAF> da Tabela <SITUACAOTRIBUTARIA> para Lançamentos de uma Situação Tributária apenas e quando o Lançamento Fiscal tiver mais de uma Situação Tributária, está deverá ser preenchida com o mesmo valor da Tag <IDLAF> da tabela <SITUACAOTRIBUTARIA> da primeira Situação Tributaria do Lançamento Fiscal.
* A Tag <**IDLAF**> da tabela <**SITUACAOTRIBUTARIA**> refere-se ao identificador de cada parcela do Lançamento está deverá ser preenchido com um valor inteiro e positivo identificando a Situação Tributaria. Para as tabelas relacionadas como por exemplo <DITEM> ou <DTRBLAF> devem conter o mesmo identificador da Situação Tributaria na qual eles fazem parte.
* A Tag <**IDLAFHST**> da tabela <**SITUACAOTRIBUTARIA**> refere-se ao identificador interno do Histórico do Lançamento Fiscal e deverá ser preenchida com o mesmo valor da tag <IDLAF> desta mesma Situação Tributaria.
* A Tag <**IDNAT**> da tabela <**SITUACAOTRIBUTARIA**> quando for inclusão deverá ser preenchida com o valor -1 o sistema fará a busca automaticamente do identificador da natureza pela Tag <CODNAT>, quando for alteração o identificador deverá estar preenchido com o identificador da Base.
* A Tag <**IDPRD**> da tabela <**DITEM**> deverá ser preenchida com valor -1 o sistema fará a busca automaticamente do identificador pela Tag <CODIGOPRD>, quando for alteração o identificador deverá estar preenchido com o identificador da Base.
* A Tag <**IDPRD**> da tabela <**DITEMCUPOMCANC**> deverá ser preenchida com valor igual a -1 o sistema fará a busca automaticamente do identificador pela Tag <CODIGOPRD>, quando for alteração o identificador deverá estar preenchido com o identificador da Base.
* A Tag <**IDTRBLAF**> da tabela <**DTRBLAF**> deverá ser preenchida com valor -1 no caso de inclusão de novo Lançamento e com o identificador do Tributo do Lançamento do Banco no caso de alteração do Lançamento Fiscal.
* A Tag <**IDRATCCU**> da tabela <**DLAFRATCCU**> deverá ser preenchida com valor -1 no caso de inclusão de novo Lançamento e com o identificador do Rateio por Centro de Custo do Banco no caso de alteração do Lançamento Fiscal.
* A Tag <**IDNFTERCEIROS**> da tabela <**DNFTERCEIROS**> deverá ser preenchida com valor -1 no caso de inclusão de novo Lançamento e com o identificador da NF de Terceiros do Banco no caso de alteração do Lançamento Fiscal.
* A Tag <**IDNOTAEMPENHO**> da tabela <**DLAFMOVNOTAEMPENHO**> deverá ser preenchida com valor -1 no caso de inclusão de novo Lançamento e com o identificador da Nota de Empenho do Banco no caso de alteração do Lançamento Fiscal.
* A Tag <**SEQUENCIAL**> da tabela <**DLAFMOVPROCESSOJUD**> deverá ser preenchida com valor -1 no caso de inclusão de novo Lançamento e com o identificador do Processo Judicial do Banco no caso de alteração do Lançamento Fiscal.
* A Tag <**IDTRBITEM**> da tabela <**DTRBITEM**> deverá ser preenchida com valor -1 no caso de inclusão de novo Lançamento e com o identificador do tributo do Item do Lançamento no Banco no caso de alteração do Lançamento Fiscal.
* A Tag <**IDLAFHST**> da tabela <**DITEM**> refere-se ao identificador interno da Situação Trinitária do Histórico do Item do Lançamento Fiscal e deverá ser preenchida com o mesmo valor da tag <IDLAF> da tabela <DITEM>.
* A Tag < **NUMITEMHST**> da tabela <**DITEM**> refere-se ao identificador interno da Situação Tributária do Histórico do Item do Lançamento Fiscal e deverá ser preenchida com o mesmo valor da tag <NUMITEM> da tabela <DITEM>.

Observação

Para Alteração de um Lançamento que já tenha sido incluído na Base deve-se enviar apenas, as chaves de todas as tabelas relacionadas ao seu Lançamento já incluído e as Tags que forem sofrer alteração, caso alguma Tabela referente a este lançamento não seja enviada o sistema entenderá que esta deverá ser excluída e assim o fará. Performance.  
Na chave de acesso de nota referenciada não é validado o tipo de caractere inserido, sendo possível informar caracteres que não são numéricos quando importado via webservice, já na inclusão manual, no formulário, só é possível inserir números no campo chave de acesso.

Maiores Informações

* [Configuração dos arquivos .config](http://tdn.totvs.com/display/LRM/RM.Host)
* [Ferramenta para a integração via WebService](http://tdn.totvs.com/display/public/LRM/WebService+RM)
