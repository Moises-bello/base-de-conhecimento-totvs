---
content_hash: 14005f7e4bdcb6bc0dd673357e9c282c314a1b44d309544ef2f2d1932125a9a5
fetched_at: '2026-06-28T21:35:28.049300+00:00'
page_id: '6066563'
product: fluig
source: tdn-fluig
title: TOTVS Sender
type: documentation
url: https://tdn.totvs.com/display/fluig/TOTVS+Sender
version: 18
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

A finalidade desse componente é ser o componente de envio utilizado nas integrações padrões da TOTVS. As propriedades comuns do componente estão listadas abaixo.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Error Interval | Inserir o intervalo (em segundos) para que o sistema aguarde, caso ocorra algum erro, para efetuar novamente a verificação de novas mensagens. |
| Tries | Inserir o número de vezes que o sistema deve tentar enviar a mensagem antes de notificar o erro ao usuário. |
| Persist | Quando selecionado o Fluig ESB irá armazenar um registro referente a execução deste componente. |
| Product | Nome do produto a ser utilizado. |

Ao selecionar uma das opções da propriedade Product serão habilitadas propriedades específicas para cada produto integrado. A seguir serão discriminados as propriedades para cada produto.

* **Datasul (Type: EAI)**: Envia para a fila do EAI uma mensagem para que seja processada.

| Campo | Descrição |
| --- | --- |
| Priority | Inserir a prioridade da mensagem na Fila do EAI. Este campo é apenas informativo para o EAI, porém, é interessante manter o valor padrão da Prioridade, que é 500. |
| Database | Selecionar dentre as opções o Banco de Dados no qual o EAI está configurado, Progress 9, Open Edge 10 Oracle ou SQL Server. |
| Host | Inserir o nome do host (servidor) e a porta para a conexão ao banco do sistema Datasul. |
| Database | Inserir o nome do banco de dados a ser acessado para criar a mensagem na Fila do Datasul EAI. Caso o banco a ser utilizado seja Progress, o nome a ser utilizado neste campo deve ser o nome que está configurado no Progress Explorer Tools, para o banco do EAI. |
| Username | Inserir o nome do usuário no banco de dados. Caso o banco do EAI seja Progress, o usuário padrão para conexão via JDBC é o sysprogress. |
| Password | Inserir a senha do usuário no banco de dados. |

* **Protheus, RM, TSS, ESB, WebEnsino e Datasul (Type: WS)**: O comportamento e configuração do componente será o mesmo do componente .

* **WEBB**: O comportamento e configuração do componente será o mesmo do componente .

* **PIMS**: O comportamento e configuração do componente será o mesmo do componente .
