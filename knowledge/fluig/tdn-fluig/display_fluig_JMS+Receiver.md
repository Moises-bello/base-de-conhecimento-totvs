---
content_hash: 80d45108e29cdad257ddac981a68fe2ae8a15ae87f42b25006a908f3fc9943f5
fetched_at: '2026-06-28T21:35:28.052234+00:00'
page_id: '6066564'
product: fluig
source: tdn-fluig
title: JMS Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/JMS+Receiver
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é receber informações no Fluig ESB através de um canal JMS.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Initial Context Factory | Inserir o nome da classe responsável pela criação dos contextos iniciais para a resolução de nomes de um serviço de diretório. |
| Provider URL | Inserir o endereço no qual está localizado o serviço de diretórios a ser utilizado. |
| Queue Factory Lookup | Inserir o nome do serviço que provê a conexão com as filas JMS. |
| Queue Name | Inserir o nome da fila a ser utilizada para a comunicação JMS. |
| User Name | Inserir o nome do usuário JMS. |
| Password | Inserir a senha do usuário JMS. |
