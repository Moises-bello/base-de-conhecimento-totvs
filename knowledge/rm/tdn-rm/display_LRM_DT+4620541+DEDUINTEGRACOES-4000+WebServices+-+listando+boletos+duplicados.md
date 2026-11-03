---
content_hash: b29f9d86539c5c6329146d6b7eb3bc61ca151da8554739fe40af5f9249b2f3c2
fetched_at: '2026-06-29T00:09:54.767248+00:00'
page_id: '445645372'
product: rm
source: tdn-rm
title: DT 4620541 DEDUINTEGRACOES-4000 WebServices - listando boletos duplicados
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+4620541+DEDUINTEGRACOES-4000+WebServices+-+listando+boletos+duplicados
version: 2
---

# WebService - Listar Boleto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | WebService Listar Boletos |
| **Situação/Requisito:** | Estamos utilizando o Webservice de listar boletos, porém quando o aluno possuí lançamentos agrupados em um único boleto, o Webservice está trazendo o mesmo boleto na listagem duplicado. O correto seria ele trazer somente um boleto. |
| **Solução/Implementação:** | Adequação do webservice ListarBoletos para que não retorne boletos duplicado quando o mesmo estiver agrupando vários lançamentos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | Informe o [linkdopacote] |
