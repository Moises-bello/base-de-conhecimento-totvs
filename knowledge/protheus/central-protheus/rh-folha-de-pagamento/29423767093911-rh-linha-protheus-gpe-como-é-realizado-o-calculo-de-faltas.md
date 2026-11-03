---
article_id: 29423767093911
category: RH - Folha de Pagamento
content_hash: e88afe8df1c6ddd89720ceca68422f95e49018a0219894af4d822901cdb325a1
fetched_at: '2026-06-28T22:44:13.412554+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como é realizado o calculo de faltas
type: support-article
updated_at: '2025-04-28T20:01:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29423767093911-RH-Linha-Protheus-GPE-Como-%C3%A9-realizado-o-calculo-de-faltas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29423751699351) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como é realizado o calculo de faltas no padrão do sistema?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE Gestão de Pessoal - Todas as versões  
  
**Solução**Para calcular as faltas o sistema por padrão observa o salário base.  
1. Cadastramos a verba de **id 0054** em **Atualizações > Definições de Cálculos > Verbas**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29423767073943)  
2. Lance a verba de id 0054 para o funcionário desejado em **Atualizações > Lançamentos > Por Funcionários**;

![](https://i.imgur.com/tQUYWCF.png)  
3. Calculamos a folha, onde podemos validar que o sistema realiza o calculo conforme o Salario Base observando o campo RA\_SALARIO no cadastro do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29423910815511)

**Calculo realizado:**

Salário Base/ dias mês \* dias lançados de falta

R$2442,80/30 dias mês= 81,43

**Importante:** No padrão o calculo das faltas para funcionários horistas como para funcionários mensalistas, tem com base o Salário, caso desejem que seja calculado com uma base diferente, como piso sindicato, salário mínimo, somente verificando a possibilidade de customização do ambiente.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
