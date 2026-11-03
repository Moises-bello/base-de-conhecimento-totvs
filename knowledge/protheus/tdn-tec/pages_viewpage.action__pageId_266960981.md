---
content_hash: aceb49c07a47c7247b32316b63f9a851bc207a9c9aac5954b6c2d6ee7721035b
fetched_at: '2026-07-02T19:24:21.272223+00:00'
page_id: '266960981'
product: protheus
source: tdn-tec
title: Destaque de palavras reservadas falhando quando possui um operador junto.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266960981
version: 1
---

|  |  |
| --- | --- |
| Situação | Ao adicionar um operador no início de uma palavra reservada, ela perde a cor de destaque |
| Ocorrência | Foi encontrado um problema na identificação dos operadores para fazer o destaque, o qual usava o mesmo processo das palavras reservadas, fazendo com que o TDS identificasse um texto como "!empty" inteiro como operador, e não o operador "!" seguido da palavra reservada "empty" |
| Correção | O processo de identificação de operadores foi alterado para considerar apenas os characteres específicos desse tipo |
| Informações adicionais | * Referente ao chamado: [TVRBJ7](http://jira.totvs.com/browse/SSIM-1216) * Referente à ocorrência: [SSIM-1216](http://jira.totvs.com/browse/SSIM-1216) * Disponível em builds superiores a 11.3.3.. |
