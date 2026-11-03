---
content_hash: d6a6d9163f22c7f2a987a20ced2b1b16f87910aed075449fea4ad894b6b377ec
fetched_at: '2026-06-29T00:08:17.118629+00:00'
page_id: '253985629'
product: rm
source: tdn-rm
title: TVATA3_DT_Permitir_Demissao_Membro_CIPA
type: documentation
url: https://tdn.totvs.com/display/LRM/TVATA3_DT_Permitir_Demissao_Membro_CIPA
version: 1
---

# NO CADASTRO DE RESCISÃO INDIVIDUAL EXIBIR MSG DE AVISO COM A POSSIBILIDADE DO USUÁRIO PROSSEGUIR COM A DEMISSÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Rescisão* | *Cadastro de Rescisão* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Rescisão** | *Cadastro de Rescisão* | |  |  | |
| **Cadastros Iniciais:** | *Cadastro de Rescisão* |
| **Parâmetro(s):** | *Data da Exoneração* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TVATA3* |
| **Requisito (ISSUE):** | *Folha* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *PFUNC, VREPRESENTANTE* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Ao tentar realizar rescisão de um membro da CIPA, era apresentada a mensagem: "Funcionário chapa 001201011623 tem estabilidade até 16/06/2018 por participar de eleição da CIPA.", e não permitia o cadastro da demissão.

Foi alterado para exibir uma mensagem de aviso, possibilitando ao usuário prosseguir com a rescisão.

Por motivo de segurança, esta alteração só foi implementada no cadastro de Rescisão Individual.

No módulo de Rescisão Coletiva continuará sendo bloqueada a demissão de membros da CIPA.
