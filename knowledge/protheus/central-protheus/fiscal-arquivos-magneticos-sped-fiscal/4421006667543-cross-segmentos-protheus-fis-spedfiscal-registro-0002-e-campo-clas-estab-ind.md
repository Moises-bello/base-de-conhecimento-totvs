---
article_id: 4421006667543
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 98c167aaad3afe9836c3e2093f2343860b745d04f2c008ff6cddcee76ae7e6f0
fetched_at: '2026-06-28T22:42:03.672917+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Protheus - FIS - SPEDFISCAL - Registro 0002 e campo CLAS_ESTAB_IND
type: support-article
updated_at: '2022-01-31T20:24:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421006667543-Cross-Segmentos-Protheus-FIS-SPEDFISCAL-Registro-0002-e-campo-CLAS-ESTAB-IND
---

**Dúvida**Como gerar o registro 0002 na EFD ICMS/IPI e alimentar o campo 02 - **CLAS\_ESTAB\_IND** ?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
O registro 0002 será preenchido com o código da Classificação do Contribuinte conforme o preenchimento da Wizard da rotina do SPED Fiscal. O campo "Tipo de Atividade" precisar ter o conteúdo  = 0 (Industrial ou equiparado) e o campo "Classe de Atividade Industrial" precisa ter o preenchimento diferente de Branco, pois este será o preenchimento do campo no registro 0002, conforme exemplo abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/q1tSPzVO1ni7iGLl2OJ8Hrl3H/?name=inline-348726031.png)
