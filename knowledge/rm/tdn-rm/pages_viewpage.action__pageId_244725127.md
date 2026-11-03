---
content_hash: 424d33e7f851c99a9b2c0800483e7599427b0f323ab83696f75e383321cbd5f9
fetched_at: '2026-06-29T00:08:15.006508+00:00'
page_id: '244725127'
product: rm
source: tdn-rm
title: DT_Vínculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244725127
version: 112
---

# Vínculo de Lançamento Financeiro

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Vincular Lançamentos* | *Vincular Lançamentos* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Baixa de Lançamentos Financeiros** | *Baixa de Lançamentos Financeiros* | | *Emissão / Recebimento de Cheque* | *Emissão / Recebimento de Cheque* | |
| **Cadastros Iniciais:** | *Lançamentos Financeiros* |
| **Parâmetro(s):** | *Fórmula composição valor original crédito adiantamento  - Fórmula para composição do valor original do crédito de adiantamento originado por adiantamento via movimento com incidência de IRRF-PJ e outras retenções diferentes das Contribuições Sociais (PIS, COFINS, CSLL). Disponível em "Contas a Pagar ou Contas a Receber" -> Baixa -> Manutenção de Baixas -> Baixa 5/5* |
| **Chamados Relacionados** | *TUJRTI* |
| **Requisito (ISSUE):** | FINTRF000161 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *FLAN, FRELLAN, FTRBLAN, FADIANTAMENTORETENCAO, FLOGVALORES* |

## Descrição

O vínculo é um processo de permite associar um valor dado como crédito de adiantamento, devolução ou nota de crédito, sendo representado como um lançamento financeiro especifico, a outro lançamento financeiro de natureza inversa para ser subtraído no seu valor de título. Esse valor dado será subtraído no lançamento financeiro durante os processos de baixa de lançamento, emissão ou recebimento de cheque, cálculo do valor líquido do mesmo. O valor de crédito de adiantamento é disponibilizado a partir do valor baixado no pagamento do adiantamento representado com um lançamento especifico da mesma natureza do lançamento que irá receber esse valor dado.

## **Procedimento para Utilização**

1. Selecionar o lançamento financeiro na tela de visão de lançamento que irá receber o valor dado como crédito de adiantamento, devolução ou nota de crédito
2. Clicar no processo "Vincular Lançamentos"
3. Selecionar o lançamento financeiro com o valor a ser dado para o lançamento selecionado
4. Após a seleção do lançamento financeiro com o valor a ser dado, salvar o vínculo entre os dois lançamentos

**Em caso de dúvidas consulte o help do aplicativo ou entre em contato pelo Help Desk**

divs
