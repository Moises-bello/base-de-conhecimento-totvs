---
content_hash: 35b2ac9cab60cbeb8a7f11c7ebda2a86acd4e1fb4c0ac36c8ee3e97e675cd0fe
fetched_at: '2026-06-29T00:10:13.304409+00:00'
page_id: '455803899'
product: rm
source: tdn-rm
title: Bloqueio de chamada de pacientes simultaneamente.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=455803899
version: 2
---

Tempo aproximado para leitura:**10 min**

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Saúde |
| Módulo: | Totvs Gestão Hospitalar |
| Função: | Painel de Eletivos |
| Ticket: | [DSAUGHCIA-8](http://jiraproducao.totvs.com.br/browse/DSAUGHCIA-8) |
| Requisito/Story/Issue (informe o requisito relacionado) : | Prioridade 6 - Item 13 - Bloqueio de Chamada de Pac Simultâneos |

## **02. SITUAÇÃO/REQUISITO**

Impedir que um paciente seja chamado por dois médicos diferentes ao mesmo tempo.

## **03. SOLUÇÃO**

Foi criada uma validação no painel de eletivos que verifica o status do paciente em  todos os registros de atendimentos abertos para este paciente, caso em algum deles o status seja "Em Atendimento"

uma mensagem é retornada ao usuário informado que o paciente se encontra em atendimento e por qual o médico o paciente está sendo atendido.

Painel de EletivosPainel de EletivosyesDemonstração

A tela abaixo mostra dois registros de atendimento para o mesmo paciente, porém cada registro pertence a um médico.

Nos dois registros de atendimento o status do paciente por hora é: "Aguardando". Obs. Está tela é visualizada com um usuário meste

este usuário tem acesso a todos os registros de atendimentos, por isso é possível visualizar o registro de atendimento de vários médicos.

Quando o usuário que está logado é do tipo médico, só é possível ver os registros de atendimento associados ao próprio médico.

Na tela abaixo, com um usuário do tipo médico logado, foi iniciado o atendimento do paciente.

Na tela abaixo, com a visão do usuário mestre podemos ver que um dos registros de atendimento teve o seu status alterado para: "Atendimento Iniciado"

Porém como se tratam de registros de atendimentos diferentes, na visão do outro médico que também tem um registro de atendimento associado

ao perfil dele, o status continua como "Aguardando", antes da implementação, seria possível chamar o paciente mesmo que ele estando em atendimento

por outro médico. Com a alteração, enquanto o paciente estiver em atendimento por algum médico a seguinte mensagem é apresentada.

## **04. DEMAIS INFORMAÇÕES**

Existem dois meios de chamar o paciente, dando um duplo clique sobre o registros (este modo pode ser habilitado ou desabilitado nas configurações do RM Saúde)

ou clicando no botão "Chamar", utilizando este botão o primeiro paciente (ordenado por tempo de espera ou classificação de risco) é chamado.

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
