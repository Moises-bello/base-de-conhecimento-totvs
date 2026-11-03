---
article_id: 10660573373591
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f022a01d4e060e0b45bf13b361db336971877b907384dac29f1bcc7daf3ea027
fetched_at: '2026-06-28T22:42:47.150582+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Zerar o empenho de apenas um item
type: support-article
updated_at: '2023-08-04T20:00:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10660573373591-Manufatura-Linha-Protheus-SIGAPCP-Zerar-o-empenho-de-apenas-um-item
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16531091822743)*** Tempo aproximado para leitura: **00:00:57 min  
  
Dúvida**É possível zerar o saldo empenhado de apenas um item através da rotina **MATA381 - Empenho Múltiplo**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Sim, através da rotina **MATA381** é possível zerar **manualmente** um único item.  
Para o item que não foi requisitado, é possível informar manualmente nos campos **D4\_QTDEORI - Quantidade Empenho** e **D4\_QUANT - Saldo Empenho** a quantidade zero.  
Caso o item já tenha sido requisitado, para zerar essa linha é necessário deixar no campo **D4\_QTDEORI** a quantidade que já foi requisitada desse item, e no campo **D4\_QUANT** a quantidade **zero**.**Saiba mais**  
Para mais informações sobre como zerar o saldo empenhado acesse: [Manufatura - Linha Protheus - SIGAPCP - Como zerar o saldo empenhado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025602231-Manufatura-Linha-Protheus-SIGAPCP-Como-zerar-o-saldo-empenhado).
