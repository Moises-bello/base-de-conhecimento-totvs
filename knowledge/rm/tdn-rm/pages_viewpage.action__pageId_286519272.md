---
content_hash: 63d53b10d96f654e99e8be79e6ca06b3cc0bf6a470d06812d3aa8167d019bef3
fetched_at: '2026-06-29T00:08:40.960156+00:00'
page_id: '286519272'
product: rm
source: tdn-rm
title: FINANCEIRO01-1902 DT Reinf - Cadastro de Cliente/Fornecedor - Campos novos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286519272
version: 103
---

# Cliente/Fornecedor

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Cliente/Fornecedor |
| **Situação/Requisito:** | A Reinf é mais um módulo do projeto do Sped e está sendo construído como complemento ao Sistema de Escrituração Digital das Obrigações Fiscais, Previdenciárias e Trabalhistas - e-Social.  Serão necessárias as seguintes implementações no TOTVS Gestão Financeira para atendimento dessa nova obrigação:  **I)** Será preciso criar um flag no Cadastro de Cliente/Fornecedor para identificar se a entidade é executora do Programa de Aquisição de Alimentos – PAA (Sim ou Não).  **II)** Na pasta Tributos, Dados Relacionados ao IRRF, atualizar a lista de opções do campo “\*Tipo de Rendimento\*”, acrescentando as opções:  • Rendimentos de empregados ou contratados – COPA; • Prêmios de árbitros, jogadores de futebol e outros membros das delegações – COPA; • Demais rendimentos tributáveis/isentos de declaração obrigatória; (Para essa opção, colocar consistência no cadastro para que NÃO seja possível selecionar esta opção se o Cliente/Fornecedor for do exterior.)  Esse campo será utilizado para selecionar os lançamentos fiscais/financeiros que serão declarados na Reinf, no Registro R-2070 - Retenções na Fonte - IR, CSLL, Cofins, PIS/PASEP - Pagamentos diversos. |
| **Solução/Implementação:** | Otimização no processo de inclusão/alteração de Cliente/Fornecedor. Foi criado o campo para identificar se a entidade é executora do Programa de Aquisição de Alimentos – PAA (Sim ou Não) e adicionado as seguintes opões no campo “\*Tipo de Rendimento\*”:  • Rendimentos de empregados ou contratados – COPA; • Prêmios de árbitros, jogadores de futebol e outros membros das delegações – COPA; • Demais rendimentos tributáveis/isentos de declaração obrigatória; (Para essa opção, colocar consistência no cadastro para que NÃO seja possível selecionar esta opção se o Cliente/Fornecedor for do exterior.) |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000060 |

divs
