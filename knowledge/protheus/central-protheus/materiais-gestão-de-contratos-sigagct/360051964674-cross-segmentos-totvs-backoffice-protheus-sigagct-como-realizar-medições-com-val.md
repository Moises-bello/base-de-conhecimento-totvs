---
article_id: 360051964674
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: c114c000d585cb9c9540b0bd76ea007960c8dead6d984f028543c03bb17db70e
fetched_at: '2026-06-28T22:37:21.649627+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar medições
  com valores maior que o previsto no Cronograma Financeiro do Contrato ?
type: support-article
updated_at: '2025-05-02T20:13:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051964674-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-medi%C3%A7%C3%B5es-com-valores-maior-que-o-previsto-no-Cronograma-Financeiro-do-Contrato
---

**Dúvida**Como realizar medições com valores maior que o previsto no Cronograma Financeiro do Contrato ?

**Ambiente**Protheus – Gestão de Contratos – A partir da versão 12.1.23

**Solução**

Para a necessidade de realização de medições com valor maior que o programado na parcela do Cronograma do Contrato, há disponível no módulo Gestão de Contratos a configuração dos campos de "Limite de Medição" existentes no cadastro do Tipo de Contrato (**CN1\_LMTMED**) e no Tipo de Planilha (**CNL\_LMTMED**) a serem utilizados no Contrato, onde se define o percentual de limite a maior.

Campo no Tipo de Contrato (CN1\_LMTMED):

![](https://totvssuporte.zendesk.com/attachments/token/EQK9vj32WdwWlaurFOCbjCNZk/?name=inline429210754.png)

Campo no Tipo de Planilha (CNL\_LMTMED):

![](https://totvssuporte.zendesk.com/attachments/token/01dIEamWTLJEh05F29mwtB5VZ/?name=inline-747370048.png)

Lembrando que a configuração realizada no campo do Tipo de Planilha sobrepõe a configuração realizada no campo do Tipo de Contrato, na utilização de configurações diferentes em um mesmo contrato.

**Obs1:**

Quando realizada uma medição com valor maior que o previsto da parcela conforme a configuração do Tipo de Contrato/Planilha, na linha da parcela do cronograma o saldo da parcela fica com valor negativo, e isso é normal, devido a medição com valor maior que o previsto:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484556251159)

**Obs2:**

Na utilização do campo de "Limite Med" informado, e realização de medições com valores maiores que o Previsto na Parcelas do Cronograma, como será consumido um saldo do contrato maior que o Previsto, posteriormente, se as parcelas posteriores não forem medidas com valores menores que os seus previstos, o contrato precisará sofrer revisão para inclusão de Saldo Total, para haver este saldo no montante total disponível no Contrato para realização das medições dessas parcelas posteriores.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
