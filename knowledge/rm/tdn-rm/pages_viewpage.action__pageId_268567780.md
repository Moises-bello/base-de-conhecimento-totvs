---
content_hash: 30be891e97f1a583c36c9bb59c2cc6b3e1b1eb7c912bacfb39f897a62bc3a4d9
fetched_at: '2026-06-29T00:08:20.081733+00:00'
page_id: '268567780'
product: rm
source: tdn-rm
title: TVBQT2_DT_Priorização_Código_Dez_Dígitos_MatMed
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268567780
version: 115
---

# Parâmetro para priorização do código de 10 dígitos de MatMed do item na ausência do código específico

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | SAÚDE |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento para convênios | Geração de XML de Materiais e Medicamentos |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Produtos | Codificação de Matmed | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado o parâmetro "Utiliza Código 10 dígitos na ausência do código específico do MatMed" para que (quando marcado) e o parâmetro "Prioriza Código de 10 Dígitos"  na tabela de preços estiver **desmarcado** e não houver código de 8 dígitos em um material ou medicamento, o sistema verifique se há o código de 10 dígitos no item e preenche o seu valor na geração do faturamento para convênios.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.13.108 da biblioteca do RM

## Procedimento para Utilização

1. Acesse o menu **Cadastros/ Faturamento /Condições Contratuais com Convênios**.
2. Na aba **Eletrônicos TISS III**, marque o parâmetro  **Utiliza Código 10 dígitos na ausência do código específico do MatMed**.
3. Na conta de um paciente, lance um medicamento que não possua código específico de 8 dígitos e possua o código específico de 10 dígitos preenchido na tabela de preços.
4. Encerre a conta.
5. Na Nova MDI, em **Faturamento/Faturamento para Convênios**, crie uma remessa e gere o Faturamento da conta em questão.

divs
