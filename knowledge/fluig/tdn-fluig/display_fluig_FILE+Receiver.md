---
content_hash: ba0887492ce7a192f9f766e197e1c645645374c50c5a187bd7ab48746a067062
fetched_at: '2026-06-28T21:35:28.008274+00:00'
page_id: '6066555'
product: fluig
source: tdn-fluig
title: FILE Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/FILE+Receiver
version: 11
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é receber informações no Fluig ESB através de um ou mais arquivos em um diretório específico. Este componente possibilita o recebimento de diversos arquivos contidos dentro de um diretório para, por exemplo, enviá-lo posteriormente a um Web Service.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do FILE Receiver. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Directory | Inserir o nome do diretório no qual o Fluig ESB irá buscar os arquivos que deverão ser processados |
| Filter Mask | Inserir a extensão dos arquivos que devem ser lidos no recebimento. Caso não seja inserido um filtro para os arquivos, todos os arquivos que estiverem no diretório informado serão lidos. |
