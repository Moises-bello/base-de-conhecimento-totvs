---
content_hash: faff64c39a3a3bd1a6caf074acf22ee07450468eaa6ea44e3731461ee108f01b
fetched_at: '2026-06-29T00:10:30.291562+00:00'
page_id: '519715390'
product: rm
source: tdn-rm
title: DSAUCLINICA-195 DT Parâmetros por Unidade de Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519715390
version: 2
---

# PARÂMETROS POR UNIDADE DE ATENDIMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Prontuário Eletrônico |  |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Unidade de Atendimento |  | |  |  | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZUNIDATEND |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta melhoria visa transformar os parâmetros gerais: "Nova prescrição só com evolução do dia", "Permite médico que não seja o responsável utilizar Anamnese/Exame Físico" e "Nova evolução só com anamnese preenchida"  em parâmetros por unidade de atendimento.

Com essa mudança, os antigos parâmetros serviram como base para o preenchimento dos mesmos parâmetros na unidade. Esses parâmetros são utilizados no Prontuário e a unidade de atendimento a ser considerada segue a seguinte regra:

***Para atendimento de internação, a unidade a ser considerada é a unidade vinculada ao leito em que o paciente está. A unidade corresponde àquela que possuir o mesmo centro de custo vinculado ao leito. Caso o atendimento não possua um leito vinculado, a unidade a ser considerada é a unidade de atendimento da parcial corrente.***

## Procedimento para Utilização

* Acesse o cadastro de Unidades de atendimento, menu Cadastros/Uso Geral/Unidade de Atendimento
* Acesse as páginas Parâmetros da Prescrição e PEP e configure as unidades de atendimento conforme a necessidade de cada uma.

* Validação ao incluir uma evolução

* Validação ao incluir uma anamnese com um médico diferente do médico responsável no atendimento

* Validação ao incluir uma nova prescrição sem evolução do dia (paciente internado)
