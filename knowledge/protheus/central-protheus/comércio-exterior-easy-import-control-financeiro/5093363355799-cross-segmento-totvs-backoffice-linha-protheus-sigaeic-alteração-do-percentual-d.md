---
article_id: 5093363355799
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 45669371c3be589d2890fc87387fe7651fd36e34a1b78d108a490aab703e99db
fetched_at: '2026-06-28T22:39:44.447176+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Alteração do percentual
  da AFRMM legislação nº 14.301
type: support-article
updated_at: '2022-03-29T13:35:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5093363355799-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Altera%C3%A7%C3%A3o-do-percentual-da-AFRMM-legisla%C3%A7%C3%A3o-n%C2%BA-14-301
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Gostaríamos de saber, o que temos que alterar no protheus, por conta da publicação **lei nº 14.301**, que altera o percentual aplicado para cálculo do AFRMM?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Na rotina de cadastro de despesas (**EICA110**) ,temos a despesa de código 405 que é AFRMM. Nela temos o campo Tipo que seria o percentual (**YB\_IDVL**)  e o campo do Percentual aplicado (**YB\_PERCAPL**), é só atualizar o campo Percentual aplicado para o percentual novo, com isso o valor da despesa é informado manualmente pelo usuário e somente é necessário se atentar aos valores informados. Reforçando que se o cliente utiliza a tabela de pré calculo (**EICTC210**) será necessário fazer o ajuste da despesa AFRMM, caso tenha esta despesa cadastrada.   
Segue abaixo um print da despesa e os campos citados em questão:

![DESPESA_AFRMM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5093340410775/DESPESA_AFRMM.png)
