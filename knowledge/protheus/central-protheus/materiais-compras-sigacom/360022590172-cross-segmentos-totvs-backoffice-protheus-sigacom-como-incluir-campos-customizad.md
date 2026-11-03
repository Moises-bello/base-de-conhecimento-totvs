---
article_id: 360022590172
category: Materiais - Compras (SIGACOM)
content_hash: db6a807ae452c168d2e90baa198b9347bfb9e56634983da4f7b227e4594c07b9
fetched_at: '2026-06-28T22:41:07.672295+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir campos
  customizados na rotina Analisa Cotação (MATA161) ?
type: support-article
updated_at: '2022-05-16T22:21:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022590172-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-incluir-campos-customizados-na-rotina-Analisa-Cota%C3%A7%C3%A3o-MATA161
---

**Dúvida:**  
Como incluir campos customizados na rotina Analisa Cotação (MATA161) ?  
  
**Ambiente:**  
Protheus - Compras – 12.1.17

**Solução:**  
Grande parte das rotinas em MVC não podem sofrer alterações em sua ordenação de campos, por esse motivo a inclusão de campos customizados deve ser efetuada via ponto de entrada.

Para a rotina em questão, devemos utilizar o ponto de entrada ***MT161CPO***.

O Ponto de Entrada ***MT161CPO*** permite incluir campos customizados nas grids "Produtos" e "Item da Proposta".

A chamada deste Ponto de Entrada ocorre ao clicar no botão "Análise da cotação" na rotina Analisa Cotações (MATA161).

**Saiba mais:**<http://tdn.totvs.com/display/public/PROT/MT161CPO+-+Ponto+de+entrada+para+incluir+campos+customizados+no+MATA161>
