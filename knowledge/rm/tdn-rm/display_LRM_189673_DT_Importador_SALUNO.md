---
content_hash: 0fee97e63660fa83d43d02c325ef09eba69673b38debc5ab310b164b28e121b4
fetched_at: '2026-06-29T00:08:22.722591+00:00'
page_id: '269439207'
product: rm
source: tdn-rm
title: 189673_DT_Importador_SALUNO
type: documentation
url: https://tdn.totvs.com/display/LRM/189673_DT_Importador_SALUNO
version: 107
---

# IMPORTADOR - SALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Importador - SALUNO* |
| **Situação/Requisito:** | *Quando se importa um aluno pelo importador ocorre o seguinte erro: Erro inserindo registro na SPESSOA: The INSERT statement conflicted with the FOREIGN KEY constraint "FKVFILIACAO\_PPESSOA". The conflict occurred in database "CorporeRM\_prototipo", table "dbo.PPESSOA", column 'CODIGO'. The statement has been terminated.* |
| **Solução/Implementação:** | *Ajuste no log do importador para exibir que mãe e/ou pai não foram encontrados ao invés de erro de chave estrangeira.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
