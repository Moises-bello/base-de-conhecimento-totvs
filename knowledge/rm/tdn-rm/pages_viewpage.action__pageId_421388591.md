---
content_hash: d52cba4c5718bd2092c0f738fd37039edef4f47173cb10d50139e8e413b75eca
fetched_at: '2026-06-29T00:09:17.434031+00:00'
page_id: '421388591'
product: rm
source: tdn-rm
title: Integração Módulo CRM - Aprovação Via Workflow
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388591
version: 4
---

A integração entre o TOTVS Gestão Financeira e o TOTVS Gestão de Relacionamento com Clientes consiste em ter uma aprovação / reprovação de Acordos. No momento que o Acordo está sendo efetivado, um atendimento é inserido no TOTVS Gestão de Relacionamento com Clientes, e até que o mesmo seja aprovado o Acordo não é criado.

Esta operação consiste em gerar conforme os parâmetros definidos no Template, um atendimento cujo objetivo é controlar as operações realizadas. Maiores detalhes [acesse aqui](http://tdn.totvs.com/x/Pv9bGQ).

**1.** Para utilizar no  a aprovação via WorkFlow necessário acessar o Módulo Gestão do Relacionamento com o Cliente no Menu WorkFlow | Tipos, incluir um novo e na aba do Tipo de atendimento informar:

* Serviço associado ao Tipo de Atendimento
* Nome e Descrição
* Salvar

**2.** Criar uma Etapa no Tipo de Atendimento e indicar que será a primeira etapa de um possível fluxo:

* Anexos / Etapas
* Novo
* Preencher os campos indicados abaixo e demais caso necessário conforme regra de negócio.
* Nome
* Descrição
* Marcar a opção: Primeira etapa de um possível fluxo
* Tipo de repasse da etapa = Atendente
* Coligada do Atendente
* Localidade e Atendente inicial da tarefa

**3.** Necessário criar demais etapas para aprovação do Acordo Financeiro conforme a regra de negócio. Pelo menos duas outras etapas deverão ser criadas, uma para aprovação e outra para reprovação do Acordo.

No Anexo - Fluxo de etapas definir os fluxos possíveis, conforme exemplo a seguir:

No Anexo de etapa onde ocorrerá a aprovação as ações deverão ser parametrizadas como a seguir:

No fluxo de etapa onde ocorrerá a reprovação as ações deverão ser parametrizadas como obrigatórias nas opções seleção e execução.

**4.** Criar um grupo de atendimento e vincular o tipo de atendimento criado a esse grupo, necessário acessar o Menu | WorkFlow | Grupos  
 Na aba do Grupo de atendimento informar:

* Nome
* Descrição

Após salvar o grupo vincular o tipo de atendimento através do Menu: Anexos | Tipo de Atendimento do Grupo de Atendimento

**5.** Criar uma classificação de Atendimento (opcional):

Acessar o Menu: Atendimento | Apoio | Classificações e informar:

* Descrição
* Habilitar a opção Permite alterar classificação
* Habilitar a opção Ativo

**6.** Parametrizar o template de acordo para usar aprovação por WorkFlow conforme os dados cadastrados no Módulo CRM

Após as parametrizações realizadas a Integração estará realizada e será possível utilizar aprovação Via WorkFlow.
