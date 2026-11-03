---
article_id: 37542614661527
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2d13a50b65ed7e16799aae99db51d342ff75eaaa83a532e242e8a3250248eac8
fetched_at: '2026-06-28T22:38:55.751843+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA175 - array out
  of bounds ( 0 of 22 )  on A175QUANT(MATA175.PRX)
type: support-article
updated_at: '2026-01-09T11:20:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37542614661527-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA175-array-out-of-bounds-0-of-22-on-A175QUANT-MATA175-PRX
---

O erro "array out of bounds (0 of 22) on A175QUANT(MATA175.PRX)" durante a baixa ocorre ao aprovar/rejeitar produto no controle de qualidade e pode estar relacionado ao posicionamento incorreto ou ao campo da segunda unidade de medida (D7\_QTSEGUM) não estar marcado como "Usado".

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37542614645143) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Durante o processe de baixa, ocorre o erro array out of bounds ( 0 of 22 )  on A175QUANT(MATA175.PRX), oque fazer para corrigir?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Ao tentar aprovar/rejeitar produto pelo controle de qualidade, é exibido o erro:

THREAD ERROR array out of bounds ( 0 of 22 )  on A175QUANT(MATA175.PRX) 13/04/2025 13:15:48 line : 2134  
Called from {|| (Positivo() .And. A175Quant()) .and. (.t.) .and. (A175GetDad())}(MSGETDAD.PRW) 03/12/2025 18:11:27 line : 1274  
----  
Called from MATA175(MATA175.PRX) 13/04/2025 13:15:48 line : 86  
Called from \_\_EXECUTE(APLIB090.PRW) 03/12/2025 18:11:24 line : 735  
Called from MDIEXECUTE(APLIB260.PRW) 03/12/2025 18:11:24 line : 921

Validamos que esse problema pode ser vinculado a posicionamento no campo da segunda unidade de medida (D7\_QTSEGUM), ou o campo não estar marcado como "Usado".

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Rotina MATA175 - Instruções padrões sobre Controle de Qualidade no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA175-Instru%C3%A7%C3%B5es-padr%C3%B5es-sobre-Controle-de-Qualidade-no-Estoque)
