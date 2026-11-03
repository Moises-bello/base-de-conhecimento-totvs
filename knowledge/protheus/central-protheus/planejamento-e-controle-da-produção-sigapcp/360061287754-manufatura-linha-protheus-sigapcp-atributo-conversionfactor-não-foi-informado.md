---
article_id: 360061287754
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6a525e40a7e418b77fc68e7054aa90b200f1e4df610b351d4831e4af548a1ba1
fetched_at: '2026-06-28T22:42:40.872177+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Atributo 'conversionFactor' não foi
  informado
type: support-article
updated_at: '2021-08-13T12:39:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061287754-Manufatura-Linha-Protheus-SIGAPCP-Atributo-conversionFactor-n%C3%A3o-foi-informado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:35 min**  
**Ocorrência**Ao tentar integrar os dados para a execução do **PCPA712 -** **MRP****M****emória**  apresenta a mensagem **Atributo 'conversionFactor' não foi informado** para as **Estruturas**no**PCPA142 - Pendencias de Integração do MRP**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**O campo **GI\_FATOR - Fator de conversão** do **produto alternativo** está **em branco**.  
  
**Solução**Informar um **fator de conversão** no **produto alternativo** do **produto** que é apresentado em **Dados Enviados** do **PCPA142** .
