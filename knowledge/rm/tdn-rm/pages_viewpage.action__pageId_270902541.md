---
content_hash: c86e5134739e517b220d34e011d5051eae2f8dc81ac031c43f125abceca4958b
fetched_at: '2026-06-29T00:08:24.759295+00:00'
page_id: '270902541'
product: rm
source: tdn-rm
title: RMEDU00003_Frequência Diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270902541
version: 11
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Gestão Educacional |
| **Versões:** | 12.1.14 |
| **Processo:** | Frequência Diária |
| **Data da publicação:** |  |

A funcionalidade do portal de frequência diária, permite aos professores digitar/informar, as faltas dos alunos, permitindo a instituição realizar um controle minucioso das ausências dos alunos, pois é informado qual dia exato o aluno esteve ausente e não apenas o total de ausências que ocorreram em uma etapa ou período letivo.

Requisitos:

* Professor possuir acesso ao menu de frequência diária no portal;
* Planos de aula e etapas devidamente cadastradas no sistema;
* Parametrização do sistema.
* Para que as faltas digitadas sejam levadas para a etapa (SNOTAETAPA), é necessário informar o valor no campo: aulas dadas.

Módulo: Serviços Globais | segurança | perfis | selecionar o perfil associado ao usuário

O perfil associado ao usuário, deve ter permissão de acesso em: | guia: acesso a menus | 11 - educacional | 11.04 - professor | 11.04.01 - diário de classe | 11.04.01.03 - frequência diária.

Currículo e oferta | oferta | turma/disciplina | anexos | etapas

Selecione a etapa de faltas, referente a qual a frequência diária será digitada. As datas de início e término da etapa estão preenchidas e são validas, ou seja, compreendidas no período letivo e a data de término é maior ou igual ao dia atual.

As datas de início e limite de digitação estão preenchidas e são validas, ou seja, compreendidas no período letivo e na etapa, e a data de término é maior ou igual ao dia atual.

É importante verificar se existe fórmula associada a etapa, pois a mesma pode realizar alterações nas frequências digitadas.

A etapa não pode estar com o parâmetro: etapa encerrada marcado.

Currículo e oferta | oferta | turma/disciplina | anexos | professor

O professor deve ser professor da turma.

Currículo e oferta | oferta | turma/disciplina | anexos | horário

Os horários da turma devem estar cadastrados.

Configurações | parâmetros | RM portal | RM portal - gerais

Caso o parâmetro: permitir ao professor alterar plano de aula/frequência sem estar cadastrado no horário da turma esteja desmarcado, o professor deve ser cadastrado como professor do horário, para permitir a digitação da frequência diária. Esse cadastro é um anexo do horário, cadastrado na turma disciplina.

Currículo e oferta | oferta | turma/disciplina | anexos | plano de aula

A etapa deve ter o plano de aula gerado.

 

Configurações | parâmetros | secretaria | notas/faltas

Caso o parâmetro: justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina estiver marcado, o professor do tipo coordenador da turma/disciplina, deve liberar a mesma, para visualização dos alunos e envio das informações para a etapa (SNOTAETAPA). A liberação é feita através do menu: aprovar frequência do portal do professor.

Caso o parâmetro: permitir a visualização das notas e faltas da etapa somente após a liberação do professor estiver marcado, o professor da turma/disciplina, deve liberar a mesma, para visualização dos alunos e envio das informações para a etapa (SNOTAETAPA). A liberação é feita através do menu: aprovar frequência do portal do professor.

Caso o parâmetro: permitir a visualização das notas das avaliações e faltas somente após a liberação do professor estiver marcado, o professor da turma/disciplina, deve liberar a mesma, para visualização dos alunos e envio das informações para a etapa (SNOTAETAPA). A liberação é feita através do menu: aprovar frequência do portal do professor.

Após logar no portal, o professor seleciona o menu de professor >> diário de classe >> seleciona o período letivo/curso/habilitação/turno e turma/disciplina >> seleciona o botão de frequência.

Selecione a etapa e preencha a data inicial e final para digitação. Os dias apresentados são os que o aluno terá as faltas marcadas, estes devem ser na data igual ou anterior à data atual.

Importante:

O sistema não limita a data inicial e final da frequência a ser digitada, porém internamente, ela não apresenta todos as datas de plano de aulas da etapa/turma/disciplina, pois é feito um calculo levando em consideração o número de planos de aulas gerados e os alunos da turma, sendo que o calculo realizado é exponencial.

O ideal, é a frequência ser digitada diária ou semanalmente, afim de evitar situações, onde o número de registros fique muito alto, o que pode travar a digitação.

Após clicar no botão selecionar, são apresentados os alunos matriculados na turma/disciplina e as datas dos planos de aula gerados, para digitação da frequência.

O dia marcado é considerado "AUSÊNCIA" e o desmarcado "PRESENÇA".

Para que as faltas digitadas sejam levadas para a etapa (SNOTAETAPA), é necessário informar o valor no campo: aulas dadas.

Ao clicar em salvar, é apresentado a mensagem de finalização do processo.

Informação

A partir da release 12.1.29, a funcionalidade de "Frequência Diária" do Portal conta com uma funcionalidade de liberação de frequência diária pelo professor.

Para que isso seja possível, o parâmetro do sistema "Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina" deve estar **DESMARCADO** (TOTVS Gestão Educacional | Configurações | Parâmetros | 15.01 - Secretaria | Notas/Faltas). Ou seja, essa opção de liberar frequência diária após salvar será exibida se a instituição **NÃO** utilizar a liberação pelo coordenador, pois se esse parâmetro estiver marcado, quem faz a liberação é o coordenador e somente pelo portal através de outra opção de menu já existente.

A opção de "Salvar" funcionará conforme atualmente, porém quando a opção de liberar estiver marcada, também será marcado o campo de controle "FrequenciaDispWeb" do plano de aula (SPLANOAULA.FREQUENCIADISPWEB = 1).

Para mais informações, acesso o [documento técnico](https://tdn.totvs.com/x/LmzNI) dessa novidade.
