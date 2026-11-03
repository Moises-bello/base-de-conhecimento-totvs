---
article_id: 4427846804503
category: Materiais - Compras (SIGACOM)
content_hash: 07cb7bfc8fa39f74e69c7919aa365143818df2f1fcb66e5308900c486241ec0d
fetched_at: '2026-06-28T22:41:19.978893+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Inclusão de CTE via
  Importador XML
type: support-article
updated_at: '2026-01-23T20:19:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427846804503-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Inclus%C3%A3o-de-CTE-via-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17174615163671) Tempo aproximado para leitura: **3 min** **Dúvida**Como incluir um CTE via Importador XML ?

Saiba como integrar o XML de CT-e acessando nossa página no YouTube: [How To | MP - SIGACOM - Integração XML CT-e Importador XML](https://www.youtube.com/watch?v=bJZ48a6i46Y)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - A partir da versão 12.1.25.  
  
**Solução**

No cadastro de Empresas SIGAMAT( SYS\_COMPANY) deverá constar o CNPJ conforme a informação da tag "toma3" contida no XML no caso de CTE:

Print da informação na Tag "toma" no XML:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427703495319)

Toma 03= CNPJ do destinatário  
Toma 00= CNPJ do remetente  
Toma 01= CNPJ do expedidor  
Toma 02= CNPJ do recebedor  
Toma 04= CNPJ do própria tag no XML

No cadastro do Fornecedor deverá constar o CNPJ do emitente do XML, segue o print no xml:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427900946839)

Ao importar o CTE os seguintes parâmetro precisam estar preenchidos:

![SX6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17174615172759)

**Obs1:**

O processo de CTE não leva em consideração o cadastro de Produto x Fornecedor, sendo que é verificado o produto cadastrado no parâmetro MV\_XMLPFCT ou tag de chave de documento origem como artigo contido no Saiba Mais:

[Cross Segmentos - Totvs Backoffice Protheus - Totvs Colaboração / Importador XML - Como são definidos os produtos e o Tipo de Documento na importação do Documento de Frete / CTe ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027518891)

**Obs2:**

Com relação à UF ou Estado no qual o CTe será gerado é levado em consideração, não a UF do Cadastro do Fornecedor, mas sim a UF ou Estado de Origem do serviço de Frete do CTe.

Dessa forma em um exemplo do XML abaixo em que o cadastro do Fornecedor do Frete possui Estado SC, embora o estado dele seja SC, o serviço de frete foi prestado de SP para GO. Conforme as tags abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6473956837271)

Desta forma o campo "UF Origem" do CTe assume o estado origem do Frete (SP), pois os impostos devem ser calculados partindo da origem do serviço.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Cross Segmentos - Totvs Backoffice Protheus - Totvs Colaboração / Importador XML - Como são definidos os produtos e o Tipo de Documento na importação do Documento de Frete / CTe ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027518891)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
