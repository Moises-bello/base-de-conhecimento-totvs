---
article_id: 360031412954
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 00516f64c4a19a2b9aedea512d4b7c13b698b719eb43248cb023e657f76a221f
fetched_at: '2026-06-28T22:39:49.925424+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC -  NOFUNCW_MENUDEFCalledByADICAOTELA
type: support-article
updated_at: '2022-01-24T19:28:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031412954-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-NOFUNCW-MENUDEFCalledByADICAOTELA
---

**Dúvida**Correção função NOFUNCW\_MENUDEFCalledByADICAOTELA  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**O sistema foi corrigido para não duplicar os itens ao acessar as adições.  
Foi substituído o fonte **EICADICAO\_RDM.PRW** pelo **EICADICAO.PRW**.   
O fonte **EICADICAO\_RDM.PRW** deve ser excluído do repositório, para remover o fonte siga as instruções do link: [PSIGABD0072 - Totvs Developer Studio - Compilar e descompilar (Excluir) fontes do RPO](http://tdn.totvs.com/pages/viewpage.action?pageId=274332945).  
  
Após exclusão do EICADICAO\_RDM.PRW, favor aplicar o pacote abaixo, que consta o EICADICAO.PRW:  
[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pacote Acumulado Comex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pacote-Acumulado-Comex)
