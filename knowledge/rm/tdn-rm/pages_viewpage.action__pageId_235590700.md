---
content_hash: 205141ce618f4569a176defe2cb900e3c39e410c605ca16e1c83c5a7b215dd86
fetched_at: '2026-06-29T00:08:05.250779+00:00'
page_id: '235590700'
product: rm
source: tdn-rm
title: TUMVL6_DT_Cópia_Anamnese_Especial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235590700
version: 119
---

# Cópia Anamnese Especial Anterior

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Prontuário Eletrônico |  |  | | --- | | **Rotina(s) envolvida(s)** | | Anamnese/Formulários Especiais | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER e ORACLE |
| **Tabelas Utilizadas:** | ``` SZANAMNESPECIAL E SZANAMNESPECIALCOMPL ``` |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementada melhoria no sistema para que ao criar uma nova anamnese, se existir uma anterior de mesmo padrão para o paciente e atendimento corrente, esta será copiada e o sistema exibirá os campos da anamnese já preenchidos com os dados da última.

## Procedimento para Utilização

1. Acesse o **Prontuário Eletrônico** e selecione um paciente.
2. Acesse a aba **Anamnese/Formulários Especiais.**
3. Se já existir um padrão de Anamnese, inclua um novo de mesmo padrão.
4. Ao salvar a aba **Anamnese Especial/Campos Complementares** será mostrada com os dados já preenchidos da anamnese anterior.

divs
