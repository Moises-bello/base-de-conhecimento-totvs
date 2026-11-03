---
content_hash: 69024393eb8649d6005d429bd37900cac893537a7ff8f1b48982b47254e8ae61
fetched_at: '2026-06-29T00:08:39.810199+00:00'
page_id: '286021941'
product: rm
source: tdn-rm
title: DT Prontuário Eletrônico do Paciente Dados de Antropometria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286021941
version: 106
---

# Prontuário Eletrônico do Paciente - Dados de Antropometria

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Itens de Enfermagem | SauItenEnfermagem | |
| **Requisito****:** | SAUHRM02-1271 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZPEPENFERMAGEM |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Este requisito consiste em disponibilizar um novo tipo para o cadastro de itens de enfermagem no **TOTVS Gestão Hospitalar** chamado **Antropometria**. Este novo tipo servirá para mensurar medidas do paciente na integração entre **TOTVS Gestão** **Hospitalar** e **Prontuário Eletrônico do Paciente**. Os itens cadastrados no **TOTVS Gestão Hospitalar** aparecerão em um painel específico para dados de antropometria dentro do **Prontuário Eletrônico do Paciente**.

## Procedimento para Utilização

**Exemplo:**

       1.            Acesse o menu **Cadastros / Cuidados com o paciente / Prescrição Médica / Itens da Enfermagem**.

Note que um novo tipo de item chamado **Antropometria** está disponibilizado para cadastro.

       2.            Ao criar um novo registro, é necessário definir a unidade de medida clicando em **Anexos/Unidade**.

       3.            No anexo de **Unidades**, crie um registro para cada unidade de medida possível.

       4.            Estes dados de antropometria cadastrados foram disponibilizados para a integração entre **TOTVS Gestão Hospitalar** e **Prontuário Eletrônico do Paciente**, e eles são utilizados na aba **Registros Clínicos**, painel **Dados de Antropometria** do **Prontuário Eletrônico do Paciente**.

divs
