---
content_hash: a30c30fe0310f201c87ded341f755ebcc1351527999173e986ba9c143d618a3e
fetched_at: '2026-06-29T00:11:49.861241+00:00'
page_id: '839300238'
product: rm
source: tdn-rm
title: 7.3 Evolução da Arquitetura da Integração das Mensagens Financeiras com o Protheus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=839300238
version: 10
---

**CENÁRIO MAPEADO**: Difícil monitoramento dos problemas de sincronismo das informações. Não havia também uma forma simples de reenviar as mensagens que já estavam desatualizadas.

**EVOLUÇÃO**: Foi realizado uma alteração na arquitetura Integração EAI 2.0 para mudar a forma de sincronismo dos dados entre RM e Protheus. Ficando mais simples e objetivo acompanhar quaisquer problemas de sincronismo e também enviar e reenviar, quando necessário, a mensagem do RM para o Protheus.

OBS: Para que esta melhoria seja disponibilizada, será necessário a execução de um script específico para habilitação de um parâmetro.

Como exemplo, considere a inclusão de um novo lançamento financeiro gerado a partir do TOTVS Educacional. Durante os procedimentos de inclusão, a mensagem que seria enviada ao Protheus não foi executada, em seu lugar ocorre a gravação de um registro no banco de dados com o conteúdo da mensagem. Assim, após consolidada toda a atualização do banco de dados da linha RM, esta mensagem registrada no banco de dados é resgatada e finalmente é enviada ao Protheus. Caso ocorra algum erro na integração, a mensagem ficará pendente de envio e poderá ser executada posteriormente, após análise e correção do erro.

Há a opção de habilitar um outro parâmetro, para que nenhuma integração seja realizada instantaneamente para o Protheus, sendo possível o agendamento de "job" através de filtro para esta execução.

Para maiores orientações sobre o envio através do filtro acesse a documentação do "job" [Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=831836464).

Se ao enviar a mensagem pendente ao Protheus o procedimento de inclusão for executado com sucesso a mensagem pendente é removida do banco de dados. Por outro lado, se ao enviar a mensagem pendente ao Protheus este reportar algum problema, a mensagem fica retida no banco de dados. Enquanto a mensagem permanecer pendente, o(s) lançamento(s) associado(s) fica(m) em estado de inconsistência, impedido(s) de ser(em) submetido(s) a outros processos do módulo Gestão Financeira, tais como baixa e o acordo.

**Visão de Mensagens Pendentes**

As mensagens pendentes poderão ser observadas na visão de monitoramento das mensagens EAI, disponível no módulo Gestão Financeira através do menu "Utilitários | Mensagem EAI". Uma vez que a causa do problema na comunicação entre os sistemas esteja solucionada, as mensagens poderão ser selecionadas e enviadas através do processo "Reenviar Mensagem". A causa da falha poderá ser melhor entendida ao editar uma mensagem pendente.

**Envio / Reenvio de Mensagem**

Uma mensagem pode existir de forma autônoma ou como parte de um agrupamento (grupo de mensagem). Ao selecionar uma ou mais mensagens da visão e solicitar o reenvio, o sistema irá identificar os respectivos grupos de mensagens associados àquelas mensagens, ordenará estes grupos por ordem cronológica de execução e irá disparar cada uma das mensagens destes grupos que estejam com status "Pendente" ou "Falha”.

Importante: Para acessar a documentação completa, [Clique Aqui!](https://tdn.totvs.com/display/public/LRM/Mensagem+EAI)
