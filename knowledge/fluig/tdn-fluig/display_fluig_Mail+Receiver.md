---
content_hash: 41af71a7767f64f4b8b8003a3ada2cb4ea35d41bfcbb4cd9fc1410c34c968663
fetched_at: '2026-06-28T21:35:28.033747+00:00'
page_id: '6066559'
product: fluig
source: tdn-fluig
title: Mail Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/Mail+Receiver
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é receber informações no Fluig ESB através de uma caixa de e-mail.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do Mail Receiver. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Host Name | Inserir o nome do servidor de e-mail no qual o Fluig ESB buscará os e-mails. |
| User Name | Inserir o nome utilizado pelo usuário para sua conta de e-mail. |
| SSL | Quando selecionado, indica que o serviço suporta uma conexão segura (HTTPS). |
| Password | Inserir a senha do usuário do e-mail. |
| Mailbox | Inserir para qual opção serão direcionados os e-mails recebidos. |
| Delete Time | Inserir o intervalo (em milissegundos) para que as mensagens sejam apagadas. |
| Protocol | Informar qual será o protocolo de e-mail que será utilizado pelo Fluig ESB para fazer a conexão: POP3 ou IMAP. |
| Mail Content | Informar a opção desejada conforme especificação abaixo.  * **Attachment:**Captura o anexo e envia para a rota como uma mensagem do Fluig ESB. * **Body Content:**Captura o texto do corpo da mensagem e envia para a rota como uma mensagem do Fluig ESB. * **Both:**Captura o texto do corpo da mensagem e o anexo e enviaambos para a rota como uma mensagem do Fluig ESB. |
