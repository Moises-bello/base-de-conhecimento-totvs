---
content_hash: 855181c098fd30e9e0f540d43117880599fa4dc4863515034a29d59e67dc62a0
fetched_at: '2026-06-29T00:08:07.675996+00:00'
page_id: '237384069'
product: rm
source: tdn-rm
title: TTVWNN_DT_SEFIP_Leva_UmCentavo_Para_Transferido
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVWNN_DT_SEFIP_Leva_UmCentavo_Para_Transferido
version: 3
---

# SEFIP LEVA UM CENTAVO PARA FUNCIONÁRIO TRANSFERIDO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | *Na geração do SEFIP com funcionários transferidos pelo Tipo 5 - Transferência sem ônus p/ Cedente, está sendo levado o valor de 0,01 no campo de Remunerações Sem 13o. Salario.*  *Para funcionário com este tipo de rescisão, transferido no dia 1o. do mês, não tem necessidade de levar este valor.*  *Neste caso, o Validador do SEFIP aceita zero no campo de remuneração.* |
| **Solução/Implementação:** | *Ajuste na geração do SEFIP para não levar 0,01 no campo de remuneração, quando o funcionário é transferido com o Tipo 5 - Transferência sem ônus p/ Cedente, no dia 1o. do mês.* |
| **Chamados   relacionados:** | *TTVWNN, TUXTBK, TUZJZD* |
| **Versões/Release:** | *11.82.44, 12.1.11* |
