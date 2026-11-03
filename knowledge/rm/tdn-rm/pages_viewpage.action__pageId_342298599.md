---
content_hash: ded6b2ca1439ec733bab4376106697c1fbf1a44bb2d8cdba8ae0ef5cdd9b93bf
fetched_at: '2026-06-29T00:08:52.664083+00:00'
page_id: '342298599'
product: rm
source: tdn-rm
title: 2222113 FINANCEIRO01-5325 DT Inclusão de liquidação duvidosa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342298599
version: 1
---

# Inclusão de liquidação duvidosa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Inclusão de liquidação duvidosa. |
| **Situação/Requisito:** | Ao executar o processo de 'Inclusão de liquidação duvidosa' para lançamentos com tipo contábil de 'baixa contábil', caso o preenchimento do 'Número do documento' estiver obrigatório nos parâmetros de 'Integração contábil', o sistema apresenta a validação da falta do 'Número de documento' nas partidas contábeis que estão sendo geradas. |
| **Solução/Implementação:** | Ajustado o serviço de contabilização da liquidação duvidosa, para que preencha o 'Número do documento' quando o lançamento tiver tipo contábil igual a contábil ou baixa contábil. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FIN000254 |
| **Documento de Referência:** | N/A. |
