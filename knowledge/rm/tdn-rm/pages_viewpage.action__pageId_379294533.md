---
content_hash: 395b3724a73b17736473fa61a1789baed604345ab1f9c33cba55f80232227f79
fetched_at: '2026-06-29T00:09:02.189336+00:00'
page_id: '379294533'
product: rm
source: tdn-rm
title: 3212450 CONTROLADORIA01-1648 DT SPED Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379294533
version: 2
---

# Geração ECD layout 5

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Contábil |
| **Função:** | SPED Contábil |
| **Situação/Requisito:** | Ao gerar o arquivo da ECD para o ano de 2016, o J150 está saindo com menos campo do que o normal, apresentando erro na validação da ECD no PVA. |
| **Solução/Implementação:** | O método responsável por retornar os campos que compõe o registro J150, no layout 5, foi modificado. O registro estava sendo criado com 6 campos, porém passou a ser gerado com 8, atendendo o manual de orientação da ECD. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A.. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
