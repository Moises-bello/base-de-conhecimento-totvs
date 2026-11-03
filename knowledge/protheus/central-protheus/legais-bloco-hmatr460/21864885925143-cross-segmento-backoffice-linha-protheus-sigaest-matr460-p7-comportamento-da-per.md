---
article_id: 21864885925143
category: LEGAIS - BLOCO H/MATR460
content_hash: 03be36f2a8938061fc5626be2eb994fe5c759427384ea12c27adc6c6794ee91c
fetched_at: '2026-06-28T22:42:15.083235+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 (P7) - Comportamento
  da pergunta Saldo em Poder 3° quando recebemos Remessa atualizando estoque.
type: support-article
updated_at: '2024-03-06T19:52:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21864885925143-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-P7-Comportamento-da-pergunta-Saldo-em-Poder-3-quando-recebemos-Remessa-atualizando-estoque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21864885886743) Tempo aproximado para leitura: **00:04:15min** **Dúvida**Recebi uma Remessa via rotina Documento de Entrada (MATA103) com uma TES que atualiza estoque (F4\_ESTOQUE = SIM) e controla poder de terceiros (F4\_PODER3 = Remessa). Ao extrair o MATR460 com a pergunta "Saldo em Poder 3°" = "Não" ele lista esse saldo na sessão "Em Estoque".  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O relatório MATR460 é um dos relatórios mais complexos do módulo de estoque, e suas perguntas mudam completamento o resultado apresentado, segue o resultado do relatório com a alteração do pergunte:

**MATR460 com a pergunta Saldo em Poder 3° = "Sim"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864885887639)

**Sessão "Em Estoque"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864891417111)

**Sessão "De Terceiros"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864885889943)

**MATR460 com a pergunta Saldo em Poder 3° = "Não"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864885891223)

**Sessão "Em Estoque"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21864891425047)

Neste cenário, o comportamento do relatório está correto, pois quando desligamos a pergunta Saldo em Poder 3° o relatório deixa de validar as TES que tem a configuração F4\_PODER3 = Remessa/Devolução e passa a olhar apenas para as movimentações que atualizaram o estoque F4\_ESTOQUE = SIM.

Dessa maneira, realmente o sistema apresenta o saldo do produto na sessão "Em Estoque" pois de fato a remessa atualizou o estoque do sistema e com a pergunta desabilitada, deixa de considerar o poder de terceiro, e ao confrontar com o relatório MATR260 por exemplo, esse mesmo saldo, será considerado como próprio.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)*
