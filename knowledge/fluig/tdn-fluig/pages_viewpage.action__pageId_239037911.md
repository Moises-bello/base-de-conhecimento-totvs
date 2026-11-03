---
content_hash: 35b7247d0d814a241c3afc91be82273d31d6c331ff0dd6ce2b0ded222a34ee6a
fetched_at: '2026-06-28T21:35:22.761477+00:00'
page_id: '239037911'
product: fluig
source: tdn-fluig
title: BPM 104 - Problemas no envio de e-mails para o responsável por uma tarefa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239037911
version: 3
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

# Ocorrência

Nosso fluig não está enviando as notificações via e-mail quando o usuário recebe uma tarefa. Verificamos e o processo está configurado corretamente para notificar o responsável.

O servidor de e-mail está OK, pois criamos um novo processo com e-mail personalizado (notifier.notify()) e estes são enviados normalmente. 

# Solução

Verificamos que o problema descrito neste chamado ocorreu porque, nas configurações de notificações do fluig, o e-mail não estava ativo.  

Para solucionar a situação, com o usuário administrador, foi necessário acessar o Painel de Controle → Colaboração → Notificações e marcar o item E-mail, conforme a imagem a seguir:
