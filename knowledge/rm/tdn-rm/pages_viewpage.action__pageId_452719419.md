---
content_hash: f177eebaec6475c1c9811d1f51c670b4e747fb127edd2ff2fdca01f05331aaa6
fetched_at: '2026-06-29T00:10:07.708541+00:00'
page_id: '452719419'
product: rm
source: tdn-rm
title: Prontuário Médico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719419
version: 11
---

**Prontuário Médico**

O Prontuário Médico tem como objetivo reunir em uma única tela todos os dados médicos de um determinado paciente:

* Consultas Médicas - Atendimentos Ambulatoriais - Atestados - CAT´s - Exames Pendentes - Medicamentos Retirados - Vacinas

**Observação:**

- Possibilidade de realizar a pesquisa por Tipo de Paciente (Pessoa/Funcionário).

- Possibilidade de ver todas as consultas e atendimentos ambulatoriais do paciente selecionado.

- Possibilidade de incluir uma nova Consulta/Atendimento para o paciente selecionado.

- Status dos Exames: Normal e Anormal.

- Para atender as demandas do evento S-2220 do eSocial, foram incluídos alguns campos referentes ao eSocial no cadastro da consulta do funcionário, entre eles o campo "Funcionário". A partir de agora, quando houver mais de um vinculo por pessoa, inclusive chapas demitidas, o sistema irá exibir somente as consultas vinculadas à chapa do funcionário e as consultas que não tiverem nenhum relacionamento de chapa.

**Consultas Médicas -**No cadastro de Consultas Médicas deverá ser informado qual o status da mesma, podendo variar entre Apto, Inapto, Apto com Restrição, Pendente ou Agendado.

Para atender o eSocial, evento S-2220, será necessário informar os seguintes campos da Consulta/Exame:

**Consulta -** Data da consulta Tipo da consulta/Tipo da consulta para o eSocial Data de emissão ASO Situação Serviço de Saúde Responsável Código do Médico

**Exame -** Data do exame Procedimento Diagnóstico Observação Exame Referencial Resultado exame Código do Laudo (Padrão Denatran). Além das informações referente ao eSocial passadas acima, será disparado um Gatilho apenas para as consultas que atenderem:

- Tipo de Atendimento "Consulta Médica Ocupacional" e "Consulta para Exame Toxicológico";

- Situação "Apto", "Inapto", "Apto com restrição".

**Observações:**

- Quando for selecionado o Tipo de Atendimento "Consulta para Exame Toxicológico", ao adicionar um exame, só vai ser possível incluir o exame informado no Parametrizador como "Exame Toxicológico".

- Quando o Tipo de Atendimento é "Consulta para Exame Toxicológico" ou "Atendimento Ambulatorial", o campo "Data de emissão ASO" não deve ser preenchido.

- Possibilidade de registrar os medicamentos retirados durante a consulta.

- A geração do relatório ASO pode ser realizada através do botão "Imprimir ASO" presente na edição da consulta.

- Somente é permitida a geração do relatório ASO para o tipo de atendimento = Consulta Médica Ocupacional, que esteja com o status diferente de "Pendente" e "Agendado".

- Possibilidade de "Adicionar Exame" para a consulta em questão. - Visualização de todos os Exames Realizados do paciente selecionado. É possível somente excluir os Exames Realizados do paciente.

- Quando no campo "Tipo da Consulta" for selecionada a opção que está associada à "Mudança de Riscos Ocupacionais" exibido no campo "Tipo da Consulta para o eSocial" o produto exibirá a pasta "Função Proposta". Através da pasta "Função Proposta" será possível informar a nova Função; Seção; Posto ou Local de trabalho do funcionário. A nova Função informada será exibida na emissão do [ASO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719163)

- O resultado do exame não é de preenchimento obrigatório  atendendo à legislação.

**Atenção:** A nomenclatura "Mudança de Função" foi alterada para "Mudança de Riscos Ocupacionais" conforme previsto na NR 07 - PORTARIA Nº 6.734, DE 9 DE MARÇO DE 2020

**Atendimentos Ambulatoriais**  - Visualização de todos os atendimentos ambulatoriais do paciente selecionado. É possível somente excluir os atendimentos/exames do paciente.

**Observações:**

- Possibilidade de "Adicionar Exame" para a consulta em questão.

Atestados Visualização de todos os atestados de acordo com a coligada contexto do paciente selecionado. É possível incluir, editar e excluir os atestados do paciente.

CAT´s Visualização de todas as CAT´s do paciente selecionado. É possível incluir, editar e excluir as CAT´s do paciente.

Exames Pendentes Visualização de todos os Exames Pendentes do paciente selecionado. É possível somente excluir os exames pendentes do paciente.

Medicamentos Retirados Visualização de todos os Medicamentos já retirados pelo paciente selecionado. É possível incluir, editar e excluir os medicamentos do paciente.

Vacinas Visualização de todas as Vacinas do paciente selecionado. É possível incluir, editar e excluir as vacinas do paciente.

**Atenção:**

Se o parâmetro "Obrigatório filtro de perfil de exames para Prontuário", localizado em Opções| Parametrizador| Exames estiver marcado será obrigatório definir no Filtro por Perfil do usuário, um filtro para validar quais exames serão disponibilizados para inclusão e edição nas consultas médicas e atendimentos ambulatoriais.

|  |  |
| --- | --- |
|  | Veja Também |

---

Exames Realizados  
Atestado de Saúde Ocupacional
