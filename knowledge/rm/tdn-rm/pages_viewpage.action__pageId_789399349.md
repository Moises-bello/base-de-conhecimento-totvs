---
content_hash: 97655616044eb4ab55b7712143e1a361813bdf9d7174f5807913abf2905f098b
fetched_at: '2026-06-29T00:11:39.719387+00:00'
page_id: '789399349'
product: rm
source: tdn-rm
title: Log de operações do eduCONNECT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=789399349
version: 3
---

Informação importante

Essa funcionalidade está disponível no TOTVS Educacional a partir da release 12.1.20.

A funcionalidade de log do eduCONNECT tem como proposta o registro de log das operações que ocorrem no eduCONNECT em caso de falha de alguma operação.

Entre as operações estão o envio de mensagens em geral ao eduCONNECT, login no TOTVS Educa Mobile pelo eduCONNECT (procedimento interno do sistema que é transparente para os usuários, mas que por alguma indisponibilidade do servidor do TOTVS Educa Mobile pode falhar), envio de mensagens através de fórmula visual e procedimentos de inclusão, atualização ou exclusão de entidades, como por exemplo categorias.

Essa funcionalidade pode ser acessada através do menu **"Atividades Acadêmicas | Central de Comunicações | eduCONNECT | Log do eduCONNECT"**.

Algumas informações ("código da chamada", "código da operação" e "origem do log") são apresentadas na visão (lista de registros de log) em forma de código, porém na edição (detalhe de cada log) o usuário poderá observar a descrição conforme a seguir:

| Código da chamada: indica o tipo de chamada realizada quando ocorreu a falha | |
| --- | --- |
| 0 | Chamada síncrona |
| 1 | Chamada assíncrona |

| Tipo de operação: indica o tipo de operação realizada quando ocorreu a falha | |
| --- | --- |
| 0 | Inserção de dados |
| 1 | Exclusão de dados |
| 2 | Atualização de dados |

| Origem do log: indica qual evento executado quando ocorreu a falha | |
| --- | --- |
| 0 | Envio de mensagens eventuais |
| 1 | Envio de mensagens utilizando fórmula visual |
| 2 | Tentativa de efetuar login no Meu eduCONNECT |
| 3 | Tentativa de efetuar login externo no TOTVS Educa Mobile |
| 4 | Manipulação do cadastro de categorias (inclusão, exclusão ou edição) |
| 5 | Envio de mensagens relacionadas à pendências financeiras |
| 6 | Envio de mensagens relacionadas à frequência do aluno |
| 7 | Envio de mensagens relacionadas à pendências na matrícula do aluno |
| 8 | Envio de mensagens relacionadas à frequência dos bolsistas de estágio |
| 9 | Envio de mensagens relacionadas à notificação do coordenador do projeto sobre envio de relatório parcial de acompanhamento |
| 10 | Envio de mensagens relacionadas à notificação do coordenador do projeto sobre envio de relatório final de acompanhamento |
| 11 | Envio de mensagens relacionadas à atividades de grupo de estudo |
| 12 | Envio de mensagens relacionadas à notificação de boletos próximos do vencimento |
| 13 | Envio de mensagens relacionadas à aprovação do plano de atividades |
| 14 | Envio de mensagens relacionadas à alteração de dados da empresa |
| 15 | Envio de mensagens relacionadas à alteração de dados da vaga de estágio |
| 16 | Envio de mensagens relacionadas à candidato selecionado à vaga de estágio |
| 17 | Envio de mensagens relacionadas à notificação de um aluno de uma etapa da turma/disciplina |
| 18 | Envio de mensagens relacionadas à inscrição em visitas e eventos |
| 19 | Envio de mensagens relacionadas à cadastro de edital |
| 20 | Envio de mensagens relacionadas ao tema do Meu eduCONNECT |
| 21 | Envio de mensagens individuais do Meu eduCONNECT |
| 22 | Envio de mensagens mensagens comuns do Meu eduCONNECT |
| 23 | Imagens das mensagens do Meu eduCONNECT |
| 24 | Manipulações de entidades Meu eduCONNECT |
| 25 | Envio de mensagens relacionadas à ocorrências para alunos |
| 26 | Envio de mensagens relacionadas à notas por etapa para alunos |
| 27 | Envio de mensagens relacionadas à faltas por etapas para alunos |
| 28 | Envio de mensagens relacionadas à disponibilização de material para usuários |

Por tratarmos de processos assíncronos, ou ainda, procedimentos que não retornam mensagens de erro passíveis de serem analisadas em tempo de execução, por exemplo, na tela de um dispositivo móvel, estas são direcionadas ao cadastro de logs do eduCONNECT, com o intuito de facilitar a interpretação dos problemas.

O formulário do log dará uma visão mais abrangente de qual o real motivo a operação não ocorreu corretamente no sistema.

Maiores detalhes do erro em questão, ficarão disponíveis na aba mensagem de log.
