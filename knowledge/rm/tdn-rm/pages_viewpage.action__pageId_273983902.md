---
content_hash: 44cbd00b042c741fa5fb4678937e5fbd7d80fd9c7b27b05ebb66d2f2d1724674
fetched_at: '2026-06-29T00:08:32.384323+00:00'
page_id: '273983902'
product: rm
source: tdn-rm
title: DT Fechamento e Reabertura do Período de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273983902
version: 122
---

# Fechamento e Reabertura do Período de Competência

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Gestão de Custos Hospitalares |
| **Rotina:** | |  | | --- | | **Rotina** | | Fechamento do Período  Reabertura do Período |  |  | | --- | | **Rotina(s) envolvida(s)** | | Período de Competência | |
| **Requisito/S****tory/Issue:** | SAUGCH01-31 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER®  Oracle® |
| **Tabelas Utilizadas:** | SZ0PERIODOCOMPETENCIA |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Foram Implementados os processos de fechamento e reabertura do período de competência, que funcionam da seguinte forma:

**Fechamento do Período:** O período será encerrado quando todos os processos obrigatórios¹ e todos os processos opcionais² forem executados com sucesso.

Com o período encerrado não será possível realizar nenhum lançamento manual nas telas Lançamento em Conta, Base Rateio, Quantidade Produzida e Consumo Hospitalar, além dos processos disponíveis nessas telas e do processo de esquema de apuração.

Importante

Para o período ser encerrado todos os processos, obrigatórios e opcionais, devem ter sido executados com sucesso, e para isso a execução não precisa ser ao mesmo tempo, quando o último processo for executado com sucesso o sistema fechará o período automaticamente.

**Reabertura do Período:** Foi implementado um novo processo, que pode ser acessado pela tela Período de Competência / Processos / Reabertura do Período.

Ao confirmar pela primeira vez a reabertura do período, será exibida a lista de processos utilizados, entre obrigatórios¹ e opcionais². Devem ser selecionados os processos que serão reabertos.

Ao executar o processo, será questionado novamente se deseja reabrir. Ao confirmar, o período será reaberto e os processos selecionados serão reabertos para reprocessamento.

¹ Processos obrigatórios: Cálculo do Rateio, Cálculo do Custo Variável Indireto, Cálculo do Custo Unitário na Conta do Paciente e Cálculo do Custo Variável Direto.

² Processos opcionais: Cálculo do Custo Doação e Desconto, Cálculo do Custo Refeição e Cálculo do Custo Repasse. Os processos opcionais são configurados nos parâmetros "Utiliza cálculo de Doação e Desconto", "Utiliza cálculo da Refeição" e "Utiliza cálculo do Repasse".

## Procedimento para Utilização

**Fechamento do Período**

1. No Gestão de Custos Hospitalares, acesse Cadastros / Período de Competência.
2. Selecione o período de competência que deseja encerrar.
3. Acesse Processos / Fechamento de Período.
4. Selecione os processos que deseja executar e clique em Executar.  
   Se todos os processos, obrigatórios e opcionais, já estiverem sido executados com sucesso, o período será fechado.

**Reabertura do Período**

1. No Gestão de Custos Hospitalares, acesse Cadastros / Período de Competência.
2. Selecione o período de competência que deseja reabrir.
3. Acesse Processos / Reabertura de Período.
4. Marque a opção "Sim".
5. Selecione os processos que serão reabertos e clique em executar.  
   Ao menos um dos processos deve ser selecionado.
6. Clique em "Sim" na mensagem exibida.  
   O período será reaberto e os processos selecionados serão reabertos para reprocessamento.

divs
