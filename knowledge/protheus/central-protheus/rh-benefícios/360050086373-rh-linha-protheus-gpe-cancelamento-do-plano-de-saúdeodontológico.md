---
article_id: 360050086373
category: RH - Benefícios
content_hash: 6ad4f14ca6997d233a912e3e498e1239373685bf92bf188f99ec9db71192336c
fetched_at: '2026-06-28T22:44:03.617453+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cancelamento do Plano de Saúde/Odontológico
type: support-article
updated_at: '2025-12-05T13:51:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050086373-RH-Linha-Protheus-GPE-Cancelamento-do-Plano-de-Sa%C3%BAde-Odontol%C3%B3gico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15496960001943) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como realizar o cancelamento do plano de saúde/odontológico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Para a exclusão do plano deve ser informado a data fim no campo "**Per. Final"** na Rotina de Planos Ativos (GPEA001)

**Obs.:** Para o cancelamento dos dependentes e agregados aplica-se o mesmo procedimento.

Rotina: **Atualizações / Benefícios / Planos de Saúde / Planos de Saúde Ativos:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15496854386583)  
  
Após o fechamento do período, o plano cancelado sai da rotina de Planos Ativos e vai para o Histórico de Alterações - GPEA002 **(Atualizações/ Benefícios / Planos de Saúde / Histórico Alterações de Planos)**

O campo **"Data Fim"** só deve ser preenchido caso queira proporcionalizar o cálculo do plano de saúde.   
Veja a documentação: [RH - Linha Protheus - GPE - Cálculo do plano de saúde proporcional após encerramento do plano](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwheUyTVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBrGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1ODIxMzIxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQyVDMyVBMWxjdWxvLWRvLXBsYW5vLWRlLXNhJUMzJUJBZGUtcHJvcG9yY2lvbmFsLWFwJUMzJUIzcy1lbmNlcnJhbWVudG8tZG8tcGxhbm8GOwhUOg5zZWFyY2hfaWRJIik4MzU3MmNiNi1iOGY4LTQ1ZjctYmUwMy1mNWU0MDgzOGY5NDIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJImVSSCAtIExpbmhhIFByb3RoZXVzIC0gR1BFIC0gQ8OhbGN1bG8gZG8gcGxhbm8gZGUgc2HDumRlIHByb3BvcmNpb25hbCBhcMOzcyBlbmNlcnJhbWVudG8gZG8gcGxhbm8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--d39e588d36303dec51571f13eddddfe24a5f2cae)

**Atenção!**

Na rotina de Plano de saúde Ativo, quando cadastrado o período final **com a data do período em aberto**,  o sistema entende que o cálculo deverá ser feito **até o mês em questão**, exemplo, se preenchido com 06/2020, então o plano ficará ativo até o final do mês de junho.  
  
Caso a empresa não queira que este desconto ocorra no mês vigente, a data fim cadastrada deverá ser do **mês anterior**. No entanto orientamos que este cadastro seja feito **antes do fechamento da folha e antes do fechamento do roteiro de cálculo em questão.**

**Saiba Mais**[RH - Linha Protheus - GPE - Histórico de planos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051263014-RH-Linha-Protheus-GPE-Hist%C3%B3rico-de-planos-ativos)[RH - Linha Protheus - GPE - Como excluir / cancelar o cálculo do plano de saúde](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054180934-RH-Linha-Protheus-GPE-Como-excluir-cancelar-o-c%C3%A1lculo-do-plano-de-sa%C3%BAde?source=search)  
[RH - Linha Protheus - GPE - Transferência em Lote do Plano de Saúde/Odontológico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042994494--RH-Linha-Protheus-GPE-Transfer%C3%AAncia-em-Lote-do-Plano-de-Sa%C3%BAde-Odontol%C3%B3gico?source=search)  
[RH - Linha Protheus - GPE - Pontos de Entrada na rotina Cálculo de Plano de Saúde - GPEM016](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059782094-RH-Linha-Protheus-GPE-Pontos-de-Entrada-na-rotina-C%C3%A1lculo-de-Plano-de-Sa%C3%BAde-GPEM016?source=search)
