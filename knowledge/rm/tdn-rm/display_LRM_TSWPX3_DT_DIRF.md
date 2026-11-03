---
content_hash: 1de5a5a469fb1303b9a90b63241d332e6d8e62aa6ab25b6b78dbe9815dbc7ec8
fetched_at: '2026-06-29T00:06:02.552795+00:00'
page_id: '198946340'
product: rm
source: tdn-rm
title: TSWPX3_DT_DIRF
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWPX3_DT_DIRF
version: 1
---

# DIRF

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *C&P.* |
| **Módulo:** | *Folha de pagamento.* |
| **Função:** | *Dirf.* |
| **Situação/Requisito:** | *Mesmo cadastrando uma nova tabela de valores fixos para desconto de "Valor a deduzir de IRRF por dependente" (Inicio de Vigência 01/04/2015 a Fim de Vigência 31/12/2015), ao gerar o arquivo, no registro "RTDP" todos os valores posteriores ao mês 04 permanecem com o valor da vigência errada.* |
| **Solução/Implementação:** | *Otimizado a rotina de obtenção do valor fixo a deduzir para IRRF dos dependentes, obtendo o valor de acordo com a interseção do primeiro e último dia do mês em cada vigência. Havendo mais de uma vigência que o primeiro ou último dia do mês interceda ao início e fim da vigência será considerado o valor da vigência com  maior data de início..* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSWPX3, TSPUXJ.* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.40* |
