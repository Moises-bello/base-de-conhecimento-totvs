---
content_hash: f696bc48d6f54f3e71b6dc6cc9b14be3dd0bbbfaed0a030e2b9c23691bd280c9
fetched_at: '2026-06-29T00:06:17.138534+00:00'
page_id: '212905209'
product: rm
source: tdn-rm
title: TTDULF_DT_Valores_Padrão_para_Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212905209
version: 3
---

# Parametrização de Valores para Registros de Atendimento.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Valors Padrão para Atendimento | SauAnsPadraoAtendAction | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZANSPADRAOATEND, SZANSPADRAOATENDITEM |
| **Sistema(s) Operacional(is):** | Windows® |
| **Versões/Release:** | 12.1.9 |

## Descrição

Criado cadastro para parametrização de valores padrão para registro de atendimentos externos e internos.

## Procedimento para Utilização

1. Acesse **Cadastros / Uso Geral / TISS / Valores Padrão para Atendimento**.
2. Clique em "**Novo**" e cadastre as informações desejadas tanto para paciente interno como para externo. Observação: A unidade de atendimento tem que estar atrelada a um convênio que use a TISS 3.0, caso contrário o restante dos dados da tela não ficarão habilitados.
3. Será necessário também informar os dados em **Anexo / Item por Especialidade**.
4. Após o cadastro, ao registrar um atendimento interno ou externo com a mesma unidade de atendimento e convênio parametrizada no cadastro o sistema irá lançar estes dados automaticamente nos "**Dados de Atendimento**", na tela de "**Informações** **ANS**", e os procedimentos, materiais ou medicamentos, serviços ou taxas, na aba "**Guia/Autorização**" bem como a Guia TISSque também foi selecionada no cadastro anterior.
