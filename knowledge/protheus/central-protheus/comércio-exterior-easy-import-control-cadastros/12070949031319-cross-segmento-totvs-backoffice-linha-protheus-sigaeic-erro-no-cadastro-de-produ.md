---
article_id: 12070949031319
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: f9dc5f90d1ab9927206b1cad7dc040d6c8eb279266c624984265752dfe59bb8f
fetched_at: '2026-06-28T22:39:52.194306+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Erro no cadastro
  de Produto type mismatch on compare on EXISTESFCPCP(MATA010PCP.PRW) '
type: support-article
updated_at: '2023-01-31T20:22:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12070949031319-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-no-cadastro-de-Produto-type-mismatch-on-compare-on-EXISTESFCPCP-MATA010PCP-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **01:00:00 min** **Dúvida**Ao alterar o cadastro de produto (**MATA010**) no SIGAEIC apresenta o erro ***type mismatch on compare on EXISTESFCPCP(MATA010PCP.PRW) .*** O que fazer para corrigir o erro?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – a partir da versão 12.1.27.  
  
**Solução**Este erro ocorre pois parâmetro **MV\_INTSFC** esta configurado incorretamente. O tipo esta cadastrado como **Lógico** sendo que o correto deve ser do tipo **Numérico** e o conteudo do parametro deve ser numerico também. 

![MV_INTSFC.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/12065678610839)

Será necessário alteração do parametro pelo configurador e uma vez efetuado este procedimento o erro não ocorerá mais.
