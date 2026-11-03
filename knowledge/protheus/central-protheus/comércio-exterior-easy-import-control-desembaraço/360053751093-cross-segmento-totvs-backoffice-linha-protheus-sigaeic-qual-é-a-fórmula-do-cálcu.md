---
article_id: 360053751093
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 65e804341e74ed1bc438553d6828015d7804859592697b39c8a716c89ec37fa7
fetched_at: '2026-06-28T22:39:49.808328+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEIC -  Qual é a fórmula
  do cálculo do rateio de despesas base de imposto?
type: support-article
updated_at: '2022-04-08T20:10:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053751093-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Qual-%C3%A9-a-f%C3%B3rmula-do-c%C3%A1lculo-do-rateio-de-despesas-base-de-imposto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Qual é a fórmula do calculo do rateio de despesas base de imposto?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**No processo se você tem uma quantidade 100 peças e uma despesa no valor de R$ 20,00, e a quantidade correspondente do primeiro item de 40 peças e do segundo item 60 peças,  a despesa será rateada no valor de (40%) para o primeiro item e no segundo (60%) para o peso é a mesma regra o que determina é a configuração da despesa, como regra  a despesa de frete sempre é rateada por peso.  
O rateio das despesas levam em consideração o cadastro da despesa, podendo ser por valor ou por peso, conforme determinado no campo "Rateia por Peso?" (YB\_RATPESO), por padrão através do valor FOB(valor da mercadoria).  
Caso o parâmetro **MV\_RATCIF** esteja habilitado *True*, o rateio ocorre através do valor **CIF** (valor da mercadoria + frete + seguro).  
Para a despesa referente a taxa Siscomex, caso o parâmetro **MV\_RATCIF** esteja habilitado *True*, esta despesa é rateada pelo valor CIF, caso esteja desligado, é rateada da mesma maneira que as outras despesas rateadas por valor.  
  
**Observação:** Utilizar o parâmetro **MV\_EIC0016** habilitado para o processo que possui DI Eletrônica (parâmetro MV\_TEM\_DI - habilitado);   
  
**Saiba mais**  
[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Desconsiderar despesas base de imposto sim e base de custo não do valor da mercadoria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036771273)
