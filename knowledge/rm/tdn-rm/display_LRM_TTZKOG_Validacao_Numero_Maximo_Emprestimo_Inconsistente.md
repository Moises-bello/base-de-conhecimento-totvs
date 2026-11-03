---
content_hash: c32be2ee9c5e95da132694d760f0f59a0754ec032a104c3e07aa6b53fd253ea2
fetched_at: '2026-06-29T00:06:24.109159+00:00'
page_id: '224111937'
product: rm
source: tdn-rm
title: TTZKOG_Validacao_Numero_Maximo_Emprestimo_Inconsistente
type: documentation
url: https://tdn.totvs.com/display/LRM/TTZKOG_Validacao_Numero_Maximo_Emprestimo_Inconsistente
version: 123
---

# MOVIMENTAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentação - Empréstimos* |
| **Situação/Requisito:** | *Ao efetuar empréstimos de exemplares em uma única movimentação, com tipos de publicação diferentes e com número máximo de empréstimos também diferente o sistema não permitia confirmar a operação alertando que o número máximo de empréstimo havia sido excedida sendo que não foi excedida.* |
| **Solução/Implementação:** | *A mensagem era retornada por uma inconsistência na validação dos diferentes tipos de publicação e as regras de empréstimo para o tipo de usuário com o tipo de publicação, após o ajuste a verificação passou a ser feita corretamente e o cálculo dos limites de empréstimos feito com sucesso.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUCKSZ* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *12.1.10* |
| **Versão Corrigida:** | *11.82.43*  **12.1.10** |
| **Versão Expedida:** | *11.82.43*  **12.1.10** |

divs
