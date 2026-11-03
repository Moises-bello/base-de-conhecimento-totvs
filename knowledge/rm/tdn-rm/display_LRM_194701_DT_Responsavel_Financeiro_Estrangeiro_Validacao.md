---
content_hash: bdeabd1e38201509ee4ec6a0fb489706db771523e243c2bb719de5054ee11128
fetched_at: '2026-06-29T00:08:22.262956+00:00'
page_id: '269090215'
product: rm
source: tdn-rm
title: 194701_DT_Responsavel_Financeiro_Estrangeiro_Validacao
type: documentation
url: https://tdn.totvs.com/display/LRM/194701_DT_Responsavel_Financeiro_Estrangeiro_Validacao
version: 112
---

# INSCRIÇÃO DO CANDIDATO - RESPONSÁVEL FINANCEIRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Inscrição do candidato - responsável financeiro* |
| **Situação/Requisito:** | *Foi identificado que quando é feito a inscrição de um candidato que possui o responsável financeiro já cadastrado por outro candidato e este responsável é estrangeiro, o sistema não conclui a inscrição alertando que o cpf do responsável já existe como cliente/fornecedor.* |
| **Solução/Implementação:** | *Foi identificado que o sistema antes de gerar o lançamento, tenta verificar se o cliente/fornecedor já existe utilizando o nome e a data de nascimento deste responsável, porém a data utilizada é a do candidato assim o sistema retorna que o cliente/fornecedor não existe e tenta inserir novamente, retornando assim o erro. Foi feita uma alteração no identificação do cliente/fornecedor para que antes de fazer a validação de um cliente/fornecedor estrangeiro o sistema carrega a data de nascimento do cadastro de pessoa, assim validando corretamente se o cliente/fornecedor existe.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | *N/A* |

divs
