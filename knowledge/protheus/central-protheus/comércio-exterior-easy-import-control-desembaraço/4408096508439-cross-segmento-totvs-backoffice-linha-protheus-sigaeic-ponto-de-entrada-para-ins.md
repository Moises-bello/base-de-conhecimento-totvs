---
article_id: 4408096508439
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: a2868c34c6bc833cf3527a79e93b4fb041901a028f3a4d5446cd983366515158
fetched_at: '2026-06-28T22:39:50.154062+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de entrada
  para inserir despesa automaticamente na tabela SWD ao gerar a nota de importação
type: support-article
updated_at: '2021-09-08T19:00:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408096508439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-entrada-para-inserir-despesa-automaticamente-na-tabela-SWD-ao-gerar-a-nota-de-importa%C3%A7%C3%A3o
---

**Dúvida**Qual ponto de entrada posso utilizar para inserir uma despesa automaticamente na SWD no momento que é gravada a nota de entrada tipo única ou mãe?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Import Control – Todas versões  
  
**Solução**Pode ser utilizado o ponto de entrada **GRAVACAO\_SF1** da função EICDI154 (Recebimento de importação).  
Este ponto de entrada é executado antes do ExecAuto com o Compras.  
  
Segue documentação sobre o ponto de entrada:  
[PE EICDI154 - Recebimento de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=574364993)
