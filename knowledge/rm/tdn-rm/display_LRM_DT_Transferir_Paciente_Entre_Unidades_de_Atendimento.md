---
content_hash: 781e17addf47222b0175fb680c0fa70e32ecabb023d59ffd584a6cd4f5492f11
fetched_at: '2026-06-29T00:08:21.411854+00:00'
page_id: '268820585'
product: rm
source: tdn-rm
title: DT_Transferir_Paciente_Entre_Unidades_de_Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Transferir_Paciente_Entre_Unidades_de_Atendimento
version: 100
---

# Atualizar movimentação de estoque ao transferir o paciente entre Unidades de Atendimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Movimentação de Estoque |  |  | | --- | | **Rotina(s) envolvida(s)** | | Mudança de Leito | |
| **Cadastros Iniciais:** | Necessária integração com o Prontuário Eletrônico do Paciente (PEP 2) |
| **Requisito (ISSUE):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-53 |
| **País:** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZPRESCRICAO, SZMOVIESTOQUE, SZMOVIESTOQUEITEM, SZAPRAZAMENTO |
| **Sistema Operacional:** | Windows® |

## Descrição

Melhoria consiste na movimentação do sistema dos itens de uma requisição de estoque para uma nova requisição com novo local de estoque e centro de custo, quando o paciente for transferido de unidade de atendimento para outra (e as unidades forem compatíveis).

## Procedimento para Utilização

1. Acesse o menu **Atendimento / Internação / Mudança de Leito.**
2. Clique em **Incluir** e selecione um paciente.
3. Preencha os dados necessários e selecione o novo leito.
4. Ao gravar, será verificada a unidade de atendimento do novo leito.

* + Se as unidades de atendimento forem compatíveis e de locais de estoque diferentes será criada uma nova movimentação de estoque com os itens pendentes da anterior. A requisição anterior terá os itens suspensos.
  + Se as unidades de atendimento forem compatíveis e de mesmo local de estoque, a movimentação de estoque terá seu centro de custo atualizado.

divs
