---
content_hash: f54d6b549b198797875e90883f95cfab0f4a263f7ae09675bd81eb9ef55cc06e
fetched_at: '2026-06-29T00:08:16.430913+00:00'
page_id: '245173148'
product: rm
source: tdn-rm
title: TVNALB_DT_Alteracao_De_Dados_Da_Requisicao
type: documentation
url: https://tdn.totvs.com/display/LRM/TVNALB_DT_Alteracao_De_Dados_Da_Requisicao
version: 115
---

# ALTERAÇÃO DE DADOS DA REQUISIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Alterar Dados da Requisição |
| **Situação/Requisito:** | Ao tentar alterar somente o campo “Salário” de uma requisição através do processo “Alterar Dados da Requisição” existente nas requisições dos tipos “Aumento de Quadro e Substituição”, o sistema retorna a seguinte mensagem:  Violação de chave estrangeira  Possíveis causas:    - exclusão de registro que possui outros registros associados    - inclusão de registro detalhe sem um registro mestre associado  E ao selecionar a aba de log, sistema reporta a mensagem abaixo indevidamente, pois neste caso não houve alteração do campo “Seção”.  Alteração de seção da requisição finalizada |
| **Solução/Implementação:** | Realizado ajuste no processo de alteração de dados da requisição. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVNALB |
| **Requisito (ISSUE):** |  |

divs
