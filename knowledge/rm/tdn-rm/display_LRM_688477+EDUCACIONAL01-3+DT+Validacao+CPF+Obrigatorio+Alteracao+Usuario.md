---
content_hash: aad8582175283e6eed4ef7236142b1b242b3991247b6d703fb20dd747389e39a
fetched_at: '2026-06-29T00:08:32.587948+00:00'
page_id: '273992194'
product: rm
source: tdn-rm
title: 688477 EDUCACIONAL01-3 DT Validacao CPF Obrigatorio Alteracao Usuario
type: documentation
url: https://tdn.totvs.com/display/LRM/688477+EDUCACIONAL01-3+DT+Validacao+CPF+Obrigatorio+Alteracao+Usuario
version: 106
---

# USUÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Usuário* |
| **Situação/Requisito:** | *Foi identificado que ao realizar alguma alteração no cadastro de usuário em um usuário que não possui CPF, o sistema passa a obrigar o preenchimento do CPF, no cadastro de pessoa o CPF é obrigatório, mas não deve ser pelo Gestão Bibliotecária.* |
| **Solução/Implementação:** | *Foi identificado que a situação ocorre devido uma alteração na função de validação da obrigatoriedade do CPF disponibilizada pelo TOTVS Gestão de Pessoas, foi feito uma alteração pela identificação do código do sistema que está enviando a informação, sendo assim, se perdeu a identificação do Gestão Bibliotecária. Foi feito o ajuste para reenviar o código do sistema da operação corrente, no caso, o Gestão Bibliotecária, assim a validação do CPF passou a ser feita corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
