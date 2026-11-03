---
content_hash: 3ddb55c3ebcf227e82da7c8f2d53f979406fad9d868f040c0e8d3d911264572f
fetched_at: '2026-06-29T00:08:20.893147+00:00'
page_id: '268590020'
product: rm
source: tdn-rm
title: TVZSDR_DT_Módulo_de_Caixa-Inclusão_de_extratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268590020
version: 113
---

# Módulo de Caixa - Inclusão de extratos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Módulo de Caixa - Inclusão de extratos |
| **Situação/Requisito:** | Ao incluir extrato (saque manual) via sessão de caixa, foi observado que o campo IDOPERACAO não é preenchido  no banco de dados, na tabela FXCX. Porém, na tabela FLOGSESSAOCAIXA, o campo é preenchido normalmente. A  ausência deste campo na tabela FXCX impossibilita o Cliente realizar um join entre as tabelas para buscar a  informação referente ao saque. |
| **Solução/Implementação:** | Otimização no processo de inclusão de Extratos na sessão de caixa. Agora o sistema grava corretamente o  IDOPERACAO realizado na inclusão do extrato pela sessão de caixa. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000228 |

divs
