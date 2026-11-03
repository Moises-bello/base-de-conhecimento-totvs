---
article_id: 360052084654
category: RH - Carol
content_hash: 57bb23d439caff24279e9d95e54cfe25c7e2b2221d9eaaa85c77b86ca73581db
fetched_at: '2026-06-28T22:44:56.613293+00:00'
product: protheus
section_id: 19035556880407
source: central-protheus
title: RH - Linha Protheus - PON - Como integrar as marcações no Protheus, quando
  existe integração entre o Clock In da Carol com o Ponto Eletrônico
type: support-article
updated_at: '2026-01-15T13:00:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052084654-RH-Linha-Protheus-PON-Como-integrar-as-marca%C3%A7%C3%B5es-no-Protheus-quando-existe-integra%C3%A7%C3%A3o-entre-o-Clock-In-da-Carol-com-o-Ponto-Eletr%C3%B4nico
---

**Dúvida**  
Como integrar as marcações no Protheus, quando existe integração entre o Clock In da Carol com o Ponto Eletrônico  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para integrar as marcações é necessário efetuar o seguinte processo:  
**1.** Primeiramente é necessário **processar a rotina** [**PONAPI01**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052840373-RH-Linha-Protheus-PON-Como-incluir-a-rotina-PONAPI01-Integra%C3%A7%C3%A3o-com-Clock-In-no-menu-do-Ponto-Eletr%C3%B4nico) **(**incluída no menu do Ponto Eletrônico) para que as marcações do Clock In sejam gravadas na tabela RR1;

**2.** Após isso é necessário processar a rotina de [**Leitura/Apontamento (PONM010)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004052211-RH-Linha-Protheus-PON-Como-funciona-a-Leitura-e-Apontamento-das-marca%C3%A7%C3%B5es) do Ponto Eletrônico para que as marcações sejam **gravadas na tabela SP8.**  
  
**Saiba Mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
