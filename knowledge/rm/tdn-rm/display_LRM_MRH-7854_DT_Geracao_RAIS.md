---
content_hash: 6925f3b2dbf20af955dc38df596dfc9a28fdf869716f4ea4ca093c03343b047d
fetched_at: '2026-06-29T00:08:29.700375+00:00'
page_id: '272160691'
product: rm
source: tdn-rm
title: MRH-7854_DT_Geracao_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-7854_DT_Geracao_RAIS
version: 1
---

# Geração RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração RAIS* |
| **Situação/Requisito:** | Ao gerar o arquivo RAIS para funcionário com valor de diferença no mês de junho e importar o arquivo no validador GDRAIS, não foi considerado o valor de diferença presente no evento com o código de cálculo ’37 – Diferença Salário’. |
| **Solução/Implementação:** | Ajuste na rotina RAIS para não considerar data de pagamento do evento para considerar código de cálculo 96 e 37 e sim mês e ano de competência para comparação com data de desligamento. |
