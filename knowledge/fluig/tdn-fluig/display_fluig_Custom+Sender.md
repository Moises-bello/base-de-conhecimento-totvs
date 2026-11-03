---
content_hash: 68e5fef94763fd31da6e85f1e33057261ee01f2cbb8fac9fb05d90c28917d400
fetched_at: '2026-06-28T21:35:28.061257+00:00'
page_id: '6066567'
product: fluig
source: tdn-fluig
title: Custom Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/Custom+Sender
version: 11
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é permitir ao usuário criar um componente *sender* próprio.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado o Fluig | ESB irá armazenar um registro referente a execução deste componente. |
| Jars Folder | Deve ser inserido o caminho do diretório ESB onde se encontra o arquivo .JAR contendo as classes que foram criadas. Após realizar a o deploy o arquivo .JAR será salvo no diretório ESB-install/ESB/lib/Custom. |
| Class Name | Inserir o nome da classe customizada a ser utilizada pelo sender. |
| Properties File | Inserir o nome do arquivo que possui as propriedades do sender customizado. Caso seja necessário passar parâmetros ao componente, estes deverão ser inseridos no arquivo .properties, e seu caminho completo ser informado neste campo. |

Veja o exemplo **ESB-Custom-Components** em nosso repositório clicando [aqui](https://git.fluig.com/projects/SAMPLES/repos/componentes/browse).
