---
article_id: 360053633354
category: MDT - EPI
content_hash: 332a90219eabe4c74abc1996e2a75adb4c1976b8058a52d563ba0181a86f29db
fetched_at: '2026-06-28T22:44:25.282915+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Ao fazer a solicitação de um EPI ao Armazém e consultar
  a tela de Saldo em Estoque a quantidade empenhada não é calculada.
type: support-article
updated_at: '2024-11-05T10:44:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053633354-RH-Linha-Protheus-MDT-Ao-fazer-a-solicita%C3%A7%C3%A3o-de-um-EPI-ao-Armaz%C3%A9m-e-consultar-a-tela-de-Saldo-em-Estoque-a-quantidade-empenhada-n%C3%A3o-%C3%A9-calculada
---

**Ocorrência**  
Ao fazer a solicitação de um EPI ao Armazém e consultar a tela de Saldo em Estoque a quantidade empenhada não é calculada.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091789473)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**A Quantidade Empenhada só é calculada quando o usuário faz a pré-requisição no estoque.  
  
**Solução**Para fazer a pré-requisição acesse o modulo 04 (Estoque/Custos) no caminho atualizações > movimentações > internas > armazém > Gerar pré-requisição (MATA106).  
  
Na tela apresentada marque o produto que deseja gerar a pré-requisição.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089636734)  
  
Preencha os parâmetros e confirme.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089636794)  
  
Após esse processo acesse novamente a rotina Funcionário x EPI no modulo medicina. Note na imagem que a legenda é alterada.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091790373)  
  
Se for incluída uma linha para baixo informando o mesmo EPI e depois aperta a tecla F4 é possível ver que o saldo de estoque também foi alterado com o calculo da quantidade empenhada.  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091790593)  
  
**Observação**  
Esse processo trata-se apenas de uma etapa da entrega do EPI com o usuário está fazendo a integração com o armazém.  
  
**![(concordo)](https://tdn.totvs.com/s/pt_BR/8100/4410012ac87e845516b70bc69b6f7a893eabaa5a/_/images/icons/emoticons/thumbs_up.svg)** Conheça o processo completo de **entrega** **de EPI** com integração com o Armazém acessando o link: **[MP - MDT - Como realizar uma entrega de EPI com solicitação ao armazém](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052864793-MP-MDT-Como-realizar-uma-entrega-de-EPI-com-solicita%C3%A7%C3%A3o-ao-armaz%C3%A9m?source=search)**  
  
**Saiba Mais**[Artigos EPI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945554-MDT-EPI)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho)  
[MP - MDT - Como gerar a tela com Consulta de Saldos em Estoque através da rotina funcionário x EPI (MDTA695)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053523834)  
[ChatBot Carol](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
