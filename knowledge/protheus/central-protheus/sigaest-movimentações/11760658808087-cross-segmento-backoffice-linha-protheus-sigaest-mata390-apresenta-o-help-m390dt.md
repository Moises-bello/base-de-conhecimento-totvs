---
article_id: 11760658808087
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b3a6688f8fc13682f07bfe12c1d38e38c09968e8f6bd16cbfa048e2c8a451cf1
fetched_at: '2026-06-28T22:38:57.178006+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA390 apresenta
  o HELP M390DTVALID impedindo alterar a data de validade
type: support-article
updated_at: '2023-01-20T17:54:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11760658808087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA390-apresenta-o-HELP-M390DTVALID-impedindo-alterar-a-data-de-validade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao tentar alterar a Data de Validade para uma data inferior a Data Base, apresenta o ***HELP M390DTVALID***, é possível esse cenário?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Devido integridade na rastreabilidade dos Lotes, no padrão não tem essa funcionalidade o help impede a alteração da data de validade para uma data inferior a data base, ou seja, informar uma data vencida.  
  
Para alterar esse comportamento padrão, somente customizando com o ***Ponto de entrada MT390VLV*** que permite customizar conforme necessidade específica. Abaixo link com o Ponto de Entrada.  
  
***MT390VLV - Validade de lotes***  
***<https://tdn.totvs.com/display/public/PROT/MT390VLV+-+Validade+de+lotes>***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11761206513943)

***Observações importantes:*** Essa é uma trava para impedir a alteração para uma data em que o Lote fique vencido e bloqueado.

Para os casos em que precisar alterar a data de validade, é possível alterar a Data Base do Protheus, retroagindo para a data desejada e alterar a Validade. Veja no print abaixo para melhor entendimento.

Reforçando, que caso, não trabalhe com Lote vencido o mesmo será bloqueado no momento em que a rotina PROCLOTE() for ativada, como **[descrito na FAQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025875571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA275-Lote-vencido-como-posso-Movimentar-ou-Inventariar-produto-com-Lote-Vencido-que-est%C3%A1-bloqueado-)**, devendo efetuar o procedimento indicado na **[mesma FAQ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025875571-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA275-Lote-vencido-como-posso-Movimentar-ou-Inventariar-produto-com-Lote-Vencido-que-est%C3%A1-bloqueado-)** para Liberação do Lote vencido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11812820963479)

***Saiba Mais:***

*[Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
