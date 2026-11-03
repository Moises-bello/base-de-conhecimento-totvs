---
content_hash: 2f178e16434af53d8ba9084e95d312731347174360d763d81b526b9aaf736d13
fetched_at: '2026-06-29T00:09:04.132400+00:00'
page_id: '382552394'
product: rm
source: tdn-rm
title: 2753774 DEDUINTEGRACOES-2400 DT Cancelamento da disciplina no dia do vencimento
type: documentation
url: https://tdn.totvs.com/display/LRM/2753774+DEDUINTEGRACOES-2400+DT+Cancelamento+da+disciplina+no+dia+do+vencimento
version: 1
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Lançamento |
| **Situação/Requisito:** | Considerando que na situação de matricula a opção “Abater valor da disciplina somente para parcelas com vencimento igual ou superior a data de alteração da situação de matricula” esteja marcada.  Temos:  Um contrato com 6 parcelas sendo 4 parcelas com lançamento gerado e baixado, a 4º parcela tem vencimento no dia 03/05/2018 e no dia 03/05/2018 teve cancelamento de uma disciplina, neste caso o sistema deveria devolver o valor correspondente a disciplina na 4 parcela rateando entre a 2 parcelas restantes.  No entanto o cáculo das parcelas 5 e 6 não está considerando o crédito financeiro gerado em função do cancelamento da disciplina no dia do vencimento da parcela 4. |
| **Solução/Implementação:** | Foi realizado um ajuste, pois quando houver um cancelamento da disciplina em que a data do cancelamento seja igual a data do vencimento da parcela, e a parcela esteja baixada, o sistema deverá realizar a devolução do crédito corretamente nas parcelas em aberto, isso considerando que na situação de matricula a opção “Abater valor da disciplina somente para parcelas com vencimento igual ou superior a data de alteração da situação de matricula”. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
| **Pacote:** | Informe o [linkdopacote] |
