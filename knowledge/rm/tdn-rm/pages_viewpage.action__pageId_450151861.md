---
content_hash: 523079b1761450f780434f5838d4bb34dd867531fb88f533db521e7f6a3ca4dd
fetched_at: '2026-06-29T00:09:55.759582+00:00'
page_id: '450151861'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-4096 Cancelar inscrição no processo seletivo com remessa bancária
  já enviada.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450151861
version: 2
---

# Parâmetro para cancelar remessa bancária automaticamente ao cancelar inscrição em um processo seletivo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Processo Seletivo |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cancelar inscrição | Cancelar inscrição | |  |  |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Geração de Lançamento  Cancelamento de remessa | Geração de Lançamento  Cancelamento de remessa | |  |  | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | DEDUINTEGRACOES-4096 |
| **País(es):** | N/A |
| **Banco(s) de Dados:** | N/A |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | N/A |

## Descrição

Ao cancelar a inscrição de um candidato em um processo seletivo, a sistema tentará, caso haja, cancelar o lançamento financeiro proveniente da inscrição do mesmo. Porém anteriormente, quando o lançamento possuía um boleto com status de remetido, era necessário que o usuário cancelasse manualmente a remessa do mesmo através do TOTVS Gestão Financeira, para que assim pudesse cancelar o lançamento financeiro e, naturalmente, a inscrição do candidato no processo seletivo.

Visando facilitar a usabilidade do sistema, foi adicionada uma nova parametrização ao TOTVS Processo Seletivo permitindo o usuário, ao cancelar a inscrição de candidato em um processo seletivo, cancelar automaticamente a remessa bancária do boleto e evitando assim o transtorno descrito anteriormente.
