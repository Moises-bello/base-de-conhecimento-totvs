---
content_hash: cf093f6ef1d8a1aa6df334adca533946b41661a686e4ae24b441554f535b460a
fetched_at: '2026-06-29T00:08:34.699900+00:00'
page_id: '274834098'
product: rm
source: tdn-rm
title: DT Justificativa de Itens Restritos por Unidade de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Justificativa+de+Itens+Restritos+por+Unidade+de+Atendimento
version: 111
---

# Justificativa de Itens Restritos por Unidade de Atendimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Justificativa de restritos por Unidade de Atendimento |  |  | | --- | | **Rotina(s) envolvida(s)** | | Cadastro de Unidades de Atendimento | | Prontuário | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-1031 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** | SZUNIDATENDITENSPRD |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação possibilita restringir itens por unidade de atendimento, para que no momento da prescrição médica o sistema solicite uma justificativa para o item em questão.

## **Procedimento para Utilização**

## Restringir item por Unidade de Atendimento

1. Acesse **Cadastros / Uso Geral / Unidades de Atendimento**.
2. Selecione um registro.
3. Acesse **Anexos / Itens Restritos por Unidade de Atendimento**.
4. Selecione um item que deseja restringir na Unidade de Atendimento selecionada.
5. Clique em **OK**.
6. É apresentada a listagem dos itens restritos para a Unidade de Atendimento selecionada.

## Prescrição de item restrito

1. Acesse o menu **Prontuário**.
2. Selecione um paciente\*.  
     
   \*Para que a justificativa seja requirida o paciente deve estar alocado na mesma Unidade de Atendimento da qual o item foi restrito.
3. Prescreva o medicamento que foi restrito para Unidade de Atendimento do paciente selecionado, para isto clique em **Nova Prescrição**.
4. Preencha os campos da prescrição.
5. Clique em **Gravar**. O sistema apresentará a tela de justificativa.

divs
