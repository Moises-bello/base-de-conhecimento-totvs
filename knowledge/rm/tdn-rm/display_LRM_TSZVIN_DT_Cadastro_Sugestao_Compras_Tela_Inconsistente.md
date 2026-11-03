---
content_hash: f5b55838b54811b8f6eb6ef9ec002afc83c776e7416a77f505bc656f54b83083
fetched_at: '2026-06-29T00:06:08.490946+00:00'
page_id: '201748377'
product: rm
source: tdn-rm
title: TSZVIN_DT_Cadastro_Sugestao_Compras_Tela_Inconsistente
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZVIN_DT_Cadastro_Sugestao_Compras_Tela_Inconsistente
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Bibliotecária* |
| **Função:** | *Sugestão de compras* |
| **Situação/Requisito:** | *O cadastro de sugestão de compras pelo portal está limpando campos ao salvar uma nova sugestão, o sistema limpa o campo Tipo de publicação e também o sistema está permitindo nos campos 'volume' e 'ano' adicionar texto que retorna erro ao tentar salvar.* |
| **Solução/Implementação:** | *Foi feito o ajuste no evento que recarrega a página, para que recarregue o tipo de publicação corretamente após salvar, e também foi adicionado na tela restrições nos campos "volume' e 'ano' para que aceitem somente números.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41* |
