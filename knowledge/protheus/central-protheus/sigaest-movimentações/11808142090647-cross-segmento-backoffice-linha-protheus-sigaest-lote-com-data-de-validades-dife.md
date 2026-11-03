---
article_id: 11808142090647
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 25276f12ae4f40c8afa647c46bf6cb82221c2372ca4857e6cfb3ea3316bcfc18
fetched_at: '2026-06-28T22:38:55.647431+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Lote com Data de Validades
  diferentes em cada Armazém
type: support-article
updated_at: '2023-01-20T17:29:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11808142090647-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Lote-com-Data-de-Validades-diferentes-em-cada-Armaz%C3%A9m
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como compartilhar um *ticket* de criação ou ajuste de Artigo no processo de KCS?]  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque/Custos - Todas as versões  
  
**Solução**

No Protheus a ***data de validade dos Lotes é determinada "por*** ***Armazém”***, portanto em uma Filial, pode conter o mesmo Lote em Armazéns diferentes com datas de validades distintas.

Veja o exemplo simulado abaixo:

 - Na Filial 01 existem 3 Armazéns 01,02 e 03.

 - Saldo do Produto código 108 Lote A no Armazém 01 com Data de Validade 20/01/2024.

 - No Armazém 02 temos o mesmo Lote A com data de Validade 28/02/2024.

 - Não tenho Saldo de Lotes no Armazém 03 ainda

***LOCAIS DE ESTOQUE (AGRA045)***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11808187070231)

***CONSULTA SALDOS POR LOTE (MATC060)***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11808258243095)

- Caso faça qualquer movimentação de Entrada (*Movimento Interno, Nota de Entrada, Inventário, etc.*) incluindo saldo para o Armazém 03 informando o Lote A, é permitido utilizar uma Data de Validade diferente das que existem nos Armazém 01 e 02.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11808250911383)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11808265532311)

 - Caso transferir pela rotina TRANSFERÊNCIAS MÚLTIPLAS (MATA261) o saldo do Lote existente, para o Armazém 03 e não informar uma Data de Validade, automaticamente é considerado a Data de Validade de Origem, mas veja bem, nesse cenário, como o Saldo desse Lote não existia no Armazém 03, o Protheus permite e digitação de uma nova Data de Validade.

 - Isso permite que a utilização de controle dos Armazéns seja por exemplo, um Armazém refrigerado, que conserva determinados produtos com uma validade maior, quando retirado desse Armazém pode alterar a Data de Validade como desejar. ***Obs.*** *Esse é um exemplo de utilização depende muito da regra de negócio de cada empresa.*

***- Observações importantes:***

 - Como posso alterar a Data de Validade dos Lotes para ficarem iguais em todos os Armazéns?

***Resp.:*** Utilizar a rotina MANUTENÇÃO DE LOTES (MATA390) pressionando a tecla F12 e com a pergunta Ajustar Validade do Lote para Todos os Armazéns.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11808302486551)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11808303099287)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11808327264791)

 - Na rotina MANUTENÇÃO DE LOTE (MATA390) constam os Pontos de Entrada abaixo para que possa customizar alterações de Data de validade dos lotes caso desejar.   
  
***MT390DTV - Data de Validade***  
***<https://tdn.totvs.com/display/public/PROT/MT390DTV+-+Data+de+Validade>***  
  
***MT390VLV - Validade do Lote***  
***<https://tdn.totvs.com/display/public/PROT/MT390VLV+-+Validade+do+Lote>***  
  
***MT390VLI***  
***<https://tdn.totvs.com/display/public/PROT/MT390VLI>***

***Saiba Mais:***

*[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus?source=search)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
