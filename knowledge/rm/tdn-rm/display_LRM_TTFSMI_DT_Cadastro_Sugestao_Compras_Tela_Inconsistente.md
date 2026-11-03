---
content_hash: be5b6e615030161e2ac9204772a5cd21b18d4fcd343a1a92677674987bef2b35
fetched_at: '2026-06-29T00:06:08.494765+00:00'
page_id: '201748389'
product: rm
source: tdn-rm
title: TTFSMI_DT_Cadastro_Sugestao_Compras_Tela_Inconsistente
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFSMI_DT_Cadastro_Sugestao_Compras_Tela_Inconsistente
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
| **Versões/Release:** | *12.1.8* |
