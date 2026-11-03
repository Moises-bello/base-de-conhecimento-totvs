---
content_hash: 7ae0c11d6c39864afc65f45a72d8af806b04f2520b89573bea59b57cd3c07c18
fetched_at: '2026-06-28T21:35:22.572586+00:00'
page_id: '237394993'
product: fluig
source: tdn-fluig
title: Splitter
type: documentation
url: https://tdn.totvs.com/display/fluig/Splitter
version: 12
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade do componente Splitter é permitir que um documento (TXT ou XML) seja dividido em várias unidades de envio.

A partir de um componente Splitter existem duas possibilidades: enviar a informação para algum componente sender (File, Email, FTP, etc) ou realizar a identificação e análise do conteúdo para que sejam tomadas algumas decisões.

A partir da atualização [Fluig ESB 12.3](http://tdn.totvs.com/display/fluig/Release+12.3.0) o componente For Each foi renomeado para Splitter. O componente For Each permitia apenas dividir arquivos no formato XML.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Type | Especificar o tipo da regra para divisão de conteúdo:  * **TOKENIZER**: Para processar arquivos XML/TXT. * **XPATH**: Para processar arquivos XML. |

### Parâmetros TOKENIZER

| Campo | Descrição |
| --- | --- |
| ContentType | Especificar qual o tipo de conteúdo da mensagem. Pode assumir dois valores:  * TXT * XML |
| Rule | Especificar qual a regra de processamento para a divisão de conteúdos da mensagem. Pode assumir três valores:   * **Default**: Utiliza um único Token como regra de divisão. * **Pair**: Utiliza par de Tokens (inicial e final) como regra de divisão. * **Contains**: Utiliza um único Token, que divide o conteúdo mensagem original com base na linha do arquivo TXT (registro) que contém token informado, mantendo o conteúdo original da linha do arquivo TXT (registro).  Observação Essa opção é habilitada somente quando:   * ContentType = TXT |
| Token | Token utilizado para a regra de divisão de mensagens. |
| Use RegExp | Especifica se o parâmetro Token deve ser tratado como uma expressão regular. Observação Essa opção é habilitada somente quando:   * ContentType = TXT * Rule = Default |
| EndToken | Token finalizador utilizado para a regra de divisão de mensagens. Observação Essa opção é habilitada somente quando:   * ContentType = TXT * Rule = Pair |
| Group Messages | Especifica a quantidade de mensagens divididas que devem ser agrupadas nas mensagens geradas pelo componente **Splitter**. Esse parâmetro deve ser alimentado caso seja necessário que duas ou mais mensagens sejam agrupadas pelo **Splitter** antes de serem entregues ao próximo componente do diagrama de integração. Valor padrão: zero (0) = uma divisão por mensagem. Observação Essa opção é habilitada somente quando:   * ContentType = TXT * Rule = Default ou Rule = Pair |
| Inherit Namespace | Especifica o nome da tag pai do elemento XML dividido pelo componente **Splitter**, e adiciona o *namespace* da tag pai no XML dividido. Observação Essa opção é habilitada somente quando:   * ContentType = XML |
| Include Tokens | Especifica se os Tokens devem fazer parte da mensagem dividida pelo componente **Splitter**. Quando essa propriedade não estiver selecionada, o componente **Splitter** irá remover o Token das mensagens geradas no processo de divisão de conteúdo. Observação Essa opção é habilitada somente quando:   * ContentType = TXT * Rule = Pair |
| Streaming | Se ativado, o componente **Splitter** irá dividir a mensagem de entrada em pedaços. Isso reduz a sobrecarga de memória durante o processamento. Quando for necessário dividir grandes mensagens é altamente recomendado selecionar o parâmetro Streaming. Com essa propriedade marcada as submensagens geradas serão agregadas fora de ordem. Se desmarcada, o componente **Splitter** vai processar mensagens subrespostas na mesma ordem em que foram divididas. Observação Essa opção é habilitada somente quando:   * ContentType = TXT |

### Parâmetros XPATH

| Campo | Descrição |
| --- | --- |
| Node Path | Especificar qual será o nível de divisão de um documento. Assim, a cada iteração do **Splitter,** o sistema será enviado para o próximo componente que estiver no intervalo definido nesse campo. Esse caminho deve ser informado no formato XPath. **Exemplo**: /root/nodes/node. |

### Parâmetros Parallel Processing

| Campo | Descrição |
| --- | --- |
| Enable | Ativa/desativa o processamento paralelo. Esse parâmetro permite configurar o pool de processos (threads) objetivando minimizar o tempo de processamento de divisão das mensagens. Quando essa propriedade está ativada, as sub-mensagens geradas serão agregadas e/ou divididas fora de ordem. |
| Core Pool Size | Especificar um número para indicar o tamanho do pool de threads que está realmente fazendo o trabalho pesado para o processo de divisão de mensagens. Por padrão, o valor usual é 8. |
| Maximum Pool Size | Especificar um número para indicar o tamanho máximo do pool de threads que está realmente fazendo o processo pesado de divisão de mensagens. Por padrão, o valor usual é 16. Sugere-se também que em geral o valor dessa propriedade seja o dobro da propriedade Core Pool Size. |
| Keep Alive Time | Especificar o tempo de duração em milissegundos que o pool irá manter as threads inativas. |

### Exemplo 1

Temos abaixo um exemplo de mensagem de entrada do componente Splitter apresentando um lote com duas notas fiscais.

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

Ao configurar os campos Type com o valor "XPATH" e Node Path com o valor /ESBMessage/infNFe, o componente irá quebrar a mensagem original em duas mensagens de saída conforme abaixo:

#### Mensagem de saída 1

009
0001
SC
9999-12-31
0001
9.999,99
]]>

#### Mensagem de saída 2

009
0002
SC
9999-12-31
0001
9.999,99
]]>

Ao configurar os campos Type com o valor "TOKENIZER", ContentType com o valor "XML", e Token com o valor "infNFe", o componente **Splitter** também irá quebrar a mensagem original da mesma maneira que os resultados apresentados pelas mensagens de saída 1 e 2.

### Exemplo 2

Temos abaixo um exemplo de mensagem de entrada do componente Splitter apresentando um lote com dois pedidos de clientes:

Para configurar o componente Splitter para dividir a mensagem acima em duas mensagens contendo um pedido em cada, é necessário configurar as seguintes propriedades:

**Type** = "TOKENIZER"

**Content Type** = "TXT"

**Rule** = "Pair"

**Token** = "PD"

**EndToken** = "END"

**Group Messages** = 0

**Include Tokens** = selecionado (necessário para que o componente Splitter mantenha nos arquivos gerados os valores encontrados nos campos Token e EndToken)

#### Mensagem de saída 1

#### Mensagem de saída 2

### Exemplo 3

Temos abaixo um exemplo de mensagem de entrada do componente Splitter apresentando um lote com dois pedidos de clientes:

Para configurar o componente Splitter para dividir a mensagem acima em mensagens que contenham somente os Itens de pedido com o código "01619002", é necessário configurar as seguintes propriedades:

**Type** = "TOKENIZER"

**Content Type** = "TXT"

**Rule** = "Contains"

**Token** = "01619002"

#### Mensagem de saída 1

#### Mensagem de saída 2
