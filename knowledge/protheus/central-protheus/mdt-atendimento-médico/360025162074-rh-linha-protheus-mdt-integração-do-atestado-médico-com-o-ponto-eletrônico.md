---
article_id: 360025162074
category: MDT - Atendimento Médico
content_hash: f65643977e8085afce5cd8d3a8090a5c65bf7c04cba4ecc1a28e2abe7b7f2e17
fetched_at: '2026-06-28T22:44:20.420203+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Integração do Atestado Médico com o Ponto Eletrônico
type: support-article
updated_at: '2025-07-29T16:57:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025162074-RH-Linha-Protheus-MDT-Integra%C3%A7%C3%A3o-do-Atestado-M%C3%A9dico-com-o-Ponto-Eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24788734997271)**Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como efetuar a integração do atestado médico com o módulo do Ponto Eletrônico (SIGAMDT x SIGAPON)?  
Integração entre Medicina e Segurança do Trabalho e Ponto Eletrônico  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Certifique-se do conteúdo dos parâmetro **MV\_PONMES** e **MV\_PAPONTA**, pois o lançamento do atestado com pré abono precisa estar dentro do período em aberto.  
  
Ajuste o conteúdo dos parâmetros abaixo:  
  
**MV\_NG2ABON**: Códigos de Abono que podem ser informados pelo programa de Atestado Médico  
Exemplo = 001,002  
  
**MV\_NG2IPON** = Integração com o Ponto = 1   
  
**MV\_MDTGPE** = S  
  
Após lançar o atestado médico no módulo SIGAMDT em **Atualizações > Atendimento Médico > Atestado Médico**, na aba Ponto Eletrônico informar o código do abono conforme definição do parâmetro **MV\_NG2ABON**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24801979059863)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24801974327703)  
  
Deverá conferir no módulo SIGAPON no caminho **Atualizações >** **Cadastro do funcionário > Pré abono.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24801979072023)** **Importante:** Na rotina cadastro do ponto > período de apontamento, só deve ter cadastrado os períodos já fechados. Logo, o período do lançamento do atestado não pode estar cadastrado nessa rotina.  
  
O cadastro do abono utilizado no atestado deve estar com o campo **Pré Abona = SIM**

Ao fazer o apontamento das marcações será atualizado nos lançamentos do funcionário o abono cadastrado.  
  
Saneamento da base deve ser realizado em caso de dúvidas consulte documentação de apoio:  
[RH - Linha Protheus - MDT - eSocial - Existe vídeos com o passo a passo de geração dos eventos SST (Medicina e Segurança do Trabalho) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410314804631-RH-Linha-Protheus-MDT-eSocial-Existe-v%C3%ADdeos-com-o-passo-a-passo-de-gera%C3%A7%C3%A3o-dos-eventos-SST-Medicina-e-Seguran%C3%A7a-do-Trabalho-no-eSocial)

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
