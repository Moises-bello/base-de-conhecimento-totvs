---
article_id: 39166545622039
category: SIGAEST - MOVIMENTAÇÕES
content_hash: fd8736a1f3bb372ac7694ff522e0d96f32623e81634f1b4ad274076c8fa33038
fetched_at: '2026-06-28T22:38:54.323528+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Array out of bounds
  ( 0 of 93 ) on A241LINOK(MATA241.PRX) 15/12/2025 11:54:06 line : 2807'
type: support-article
updated_at: '2026-03-20T11:55:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39166545622039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Array-out-of-bounds-0-of-93-on-A241LINOK-MATA241-PRX-15-12-2025-11-54-06-line-2807
---

O erro "array out of bounds" ao salvar uma Movimentação Interna (MATA241) ocorre porque a função interna A241LINOK não é encontrada. A solução é acessar o configurador e marcar o campo D3\_Sublote como usado na aba USO.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39166545616279) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao tentar salvar uma Movimentação Interna (MATA241) apresenta o error.log abaixo. Como resolver?

THREAD ERROR ([3897696], protheus, UNKNOWHOST) 18/03/2026 10:16:26  
**array out of bounds ( 0 of 93 ) on A241LINOK(MATA241.PRX) 15/12/2025 11:54:06 line : 2807**

[TOTVS build: 7.00.240223P-20260211]  
Called from { |x| A241LinOk(x)}(MSGETDAD.PRW) 25/02/2026 13:54:48 line : 543  
Called from MSGETDADOS:LINHAOK(MSGETDAD.PRW) 25/02/2026 13:54:48 line : 547  
Called from MSGETDADOS:TUDOOK(MSGETDAD.PRW) 25/02/2026 13:54:48 line : 714  
Called from {||(AEVAL(ACAMPOSVLD,BBLKVLD),IIF(OGET:TUDOOK() .AND. CHKGETFIX(ACAMPOSVLD, .F. , .T. ) .AND. CHKOPSUSP(),(ODLG:END(),NOPCA:=1),NOPCA:=0))}(MATA241.PRX) 15/12/2025 11:54:06 line : 1050  
Called from SAFEEVAL(MSLIB.PRW) 25/02/2026 13:54:48 line : 7088  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Esse incidente ocorre devido não encontrar a função interna A241LINOK, pois a mesma esta declarada na rotina MATA241 de 15/12/2025.

**Solução**  
Para solução do error.log é necessário acessar o configurador, e colocar o campo **D3\_Sublote**como **usado**, na aba **USO**.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
