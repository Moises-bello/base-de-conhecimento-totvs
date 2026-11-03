---
content_hash: d82713796c0dca10a5bb70d111119b77ced8b7b16a44b9fff4b794051af90e83
fetched_at: '2026-06-29T00:06:12.114800+00:00'
page_id: '204968724'
product: rm
source: tdn-rm
title: TTJXIC_DT_Requisicao_de_Transferencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJXIC_DT_Requisicao_de_Transferencia
version: 1
---

# REQUISIÇÃO DE TRANSFERÊNCIA COM ALTERAÇÃO DE DADOS FUNCIONAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Requisição de Transferência com Alteração de Dados Funcionais |
| **Situação/Requisito:** | Ao tentar realizar o processo de desligamento para um funcionário que irá ser transferido entre coligadas com alteração de CNPJ e exibida a mensagem: "As requisições de Desligamento e requisições que alteram no CNPJ do funcionário (Transferência ou Transferência com Alteração de Dados Funcionais) São obrigatórios. Não existe nenhuma requisição com estas características para a chapa xxxxx". Porém foi criada uma requisição de Transferência com Alteração de Dados Funcionais e está com o status Aprovada. |
| **Solução/Implementação:** | Verificado que ao buscar os dados para validar se existe requisição de desligamento ou de Transferência e Transferência com Alteração de Dados funcionais, o sistema passava o código da coligada de destino para buscar a requisição e não da coligada de origem, com isso nenhuma requisição era retornada. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTJXIC |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 12.1.8 |
