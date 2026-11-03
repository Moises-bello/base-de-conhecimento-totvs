---
content_hash: 264803786d2e5ebbedba8b2387affc2db11f17c92710311abf99afed80ee5992
fetched_at: '2026-06-28T21:35:28.026309+00:00'
page_id: '6066557'
product: fluig
source: tdn-fluig
title: FTP Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/FTP+Receiver
version: 11
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é conectar a um servidor FTP para colher as informações das quais o Fluig ESB necessita para serem processadas.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do FTP Receiver. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Host Name | Inserir o nome do host a ser utilizado para a comunicação FTP. |
| Port | Inserir o número da porta do host FTP a ser conectado. A porta padrão para conexão FTP é a 21. |
| Timeout | Inserir o intervalo (em segundos) para que o usuário seja notificado quando o sistema não consegue enviar um comando. |
| Directory | Inserir o diretório FTP onde as mensagens devem ser recebidas. |
| User Name | Inserir o nome do usuário FTP. |
| Anonymous | Quando selecionado, indica que o usuário FTP é anônimo. |
| Password | Inserir a senha do usuário FTP. |
| Filter Mask | Inserir a extensão dos arquivos que devem ser lidos no recebimento. Ex.: \*.txt. Caso não seja inserido um filtro para os arquivos, todos os arquivos que estiverem no diretório informado serão lidos. |
| Order | Selecionar a forma de ordenação do recebimento das mensagens, podendo ser por data ou nome. |
| Connection Mode | Selecionar o modo de conexão, podendo ser ativa ou passiva. |
| Transfer Mode | Selecionar qual o modo de transferência, podendo ser ASCII ou BINARY. |
| Delete File | Quando selecionado, indica que o arquivo será excluído após o recebimento. |
| SSH Client | Quando selecionado, indica conexão via Secure FTP Server. |
