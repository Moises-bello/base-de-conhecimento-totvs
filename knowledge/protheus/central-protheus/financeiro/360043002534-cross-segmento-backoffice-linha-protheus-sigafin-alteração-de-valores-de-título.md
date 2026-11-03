---
article_id: 360043002534
category: Financeiro
content_hash: a2975a7a2ed9e09c22085043b8d05c3561c64f03eccb95aa0b2c2a214ef63f9b
fetched_at: '2026-06-28T22:38:01.138580+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus- SIGAFIN - Alteração de valores
  de título gerados por Desdobramento
type: support-article
updated_at: '2022-09-05T20:21:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043002534-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Altera%C3%A7%C3%A3o-de-valores-de-t%C3%ADtulo-gerados-por-Desdobramento
---

**Dúvida**Alteração de valores de títulos gerados por desdobramento?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12.1.17  
  
**Solução**Para solucionar essa dúvida, segue os parâmetros envolvidos.

Se **MV\_NRASDSD** = **.F.** processo novo com rastreio

Na alteração do título filho do desdobramento o campo **VALOR** será bloqueado para edição (*When*).  

Se **MV\_NRASDSD** = **.T.** processo antigo sem rastreio

Na alteração do título filho será permitida a alteração do campo **VALOR**Nesse caso será exibido um aviso **QUE A ALTERAÇÃO NÃO SERÁ REPLICADA PARA OS OUTROS TÍTULOS DO DESDOBRAMENTO.**
