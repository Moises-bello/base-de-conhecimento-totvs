---
article_id: 6343522319383
category: Financeiro
content_hash: 7dbdebaac1d6b8b827154a4f4b0bf675c0965e6f11cb7d7caa84076cf702d41c
fetched_at: '2026-06-28T22:38:01.164736+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus -  SIGAFIN - HELP: USONATGR'
type: support-article
updated_at: '2025-10-10T11:36:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6343522319383-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-HELP-USONATGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35542831051543) Tempo aproximado para leitura: **00:05 min****Ocorrência**Durante a movimentação Bancária ocorre HELP: USONATGR

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6342883361303)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**No cadastro de natureza FINA010 o campo ED\_USO, está preenchido com um tipo específico dentro das possibilidades:  
1. Contas da Receber  
2. Contas a Pagar  
3. Mov. Bancária

**Solução**Acesse o cadastro de natureza (**FINA010**) e altere o campo **ED\_USO** para o valor **0 – Livre**.  
Dessa forma, não haverá restrição para a utilização da natureza durante a movimentação bancária.

**Saiba mais**[892799 DSERFINP-2148 DT Help USONATGR na variação monetária (FINA350)](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=315229561)  
[Naturezas - FINA010 - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Naturezas+-+FINA010+-+Financeiro+-+P12)
