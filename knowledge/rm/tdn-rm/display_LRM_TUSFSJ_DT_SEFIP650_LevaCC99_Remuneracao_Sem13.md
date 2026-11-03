---
content_hash: 8d0a7188a754cc85eaf1cd6bcd0b3702c7f8b674954b44f40efa201395c85f4f
fetched_at: '2026-06-29T00:08:06.011484+00:00'
page_id: '236427308'
product: rm
source: tdn-rm
title: TUSFSJ_DT_SEFIP650_LevaCC99_Remuneracao_Sem13
type: documentation
url: https://tdn.totvs.com/display/LRM/TUSFSJ_DT_SEFIP650_LevaCC99_Remuneracao_Sem13
version: 2
---

# SEFIP 650 ESTÁ LEVANDO O VALOR DO CC 99 NO CAMPO REMUNERAÇÃO SEM 13o.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | *Na geração do SEFIP 650 com o parâmetro "Considere aviso prévio no SEFIP" marcado, o valor da Diferença do Aviso Prévio Indenizado, CC 99, está compondo o campo "Remuneração sem 13º salário".*  *Esta diferença não pode ser acumulada neste campo por já ter sido levada na GRRF.*  *Com o parâmetro desmarcado, o valor do SEFIP 650 fica correto.* |
| **Solução/Implementação:** | *Ajuste no SEFIP 650 para não levar o valor da Diferença do Aviso Prévio Indenizado, CC 99, no campo "Remuneração sem 13º salário", mesmo que o parâmetro "Considere aviso prévio no SEFIP" esteja marcado.* |
| **Chamados   relacionados:** | *TUSFSJ, TUUHV7* |
| **Versões/Release:** | *11.82.44, 12.1.11* |
