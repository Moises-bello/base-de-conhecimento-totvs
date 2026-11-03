---
content_hash: 091acf3914ae9248ba9df0f19bc30c7bd536120bef963b2037ee3a294a2c0714
fetched_at: '2026-06-29T00:11:04.108971+00:00'
page_id: '625448838'
product: rm
source: tdn-rm
title: Mensagem EAI
type: documentation
url: https://tdn.totvs.com/display/LRM/Mensagem+EAI
version: 23
---

**Evolução da Arquitetura da Integração com Protheus**

Visando oferecer uma melhor usabilidade na integração por mensagens EAI 2.0, as mensagens associadas ao ciclo de vida de um lançamento financeiro no BackOffice Linha RM (inclusão, alteração, cancelamento, baixa, cancelamento da baixa, acordo e cancelamento do Acordo), passam a dispor de um novo modelo de integração. Esta evolução, no momento, se aplica exclusivamente aos lançamentos gerados pelo Educacional e a habilitação da funcionalidade está sendo feita de forma progressiva e controlada, apenas para alguns clientes.

**Como funciona**

Como exemplo, considere a inclusão de um novo lançamento financeiro gerado a partir do TOTVS Educacional. Durante os procedimentos de registro da inclusão do lançamento financeiro, a mensagem que seria enviada ao Protheus não é executada, em seu lugar ocorre a gravação de um registro no banco de dados com o conteúdo da mensagem. Assim, após consolidada toda a atualização do banco de dados da linha RM, esta mensagem registrada no banco de dados é resgatada e finalmente é enviada ao Protheus.

O envio da mensagem ocorre a partir de um estado consistentemente gravado no RM. Se ao enviar a mensagem pendente ao Protheus o procedimento de inclusão for executado com sucesso a mensagem pendente é removida do banco de dados. Por outro lado, se ao enviar a mensagem pendente ao Protheus este reportar algum problema, a mensagem fica retida no banco de dados. Enquanto a mensagem permanecer pendente, o(s) lançamento(s) associado(s) fica(m) em estado de inconsistência, impedido(s) de ser(em) submetido(s) a outros processos do módulo Gestão Financeira, tais como baixa e o Acordo.

Comportamento Original:

A mensagem ao Protheus (em azul) é executada ao longo da execução do processo no RM (em verde). Se porventura o processamento for interrompido pelo RM após acionado o envio da mensagem, o processo RM pode sofrer um rollback (desfazimento) automático, sem efeito no processo no Protheus, gerando inconsistência.

Novo processo de envio de mensagens:

Neste caso, o processo do RM (em verde) é executado normalmente até o seu final levando a base a um ponto de consistência. Após o processo ser encerrado com sucesso, ocorre o disparo de um novo processo apenas para o envio da mensagem ao Protheus (em azul). Se a execução do envio da mensagem ao Protheus retornar um erro, a mensagem fica registrada no banco de dados do RM e poderá ser reenviada após uma ação corretiva.

**Configuração Necessária**

A natureza do Protheus é significativamente mais restritiva que o RM no que diz respeito ao tratamento das datas de emissão e vencimento na manutenção do lançamento, e da data de baixa, por ocasião da baixa do lançamento. Neste cenário, é necessário que sejam habilitadas algumas restrições na configuração do RM, de modo que não ocorra de um processo iniciado no RM seja bloqueado de ser concluído no Protheus, com prejuízo de necessariamente este procedimento ser desfeito e novamente aplicado com os devidos ajustes.

Seguem algumas orientações de ajustes e procedimentos:

1) Desabilitar o parâmetro "Permite data de vencimento menor que data de emissão" em parâmetros do TOTVS Gestão Financeira, nos parâmetros de inclusão de lançamentos.

2) Desabilitar o parâmetro "Permite data de baixa menor que data de emissão" nos parâmetros do TOTVS Gestão Financeira, nos parâmetros de baixa dos lançamentos.

3) Ao executar a baixa manual, o atributo "Data de baixa igual ao vencimento" não deve ser marcado, e não deve ser informada uma data futura.

**Observação:** As orientações de ajustes e procedimentos 1), 2) e 3) serão validadas pelo sistema durante os processos, caso não estejam conforme orientação serão exibidas mensagens de aviso orientando sobre as mesmas. Estas validações visão garantir que os processos sejam concluídoscom sucesso no Protheus.

**Visão de Mensagens Pendentes**

As mensagens pendentes poderão ser observadas na visão de monitoramento das mensagens EAI, disponível no módulo Gestão Financeira através do menu "Utilitários | Mensagem EAI". Uma vez que a causa do problema na comunicação entre os sistemas esteja solucionada, as mensagens poderão ser selecionadas e enviadas através do processo "Reenviar Mensagem". A causa da falha poderá ser melhor entendida ao editar uma mensagem pendente.

Ao solicitar a edição da mensagem EAI pendente será apresentado detalhamento da mensagem, com a mensagem de erro gerada pelo EAI e o detalhamento do conteúdo da mensagem na aba "Metadados", em formato XML.

**Envio / Reenvio de Mensagem**

