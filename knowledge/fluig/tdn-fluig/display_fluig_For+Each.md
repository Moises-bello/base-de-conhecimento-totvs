---
content_hash: 8314662ccbaae23c8e8ce84d99cdc6275dcb0a651fe9db941ef4dcb4daf0c93b
fetched_at: '2026-06-28T21:35:28.084890+00:00'
page_id: '6066573'
product: fluig
source: tdn-fluig
title: For Each
type: documentation
url: https://tdn.totvs.com/display/fluig/For+Each
version: 12
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A partir da atualização [Fluig ESB 12.3](http://tdn.totvs.com/display/fluig/Release+12.3.0) o componente For Each foi renomeado para Splitter. Os diagramas antigos que possuíam o componente ForEach serão automaticamente convertidos para o componente Splitter utilizando as configurações previamente realizadas, não afetando o funcionamento do mesmo.

A finalidade desse componente é permitir que um documento XML seja dividido em várias unidades de envio. Um pré requisito do componente for-each é que a mensagem de entrada esteja no formato XML.

A partir de um componente For Each existem duas possibilidades: enviar a informação para algum componente sender (File, Email, FTP, etc), ou realizar a identificação e análise do conteúdo para que sejam tomadas algumas decisões.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Node Path | Especificar qual será o nível de divisão de um documento. Assim, a cada iteração do For Each, o sistema será enviado para o próximo componente que estiver no intervalo definido neste campo. Este caminho deve ser informado no formato XPath.  Ex.: /root/nodes/node. |

A critério de exemplo, suponhamos que a mensagem de entrada do componente **For Each** seja conforme o XML abaixo apresentando um lote com duas notas fiscais.

xml


Nota Fiscal
Nota Fiscal

009
0001
SC
9999-12-31
0001
9.999,99

009
0002
SC
9999-12-31
0001
9.999,99
]]>

Ao configurar o campo **Node Path** com o valor *ESBMessage/infNFe*, o componente irá quebrar a mensagem original em duas mensagens de saída conforme abaixo.

xml

009
0001
SC
9999-12-31
0001
9.999,99


009
0002
SC
9999-12-31
0001
9.999,99
]]>
