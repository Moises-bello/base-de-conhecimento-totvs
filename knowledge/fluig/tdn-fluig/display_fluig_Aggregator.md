---
content_hash: 4bb632c5c41fbaee17bcf22c5fbd0f38fe83db689d1faef03bef7e44cdde76a4
fetched_at: '2026-06-28T21:35:22.580306+00:00'
page_id: '237395229'
product: fluig
source: tdn-fluig
title: Aggregator
type: documentation
url: https://tdn.totvs.com/display/fluig/Aggregator
version: 9
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade do componente Aggregator é permitir que vários documentos (TXT ou XML) sejam agregados em uma única unidade de envio. A partir de um componente Aggregator existem duas possibilidades de conexão com outros componentes:

1. Enviar a informação para algum componente sender (File, Email, FTP, etc);
2. Realizar a identificação e análise do conteúdo para que sejam tomadas algumas decisões.

O componente Aggregator está disponível a partir da atualização Fluig ESB 12.3.x.

### Parâmetros

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Completion Size | Número máximo de mensagens agregadas. Esta é definida com um valor numérico entre 1 e 9999. |
| Completion Timeout | Tempo, em segundos, que o componente deve ficar inativo (sem receber mensagens) antes de encerrar a agregação. Esta opção pode ser definida como um valor entre 1 e 9999. Não é possível utilizar esta opção juntamente com o parâmetro **CompletionInterval**, apenas um dos dois pode ser utilizado. |
| Completion Interval | Período, em segundos, que o componente será agendado para encerrar a agregação. O ESB mantém uma tarefa em *background* que é ativada a cada período configurado. Não é possível utilizar esta opção juntamente com o parâmetro **completionTimeout**, apenas um deles pode ser utilizado. |
| Use Persistence | Quando selecionado, o ESB persistirá o conteúdo das mensagens agregadas em memória secundária até que o processo de agregação seja concluído. Esta opção é recomendada quando houver o requisito de continuar agregando mensagens mesmo após o reinício do serviço do ESB para agregações que não foram concluídas anteriormente. As mensagens agregadas são mantidas em persistência local no diretório: ${ESB\_HOME}/data/hawtdb.dat. |
| Ignore Invalid Correlation Keys | Quando selecionado, configura o componente para ignorar os tokens de correlação, que não podem ser avaliados para um valor. Por padrão, o ESB vai lançar uma exceção quando não encontrar um identificador na mensagem para agregação, mas é possível ativar esta opção para ignorar esta situação. |
| Type | Configura o componente para agregar tipos de conteúdos de mensagens distintas. Os valores possíveis são:  * TXT; * XML. |

### Parâmetros TXT

| Campo | Descrição |
| --- | --- |
| Correlation Type | Especifica qual a regra de agregação das mensagens. Pode assumir dois (2) valores:  * All Messages - agrega todas as mensagens; * Contains - agrega as mensagens de acordo com o token informado no parâmetro **Contains Token**. |
| Contains Token | Agrega as mensagens que contém o token especificado neste parâmetro. |
| Use Line Break | Insere caractere de quebra de linha nas mensagens. |

### Parâmetros XML

| Campo | Descrição |
| --- | --- |
| CorrelationType | Especificar qual o tipo de conteúdo da mensagem. Pode assumir dois (2) valores:  * All Messages - todas as mensagens; * XPath - agrega as mensagens de acordo com o token informado no parâmetro **XPath**. |
| XPath | Agrega as mensagens que contém o XPath informado neste parâmetro. |
| Root Tag Name | Cria uma tag XML raiz para a agregação contendo o nome especificado neste parâmetro. |

#### Exemplo 1

A seguir é apresentado um exemplo de mensagens de entrada do componente Aggregator contendo duas notas fiscais distintas.

Nota Fiscal
Nota Fiscal

009
0001
SC
9999-12-31
0001
9.999,99



Nota Fiscal
Nota Fiscal

009
0002
SC
9999-12-31
0001
9.999,99
]]>

Ao configurar os campos **completionSize** com o valor "2", **Type** com o valor "XML", **XmlCorrelationType** com o valor "XPath", **XPath** com o valor "/ESBMessage/infNFe/NFSer" e **rootTagName** com o valor "NFeLote", o componente unirá as mensagens originas em uma mensagem de saída conforme abaixo:

#### Mensagem de saída

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

```

```

#### Exemplo 2

A seguir é apresentado um exemplo de duas mensagens de entrada do componente Aggregator contendo pedidos de clientes:

#### Mensagem 1

#### Mensagem 2

Para configurar o componente para agregar somente as informações do cliente código "002 - Cliente Varejo" acima em uma única mensagem, é necessário configurar as seguintes propriedades:

**completionSize** = 2

**Type** = "TXT"

**TxtCorrelationType** = "Contains"

**containsToken** = "002 - Cliente Varejo"

**useLineBreak** = "true"

#### Mensagem de saída
