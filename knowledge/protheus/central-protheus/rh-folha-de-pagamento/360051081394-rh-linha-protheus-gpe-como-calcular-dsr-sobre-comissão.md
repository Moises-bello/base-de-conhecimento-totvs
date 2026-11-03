---
article_id: 360051081394
category: RH - Folha de Pagamento
content_hash: cb5bb6e40c5e0a2b78941d298f1ff0e761baeb677cca10db70f10881f424ad8d
fetched_at: '2026-06-28T22:44:12.252886+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular DSR sobre comissão
type: support-article
updated_at: '2025-04-23T12:07:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051081394-RH-Linha-Protheus-GPE-Como-calcular-DSR-sobre-comiss%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26335166543895)** Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**Como parametrizar o Sistema para calcular DSR sobre Comissões?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Para que o sistema calcule DSR sobre comissões, siga a orientação abaixo:  
  
1. Para **comissão** na Folha de Pagamento, na rotina Verba, para a verba de **Comissão** de **ID 0165**, na aba **Incidências,** campo **Verba DSR relacione** a verba de **DSR Comissão** de **ID** **0166:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079621694)  
  
2. Para **comissão** na **Rescisão,** na rotina Verba, na verba de **Comissão Rescisão** de **ID 0121,** na aba **Incidências,** campo **Verba DSR** relacione a verba de **DSR Comissão Rescisão** de ID **0122:**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079622154)

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
