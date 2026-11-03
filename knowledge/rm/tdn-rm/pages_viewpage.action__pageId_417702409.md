---
content_hash: 85d20f1c41d05f2950d842e604500f05edcd39ea67d569c5317e73874b037957
fetched_at: '2026-06-29T00:09:12.913002+00:00'
page_id: '417702409'
product: rm
source: tdn-rm
title: 3931988 FOPCALCULO01-4860 Alteração de Histórico Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417702409
version: 1
---

# Histórico Salarial

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Histórico Salarial |
| **Situação/Requisito:** | Após informar o novo salário, a linha de um centavo é deletada do Histórico, e a Data do novo salário é alterada retirando o ‘horário’ de dez segundos que o produto usou no momento que inseriu a segunda linha salarial.  Porem no momento de salvar esta alteração passo a ocorrer o erro abaixo:  “ORA-01722: número inválido” |
| **Solução/Implementação:** | Ajustado a alteração do histórico salarial para não ocorrer o erro acima quando o histórico for Alterado/Incluído. |
| **Tickets relacionados:** | 3931988 |
