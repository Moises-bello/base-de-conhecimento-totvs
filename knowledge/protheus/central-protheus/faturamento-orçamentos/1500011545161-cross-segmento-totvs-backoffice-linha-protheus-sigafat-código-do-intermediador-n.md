---
article_id: 1500011545161
category: Faturamento - Orçamentos
content_hash: c3d85c473222287730e88270de468893bebf2e9bd5b97c097ea8135552e4744b
fetched_at: '2026-06-28T22:38:24.920938+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Código do intermediador
  no Orçamento de Vendas
type: support-article
updated_at: '2021-12-08T19:19:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011545161-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-C%C3%B3digo-do-intermediador-no-Or%C3%A7amento-de-Vendas
---

**Dúvida**Como utilizar o Código do Intermediador no Orçamento de Vendas, uma vez que a efetivação do orçamento gera pedido de vendas?

**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT  - A partir da versão 12.  
  
**Solução**

Em atendimento à legislação da Nota Técnica 2020.006,  foi adicionado um tratamento do campo do "**Código do Intermediador"** nas rotinas do **Pedido de Venda** e na **Emissão do Documento Fiscal de Saída,** sendo criados os campos **C5\_INDPRES** e **C5\_CODA1U** no pedido de vendas, e o campo **F2\_CODA1U** no Documento de Saída, além do parâmetro **MV\_NT2006I**.

Para adequar  o orçamento de vendas (**MATA415**), para que  possa enviar as informações para o pedido de vendas preenchido na sua efetivação, foram criados os campos **CJ\_INDPRES** e **CJ\_CODA1U** no cabeçalho do orçamento (**SCJ**), que são os campos pares para **C5\_INDPRES** e **C5\_CODA1U** no pedido de vendas (**MATA410**).

Para criação dos campos  e parâmetro, além das tabelas envolvidas no processo, é necessário executar o **UPDDISTR** com o **SDFBRA** (Pacote de Dicionário) disponível em: **<https://suporte.totvs.com/portal/p/10098/download?e=1013133>**

**Obs: Os campos do Orçamento  foram incorporados neste sdfbra.**

Ainda para o Orçamento, é necessário aplicar o pacote expedição contínua do módulo que já contém, as alterações de fontes para considerar os novos campos da **SCJ**: **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**

**Saiba mais:** **[11198080 DSERFAT-20035 DT Orçamentos de Venda - Código Intermediador](https://tdn.totvs.com/x/inenJ)**

**Saiba mais a respeito da NT2020.006 - Indicativo de presença e intermediador nos links abaixo:**

**<https://tdn.totvs.com/x/KmsIJ>**

**<https://tdn.totvs.com/x/sb0oJ>**

**[11013572 DSERFAT-19681 DT TeleVenda - Código do Intermediador](https://tdn.totvs.com/x/YqoPJ)**
