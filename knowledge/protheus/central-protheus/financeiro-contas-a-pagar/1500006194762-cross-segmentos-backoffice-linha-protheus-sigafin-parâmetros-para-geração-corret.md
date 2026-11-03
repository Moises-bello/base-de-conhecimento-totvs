---
article_id: 1500006194762
category: Financeiro - Contas a Pagar
content_hash: afb9b8e6c5b2834092457a63f7c7345a6a4941bebb6be83fa4a1a2ad2f232d2d
fetched_at: '2026-06-28T22:38:07.150559+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Parâmetros para geração
  correta dos impostos PCC e IR para Empresa Pública
type: support-article
updated_at: '2022-08-05T16:52:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006194762-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Par%C3%A2metros-para-gera%C3%A7%C3%A3o-correta-dos-impostos-PCC-e-IR-para-Empresa-P%C3%BAblica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como gerar os impostos PCC e IR para empresa Pública  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Para a geração correta dos impostos PCC e IR quando a empresa é publica (MV\_ISPPUBL = 1) é necessário que os parâmetros **MV\_VL10925** e **MV\_VLRETIR** estejam zerados e os parâmetro **MV\_BX10925** e **MV\_ISPPUBL** estejam com seus conteúdos iguais a 1.

**Saiba Mais**:  
[DT\_EMPRESA\_PUBLICA\_CARTEIRA\_PAGAR](https://tdn.totvs.com/display/public/PROT/TUB906_DT_EMPRESA_PUBLICA_CARTEIRA_PAGAR)
