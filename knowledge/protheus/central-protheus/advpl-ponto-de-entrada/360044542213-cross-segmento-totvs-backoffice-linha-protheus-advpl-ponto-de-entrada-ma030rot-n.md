---
article_id: 360044542213
category: ADVPL - Ponto de Entrada
content_hash: 6ee7f58e79f944eddefc86271bda3a6bb2d68eebe4cac6528616cb4175fa948d
fetched_at: '2026-06-28T22:40:11.849571+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MA030ROT não executa com o parâmetro MV_MVCSA1 ativo
type: support-article
updated_at: '2021-12-29T20:57:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044542213-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MA030ROT-n%C3%A3o-executa-com-o-par%C3%A2metro-MV-MVCSA1-ativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ponto de entrada **MA030ROT** não executa com o parâmetro **MV\_MVCSA1** ativo  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**O parâmetro **MV\_MVCSA1** faz um desvio na rotina **MATA030** e o cadastro de cliente passa a ser construído em **MVC** via **CRMA980**, logo a construção do ***aRotina*** também não é feita no **MATA030** e o PE ***MA030ROT*** não ira funcionar. Para isso existe o PE ***CRM980MDef*** que trata o ***aRotina*** construído no **CRMA980** e tem a mesma função.

**Saiba mais**  
[PE CRM980MDEF Adiciona novas funcionalidades em Ações Relacionadas no browse](https://tdn.totvs.com/x/R6sGEQ)
