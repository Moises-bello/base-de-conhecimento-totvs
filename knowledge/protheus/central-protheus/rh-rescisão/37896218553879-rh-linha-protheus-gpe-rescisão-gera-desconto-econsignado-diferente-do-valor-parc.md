---
article_id: 37896218553879
category: RH - Rescisão
content_hash: 5efae0debadf4abfb49bfa8d8db47af9ce18c0cd6e1dc71aaafe761dda04bdb2
fetched_at: '2026-06-28T22:43:50.865232+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Rescisão gera desconto eConsignado diferente do
  valor parcela valores futuros
type: support-article
updated_at: '2026-01-26T11:38:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37896218553879-RH-Linha-Protheus-GPE-Rescis%C3%A3o-gera-desconto-eConsignado-diferente-do-valor-parcela-valores-futuros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37896218543895) Tempo aproximado para leitura: **01:30  min**  
  
**Dúvida**  
Por que rescisão gera desconto eConsignado diferente do valor parcela valores futuros?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
O cálculo considera margem INSS (somar verbas de provento Sim INSS, menos verbas de desconto Sim INSS, menos desconto INSS, IR, pensão e aplica os 35%), se a margem for inferior ao valor parcela, desconta a margem.

**Exemplo:**

**Valores futuros:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37896218544535)

**Valor parcela 500,00**

**Rescisão**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37896218547223)

**2.012,90 (salário) - 838,71 (faltas) - 88,06 (INSS) = 1.086,13 \* 35% = 380,15 valor desconto.**

**Como a margem 35% 380,15 é inferior ao valor parcela 500,00, no calculo é gerado valor margem 380,15.**

**Obs: A formula padrão considera verbas sim INSS, INSS, IRRF e pensão, para considerar verbas de provento Não INSS em base, lançar verba em mnemonico** **P\_ADICON e verbas de desconto Não INSS lançar em mnemonico P\_DEDCONS.**

Saiba Mais:

[RH - Linha Protheus - GPE - Cálculo eConsigando em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32327889957271-RH-Linha-Protheus-GPE-C%C3%A1lculo-eConsigando-em-rescis%C3%A3o)
