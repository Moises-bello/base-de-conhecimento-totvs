---
article_id: 360024186871
category: RH - Rescisão
content_hash: 1620f434699636ea24655a9ab9646395eab951d585ebe5e60233f847401dc7d4
fetched_at: '2026-06-28T22:43:50.832096+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Problema Regra de dependência não respeitada (Dt.
  Demissao / RG_DTAVISO)
type: support-article
updated_at: '2025-05-05T20:48:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024186871-RH-Linha-Protheus-GPE-Problema-Regra-de-depend%C3%AAncia-n%C3%A3o-respeitada-Dt-Demissao-RG-DTAVISO
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26496819300887)***Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao tentar calcular uma rescisão complementar através da rotina GPEM040, o sistema apresenta a mensagem: "**Problema Regra de dependência não respeitada (Dt. Demissao / RG\_DTAVISO)**"  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022087551)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) – GPE Gestão de Pessoal – A partir da versão 11.80  
  
**Causa**Essa mensagem ocorre devido a não existir as pastas (**SXA**) de rescisão no sistema.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022087951)  
  
  
  
**Solução**Para solucionar essa ocorrência, seguir os passos abaixo:  
1. Acessar via **Configurador**, **Base de Dados**, procurar a tabela **SRG** (Rescisões);  
2. Entre como editar e acesse no menu a opção **Pastas**;  
3. Inclua as Pastas conforme imagem abaixo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022088271)

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
