---
content_hash: 844275b49f56db18e3ec6a603e283bd24f64f433b098b4087813ea7ff8f91f91
fetched_at: '2026-06-29T00:08:50.244966+00:00'
page_id: '333779270'
product: rm
source: tdn-rm
title: Notas/Faltas Unificadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=333779270
version: 20
---

**Portal do aluno| Central do aluno| Notas/faltas Unificadas**

Este menu tem como objetivo unificar visualização das notas e faltas das etapas de todas as disciplinas em que o aluno está matriculado no período letivo.

Neste menu, o aluno/responsável poderá visualizar as etapas de Notas/Faltas,Observação (ficará ao lado da etapa de Notas) e o campo Percentual de faltas (como ocorre no [Widgets de faltas](http://tdn.totvs.com/pages/viewpage.action?pageId=309406432)), além disso contará com a exibição de cinco Widgets para melhor exibição do desempenho acadêmico em um único menu.

* Acontece hoje;
* Disciplinas em Curso;
* Frequência(Limite de faltas);
* Notas por Avaliação;
* Notas por etapas)

Para melhor visualização dos Widgtes para o menu, serão exibidos apenas dois, porém, o aluno/responsável poderá alterar qual o Widgets deseja ser exibido através do Lisbox.

Observação: A permissão da exibição dos Widgtes para este menu segue a mesma regra informado [aqui.](http://tdn.totvs.com/pages/viewpage.action?pageId=284880323)

# Parametrização para exibição das etapas de Notas/Faltas Unificadas

**1)** Conceder a permissão para o aluno/responsável em: Serviços Globais | Segurança | Perfil | Educacional (Portal) | Nota/falta Unificada.

**2)** Para unificar o nome da etapa de notas/faltas, foram criados dois campos: Agrupador e Nome Reduzido no cadastro das etapas de notas/faltas.

* O campo "Agrupador": Será responsável por criar os grupos na exibição do Grid e colocar todas as etapas que possuam o mesmo "agrupador" juntas na sua exibição.
* O campo "Nome reduzido": Este campo será exibido no título da coluna de cada etapa logo abaixo do seu agrupador, limitado a 10 caracteres. Otimizando assim a exibição de todo o conteúdo.

    A ordem de exibição das colunas e consequentemente os grupos, serão exibido seguindo o critério de ordenação:

**1º** Ordem alfabética do Agrupador

**2º** Ordem numérica do Código da Etapa

**3º**Ordem decrescente do tipo da etapa (Notas primeiro)

IMPORTANTE!!!

Para que a exibição correta da unificação das etapas de Notas e Faltas, o nome informando no campo Agrupador e no campo Nome Reduzido, deverá ser escrito com as mesmas características.

Caso não deseje agrupar as etapas de Notas/Faltas de acordo com o Bimestre / Semestre, basta unificar o nome campo: Nome reduzido.

Quando o aluno/responsável, selecionar o menu, a exibição das etapas será da mesma forma que ocorre atualmente, porém, o nome das etapas de Notas/Faltas serão de acordo com o nome informando no campo: Nome reduzido.

Caso a IE deseje agrupar apenas as etapas de Notas/Faltas de acordo com o Bimestre / Semestre e manter o nome original da etapa de Notas/Faltas, basta unificar apenas o nome campo: Agrupador.

Quando o aluno/responsável selecionar o menu, a exibição das etapas estará agrupada de acordo com o nome informando no campo: Agrupador,  porém, o nome das etapas Notas/Faltas será a mesma informando no cadastro das etapas realizado.

Para facilitar a atualização das etapas de Notas/faltas, os formulários de cadastro e atualização dos modelos de etapas contemplará os novos campos

* Currículo e Oferta | Oferta | **Período Letivo**;
* Currículo e Oferta | Oferta | **Parametrização por Curso**;
* Currículo e Oferta | Oferta | **Estrutura de Oferta**;
* Atividades Acadêmicas | Assistentes | **Atualizar Etapas da Turma/Disciplin**a (a atualização será de acordo com a parametrização definida em: Configurações | Secretaria | Período letivo | Buscar modelo de etapa)

Caso a etapa de Notas/Faltas não esteja liberada para visualização, ao logar no portal e selecionar o menu: Notas Faltas Unificadas, será exibido a mensagem: Não possui etapas disponíveis para visualização.

# Parametrização para exibição da coluna OBS (Comentário(s) do professor)

A coluna OBS, é responsável por exibir o comentário inserido pelo professor na etapa de Notas. Caso existir um comentário, será exibido o ícone .

Para visualizar a informação, o aluno/responsável deverá colocar o cursor do mouse sobre o ícone.

Caso a IE decida não exibir a coluna em questão, foi criado o parâmetro:"Exibir colunas de comentário de notas na tela de nota/falta unificada do novo portal do aluno" disponível em: **RM | RM Portal-Gerais | Portal-Geral 5/12 | Novo portal do aluno,**onde como default, o mesmo virá  desmarcado (onde não será exibido a coluna OBS), para exibir, basta marcar o parâmetro em questão.
