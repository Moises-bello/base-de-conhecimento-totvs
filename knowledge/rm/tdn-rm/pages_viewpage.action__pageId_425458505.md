---
content_hash: 789e66fa1373f6bf632bb4bceb528d8599fbfed1b777410af158dbb3ccbee3d6
fetched_at: '2026-06-29T00:09:30.753395+00:00'
page_id: '425458505'
product: rm
source: tdn-rm
title: Gerar Atendimento a partir dos Prospect/Suspect
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458505
version: 1
---

**Gerar Atendimento a partir dos Prospect/Suspect**   
Este processo permite gerar atendimento através do cliente selecionado de diversas partes do sistema. Trata-se de um processo genérico. Seu objetivo é otimizar a abertura do atendimento para todos os tipos de clientes (clientes, prospect/suspect, aluno, professor, pessoa).   
É possível avançar o atendimento para um grupo e tipo de atendimento ou repassá-lo para um atendente e/ou grupo de atendentes. Sua tela de edição é composta pelos campos: Grupo de Atendimento, Tipo de Atendimento, Classificação, Produto, Motivo de Repasse, Solicitação, Tornar o Atendente que Receber o Atendimento Responsável pelo contato com o Cliente, Avanço de Etapa e Repasse (para marcação do tipo de andamento que prosseguirá a solicitação) e Atendentes/Grupo (para escolha do responsável quando a opção Repasse for marcada). Os campos podem ser habilitados/desabilitados  ou obrigatórios de acordo com as opções marcadas.   
Quando a opção "Avançar Atendimento para a primeira etapa do fluxo de etapas"  estiver marcado o atendimento é gerado e inserido na 1ª etapa do fluxo. Caso seja a opção "Repassar Atendimento" marcada, será apresentado uma lista com todos os "atendentes/grupos" possíveis de receberem repasse. Sendo possível marcar mais de um item.  
Vale ressaltar que o sistema respeita a regra:

* Quando a quantidade de Atendente/Grupos for maior que a de clientes.

Ex.: Dois clientes são selecionados e Opção Marcada é: Repassar Atendimento. Atendentes/Grupos de Repasse = Três registros são selecionados.  
Será apresentado uma mensagem será apresentada informando que o atendimento só será criado e repassado para os primeiros atendentes/grupos escolhidos , ou seja o primeiro cliente será repassado para o primeiro grupo/atendente e o segundo cliente para o segundo grupo/atendente.

* Quantidade de Clientes é maior que o número de Atendente/Grupos selecionados.

Ex.: Três clientes são selecionados e a Opção Marcada é: Repassar Atendimento. Atendentes/Grupos de Repasse = Dois registros são selecionados.  
 O sistema repassará o primeiro cliente para o primeiro atendente/grupo, o segundo cliente para o segundo atendente/grupo e no terceiro cliente retornará para o primeiro atendente/grupo novamente. Feito isso os atendimentos são criados e repassados aos seus respectivos grupos.  
**Observação.:**   
A geração de um novo atendimento irá afetar a tabela HATENDIMENTOBASE. A tabela HCLIENTEATENDIMENTO que terá o relacionamento entre o atendimento criado e o tipo do cliente (clientes, prospect, aluno, professor, pessoa). Quando o processo for executado a partir de um cliente de uma Campanha de Marketing o campo "CODCOLIGADACAMPANHA" e "CODCAMPANHA" serão preenchidos, relacionando o atendimento á campanha de marketing.
