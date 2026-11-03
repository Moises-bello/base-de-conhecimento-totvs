---
article_id: 4404429693335
category: RH - Error.log
content_hash: 1e46693689307fb5a938d965628a15f51e664f59a0be7f880eb5536a98e1f39c
fetched_at: '2026-06-28T22:44:49.555293+00:00'
product: protheus
section_id: 32419193161751
source: central-protheus
title: RH - Linha Protheus - PON - Error.log ao gerar o Relatório de Espelho de Ponto
  Eletrônico - type mismatch on compare  on PONR010(PONR010.PRX)
type: support-article
updated_at: '2025-10-13T16:49:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404429693335-RH-Linha-Protheus-PON-Error-log-ao-gerar-o-Relat%C3%B3rio-de-Espelho-de-Ponto-Eletr%C3%B4nico-type-mismatch-on-compare-on-PONR010-PONR010-PRX
---

**![relogio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33377381428503) Tempo aproximado para leitura: **00:01:00 min******Ocorrência**Ao gerar o **Relatório de Espelho de Ponto**, na rotina **PONR010**, gera *error log*: "***type mismatch on compare  on* PONR010(PONR010.PRX)**"  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre em ambiente que possui o grupo de perguntas **PNR010** fora do padrão  
  
**Solução**Acesse o Módulo de **Configurador**, em **SIGACFG**, logado na Empresa que o erro ocorre, no grupo de perguntas de nome **PNR010**. Para isso:  
-> Acesse o Módulo de Configurador, em **SIGACFG**;  
-> Acesse a rotina **Base de Dados/Dicionário/Bases de Dados**;  
-> Abra o dicionário da empresa e Vá na opção ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33377441750679)"Perguntas";  
-> Busque ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33377441753111) pela pergunta "**PNR010**";  
-> Clique sobre ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33377381435543)"Editar";  
-> Após abertura em modo edição, faça os devidos ajustes de acordo com o padrão demonstrado abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33377381436567)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33377441757719)

**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
