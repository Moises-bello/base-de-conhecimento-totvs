---
article_id: 4403121832471
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 1d81be03d49a8501ee763d70b253ecb1d2fa6c68fab2f7d425af4765818e0287
fetched_at: '2026-06-28T22:38:30.065770+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FAT - Ponto de Entrada
  MA030BUT não funciona
type: support-article
updated_at: '2025-01-10T20:15:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403121832471-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FAT-Ponto-de-Entrada-MA030BUT-n%C3%A3o-funciona
---

**Dúvida**Ponto de Entrada MA030BUT não funciona após versão 12 do Protheus .

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Faturamento - Todas as versões  
  
**Solução**Verifique na tabela **SX3** se consta no dicionário de dados a tabela **G3Q**, caso conste, sua a rotina já está no padrão MVC, desta forma, é necessário que a implementação do código siga o padrão da documentação abaixo:

**ADVPL utilizando MVC**  
<http://tdn.totvs.com/display/public/mp/AdvPl+utilizando+MVC>  
  
**Pontos de Entrada MVC MATA030 na P12**  
<http://tdn.totvs.com/display/PROT/ADV0065_PE_MVC_MATA030_P12>  
  
Segue também uma documentação constando a maioria das rotinas que já estão no padrão MVC:  
  
**Fontes em MVC**  
<http://tdn.totvs.com/display/PROT/Fontes+em+MVC>
