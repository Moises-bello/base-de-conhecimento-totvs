---
article_id: 360028611432
category: Materiais - Compras (SIGACOM)
content_hash: 071738d07da58e419b9b0fb4dd2964201b8890d11ecba4b77d3340c70786675a
fetched_at: '2026-06-28T22:41:18.800155+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A100ASSIQS -
  Situação não permitida: Fornecedor não possui IQS'
type: support-article
updated_at: '2022-05-18T20:55:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028611432-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A100ASSIQS-Situa%C3%A7%C3%A3o-n%C3%A3o-permitida-Fornecedor-n%C3%A3o-possui-IQS
---

**Dúvida**

Help A100ASSIQS - Situação não permitida: Fornecedor não possui IQS

 

**Ambiente**Protheus – Compras – A partir da versão 11.80

**Solução**

Ao alterar o cadastro do fornecedor na rotina MATA060 o sistema exibe a mensagem, situação não  permitida fornecedor não possui IQS.

Como definir o IQS.

Os fatores de IQS são cadastrados e definidos na rotina 'Fatores de IQS' no menu 'Atualizações', opção 'Índice Qualidade', rotina 'Fatores de IQS'.

Esta mensagem ocorre quando o parâmetro ***MV\_QASSIQS*** está configurado como "N", indicando que o arquivo Produto X Fornecedor (SA5) possui a situação "Assegurado" sem Nota de IQS definida.  
  
Para permitir o preenchimento da situação "A" altere o parâmetro acima para S.

***Saiba Mais :***

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
