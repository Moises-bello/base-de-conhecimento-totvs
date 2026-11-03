---
article_id: 4415110649239
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 9851f0529a64e4d9c8adff70272f9aadb9080ae85e8df45ddb0a000d5363681d
fetched_at: '2026-06-28T22:39:47.798105+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Resolução GECEX
  Nº 269 '
type: support-article
updated_at: '2022-06-03T19:22:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415110649239-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Resolu%C3%A7%C3%A3o-GECEX-N%C2%BA-269
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**De acordo com a **Resolução Gecex Nº 269 de 4 de novembro de 2021** foi regulamentada a medida para aplicação de uma redução de 10% nas alíquotas ad valorem do Imposto de Importação (II) de aproximadamente 87% do universo tarifário, sem abranger as exceções já existentes no Mercosul, vigente a partir e 12 de novembro de 2021.  Existe algum procedimento ou atualização a respeito dessa portaria?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Para os clientes que utilizam o SIGAEIC todo o procedimento deve ser revisado e realizado pelo cliente, conforme abaixo:  
1) A definição do imposto de importação fica na rotina de **NCM** (**EICA130**), então qualquer alteração de alíquota do imposto de importação deve ser realizada na mesma, manualmente em Atualizações \ tabelas \ NCM.  
2) Se o imposto for especifico, existe o regime de tributação que pode ser utilizado na rotina de Embarque/Desembaraço para tais situações.  
3) Temos alguns clientes que utilizam a ferramenta **ComexContent**.  Para os clientes que utilizam a ferramenta **ComexContent**: as alíquotas serão atualizadas automaticamente, a partir da data de validade.  
  
**Saiba mais**[Integração Comex Conteudo x Easy Import Control](https://tdn.totvs.com/pages/releaseview.action?pageId=224119853)
