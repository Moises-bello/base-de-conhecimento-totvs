---
content_hash: 30052a3e31d9d2205b465c3081b31bb0a04c6ff6b64e44cdf6bd5f73e1efb7d1
fetched_at: '2026-06-29T00:08:29.406452+00:00'
page_id: '272144939'
product: rm
source: tdn-rm
title: MRH7854_DT_Geracao_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH7854_DT_Geracao_RAIS
version: 109
---

# Geração RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração RAIS* |
| **Situação/Requisito:** | Ao gerar o arquivo RAIS para funcionário com valor de diferença no mês de junho e importar o arquivo no validador GDRAIS, não foi considerado o valor de diferença presente no evento com o código de cálculo ’37 – Diferença Salário’. |
| **Solução/Implementação:** | *Ajuste na rotina RAIS para não considerar data de pagamento do evento para códigos de cálculo 96 e 37 e sim mês e ano de competência para comparação com data de desligamento.*divs |
