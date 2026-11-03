---
content_hash: 3c13a6283de62ec7c7353ce33c6ed10753bb6f97bc2520040624163eee0c8c04
fetched_at: '2026-06-29T00:11:59.901435+00:00'
page_id: '876232643'
product: rm
source: tdn-rm
title: DT - Liberação de Competência - Tratativa para executar o processo "Atualiza
  Campo Desconto Simplificado"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=876232643
version: 11
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Liberação de Competência - Tratativa para executar o processo "Atualiza Campo Desconto Simplificado" |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11680](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11680 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.257
* 12.1.2406.205
* 12.1.2410.133 e superiores

## **03. SITUAÇÃO/REQUISITO**

No processo de **"Validação da Liberação de Competência"**, deverá ser implementada uma nova regra para alertar o usuário caso existam funcionários com os seguintes campos não preenchidos:

* **PFPERFF.IRRFSIMPLIFICADOCAIXA**
* **PFPERFF.IRRFFERSIMPLIFICADOCAIXA**
* **PFPERFF.IRR13SIMPLIFICADOCAIXA**

Essa obrigatoriedade visa garantir que, na geração da DIRF 2024/2025, os valores de desconto simplificado sejam devidamente considerados, uma vez que a nova versão da DIRF passa a ler esses campos.

## **04. SOLUÇÃO**

Foi implementada no processo de **Validação da Liberação de Competência** uma validação que emitirá **Aviso** quando os campos **IRRFSIMPLIFICADOCAIXA**, **IRRFFERSIMPLIFICADOCAIXA** ou **IRRF13SIMPLIFICADOCAIXA** da tabela **PFPERFF** estiverem preenchidos com valores **menores que 2** ou estiverem **NULL.** Essa validação será aplicável somente ao ano competência de **2024**.

Mensagem que será visualizada no log de avisos.

Diante do aviso apresentado, o usuário terá duas opções:

1. **Abortar a Liberação de Competência:**

   * Interrompe o processo para corrigir os valores dos campos mencionados.
   * O usuário deverá executar o processo **"Atualiza Campo Desconto Simplificado"**, que atualiza automaticamente os campos **IRRFSIMPLIFICADOCAIXA**, **IRRFFERSIMPLIFICADOCAIXA** e **IRRF13SIMPLIFICADOCAIXA** com os valores apropriados.
   * Essa ação garante a conformidade necessária para a correta geração da DIRF 2024/2025.
   * Exemplo de campos que precisarão serem atualizados com 2 ou 3 antes da liberação de competência:
2. **Seguir com a Liberação de Competência:**

   * Permite continuar o processo, ignorando o aviso apresentado.
   * O usuário deverá marcar os parâmetros:
     + **"Li e estou ciente dos avisos que foram dados para as coligadas abaixo".**
     + **"Desejo liberar a competência das coligadas que tiveram avisos".**

* + É imprescindível que, antes de gerar a DIRF 2024/2025, o processo **"Atualiza Campo Desconto Simplificado"** seja executado para garantir a conformidade necessária à geração da declaração.

## **05. DEMAIS INFORMAÇÕES**
