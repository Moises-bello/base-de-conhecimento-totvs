---
article_id: 40910862081175
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 94f4e830c4f470293d880a8c007d94aabefd81342280b3dd0fd43a7f415d0d5c
fetched_at: '2026-06-28T22:42:42.165500+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Decimais no campo de quantidade base
type: support-article
updated_at: '2026-06-02T18:44:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40910862081175-Manufatura-Linha-Protheus-SIGAPCP-Decimais-no-campo-de-quantidade-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40910862063895) Tempo aproximado para leitura: **00:00:52 min**  
  
**Dúvida**  
É possível fazer com que o campo **nQtdBase**  - **Quantidade Base** , da rotina **PCPA200 - Cadastro de Estrutura** receba valor decimal?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Sim, é possível, para isso ajuste o tamanho do campo **B1\_QB - Quantidade Base** para o tamanho e número de decimais necessários.  
O ajuste é realizado no campo **B1\_QB** pois é neste campo que é gravada a informação da variável **nQtdBase** e a partir da definição desse campo que a variável **nQtdBase** é construída em tela.  
A informação decimal gravada nesse campo também será utilizada no cálculo da necessidade dos itens da estrutura.
