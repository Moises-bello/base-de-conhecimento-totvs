---
content_hash: 3e02a14c4fae2f19355c7c48051e8f68a22c338e8d860b85fced8af5dd3d57dc
fetched_at: '2026-06-29T00:08:16.893735+00:00'
page_id: '248581862'
product: rm
source: tdn-rm
title: ER_SAUHRM01-715_Item_para_registro_de_informações_cirúrgicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=248581862
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-6 |
| **Requisito** | SAUHRM01-714 | **Subtarefa** | SAUHRM01-715 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Criar item de enfermagem para o lançamento de taxas, procedimentos para o registro de informações cirúrgicas. Ao executar o processo de dados para faturamento, lançar os itens de débito associados.

 

## Definição da Regra de Negócio

**RN001** 

1. Na tela de Itens da Enfermagem, criar uma opção com o Tipo de Item "Itens p/ registro de inf. cirúrgica"

**RN002**

1. Na tela de Registro de Informações de Cirurgias, criar um anexo "Itens para Registro de Informação Cirúrgica"

**RN003** 

1. Na tela de Elaboração de Contas, caso exista um Item de Débito associado, efetuar o lançamento do mesmo na conta do atendimento.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Itens de Enfermagem | [Criação] | [Cadastros -> Cuidados com o Paciente ->  Prescrição Médica -> Itens da Enfermagem] | RN001 |
| Registro de Informações de Cirurgias | [Criação] | [Cuidados com o Paciente -> Centro Cirúrgico ->  Registro de Informações Cirúrgicas] | RN002 |
| Elaboração de Contas | [Alteração] | [Tesouraria -> Lançamentos na Conta do Paciente] | RN003 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
