---
article_id: 360027518891
category: Materiais - Compras (SIGACOM)
content_hash: 3752fcb41a2faa7d4d38ae22045df882a4f7f0ed269f4beaf93927e4c7020584
fetched_at: '2026-06-28T22:41:08.687264+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como são definidos
  os produtos e o Tipo de Documento na importação do Documento de Frete / CTe no Importador
  XML?
type: support-article
updated_at: '2025-09-10T16:17:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027518891-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-s%C3%A3o-definidos-os-produtos-e-o-Tipo-de-Documento-na-importa%C3%A7%C3%A3o-do-Documento-de-Frete-CTe-no-Importador-XML
---

**Dúvida**

Como são definidos os Produtos e Tipo de Documento utilizados na importação de XML de Documento de Frete / CTe no Importador XML / TOTVS Colaboração ?

**Ambiente**

Protheus – Compras – A partir da versão 12

**Solução**

Regras para definição do produto e tipo de documento a ser utilizado na importação do documento CTE:

* Quando o XML de um CTe possui vínculo com alguma nota fiscal de origem, e ao importar é encontrada este Documento Origem na base de dados, o documento é importado como **Tipo Complemento** e os **produtos são os mesmos da nota fiscal de origem;**
  + *Este vinculo existente no XML é através de uma Tag que contém o chave da NF de Origem, e para que ocorra dessa forma, deve-se também existir na base de dados uma NF com esta "Chave Origem" contida no XML do Frete (A* *Tag "infNFe" contém a chave da "NF Origem" no XML de CTe).*
* Quando não existe nenhum vínculo de nota fiscal de origem no XML, é executado o ponto de entrada ou parâmetro MV\_XMLPFCT para definição do produto/tipo de documento e a NF é do tipo Normal e;
* Quando não possui vinculo com nota fiscal de origem no XML, a ordem de execução dos ponto de entradas ou parâmetro é a seguinte:

1) Ponto de entrada A116PRDF ([TC02020 - A116PRDF - Customização da Identificação do Produto Frete](http://tdn.totvs.com/pages/viewpage.action?pageId=47908250))

2) Ponto de entrada A116ITPCT ([TC02019 - A116ITPCT - Determina se o CTe deve gerar nota do tipo Normal](http://tdn.totvs.com/display/PROT/TC02019+-+A116ITPCT+-+Determina+se+o+CTe+deve+gerar+nota+do+tipo+Normal))

3) Parâmetro MV\_XMLPFCT ([TC03 - Parâmetros](http://tdn.totvs.com/pages/viewpage.action?pageId=271662192))

Resumindo, abra o arquivo XML do CTE. Busque e localize a tag <infNfe> . Copie a chave de acesso que consta dentro dessa tag. Faça um filtro na SF1 buscando por F1\_CHVNFE = chave de acesso que copiou da tag <infNfe> do XML.

É essa a consulta realizada pelo sistema para localizar a nota de compra de origem.

***Saiba Mais :***

[TOTVS Colaboração - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=271661626)

[Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
