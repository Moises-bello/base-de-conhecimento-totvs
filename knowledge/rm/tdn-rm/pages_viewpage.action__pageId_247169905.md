---
content_hash: 09c8e1030273eb9d287b497a17e27777c37b4b1253c2b4657253f1f14893ce75
fetched_at: '2026-06-29T00:08:16.452772+00:00'
page_id: '247169905'
product: rm
source: tdn-rm
title: TVJVJX_DT_Módulo_de_Caixa_Autenticação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=247169905
version: 102
---

# Módulo de Caixa - Autenticação

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Módulo de Caixa - Autenticação |
| **Situação/Requisito:** | Após realizar uma baixa pela sessão de caixa, nas versões 12.1.11, o sistema realiza primeiro a autenticação e  depois a impressão do recibo. Na versão 11.4x, era impresso primeiro o recibo e posteriormente a autenticação  era realizada. Em alguns casos é necessário que seja gerado primeiro o relatório de recibo para depois  autenticar pois utiliza-se o documento do relatório para impressão da autenticação. |
| **Solução/Implementação:** | Melhoria no processo da Autenticação Mecânica e Impressão de Relatório/Recibo. Agora o sistema contêm o  parâmetro Contas a Receber >> Caixa >> Autenticação do Caixa >> "Permite imprimir Autenticação Mecânica após  impressão do Relatório/Recibo" que tem a função de alterar a ordem de impressão ao realizar a baixa ou estorno  na sessão de caixa da Autenticação Mecânica para depois da impressão do Relatório/Recibo caso seja marcada  (ativada). |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000221 |

divs
