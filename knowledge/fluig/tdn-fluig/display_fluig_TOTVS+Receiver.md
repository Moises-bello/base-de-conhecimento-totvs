---
content_hash: 649634066f0847605e1ac0b8a12b96de11ec3f4e499eae59e8bc5deed2decf60
fetched_at: '2026-06-28T21:35:28.045104+00:00'
page_id: '6066562'
product: fluig
source: tdn-fluig
title: TOTVS Receiver
type: documentation
url: https://tdn.totvs.com/display/fluig/TOTVS+Receiver
version: 18
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é ser o componente de recebimento utilizado nas integrações padrões da TOTVS. As propriedades comuns do componente estão listadas abaixo.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Interval | Inserir o intervalo (em segundos) para a verificação de novas mensagens. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Product | Selecionar o produto TOTVS do qual o componente irá receber as mensagens. |

Ao selecionar uma das opções da propriedade **Product** serão habilitadas propriedades específicas para cada produto integrado. A seguir serão discriminados as propriedades para cada produto.

* **Datasul (Type: EAI)**: Busca as mensagens que se encontram na Fila do EAI Datasul, para serem processadas pelo Fluig ESB. As propriedades apresentadas a seguir são *tags* encontradas dentro do cabeçalho das mensagens padrão Datasul, e se configuradas, servirão como filtro na busca das mensagens.

A primeira tabela demonstra os campos disponíveis na aba **Message** e a próxima demonstra as propriedades disponíveis na aba **Database Configurations**.

| Campo | Descrição |
| --- | --- |
| Application | Nome do aplicativo aonde a mensagem foi gerada (tag DatasulMessage\MessageHeader\TransactionId\Application) |
| Document Type | Nome da transação. Esta informação é encontrada no registro da fila EAI e normalmente é idêntica ao parâmetro Transaction. |
| Update Status | Quando selecionado, o Fluig ESB atualiza a status da mensagem que foi processada da fila. Caso este campo não seja marcado, o Fluig ESB irá processar mais de uma vez a mesma mensagem que está na fila, pois seu status não será alterado para processada. |
| Insert Protocol | Quando selecionado, o Fluig ESB criará uma mensagem de retorno após ler a mensagem postada na Fila do EAI. Este é o único meio de saber qual o horário em que a mensagem foi processada. |
| Return Message | Quando selecionado, buscará as mensagens de retorno da Fila do EAI. |

| Campo | Descrição |
| --- | --- |
| Database | Selecionar qual o tipo de banco de dados o EAI está configurado. |
| Host | Inserir o nome do host e a porta a ser utilizada para a comunicação com o sistema Datasul. |
| Database | Inserir o nome do banco de dados a ser utilizado para a comunicação com o sistema Datasul. |
| User Name | Inserir o nome do usuário no banco de dados. O usuário padrão no PROGRESS para conexão através do JDBC é o sysprogress. |
| Password | Inserir a senha do usuário no banco de dados. |

* **Protheus, RM, TSS, ESB e WEBB** : O comportamento e configuração do componente será o mesmo do componente .

* **WebEnsino e Datasul (Type: WS)**: O comportamento e configuração do componente será o mesmo do componente .

* **PIMS**: O comportamento e configuração do componente será o mesmo do componente .
