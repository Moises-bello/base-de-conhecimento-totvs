---
content_hash: 41a41702e2c87b00ccdc84977a9bf76af8e920f46215c25aca1c91dc7291c920
fetched_at: '2026-06-28T21:35:28.055288+00:00'
page_id: '6066565'
product: fluig
source: tdn-fluig
title: JMS Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/JMS+Sender
version: 11
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é disponibilizar informações do Fluig ESB em um canal JMS.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado o Fluig ESB irá armazenar um registro referente a execução deste componente. |
| Initial Context Factory | Inserir o nome da classe responsável pela criação dos contextos iniciais para a resolução de nomes de um serviço de diretório. |
| Provider URL | Inserir o endereço no qual está localizado o serviço de diretórios a ser utilizado. |
| Queue Factory Lookup | Inserir o nome do serviço que provê a conexão com as filas JMS. |
| Queue Name | Inserir o nome da fila a ser utilizada para a comunicação JMS. |
| User Name | Inserir o nome do usuário JMS. |
| Password | Inserir a senha do usuário JMS. |
