---
content_hash: 93c27a923d97df13d52a8d08f62206fe8501cbf5f6ef9eb04a3fb7ab625e11da
fetched_at: '2026-06-29T00:08:10.821168+00:00'
page_id: '240982607'
product: rm
source: tdn-rm
title: ER_SAUHRM01-11_Parametrização_de_KITs_e_Materiais_associados_por_Unidade_e_Via_de_acesso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240982607
version: 118
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-5 |
| **Requisito** | SAUHRM01-11 | **Subtarefa** | SAUHRM01-72 |
| **Chamado** |  | | |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Este documento tem como objetivo especificar a parametrização de kits e materiais associados por Unidade e Via de acesso.

## Definição da Regra de Negócio

**RN001** - Adicionar na tela de padrões de prescrição uma opção para selecionar a qual unidade de atendimento aquele padrão está associado. 

**RN002** - Este cadastro deve ser considerado na integração com o PEP 2 no que se refere às diluições.Somente deverão aparecer os diluentes referentes à unidade de atendimento do paciente selecionado.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Padrões de prescrição] | [Criação] | [Cadastros -> Cuidados com o paciente ->  Prescrição Médica -> Padrões de Prescrição] | RN001 |
| Prescrição de medicamento com diluição | [Alteração] | [PEP 2 -> Prescrição médica -> Painel de Medicamentos] | RN002 |

**Exemplo de Aplicação:**

1. Acessar o menu "Cadastros > Cuidados com o paciente> Prescrição Médica > Padrões de Prescrição";
2. Preencher as informações referentes ao princípio ativo;
3. Selecionar um registro em "Anexos > Padrão de prescrição";
4. Na aba "Padrão de prescrição", selecionar um registro;
5. Na tela de Padrão de prescrição, aba "Unidades de atendimento", selecionar a unidade de atendimento correspondente.

**Tabelas Utilizadas**

* SZDOSAGEMUNIDATEND - Tabela com o relacionamento entre o Padrão de Prescrição e a Unidade de Atendimento.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
