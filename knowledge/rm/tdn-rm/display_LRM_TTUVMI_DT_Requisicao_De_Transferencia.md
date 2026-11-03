---
content_hash: 0bed53abb08d4ff3774593f5380439ee6dc0fb1a44a13a4a2d97e02e45543c53
fetched_at: '2026-06-29T00:08:07.314645+00:00'
page_id: '237380446'
product: rm
source: tdn-rm
title: TTUVMI_DT_Requisicao_De_Transferencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUVMI_DT_Requisicao_De_Transferencia
version: 117
---

# REQUISIÇÃO DE TRANSFERÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Requisição de Transferência* |
| **Situação/Requisito:** | *Ao realizar transferência de Funcionário com mudança de CNPJ, sistema apresenta erro: Não existe Requisição de Transferência aprovada para o funcionário selecionado!* *A transferência de funcionários entre CNPJs é feita pelo processo de Rescisão.*  *Como a utilização da Requisição de Desligamento é obrigatória, é necessário existir uma requisição de 'Transferência com Alteração de Dados Funcionais' ou 'Transferência' aprovada.* *Porém, no parametrizador apenas a Requisição de Desligamento é obrigatória.* |
| **Solução/Implementação:** | *Ajuste no processo de Transferência de Funcionário com mudança de CNPJ. Ao efetuar a transferência, se somente a Requisição de Desligamento for obrigatória, mas não for obrigatório haver uma Requisição de Transferência ou Transferência com Alteração de Dados Funcionais para mudança de CNPJ, a transferência é efetivada mesmo sem haver uma Requisição correspondente.Informe a solução/implementação.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTUVMI* |
| **Requisito (ISSUE):** |  |

divs
