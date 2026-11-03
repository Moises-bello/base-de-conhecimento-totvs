---
content_hash: 604579d598d7e880c942c276076cc4d1fd1e69affbe1175e10211ed57b593db7
fetched_at: '2026-06-28T21:35:28.058103+00:00'
page_id: '6066566'
product: fluig
source: tdn-fluig
title: Custom Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/Custom+Receiver
version: 10
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é permitir ao usuário criar um componente receiver próprio.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Jars Folder | Deve ser inserido o caminho do diretório ESB onde se encontra o arquivo .JAR contendo as classes que foram criadas. Após realizar a o deploy o arquivo .JAR será salvo no diretório fluig/ESB/lib/Custom. |
| Class Name | Inserir o nome da classe customizada a ser utilizada pelo receiver. |
| Properties File | Inserir o nome do arquivo que possui as propriedades do receiver customizado. Caso seja necessário passar parâmetros ao componente, estes deverão ser inseridos no arquivo .properties, e seu caminho completo ser informado neste campo. |

Veja o exemplo ESB-Custom-Components em nosso repositório clicando [aqui](https://git.fluig.com/projects/SAMPLES/repos/componentes/browse).
