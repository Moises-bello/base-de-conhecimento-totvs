---
content_hash: f1ff4b1b0c83626b4c6068be378c6bb936d3466a1d06f015480eaf737529e1b8
fetched_at: '2026-06-29T00:06:19.600576+00:00'
page_id: '219700220'
product: rm
source: tdn-rm
title: TTU801_DT_Livro_Certificados_Diplomas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTU801_DT_Livro_Certificados_Diplomas
version: 2
---

# LIVRO PARA REGISTRO DE CERTIFICADOS / DIPLOMAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Livro para registro de certificados / diplomas* |
| **Situação/Requisito:** | *Registro de segunda via de diploma apresentou problema na numeração da folha do livro. Última folha está sendo gravada com sequência 3 mil e pouco quando deveria ser quinhentos e pouco. Isso ocorre com livros de todos os contextos. Não temos como emitir os diplomas em razão da geração incorreta. Observamos que o comportamento mudou após a implantação da versão 11.82.41.118.* |
| **Solução/Implementação:** | *Ajuste no aplicativo, na numeração da última folha do livro, quando se efetua o processo de geração de certificação/diplomação, para que quando o livro for de reinicio continuo por livro e possuir livro anterior, seja feito o seguinte calculo: subtrair do último registro do livro o primeiro registro e o resultado desta subtração se soma 1 e divide pela quantidade de registro por folha, com este calculo se tem o número da última folha.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.8.102* |
| **Versão Expedida:** | *N/A* |

divs
