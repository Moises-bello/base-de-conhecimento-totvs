---
content_hash: f2f573ff7989d3480cb7cda21b9f0d230357bbeee48b8d0e9c4e69efbdff9a5d
fetched_at: '2026-06-29T00:12:01.363277+00:00'
page_id: '893921587'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Cobrança partilhada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=893921587
version: 4
---

## 📌 Introdução

Este processo visa aprimorar a rotina de cobrança e agrupamento de boletos.  
Com a atualização, o processo de **“boleto MultiColigada”** foi alterado para **“Cobrança Partilhada”**, refletindo a nova estrutura de como os boletos são agrupados.

Este processo facilita a geração de boletos de forma mais agrupada e detalhada, além de melhorar a organização das cobranças ao permitir diferentes formas de agrupamento entre clientes, contratos e vencimentos.

⚠️ **Observação:** O modelo de **Cobrança Partilhada** não contempla o uso de **boleto híbrido**.

---

## ▶️ Procedimentos para Utilização

Na visão de lançamentos, selecione os lançamentos que irão gerar os boletos e, em seguida, clique em:  
**Processos > Cobrança Partilhada**

---

## 🧩 Agrupadores Disponíveis

Na tela apresentada para geração de boletos agrupados de forma mais dinâmica, foram introduzidos novos agrupadores.  
Esses agrupadores podem ser utilizados para diferentes combinações de filtros, conforme os requisitos de cada situação.

Os agrupadores disponíveis são:

* **Cli/For (Padrão):**  
  Agrupamento simples entre cliente e fornecedor.
* **Cli/For + Contrato:**  
  Agrupamento por cliente, fornecedor e contrato.
* **Cli/For + Contrato + Competência:**  
  Agrupamento que inclui a competência do lançamento.
* **Cli/For + Contrato + Vencimento:**  
  Agrupamento que inclui o vencimento.

⚠️ **Importante:**  
Quando este agrupador for utilizado, o campo **“Vencimento”** será bloqueado, pois o vencimento será determinado de acordo com os lançamentos registrados.

---

## 💼 Conta Caixa do Lançamento

Existe um campo específico para informar a **Conta Caixa do Lançamento**.

Este campo valida se a conta caixa utilizada nos lançamentos é a mesma para todos os grupos de lançamentos, garantindo que, ao gerar o boleto, a conta caixa associada esteja correta.

---

## ✅ Execução do Processo

Ao final, ao clicar em **Executar**, o processo será realizado e o **boleto será gerado** conforme os agrupamentos e parâmetros definidos.
