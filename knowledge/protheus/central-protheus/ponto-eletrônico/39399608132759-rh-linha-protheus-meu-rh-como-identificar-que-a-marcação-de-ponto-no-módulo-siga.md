---
article_id: 39399608132759
category: PONTO ELETRÔNICO
content_hash: ccfed2c056db4757808e75f48ca58ec2c5ff6520664cbd36b50e35da21a88596
fetched_at: '2026-06-28T22:44:36.432823+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como identificar que a marcação de ponto no
  módulo SIGAPON, foi realizada pelo App Meu RH
type: support-article
updated_at: '2026-03-30T19:41:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39399608132759-RH-Linha-Protheus-Meu-RH-Como-identificar-que-a-marca%C3%A7%C3%A3o-de-ponto-no-m%C3%B3dulo-SIGAPON-foi-realizada-pelo-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39399598226711) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como identificar que a marcação de ponto no módulo SIGAPON, foi realizada pelo App Meu RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
É possível identificar que a marcação de ponto foi feita pelo Meu RH, **consultando o campo P8\_FLAG via tabela SP8 em período aberto de ponto, ou então o campo PG\_FLAG da tabela SPG em período de apontamento fechado.**  
  
Ambas as tabelas, são possíveis extrair via Consulta Genérica.  
  
Acessando o módulo **16 - SIGAPON**, também é possível identificar o conteúdo da *FLAG* de marcação.  
Para isso, acessar o menu **Lançamentos > Integrados, selecionar o funcionário, em Outras ações > Alterar.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39399598230295)  
  
Essa visualização pelo Integrados, somente é permitida para períodos de apontamento em aberto.  
Para períodos fechados, somente via Consulta Genérica na tabela SPG.  
  
**Saiba Mais**  
[**CLIQUE AQUI**para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
