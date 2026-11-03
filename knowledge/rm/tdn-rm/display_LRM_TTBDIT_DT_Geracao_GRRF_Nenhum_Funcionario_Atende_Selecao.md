---
content_hash: ce2b4b1ea8f8552f4da26804eb9d3c64d859c1dd4e945828711970e0a79262a9
fetched_at: '2026-06-29T00:06:04.661273+00:00'
page_id: '200910164'
product: rm
source: tdn-rm
title: TTBDIT_DT_Geracao_GRRF_Nenhum_Funcionario_Atende_Selecao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBDIT_DT_Geracao_GRRF_Nenhum_Funcionario_Atende_Selecao
version: 4
---

# FOLHA DE PAGAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *GRRF* |
| **Situação/Requisito:** | *Ao gerar GRRF na base de produção ocorre erro 'Nenhum Funcionário atende a Seleção'.* |
| **Solução/Implementação:** | *Foi ajustado na rotina de rescisão coletiva para não informar a hora no campo data de demissão. Alterado também na GRRF para aceitar caso tenha algum caso com hora no campo data de demissão* |
| **Chamados relacionados:** | *TSWHGN* |
| **Versões/Release:** | *12.1.7* |
