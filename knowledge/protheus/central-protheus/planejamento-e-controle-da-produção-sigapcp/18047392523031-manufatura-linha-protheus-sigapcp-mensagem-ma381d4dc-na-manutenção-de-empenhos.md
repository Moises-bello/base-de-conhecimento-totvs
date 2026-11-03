---
article_id: 18047392523031
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: e2f43e861aac93e6316a37039d6c849d12020274b56ea6ba82a31cc52ad083ed
fetched_at: '2026-06-28T22:42:44.499302+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MA381D4DC na manutenção de
  empenhos
type: support-article
updated_at: '2023-10-05T13:55:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18047392523031-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MA381D4DC-na-manuten%C3%A7%C3%A3o-de-empenhos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18047412613015) Tempo aproximado para leitura: **00:01:02 min****Ocorrência**Ao realizar a manutenção dos empenhos na rotina **MATA381 - Empenho Múltiplo** é apresentada a mensagem **MA381D4DC**.

![Imagem.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/18047396349975)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem é apresentada quando para algum dos itens empenhados a quantidade informada no campo **D4\_QUANT - Saldo da quantidade empenhada** é maior do que a soma da quantidade empenhada do endereço para esse registro.  
  
**Solução**Para cada item empenhado, verifique a quantidade informada no campo **D4\_QUANT** e clicando em **Outras Ações** - **Endereços**, compare a quantidade do campo **D4\_QUANT** com a soma do campo **DC\_QUANT - Quantidade da Composição**.  
Para aqueles registros que tiverem **D4\_QUANT** maior do que a soma do campo **DC\_QUANT**, faça os  ajustes pertinentes de modo que o **D4\_QUANT** seja maior ou igual a soma do campo **DC\_QUANT**.
