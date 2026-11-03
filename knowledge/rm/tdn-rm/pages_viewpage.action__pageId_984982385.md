---
content_hash: 04cce5ca8e0d3287bb6b5bb14999db36ee71b2cf1acbd0fe5f8eb805d0e6b50f
fetched_at: '2026-06-29T00:12:16.279094+00:00'
page_id: '984982385'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Lançamentos Legados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=984982385
version: 3
---

## Introdução

Consideram-se **lançamentos legados** todos os lançamentos que possuem **código da aplicação = X** e que **não estão vinculados** diretamente a:

* Contratos de locação,
* Fundos promocionais, ou
* Condomínios.

Durante a **implantação**, essa massa de dados deve ser carregada manualmente em uma tabela específica: **XALGFLANLEGADO**.

A identificação da **Origem** dos lançamentos deve ser determinada como abaixo:

* Locação = 1,
* Fundo Promocional = 2,
* Condomínio = 3

A partir da inclusão nessa tabela:

* Os registros poderão ser exibidos na visão de **Lançamentos de Shopping**.
* Esses lançamentos poderão ser **selecionados** para compor boletos de cobrança partilhada.

⚠️ **Atenção**:  
Esse processo de importação **não é automatizado pelo sistema**. Ele deve ser realizado **manualmente pelo implantador**.

---

## Acordos sobre Lançamentos Legados

Os registros com **código da aplicação = X** também podem ser utilizados para **acordos de cobrança** quando necessário.

* Ao serem gerados lançamentos de acordo, **se estiverem presentes na tabela `XALGFLANLEGADO`**, serão igualmente controlados por ela.
* Caso sejam **excluídos**, serão automaticamente **removidos da tabela**.

---

## Resumo do Fluxo

1. Identificar lançamentos legados (**código aplicação = X** e sem vínculo com contrato, fundo ou condomínio).
2. Importar manualmente para a tabela **XALGFLANLEGADO**.
3. Visualizar os registros na tela de **Lançamentos de Shopping**.
4. Selecionar lançamentos para compor **boletos de cobrança partilhada**.
5. Permitir acordos sobre esses lançamentos, com inclusão e exclusão refletidas na tabela.
