---
content_hash: 3e200681469299bd3178f4449d583bac383ab66b2cda327f34d766bd2032d3fd
fetched_at: '2026-06-29T00:09:29.730199+00:00'
page_id: '425457414'
product: rm
source: tdn-rm
title: 4024922 FOPCALCULO01-4918 RM x DCTFWeb - PIS para Estagiários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425457414
version: 1
---

# RM x DCTFWeb

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | RM x DCTFWeb |
| **Situação/Requisito:** | Ao gerar o relatório Compartativo RM x DCTF web, o sistema gera mensagem de erro para estagiários: Funcionário "ALEXANDRE LIMA DE FREITAS" com o PIS "00000000000" não foi encontrado na base, verifique o cadastro..    Essa mensagem se dá de maneira indevida, pois para estagiários não há obrigatoriedade de informar número de PIS ao eSocial. Desse modo, a validação de PIS não deveria se aplicar a estagiários. |
| **Solução/Implementação:** | Ajuste no comparativo DCTFWeb x TAF, para quando o funcionário é estagiário e não tem PIS. |
| **Tickets relacionados:** | 4024922 |
