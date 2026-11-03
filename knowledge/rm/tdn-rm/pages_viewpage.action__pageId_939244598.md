---
content_hash: 6307ee9309db0ea42b6f700c32ba6408d5d4ee9a5bc051569f600f0154f8cb3c
fetched_at: '2026-06-29T00:12:09.070248+00:00'
page_id: '939244598'
product: rm
source: tdn-rm
title: 03. Contratos 2.0 | Processos | Reclassificação Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=939244598
version: 8
---

ReclassificacaotrueReclassificar Contabilidade

O processo de **Reclassificar Contabilidade** do contrato tem como objetivo de incrementar a "Data Fim Curto Prazo" de um item de contrato de arrendamento, e com a mudança desta data,  reclassificar as parcelas de "Longo Prazo" que ficarem anterior ou igual a nova data para "Curto Prazo".

Parâmetros que serão informados no processo:

* Meses a incrementar (Deve-se escolher a quantidade de meses que a data fim curto prazo vai avançar)
* Utiliza último dia do mês, quando estiver marcado o sistema avançará a quantidade de meses especificada no parâmetro anterior, e ajustará a nova data fim curto prazo para o último dia do mês resultante. Caso o parâmetro esteja desmarcado, será realizado apenas a soma dos meses informados na data atual de fim do curto prazo, mantendo o dia que estava originalmente.
* Data Contabilização.

**Exemplo 01**:

   "Data Fim Curto Prazo" = 10/05/2024

   Processo de de reclassificação, adicionando 2 meses, sem marcar a opções último dia

   A nova data    "Data Fim Curto Prazo" = 10/07/2024

**Exemplo 02**:

   "Data Fim Curto Prazo" = 10/05/2024

   Processo de de reclassificação, adicionando 2 meses, marcando a opções último dia

   A nova data "Data Fim Curto Prazo" = 31/07/2024

**Exemplo 03**:

   "Data Fim Curto Prazo" = 31/01/2024

   Processo de de reclassificação, adicionando 1 meses, sem marcar a opções último dia

   A nova data "Data Fim Curto Prazo" = 28/02/2024

Cancelar Reclassificação Contábil

Este processo permite o cancelamento da última reclassificação realizada nos itens de contrato de arrendamento selecionados. Assim, os campos indicados abaixo terão seus valores ajustados para o que estava registrado antes da última execução:

* **Classificação de Prazo** das parcelas afetadas pela última execução.
* Campo **Data Fim Curto Prazo** na aba de Identificação do item do contrato.

Após a execução do processo, será gerado um registro no **Histórico de Processos** e a reclassificação cancelada será removida do **Histórico de Reclassificação**.
