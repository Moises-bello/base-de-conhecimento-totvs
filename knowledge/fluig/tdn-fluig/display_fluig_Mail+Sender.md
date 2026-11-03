---
content_hash: 5e0d4af7c4e2711e26d963ca32fd72c589bff5a5313842c66977a1fdb8a2f1be
fetched_at: '2026-06-28T21:35:28.037343+00:00'
page_id: '6066560'
product: fluig
source: tdn-fluig
title: Mail Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/Mail+Sender
version: 11
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é disponibilizar informações do Fluig ESB em uma conta de e-mail.

Este componente é muito parecido ao MailNotifier, porém, o que os diferenciam é que o MailNotifier só pode ser ligado ao componente OnError.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado o Fluig ESB irá armazenar um registro referente a execução deste componente. |
| Host Name | Inserir o nome do servidor de e-mail que será utilizado para enviar as mensagens. |
| Requires SMTP Autentication | Caso seja necessário se autenticar no servidor de envio do e-mail, esta opção deverá ser marcada e preencher os campos User Name e Password. |
| User Name | Nome do usuário para se autenticar no servidor de SMTP. |
| Password | Senha do usuário para se autenticar no servidor de SMTP. |
| From | Inserir o endereço de e-mail do remetente. |
| To | Inserir o endereço de e-mail de destino. |
| Subject | Inserir a descrição do assunto da mensagem. |
| Send text as HTML | Quando assinalado este campo, a mensagem de e-mail será enviada no formato HTML. O formato padrão do Fluig ESB é texto. |
| Attached | Quando selecionado, indica que um arquivo será enviado anexo à mensagem de notificação. |
| File Name | Inserir o nome do arquivo que seguirá anexo à mensagem. Este campo é habilitado somente quando selecionada a opção *Attached*. |
| Body | Inserir o corpo da mensagem a ser enviada. |
