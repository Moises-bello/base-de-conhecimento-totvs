---
content_hash: bf0e486e67f786a3553c171aaea4e6c1d977437452836922d1e4da6325de11ee
fetched_at: '2026-06-29T00:09:09.681685+00:00'
page_id: '393362437'
product: rm
source: tdn-rm
title: 2548046 FOPROTINAS01-5470 - Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393362437
version: 6
---

# Grupo AAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Encargos - Lançamentos Financeiros |
| **Situação/Requisito:** | Ao realizar a geração do lançamento financeiro do tipo 'Líquido Salarial' para funcionário com data de demissão no ano atual e para outro funcionário com data de demissão no ano anterior, em que ambos os funcionários tinham rescisão complementar calculada no mesmo mês, apenas o funcionário com data de demissão no ano anterior gerava valor. |
| **Solução/Implementação:** | Foi realizada a correção para que não seja gerado o lançamento financeiro do tipo 'Líquido Salarial' quando o funcionário estiver demitido. Nestes casos deve ser utilizado o lançamento do tipo 'Líquido Rescisão' para ambos os casos descritos acima. |
| **Tickets relacionados:** | 2548046 |
