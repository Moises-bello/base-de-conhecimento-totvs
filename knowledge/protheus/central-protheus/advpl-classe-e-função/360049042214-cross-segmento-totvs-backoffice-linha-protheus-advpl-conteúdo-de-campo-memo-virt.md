---
article_id: 360049042214
category: ADVPL - Classe e Função
content_hash: 46bf3edbb21e3c0ca1a3e62e9cf43c394b580efeb69c1c1053760dbc48acf605
fetched_at: '2026-06-28T22:40:15.675343+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Conteúdo de campo
  Memo Virtual não é gravado na tabela SYP utilizando função MSMM.
type: support-article
updated_at: '2022-01-05T13:24:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049042214-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Conte%C3%BAdo-de-campo-Memo-Virtual-n%C3%A3o-%C3%A9-gravado-na-tabela-SYP-utilizando-fun%C3%A7%C3%A3o-MSMM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Conteúdo de campo **memo virtual**  com inicializador padrão utilizando a função [MSMM](https://tdn.totvs.com/display/public/PROT/Msmm+-+Pesquisa+do+campo+MEMO+Virtual)() criado no cadastro de clientes  não  grava  seu conteúdo na tabela SYP, por que?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Para que seja possível a gravação de seu conteúdo antes é necessário a utilização dos pontos de entrada [MA030MEM](https://tdn.totvs.com/pages/releaseview.action?pageId=6784249) ou [CRM980MMEM](https://tdn.totvs.com/pages/viewpage.action?pageId=285649164) caso utilize a versão do cadastro em MVC (**MV\_MVCSA1 = .T.** ). para que a rotina possa tratar estes campos.  
  
**Saiba mais**  
[MSMM()](https://tdn.totvs.com/display/public/PROT/Msmm+-+Pesquisa+do+campo+MEMO+Virtual)  
[Tablela SX3](https://tdn.totvs.com/display/framework/SX3+-+Campos+das+tabelas)
