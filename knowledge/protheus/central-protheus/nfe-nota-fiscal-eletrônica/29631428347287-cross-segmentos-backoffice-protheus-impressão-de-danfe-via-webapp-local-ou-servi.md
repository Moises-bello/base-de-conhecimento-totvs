---
article_id: 29631428347287
category: NFe - Nota Fiscal Eletrônica
content_hash: a060b1ade8f758a55c7ad82662114cec708a20f35f7735e5c392d744c21be0b7
fetched_at: '2026-06-28T22:40:07.223112+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Impressão de Danfe via WebApp (Local
  ou Servidor)
type: support-article
updated_at: '2025-01-30T18:09:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29631428347287-Cross-Segmentos-Backoffice-Protheus-Impress%C3%A3o-de-Danfe-via-WebApp-Local-ou-Servidor
---

**Dúvida**Como imprimir a DANFE na rotina SPEDNFE e escolher entre local ou servidor via WebApp?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus 12.1.2410  
  
**Solução**Caso já esteja na versão 12.1.2410, precisará ser instalado o webagent para que o Smartclient Web consiga mapear a sua maquina local.   
  
Segue abaixo a documentação completa:  
- [Clique aqui.](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent)

Após a instalação, certifique-se de que o serviço WEBAGENT esteja em funcionamento no windows:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29631468450711)

Certifique-se ao abrir o Protheus, se está habilitado o agente local:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29631468452119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29631428318871)

Ao entrar na rotina é possível escolher o destino da impressão da DANFE:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29631468456343)

**Obs.: É necessário que as estações de trabalho possuam o webapp instalado para que o mesmo possa mapear a maquina local.**
