---
content_hash: 4140d0c7ddb942e5fb6638ad7aa2fc10134c94c0789ff30e61153a70806b0172
fetched_at: '2026-06-29T00:10:47.434987+00:00'
page_id: '557322550'
product: rm
source: tdn-rm
title: Replicar lançamento selecionado por intervalo de datas em Honorários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=557322550
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Processos**
   1. **Replicar lançamento selecionado por intervalo de datas**
4. **Anexos**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

Replica os lançamentos selecionados durante o período de referência indicado pelo usuário.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Serão listados no grid todos os atendimentos de acordo com o filtro selecionado pelo usuário. Clique duas vezes no atendimento para acessar os detalhes.

Procesos

## **03. Processos**

**3.1 Replicar lançamento selecionado por intervalo de datas**

Para executar este processo, selecione o lançamento na aba 'Honorários', clique no menu 'Processos' ainda na mesma aba, e depois 'Replicar lançamento selecionado por intervalo de datas'.

Selecione o período de referência para replicar:

Para executar esse processo, é necessário:

* O usuário que executa o processo deve ter perfil de Faturamento
* O atendimento que possui esse atendimento não pode estar com o Status = Fechado
* A data de início indicada no período de referência deve ser menor ou igual que a final
* O período de referência deve estar entre data inicial e final da parcial
* O lançamento a ser replicado não pode já ter sido estornado

Caso qualquer um desses casos não seja verdadeiro, ao tentar executar, um aviso explicando o acontecido aparece na tela e o processo é abortado:

Quando o processo é concluído com sucesso, uma réplica dos lançamentos selecionados é criada para cada dia do período informado. Quando mais de um lançamento é selecionado, se um deles não pode ser replicado por uma das razões acima, o processo o desconsidera e replica apenas o(s) lançamento(s) válidos :

## **04. Anexos**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Data Entrada | Data de início da parcial |
| Data Saída | Data final da parcial |
| Estornado | Indica se o pedido já foi estornado |
| Período de Referência | Indica o  que o intervalo de datas que os lançamentos serão replicados |
| Status Atend | Status do Atendimento |

## **05. TABELAS UTILIZADAS**

* SZATENDHONORARIO
* SZATENDIMENTO
* SZPARCIALATEND
