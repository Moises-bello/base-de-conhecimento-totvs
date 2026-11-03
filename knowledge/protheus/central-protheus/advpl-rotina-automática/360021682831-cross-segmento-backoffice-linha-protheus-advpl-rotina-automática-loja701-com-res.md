---
article_id: 360021682831
category: ADVPL - Rotina Automática
content_hash: 3986df2eb337dd36e3a4bac358d0b817fa0da6a4bf5494d2be10c51c8eeecac9
fetched_at: '2026-06-28T22:40:24.195485+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Rotina automática Loja701
  com reserva
type: support-article
updated_at: '2022-04-11T11:37:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021682831-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-Loja701-com-reserva
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao executar de forma automática a rotina LOJA701 informando o campo LR\_ENTREGA e a variável AUTRESERVA = 3, não sendo realizada a reserva do produto (B2\_RESERVA).  
  
**Ambiente**Protheus – ADVPL – A partir da versão 11.8  
  
**Causa**Este erro ocorre quando o ambiente não está configurado adequadamente para utilizar a reserva de produto.  
  
**Solução**Efetuar a configuração dos parâmetros abaixo:

1. MV\_LJPEDVE = .T.
2. MV\_LJTESPE = Determina o TES que será utilizado para a emissão do Pedido de Venda através da rotina de Venda Assistida. Este TES não deve gerar movimento financeiro (Campo Gera Dupl. = Não).
3. MV\_LJCONDP = Determina a Condição de Pagamento que será utilizada para a emissão do Pedido de Venda através da rotina de Venda Assistida. Esta condição de pagamento é meramente informativa pois o TES utilizado não pode gerar movimento financeiro.
4. Efetuar o cadastro de Identificação de Lojas (LOJA080).

**Saiba mais**  
[SIGALOJA 0381 Ao efetuar reserva [F11], o sistema apresenta uma mensagem informando que não possuo lojas cadastradas(SLJ), o que verificar ?](http://tdn.totvs.com/pages/viewpage.action?pageId=240301447)  
[SIGALOJA 0204 O que preciso verificar quando a minha venda com reserva não está funcionando?](http://tdn.totvs.com/pages/viewpage.action?pageId=224116080)  
[SIGALOJA 0196 Como habilitar a emissão de pedido de venda na Rotina Venda Assistida?](http://tdn.totvs.com/pages/releaseview.action?pageId=224459923)

[ExecAuto LOJA701](http://tdn.totvs.com/pages/viewpage.action?pageId=6787264)
