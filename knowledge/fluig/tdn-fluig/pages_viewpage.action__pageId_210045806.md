---
content_hash: 3bda1a84082960e56dbb97254ef31eee0a20046269863549f7d50957ff518d8b
fetched_at: '2026-06-28T21:35:19.515374+00:00'
page_id: '210045806'
product: fluig
source: tdn-fluig
title: ESB - Qual o comportamento do TOTVS ESB quando perde a comunicação com o License
  Server?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210045806
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS ESB

# Ocorrência

Gostaria de confirmar o comportamento do TOTVS ESB quando este perde a comunicação com o License Server. O serviço para sozinho ou fica apresentando algum erro no log? O sistema gera alguma notificação em caso de perda de conexão com o LS?

# Solução

A falta de comunicação com o LS é exibida no arquivo de log. Após três tentativas de reconexão o serviço para e é preciso reiniciá-lo assim que o LS estiver disponível.

Na tela do TOTVS ESB não é apresentada nenhuma notificação sobre a perda de conexão com LS.
