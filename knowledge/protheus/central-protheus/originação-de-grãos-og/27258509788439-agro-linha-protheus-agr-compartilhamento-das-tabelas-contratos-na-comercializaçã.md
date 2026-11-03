---
article_id: 27258509788439
category: Originação de Grãos (OG)
content_hash: a3a0134c8a8f460e7a6e4e17befc541bbcf7559562b1157e27d2b80a93fce4ec
fetched_at: '2026-06-28T22:45:37.609010+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Compartilhamento das tabelas - Contratos na comercialização
  x Previsões financeiras
type: support-article
updated_at: '2025-01-17T19:07:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27258509788439-Agro-Linha-Protheus-AGR-Compartilhamento-das-tabelas-Contratos-na-comercializa%C3%A7%C3%A3o-x-Previs%C3%B5es-financeiras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27258509768983) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Para que serve os **Compartilhamento das tabelas - Contratos na comercialização x Previsões financeiras**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O contrato de comercialização pode gerar as previsões financeiras como títulos no Contas à Pagar (compras) ou no Contas à Receber (Vendas). 

Caso desejar que não gere previsão financeira, é possível desabilitar esta funcionalidade através do parâmetro: **MV\_AGRPREV****- Permitir incluir contratos de compra e venda sem informar previsão financeira**. 

**MV\_AGRPREV****= .F. >** Exige as previsões financeiras nos contratos de compra e venda

**MV\_AGRPREV = .T. >** Permite incluir contratos de compra e venda sem informar previsão financeira

Os títulos são criados com a seguinte configuração: 

|  |  |
| --- | --- |
| **Prefixo** | CTR |
| **No. Titulo** | Número do Contrato |
| **Parcela** | Parcela da previsão financeira no contrato |
| **Série** | (em branco) |
| **Tipo** | PR |

Desta forma, para que não tenha duplicidade de títulos no financeiro segue abaixo as configurações possíveis: 

**Configuração 1 - Utilizando a Comercialização Clássica e****MV\_AGRPREV** **= .F.**

|  |  |
| --- | --- |
| **NJR - Contrato**  **NNW - Alteração do Contrato**  **NN7 - Previsão Financeira Contratos**  **NNY - Cadências do Contrato** | **SE1 - Contas a Receber**  **SE2 - Contas a Pagar**  **N8L - Vinculo Titsa Receber**  **N8M - Vinculo Tits  a Pagar** |
| Exclusivo | Exclusivo |

**Configuração 2 - Utilizando a Comercialização Clássica e****MV\_AGRPREV****= .T.**

|  |  |
| --- | --- |
| **NJR - Contrato**  **NNW - Alteração do Contrato**  **NN7 - Previsão Financeira Contratos**  **NNY - Cadências do Contrato** | **SE1 - Contas a Receber**  **SE2 - Contas a Pagar**  **N8L - Vinculo Titsa Receber**  **N8M - Vinculo Tits  a Pagar** |
| Exclusivo | Exclusivo |
| Exclusivo | Compartilhado |

**Configuração 3 - Utilizando a Nova Comercialização e****MV\_AGRPREV****= .F.**

|  |  |
| --- | --- |
| **NJR - Contrato**  **NNW - Alteração do Contrato**  **NN7 - Previsão Financeira do Contrato**  **NNY - Cadências do Contrato**  **N9A - Regras Fiscais do Contrato** | **SE1 - Contas a Receber**  **SE2 - Contas a Pagar**  **N8L - Vinculo Titsa Receber N8M - Vinculo Tits  a Pagar** |
| Exclusivo | Exclusivo |
| Compartilhado | Exclusivo |
| Compartilhado | Compartilhado |

**Configuração 4 - Utilizando a Nova Comercialização e****MV\_AGRPREV****= .T.**

|  |  |
| --- | --- |
| **NJR - Contrato**  **NNW - Alteração do Contrato**  **NN7 - Previsão Financeira do Contrato**  **NNY - Cadências do Contrato**  **N9A - Regras Fiscais do Contrato** | **SE1 - Contas a Receber**  **SE2 - Contas a Pagar**  **N8L - Vinculo Titsa Receber**  **N8M - Vinculo Tits  a Pagar** |
| Exclusivo | Exclusivo |
| Compartilhado | Exclusivo |
| Compartilhado | Compartilhado |
| Exclusivo | Compartilhado |
