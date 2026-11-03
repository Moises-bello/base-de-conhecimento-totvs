---
article_id: 4412890914711
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 733c2795491c27ed3846fb29f818519d261088913bb9cdfc599dc9ac3a1ca2ef
fetched_at: '2026-06-28T22:39:50.156895+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de entrada
  para não permitir gerar a nota quando há diferença dos valores
type: support-article
updated_at: '2021-11-11T19:12:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890914711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-entrada-para-n%C3%A3o-permitir-gerar-a-nota-quando-h%C3%A1-diferen%C3%A7a-dos-valores
---

**Dúvida**Gostaria de saber se existe um ponto de entrada para não permitir gerar a nota de importação (**EICDI154**) quando há diferença dos valores informados x calculados?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**É possível utiliza o ponto de entrada Execblock(**"EICDI154",.F.,.F.,"FINALGRAVA**") que é chamado após a apuração dos valores do recebimento de importação, permite determinar se o sistema deverá prosseguir com a geração do recebimento de importação. Neste momento estará disponível a variável **lRetorno**. Vide também a variável [**lComDiferenca**](https://tdn.totvs.com/pages/releaseview.action?pageId=574364993).   
Este cenário é somente para os ambientes que estão com o parâmetro **MV\_TEM\_DI = F** .  
  
**Saiba mais**[PE EICDI154 - Recebimento de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=574364993)