Uma mensagem pode existir de forma autônoma ou como parte de um agrupamento (grupo de mensagem). Ao selecionar uma ou mais mensagens da visão e solicitar o reenvio, o sistema irá identificar os respectivos grupos de mensagens associados àquelas mensagens, ordenará estes grupos por ordem cronológica de execução e irá disparar cada uma das mensagens destes grupos que estejam com status "Pendente" ou "Falha".

Esta execução avançará de mensagem em mensagem em cada grupo até que todas tenham sido enviadas ou até que ocorra o primeiro erro. Esta medida é importante porque, em alguns casos, existe dependência entre as mensagens, como por exemplo no TOTVS Educacional quando associa um lançamento existente a uma bolsa 100%, este modifica o lançamento financeiro e, em seguida, efetua a respectiva baixa. Neste cenário, se houver impedimento para a modificação do lançamento, a mensagem de baixa deve aguardar a correção do impedimento.

Manutenção de Lançamentos

O processo de inclusão, alteração e cancelamento de lançamentos financeiros, integrados ao Protheus no contexto desta nova arquitetura dispõe de alguns mecanismos visando facilitar a correção de eventuais problemas:

* Ao proceder a inclusão de novo lançamento, se houver algum problema para o envio da mensagem, este será marcado como pendente de envio de mensagem EAI e permanecerá bloqueado para execução de outros processos (ex.: baixa, Acordo, etc.).
* Se o lançamento foi incluído no RM, mas ainda não foi integrado ao Protheus, este poderá ser editado ou cancelado. Se editado neste contexto, ocorrerá a substituição da mensagem EAI pendente por uma nova modificada, que será submetida a uma nova tentativa de envio. Se cancelado neste contexto, ocorrerá apenas a remoção da mensagem EAI pendente procedendo o processo de cancelamento no RM sem a obrigação de primeiro enviar a mensagem de inclusão.
* Se o lançamento foi incluído no RM e corretamente integrado ao Protheus, ao editar este lançamento o mesmo será modificado no RM e uma mensagem de alteração enviada ao Protheus. Ocorrendo algum impedimento para alteração deste lançamento no Protheus, o lançamento ficará bloqueado para outros processos, inclusive para cancelamento.
* Foi criado o novo status 'Em Processamento' na mensagem EAI. Quando uma mensagem pendente inicia o processo de comunicação com o Protheus, o seu status é modificado de 'Pendente' para 'Em Processamento'. Se o usuário solicitar uma nova geração de financeiro (lançamento) a partir da visão da parcela do módulo Educacional, por exemplo, se houver alguma mensagem associada ao lançamento com status 'Em Processamento' a geração do financeiro (e consequentemente o reenvio da mensagem ao Protheus) é abortada com mensagem indicando que a alteração anterior ainda está sendo integrada com o BackOffice Protheus
Baixa de Lançamentos

O processo de baixa e cancelamento de baixa de lançamentos financeiros integrados ao Protheus no contexto desta nova arquitetura dispõe de alguns mecanismos visando facilitar a correção de eventuais problemas:

* Ao realizar a baixa de um lançamento, este será validado da não existência de bloqueio para o envio de mensagem EAI devido a alguma mensagem EAI anterior ainda pendente de envio. Não existindo impedimento a mensagem EAI é colocada em fila de processamento.
  + **Obs.:** Foi habilitado apenas para um cliente o armazenamento das mensagens de Baixa, fazendo com que não exista à espera do envio e resposta da integração, para que o processo de Baixa encerre sem aguardar o encerramento das trocas de mensagem do EAI. Desta forma as mensagens de Baixa manual e Retorno Bancário irão ficar na fila com o Status = Pendente, e será necessário ação manual de envio da mensagem para que o EAI conclua a integração.
* Ao realizar o cancelamento da baixa de um lançamento é avaliado se a mensagem EAI de baixa foi efetivamente enviada e processada com sucesso pelo Protheus. Caso a baixa não tenha sido integrada ao Protheus devido a algum incidente, esta baixa poderá ser cancelada no RM sem o envio de mensagem EAI no Protheus.
Acordo de Lançamentos

O processo de Acordo e cancelamento de Acordo de lançamentos financeiros integrados ao Protheus no contexto desta nova arquitetura dispõe de alguns mecanismos visando facilitar a correção de eventuais problemas:

* Ao incluir o acordo de um lançamento será validada a não existência de bloqueio para o envio de mensagem EAI devido a alguma mensagem EAI anterior ainda pendente de envio. Não existindo impedimento, a mensagem EAI é colocada na fila de processamento.
  + **Obs.:** Foi habilitado apenas para um cliente o armazenamento das mensagens de Acordo, fazendo com que não exista à espera do envio e resposta da integração, para que o processo de Acordo encerre sem aguardar o encerramento da troca de mensagem do EAI. Desta forma as mensagens de Acordo irão ficar na fila com o Status = Pendente, e será necessário ação manual de envio da mensagem para que o EAI conclua a integração.
* Ao realizar o cancelamento do acordo de um lançamento é avaliado se a mensagem de acordo foi enviada e processada com sucesso pelo Protheus. Caso o acordo não tenha sido integrado ao Protheus devido a algum incidente o mesmo poderá ser cancelado no RM sem o envio de mensagem EAI no Protheus.
