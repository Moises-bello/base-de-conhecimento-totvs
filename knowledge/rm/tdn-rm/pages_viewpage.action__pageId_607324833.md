---
content_hash: 8a4cd2194e27a478878790e8e19363e459bf3beee56f68a1248143bb4c0250a2
fetched_at: '2026-06-29T00:10:58.830482+00:00'
page_id: '607324833'
product: rm
source: tdn-rm
title: 2.16.1 Cancelamento da Liquidação Duvidosa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607324833
version: 2
---

Para **cancelar** uma inclusão em Liquidação Duvidosa, selecione o lançamento, acesse Processos | Cancelar Liquidação Duvidosa

Informe a Data do Cancelamento e clique em Avançar e logo em seguida clique em Executar

Ao executar o processo informando a "Data do Cancelamento", para os lançamentos com status de "*Liquidação Duvidosa*" ou "*Liquidação Duvidosa Parcial*", o status desses lançamentos ficarão com status de "*Liquidação Não Duvidosa*".

**Validações para Cancelamento da Liquidação Duvidosa**

* O Status da liquidação duvidosa do lançamento deverá ser liquidação duvidosa ou liquidação duvidosa parcial;
* O Lançamento deve estar em aberto ou parcialmente baixado (caso a baixa tenha sido executada antes da liquidação duvidosa). Se algum processo tiver sido executado após a liquidação duvidosa, ele deve ser desfeito antes do cancelamento.
* O Lançamento não pode ter "baixa pendente".
* Como podem existir vários registros de liquidação duvidosa em um mesmo lançamento a operação será realizada sobre aquele que estiver ativo (não cancelado). Caso não existe algum nada será realizado.
* A data de cancelamento da liquidação deve ser maior ou igual a data da própria liquidação e não pode ser maior que a data atual.

**Resultado da execução do processo:**

* Para os lançamentos que estiverem com o status de liquidação duvidosa ou liquidação duvidosa parcial, a contabilização será estornada e o status de liquidação duvidosa voltará para não duvidoso.
* O status do registro da liquidação duvidosa passará para "*Cancelada*", para manter o histórico de liquidações duvidosas.

Para **visualizar** a Liquidação Duvidosa Cancelada, acesse Anexos | Liquidação Duvidosa

O Anexo "Liquidação Duvidosa" na visão Geral de Lançamentos irá exibir todas as Liquidações existentes para o lançamento financeiro.
