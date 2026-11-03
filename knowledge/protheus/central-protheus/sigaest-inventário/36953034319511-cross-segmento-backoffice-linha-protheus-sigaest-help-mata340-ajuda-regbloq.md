---
article_id: 36953034319511
category: SIGAEST - INVENTÁRIO
content_hash: 36ed44f8adfb23a5f9030a355db8d1516cefdc3c84113387a2b15c7fa86b6171
fetched_at: '2026-06-28T22:38:50.441112+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento – Backoffice (Linha Protheus) - SIGAEST-  Help MATA340 AJUDA
  REGBLOQ
type: support-article
updated_at: '2025-12-18T19:13:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36953034319511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-MATA340-AJUDA-REGBLOQ
---

Ao processar o Acerto de inventário por armazém sem informar código de produto, o sistema considera todos os produtos do armazém, atribuindo quantidade zero aos não contados. Produtos bloqueados (B1\_MSBLQL = 1) geram erro, pois não podem ser movimentados. A solução é desbloqueá-los temporariamente, processar o inventário e bloqueá-los novamente, sem necessidade de contagem, pois serão considerados com quantidade zero.

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36953034302103) Tempo aproximado para leitura: **00:03:37** min  
  
**Dúvida**  
Ao tentar processar o Acerto de inventário por armazém (tanto pelo ACD quanto pela MATA340) é gerado o erro AJUDA:REGBLOQ Este registro está bloqueado para uso.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque - Todas as versões  
  
**Solução**  
Quando informamos um inventário por armazém sem informar um código de produto, o sistema assume que todos os produtos que constam dentro do armazém informado será inventariado. Para aqueles produtos que não forem contados, se assume a quantidade 0 automaticamente para ser processado no momento do Acerto.

Porém, dentre esses produtos podem existir produtos que já não estão mais em uso e estão bloqueados**(B1\_MSBLQL = 1).**

Como produtos bloqueados não podem ser movimentados em nenhum tipo de processo, é necessário desbloquear temporariamente esses produtos, gerar o processamento do inventário e depois disso bloqueá-los novamente. Lembrando que não é preciso realizar a contagens desses pois serão considerados com a quantidade 0.

Outra sugestão seria utilizar a opção de regar o mestre de forma automática. Dessa forma, serão gerado mestres para cada produto individualmente, porém, para os produtos bloqueados não serão gerados. Maiores detalhes:

[Cross Segmento – Backoffice (Linha Protheus) - SIGAACD- Mestre de inventário automático - ACDA030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37095622737431)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data calculada*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021321072-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-calculada?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  MATA271 - Bloqueio de produtos para inventário por data informada*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021554891-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-informada?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar o estorno (exclusão) de movimento de Inventário?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402384407063)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MILE importação de arquivo da tabela SB7 (Digitação do inventário)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10573324218007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SB7-Digita%C3%A7%C3%A3o-do-invent%C3%A1rio-)

[*Clique aqui e veja mais artigos sobre Inventário no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)
