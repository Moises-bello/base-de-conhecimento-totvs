---
article_id: 1500011483182
category: Call Center - Televendas
content_hash: e2c305cdf23b7cab37640f221837dadf74d6b1dc999afc80190bfa66754f927b
fetched_at: '2026-06-28T22:41:30.228187+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Código de Intermediador no
  Call Center
type: support-article
updated_at: '2024-04-29T13:13:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011483182-Cross-Segmentos-Backoffice-Protheus-SIGATMK-C%C3%B3digo-de-Intermediador-no-Call-Center
---

**Dúvida**Como utilizar o Código do Intermediador no Call Center, uma vez que o atendimento televendas pode gerar pedido de vendas ou nota fiscal direto?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

Em atendimento à legislação da Nota Técnica 2020.006,  foi adicionado um tratamento do campo do "**Código do Intermediador"** nas rotinas do **Pedido de Venda** e na **Emissão do Documento Fiscal de Saída,** sendo criados os campos **C5\_INDPRES** e **C5\_CODA1U** no pedido de vendas, e o campo **F2\_CODA1U** no Documento de Saída, além do parâmetro **MV\_NT2006I**.

Para adequar o módulo Call Center, para que o orçamento televendas (**TMKA273**) possa enviar as informações para o pedido de vendas preenchido, foram criados os campos **UA\_INDPRES** e **UA\_CODA1U** no cabeçalho de **Atendimento Televenda** (**SUA**), que são os campos pares para **C5\_INDPRES** e **C5\_CODA1U** no pedido de vendas.

Para criação dos campos  e parâmetro, além das tabelas envolvidas no processo, é necessário executar o **UPDDISTR** com o **SDFBRA** (Pacote de Dicionário) disponível em: **<https://suporte.totvs.com/portal/p/10098/download?e=1013133>**

**Obs: Os campos do Call Center foram incorporados neste sdfbra.**

Ainda para o Call Center, é necessário aplicar o pacote expedição contínua do módulo que já contém, as alterações de fontes para considerar os novos campos da SUA :  **[SIGATMK](https://tdn.totvs.com/pages/releaseview.action?pageId=521997552)**

**Saiba mais:** **[11013572 DSERFAT-19681 DT TeleVenda - Código do Intermediador](https://tdn.totvs.com/x/YqoPJ)**

**Saiba mais a respeito da NT2020.006 - Indicativo de presença e intermediador nos links abaixo:**

* **[DT Nota Técnica 2020.006 Intermediador da Operação Marketplace e outros](https://tdn.totvs.com/x/KmsIJ)**
* **[NT2020.006 - Indicativo de presença e intermediador](https://tdn.totvs.com/x/sb0oJ)**
