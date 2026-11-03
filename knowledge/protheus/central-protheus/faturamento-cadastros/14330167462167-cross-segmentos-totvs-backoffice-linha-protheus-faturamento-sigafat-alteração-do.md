---
article_id: 14330167462167
category: Faturamento - Cadastros
content_hash: 4667c4eeb41f19e2fc20f87fbbc1c299cb7c7a282f85943f76071145359be3ca
fetched_at: '2026-06-28T22:38:35.497202+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Alteração do campo "A1_DESC" para igualar com o campo C5_DESC1 '
type: support-article
updated_at: '2025-01-10T20:25:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14330167462167-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Altera%C3%A7%C3%A3o-do-campo-A1-DESC-para-igualar-com-o-campo-C5-DESC1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como igualar o conteúdo do campo "A1\_DESC" com o campo C5\_DESC1 no Pedido de Venda.

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões;  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
1. Acessar o Configurador (SIGACFG), Ir em Base de Dados >> Dicionario >> Bases de Dados.  
2. Localizar a tabela SA1 e editar o campo A1\_DESC.  
3. Realizar a alteração das seguintes informações;

|  |  |  |
| --- | --- | --- |
| **A1\_DESC** | **De** | **Para** |
| **Tamanho** | 2 | 5 |
| **Decimal** | 0 | 2 |
| **Formato** | 99 | @E 99.99 |

Configuração do campo realizada A1\_DESC.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14329411136279)
