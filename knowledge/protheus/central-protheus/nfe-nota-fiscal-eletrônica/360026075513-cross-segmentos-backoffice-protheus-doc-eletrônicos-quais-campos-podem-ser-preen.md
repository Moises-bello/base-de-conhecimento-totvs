---
article_id: 360026075513
category: NFe - Nota Fiscal Eletrônica
content_hash: 4f3a4770de95b062e8cf5175e7fe9face17601e92b278217ed61a715dadbcd12
fetched_at: '2026-06-28T22:40:07.099506+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Quais campos podem
  ser preenchidos para gerar a TAG Xprod
type: support-article
updated_at: '2025-04-10T15:01:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026075513-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Quais-campos-podem-ser-preenchidos-para-gerar-a-TAG-Xprod
---

**Dúvida**Quais campos podem ser preenchidos para gerar a TAG Xprod ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Por padrão do **NFESEFAZ**  a TAG **<xProd>** é gerado o conteúdo do **cadastro de produto** da tabela SB1 do campo B1\_DESC e pode ser configurado para gerar da amarração da tabela SA7 **produto x cliente** ou SA5 da tabela SA7 **produto x fornecedor**.

1. **Preencher no** **TES** o poder de terceiro **diferente** de **não controla, campo *Poder Terc F4\_PODER3.*** Ao utilizar amarração ***produto x cliente***  SA5 da tabela SA7 ***produto x fornecedor***

![20220418_090239.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5516039763735)

2. Preencher no cadastro de **Produto X Cliente** os campos ***Cod. Prod Cli.*** A7\_CODCLI  ***Descr. Client.*** A7\_DESCCLI  **ou Produto X Fornecedor  *Cod. Prod For.*** A5\_CODPRF e  ***Descr. Prod. Fr.*** A5\_DESREF

![20220418_090239.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5516308305047)

![20220418_091110.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5516406906135)

3. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar**  **MV\_NFPTER =** **.T.**

![20220418_093417.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5516531207703)

* **Saiba mais:**

Os campos **(SC6->C6\_DESCRI e o SB1->B1\_DESC)** em questão são gravados com o tamanho de 30 no padrão, para que seja informado o valor de 120 caracteres será necessário fazer esta alteração em ambos.
