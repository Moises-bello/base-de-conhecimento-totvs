---
content_hash: ad7f0d1f51d2d7501079a2b331fdb98fb1613f36ac06485d1e5187bfbf21e3b3
fetched_at: '2026-06-29T00:08:51.144212+00:00'
page_id: '336409014'
product: rm
source: tdn-rm
title: 2111085 PORTALMOBILE01-3327 DT CPF obrigatório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=336409014
version: 1
---

# CPF obrigatório

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Processo Seletivo (Portal) |
| **Função:** | Inscrição |
| **Situação/Requisito:** | Ao parametrizar o sistema para utilizar o CPF como login, o usuário era obrigado a informar o CPF do candidato e/ou do responsável pela inscrição (caso existisse). |
| **Solução/Implementação:** | Foi realizado ajuste na rotina para tratar a obrigatoriedade do campo CPF de forma dinâmica, ou seja, quando o parâmetro de utilizar o CPF para login estiver marcado e o candidato possuir responsável pela inscrição, esse terá o CPF obrigatório e o candidato não. Caso só exista o candidato esse passará a ter o CPF obrigatório. Durante a parametrização do processo seletivo, não será mais obrigado marcar o campo de obrigatório para o CPF do candidato e/ou responsável quando a opção de utilizar o CPF para login estiver selecionada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
