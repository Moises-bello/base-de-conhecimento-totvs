---
article_id: 22672045330327
category: Materiais - Compras (SIGACOM)
content_hash: 517943aa37761f9d9cc1faf1018f137c8f300e0e2111c23672b36fcd08866000
fetched_at: '2026-06-28T22:41:19.983631+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Inclusão de CTE, qual
  rotina utilizar ?
type: support-article
updated_at: '2024-04-09T13:09:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22672045330327-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Inclus%C3%A3o-de-CTE-qual-rotina-utilizar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22672045300375) Tempo aproximado para leitura:

**Dúvida**Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Inclusão de CTE, qual rotina utilizar ? MATA103 ( documento de entrada ) ou MATA116 ( NF conhecimento de frete ).  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras -  A partir da versão 12  
  
**Solução**No módulo de compras, temos duas rotinas onde uma nota de CTE ( conhecimento de transporte eletrônico ) pode ser incluída.

Sçao elas:

- a rotina MATA103 ( Documento de Entrada ), do Menu: Compras -> Atualizações -> Movimentos - > Documento de Entrada;

- e a rotina MATA116 ( conhecimento de frete ), do Menu: Compras -> Atualizações -> Movimentos -> Conhecimento Frete.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22672045301655)             ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22672052577559)

**Porém há uma diferença entre as duas rotinas. O fornecedor do CTE.**

Quando o fornecedor do CTE é o mesmo fornecedor da nota de origem ( compra original ), o CTE poderá ser incluído também pela MATA103 como pela MATA116, **pois para a entrada de um CTE, o tipo da Nota será igual a Complemento e o tipo do Complemento será igual a Frete.**

Com essas informações, haverá a necessidade de se vincular uma nota de origem. Toda nota de entrada do tipo Complemento, é necessário ter vínculo de uma nota de origem.

Logo, quando os fornecedores, origem e CTE forem iguais, ambas as rotinas ( MATA103 e MATA116 ) conseguirão localizar a origem pelo fornecedor ( código e loja ).

**Incluindo um CTE pela rotina Documento de Entrada ( MATA103 ).**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22672045303447)**

**O produto a ser colocado é o mesmo da origem e, o valor deverá ser informado no campo de valor total do item, e o sistema colocará o mesmo valor no campo de valor unitário. Preencha-se o TES também e, em seguida clica-se em Outras Ações -> Origem, para poder selecionar a nota de origem referente ao CTE.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22672052580759)**

**Mas, quando o fornecedor do CTE for diferente do fornecedor da origem, o CTE somente poderá ser incluído pela MATA116, pois ela propicia através das perguntas de parâmetros da rotina, que a origem possa ser procurada e localizada pelo sistema, quando os fornecedores são diferentes.**

Na parte de cima, os parâmetros para localização da nota de origem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22672052583703)

Na parte de baixo parâmetros com as informações do CTE.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22672045308951)

Mais detalhes de como incluir um CTE pela rotina MATA116, vide documento abaixo :

**[Como incluir um CTE pela rotina MATA116](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022204312-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-incluir-Nota-de-Conhecimento-de-Frete-MATA116)**

**IMPORTANTE :**

**1- ) No compras só conseguimos vincular notas de origens de entrada com os CTE´s**

Quando houver necessidade de se vincular uma nota de saída à um CTE, o módulo a ser utilizado é o GFE ( gestão de frete embarcador ), pelo compras não conseguimos.

**2-) Com o tipo da nota de entrada = Complemento não é possível vincular um pedido de compras. Por padrão somente vinculamos à origem.**

Caso seja necessário vincular um pedido de compras, o CTE pode ser incluído com o tipo da Nota = Normal, porém não haverá vínculo da nota de origem.

***Saiba Mais :***

*[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*
