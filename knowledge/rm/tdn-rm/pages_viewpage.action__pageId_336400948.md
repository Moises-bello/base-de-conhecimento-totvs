---
content_hash: 16bcca72790bc067d92c1b47140d83ea1eb4510d0b1a0550b335158bcbe96995
fetched_at: '2026-06-29T00:08:51.053736+00:00'
page_id: '336400948'
product: rm
source: tdn-rm
title: 2132860 FOPROTINAS01-3503 DT SALDO RESTANTE DE FÉRIAS NO RM PORTAL DIFERENTE
  DA MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=336400948
version: 1
---

# AJUSTE DO CÁLCULO DE SALDO RESTANTE DE FÉRIAS NO RM PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Sugestão de Férias - RM Portal |
| **Situação/Requisito:** | O saldo restante para marcação de férias no RM Portal não coincide com o valor demonstrado através da MDI. Essa diferença deve-se ao fato de o cálculo utilizado no TOTVS Folha de Pagamento não considerar as faltas do funcionário referentes ao primeiro mês do período aquisitivo, quando o período não começa no dia 1 do mês e não é o primeiro período aquisitivo do funcionário. Mais detalhes em <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.CadastroFerias.aspx> |
| **Solução/Implementação:** | O cálculo realizado para obter o 'Saldo Restante' no RM Portal ao cadastrar nova sugestão de férias foi ajustado para também não considerar as faltas do funcionário referentes ao primeiro mês do período aquisitivo, quando o período não começa no dia 1 do mês e não é o primeiro período aquisitivo do funcionário. Vale ressaltar que, apesar de o parâmetro de utilização de controle de faltas modificar a forma como o TOTVS Folha de Pagamento realiza o cálculo do saldo restante, esse parâmetro não interfere no comportamento do RM Portal, que sempre considera as faltas descontadas na ficha financeira do funcionário. |
| **Tickets relacionados:** | 2132860 |
