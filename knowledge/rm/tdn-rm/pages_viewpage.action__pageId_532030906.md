---
content_hash: 440b40ac89c9a629066817a10fc99dc11dc3555d9bae8127d727310a6179b58d
fetched_at: '2026-06-29T00:10:36.282357+00:00'
page_id: '532030906'
product: rm
source: tdn-rm
title: RMCTB00004_Layout Importação de Plano de Contas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532030906
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.20 |
| **Ocorrência:** | Layout de Importação de Plano de Contas. |
| **Ambiente:** |  |
| **Passo a passo:** | As informações do layout  abaixo deverão ser disponibilizadas em um único arquivo, pois no momento da importação o sistema irá distinguir a informação através do identificador de Linha.  Para os Campos "Analítica ou Sintética", "Devedora ou Credora", "Distribuição Gerencial" e "Conta Global" devem ser informados no arquivo de origem (.txt) somente letras. Ou seja, Analítica = A, Sintética = S, Devedora = D, Credora = C, Distribuição Gerencial = (S para sim ou N para não) e Conta Global = (S para sim ou N para não).     | # | Descrição | Tipo | Tamanho | Obrigatório | Observação | | --- | --- | --- | --- | --- | --- | | **0** | Identificador de Linha | Alfa | 1 | X | "M" Indica Linha de Mestre | | **1** | Código da Conta | Alfanumérico | 40 | X |  | | **2** | Código Reduzido | Alfanumérico | 20 | X |  | | **3** | Descrição | Alfanumérico | 40 | X |  | | **4** | Analítica ou Sintética | A ou S | 1 | X | A = Analítica  S = Sintética | | **5** | Devedora ou Credora | D ou C | 1 | X | D = Devedora  C = Credora | | **6** | Distribuição Gerencial | S ou N | 1 | X | S = Possui Distribuição  N = Não possui distribuição | | **7** | Conta Global | S ou N | 1 | X | S = É Global  N = Não é Global | | **8** | Campo Opcional | Numérico | 4 | x |  | | **9** | Natureza Conta P/ SPED Contábil \* | Tabela - Natureza Conta | 2 | X |  | | **10** | Data Inclusão | Alfanumérico | 10 | X |  | | **11** | Conta de estorno | Alfanumérico | 40 | x |  |  * **Tabela Natureza da conta**  | **00** | Não Informado | | --- | --- | | **01** | Contas de Ativo | | **02** | Contas de Passivo | | **03** | Patrimônio Líquido | | **04** | Contas de Resultado | | **05** | Contas de Compensação | | **09** | Outras |   **Linha da Distribuição Gerencial**  Layout utilizado somente para as contas com Distribuição Gerencial informada no Plano de Contas   |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | # | **Descrição** | **Tipo** | **Tamanho** | **Obrigatório** | **Observação** | | **1** | Identificador de linha | D | 1 | X |  | | **2** | Código da Conta Gerencial | Alfanumérico | 40 | X |  | | **3** | Percentual | Numérico c/ 2 decimais |  | X |  | |
| **Observações:** |  |
