---
content_hash: 71500a233300c7c78f195d682caa708c8f81cb1b0b0f12cdb388d7e5dc3cd7a8
fetched_at: '2026-06-29T00:08:06.109528+00:00'
page_id: '236433322'
product: rm
source: tdn-rm
title: TUSHPF_DT_GRRF_Gera_BaseFGTS13_Negativa
type: documentation
url: https://tdn.totvs.com/display/LRM/TUSHPF_DT_GRRF_Gera_BaseFGTS13_Negativa
version: 4
---

# GRRF ESTÁ GERANDO BASE DE FGTS 13o. COM VALOR NEGATIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *GRRF* |
| **Situação/Requisito:** | *Geração da GRRF está permitindo Base de FGTS 13o. com valor negativo.*  *Caso ocorreu devido a ter sido pago adiantamento da 1a.parcela de 13o. em férias no início do ano, e no mês seguinte o funcionário foi demitido antes de ter adquirido 6 avos de direito.*  *Nesta situação o desconto efetuado no evento de CC 35 foi maior que o pagamento de 13o. na rescisão, resultando em uma Base de FGTS 13o. negativa.*  *Na GRRF não pode ser enviada Base de FGTS negativa, neste caso o valor deve ser zerado.* |
| **Solução/Implementação:** | *Ajuste na GRRF para zerar o valor da Base de FGTS 13o., caso o valor total resulte em um valor negativo.* |
| **Chamados   relacionados:** | *TUSHPF, TUUSU4* |
| **Versões/Release:** | *11.82.44, 12.1.11* |
