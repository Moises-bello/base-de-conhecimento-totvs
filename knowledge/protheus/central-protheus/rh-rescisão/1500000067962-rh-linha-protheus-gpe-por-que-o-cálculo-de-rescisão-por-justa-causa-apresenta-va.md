---
article_id: 1500000067962
category: RH - Rescisão
content_hash: 3e916332454cc6dbffe76577140ab7e1d13ee89675d76d882a0c7c6c08db9437
fetched_at: '2026-06-28T22:43:53.646341+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que o cálculo de rescisão por justa causa apresenta
  valor de IR 13. Salário
type: support-article
updated_at: '2023-11-20T13:40:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000067962-RH-Linha-Protheus-GPE-Por-que-o-c%C3%A1lculo-de-rescis%C3%A3o-por-justa-causa-apresenta-valor-de-IR-13-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19194262823703)** Tempo aproximado para leitura:**00:01:30 min**

**Dúvida**Por que o cálculo de rescisão por justa causa apresenta valor de IR 13. Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**A rescisão não apresenta o valor de 13 salário, quando no tipo de rescisão em tabela S043 está com N para 13. Caso seja lançada alguma verba com incidência IR Sim e Ref 13 Salário Sim, o Sistema irá calcular imposto de renda quando o valor do lançamento se enquadrar em tabela de desconto

**Exemplo:**

**Tabela S043**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098944014)

**Obs: A tabela S043 é configurada conforme cada entendimento quanto aos pagamentos rescisão por justa causa.**

**Cálculo Rescisão.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000068182)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000068242)

**Neste exemplo a verba 210 (hora extra 100%), está configurada com incidência Sim para IR e Sim para Ref 13. Salário e por este motivo o Sistema calculou o IR 13. Salário.**

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

[RH - Linha Protheus - GPE - Como parametrizar a tabela S043 para cadastrar um novo tipo de rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004395831-RH-Linha-Protheus-GPE-Como-parametrizar-a-tabela-S043-para-cadastrar-um-novo-tipo-de-rescis%C3%A3o?source=search)
