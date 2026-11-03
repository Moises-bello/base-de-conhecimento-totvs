---
article_id: 1500005555281
category: SIGAEST - CUSTOS
content_hash: f1ce0344a8cff502b96fa84c9f69c4bc475e7e231d8e7498c1ef7cb935b016ed
fetched_at: '2026-06-28T22:39:02.159300+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Execução
  do Recálculo do Custo Médio em modo exclusivo ou compartilhado?
type: support-article
updated_at: '2025-03-12T12:26:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005555281-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Execu%C3%A7%C3%A3o-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio-em-modo-exclusivo-ou-compartilhado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503879108375)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Devo executar o Recálculo do Custo Médio apenas em modo exclusivo? Ou é possível também em modo Compartilhado?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos- Todas as versões  
  
**Solução**É possível definir se o Recálculo do Custo Médio ocorrerá de forma exclusiva ou compartilhada através do parâmetro **MV\_CUSTEXC**, onde:

|  |  |
| --- | --- |
| MV\_CUSTEXC = S | Executa o Recálculo do CM somente em modo exclusivo |
| MV\_CUSTEXC = N | Permite executar o Recálculo do CM em modo compartilhado |

Então, basta avaliar internamente qual a forma mais se adequará para ser efetuado o processo, sendo que, por boa prática, é recomendável que o Custo Médio seja processado sem que outros usuários façam movimentações para evitar distorções nos custos pós-recálculo.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
