---
article_id: 360044514053
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 0593bee0e1f5b476c0600f0e2622103737acde5fbfc7844a35fb49e1b15bce3e
fetched_at: '2026-06-28T22:42:47.072444+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Tempo da MOD está divergente da SD3
  ao imprimir o relatório MATR860 ou PCPR860
type: support-article
updated_at: '2026-04-28T21:11:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044514053-Manufatura-Linha-Protheus-SIGAPCP-Tempo-da-MOD-est%C3%A1-divergente-da-SD3-ao-imprimir-o-relat%C3%B3rio-MATR860-ou-PCPR860
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40083600653591) Tempo aproximado para leitura:**00:00:00 min**  
  
**Dúvida**  
Por que o tempo da **MOD - Mão de Obra** está divergente da **SD3 - Movimentações Internas** ao imprimir o relatório **MATR860 - Relação Por OP** ou **PCPR860 - Relação das OPs Movimentos**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Na tabela **SD3** a **MOD** sempre é gravada em formato **centesimal**, e no relatório **MATR860** ou **PCPR860** a **MOD** respeita o conteúdo do parâmetro **MV\_TPHR - Define a unidade padrão para tempos utilizados pelo sistema de PCP e ESTOQUE.** O tipo de hora pode ser **N - Normal** ou **C - Centesimal.**  
Então, se o parâmetro estiver com o conteúdo igual a **N**, o Sistema converte o tempo da **MOD** para o formato **normal**, ou seja, diferente do que está gravado na tabela.   
  
**Saiba mais**  
Para dúvidas de como cadastrar a **MOD** na estrutura acesse: [Manufatura - Linha Protheus - SIGAPCP - Como registrar a quantidade do MOD na estrutura do produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024715313)
