---
content_hash: 8f0480cdb82e100b4b2a690a4a5088291483b3c4e6df66439f92cd3160577c54
fetched_at: '2026-06-28T21:35:28.030289+00:00'
page_id: '6066558'
product: fluig
source: tdn-fluig
title: FTP Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/FTP+Sender
version: 14
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é enviar informações do Fluig ESB para um servidor FTP.

Este componente faz com que o Fluig ESB se conecte a um serviço de FTP para enviar as informações.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do sender FTP. |
| Error Interval | Inserir o intervalo (em milissegundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. O valor mínimo deve ser 1, caso contrário, este não será executado. |
| Persist | Quando selecionado, um registro será salvo no banco do Fluig ESB contendo a descrição da execução. |
| Host Name | Inserir o nome do servidor a ser utilizado para a comunicação FTP. |
| Port | Inserir o número da porta do host FTP a ser conectado. A porta padrão para servidores FTP é a porta 21. |
| Timeout | Tempo em segundos para que o FTP sender ocioso perca a conexão. |
| Directory | Inserir o diretório FTP onde as mensagens devem ser recebidas. |
| User Name | Inserir o nome do usuário para o serviço FTP. |
| Anonymous | Quando selecionado, indica que o usuário FTP é anônimo. |
| Password | Inserir a senha do usuário para o serviço FTP. |
| File Name | Inserir o nome do arquivo no qual as informações serão gravadas. |
| Append if file exists | Quando selecionado, indica que o conteúdo é incremental, ou seja, o conteúdo deve ser adicionado no final do arquivo caso esse já exista. |
| Connection Mode | Selecionar o modo de conexão, podendo ser ativa ou passiva. |
| Transfer Mode | Selecionar qual o modo de transferência, podendo ser ASCII ou BINARY. |
| SSH Client | Indica conexão segura SFTP. |

Observação

Em alguns ambientes, o Fluig ESB está instalado em um servidor Windows e o servidor de FTP está em Linux. Para este cenário é necessário a criação de um componente customizado. Conforme exemplo:
