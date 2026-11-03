---
content_hash: ba7a20ccd631094bdb89f9789fa0d5f000d3cb653351091c987613d6f732cd09
fetched_at: '2026-06-29T00:08:58.033529+00:00'
page_id: '358458861'
product: rm
source: tdn-rm
title: 2689270 RMSAU-3738 Faturamento de Parcial do SUS
type: documentation
url: https://tdn.totvs.com/display/LRM/2689270+RMSAU-3738+Faturamento+de+Parcial+do+SUS
version: 1
---

# Faturamento SUS AIH

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Realizar o faturamento de Elaborações AIH (SUS) |
| **Situação:** | Ao tentar realizar o faturamento de uma Elaboração com Data de Saída vazia, ou seja, de uma parcial na qual o paciente ainda está internado, o sistema apresenta um erro de validação para o campo "Ano / Mês apresentação". |
| **Solução:** | Incluído verificação se a Data de Saída está vazia antes de realizar a validação da mesma. Caso esteja vazia, o faturamento ocorre normalmente. |
