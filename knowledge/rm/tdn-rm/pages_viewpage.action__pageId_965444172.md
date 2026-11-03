---
content_hash: 5cd7f831931bb2ca9f9fc35c40fb81802137d2dd3219746f6a59c669cee44059
fetched_at: '2026-06-29T00:12:14.095836+00:00'
page_id: '965444172'
product: rm
source: tdn-rm
title: 05 - Notificações Internas Automáticas (Solicitação de aprovação, aprovação,
  reprovação e conclusão do processamento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=965444172
version: 32
---

# Sumário

---

**Sumário**

# Objetivo

---

A **notificação interna automática** tem como objetivo enviar um e-mail ao usuário do sistema sempre que ocorrer uma ação de **solicitação de aprovação**, **aprovação**, **reprovação** ou **conclusão do processamento** na Central de Comunicação.

Parametrização do remetente

É possível que seja definido um remetente especifico para esse tipo de notificação nos parâmetros do TOTVS Educacional.

**Educacional > Parâmetros > RM Portal > Portal Gestão Educacional > Central de Comunicação**.

**Importante:**  
Esse remetente será utilizado **apenas** nos e-mails de notificação interna. Para os demais e-mails enviados pela Central de Comunicação, o remetente poderá ser definido pelo próprio usuário no momento do envio da mensagem.

Caso não parametrize as configurações do remetente, serão utilizados o nome e o e-mail do remetente definidos na coligada global, em: **Parâmetros Globais > Envio de E-mails.**

# Notificação de solicitação de aprovação de mensagem

---

Quando a regra de comunicação exige aprovação, ao enviar uma mensagem, será disparado um e-mail para o usuário aprovador. Esse e-mail informará que uma nova mensagem foi registrada na Central de Comunicação e requer aprovação para continuar o fluxo de envio.

No corpo do e-mail, haverá um link que redireciona diretamente para a mensagem que necessita de aprovação. Alternativamente, o aprovador também pode acessar a mensagem manualmente, através do caminho: **Central de Comunicação > Gestão de Mensagens**.

Exemplo de e-mail enviado para usuário que é o aprovador da mensagem:

# Notificação de aprovação

---

Quando o usuário responsável pela aprovação aprovar a mensagem, uma notificação via e-mail será enviada ao usuário solicitante e a mensagem será enviada imediatamente ou conforme o agendamento configurado.

Exemplo de e-mail enviado para usuário solicitante quando a mensagem for aprovada:

# Notificação de reprovação

---

Quando o usuário responsável pela aprovação reprovar a mensagem, será disparada uma notificação via e-mail ao usuário solicitante informando a reprovação, incluindo a justificativa. A mensagem não será enviada e seu status será alterado para **“Reprovado”** na Gestão de mensagens.

Exemplo de e-mail enviado para usuário solicitante quando a mensagem for reprovada:

# Notificação de processamento

---

Após o processamento da mensagem será enviado um e-mail ao usuário responsável pelo envio informando que o processamento da mensagem foi finalizado.

O e-mail incluirá informações sobre o **status do envio** e o **log do processamento**.

Exemplo de notificação de processamento:

**Para obter mais informações sobre os processos de aprovação e reprovação, [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=948650355).**
