---
article_id: 360025899311
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 0f21a875401ec7628455aee8f3834fba56e7759aef8df345bb9f753990647e94
fetched_at: '2026-06-28T22:41:48.230125+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 PREENCHIMENTO
  DO CAMPO N1_MESCPIS
type: support-article
updated_at: '2022-10-20T13:50:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025899311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-PREENCHIMENTO-DO-CAMPO-N1-MESCPIS
---

**Ocorrência**  
Na inclusão de um ativo fixo, ao informar o numero de meses no campo N1\_MESCPIS e confirmar o ativo, retorna mensagem.

Help : AF012MESPIS

Problema : O campo [Meses Cl.Pis] deve estar zerado para a condição de cálculo de PIS igual a (SIM ou Não)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024832471/mceclip0.png)

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 12

**Causa**

Este campo é preenchido de acordo com o que foi definido no campo N1\_CALCPIS, determinando se será informada fração ou não referente ao pis.

Ao informar como sim e preencher o campo N1\_MESCPIS com numero de meses, retorna esta mensagem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024838391/mceclip3.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024841491/mceclip4.png)

**Solução**

N1\_CALCPIS - Indica a forma em que deverá ser efetuado o cálculo do crédito de PIS/Cofins, no módulo Fiscal, nas depreciações/aquisições do ativo imobilizado.

 1 = Calcula PIS/Cofins nas depreciações/aquisições. A apropriação ocorre somente no mês de  aquisição do bem. Não é necessário informar o campo Meses Cl. PIS (N1\_MESCPIS).

 2 = Não calcula PIS/Cofins nas depreciações/aquisições.

3 = Calcula PIS/Cofins nas depreciações/aquisições de forma fracionada podendo ser em 48 ou 24

meses, assim o crédito é apurado mensalmente a partir do mês de aquisição do ativo.É necessário informar o campo Meses Cl. PIS (N1\_MESCPIS).

Obs: em caso de duvida no preenchimento, entre em contato com o Time do modulo Fiscal

Veja mais :

[MP - SIGAATF - POSSIBILIDADES VÁLIDAS PARA PREENCHIMENTO DO CAMPO MESES Cl. PIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021278592-MP-SIGAATF-POSSIBILIDADES-V%C3%81LIDAS-PARA-PREENCHIMENTO-DO-CAMPO-MESES-Cl-PIS?source=search)
