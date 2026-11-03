---
content_hash: a0a460beb59268dfb2f15bb49bd77dfea6b4d3fcf5f167c2419ca723625071be
fetched_at: '2026-06-29T00:08:13.253525+00:00'
page_id: '243658809'
product: rm
source: tdn-rm
title: TVEXV8_DT_Restauração_Ficha_Financeira_Erro_Chave_Duplicada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243658809
version: 114
---

# RESTAURAÇÃO DA FICHA FINANCEIRA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Restauração da Ficha Financeira Complementar* |
| **Situação/Requisito:** | *Ao tentar restaurar a ficha financeira complementar o sistema apresenta o seguinte erro de* *Chave duplicada* *ao executar a cópia do registro na PFVERBASDIS.*  *Ao acessar a tabela PFVERBASDISHIST o cliente possui dois eventos iguais lançados nesta tabela, um com valor negativo e outro com valor positivo. Todas os campos que são chaves primárias da tabela estão com registro igual exceto o campo PERIODOREF.* |
| **Solução/Implementação:** | *Ajuste na rotina de restauração de ficha financeira complementar para tratar o campo PERIODOREF* |
| **Chamados relacionados:** | *TVEXV8* |

divs
