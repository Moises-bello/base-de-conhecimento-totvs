---
article_id: 34876204341271
category: Ferramentas
content_hash: c44f6ad959b4d4150627789ccef05cd92740d2675515a2903155a75beb860d6a
fetched_at: '2026-06-28T22:42:17.978837+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - A chave CheckSpecialKey em seu ambiente está desligada,
  você deve liga-la para seu uso da seção
type: support-article
updated_at: '2025-09-11T20:17:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34876204341271-Framework-Linha-Protheus-A-chave-CheckSpecialKey-em-seu-ambiente-est%C3%A1-desligada-voc%C3%AA-deve-liga-la-para-seu-uso-da-se%C3%A7%C3%A3o
---

**Dúvida**

Mensagem apresentada dentro de processos no Protheus: A chave CheckSpecialKey em seu ambiente está desligada. Você deve ativá-la para utilizar esta funcionalidade na seção **[GENERAL]**

**Ambiente**  
Protheus - Appserver - A partir da versão 12

**Solução**

Para garantir o correto funcionamento do sistema, retire ou comente a chave [**Checkspecialkey**] da seção [**General**] no arquivo de configuração do Appserver. Segue documentação onde não permite mais desabilitar a chave: [DFRM1-38351 DT Emitir alerta ao identificar SpecialKeys distintos](https://tdn.totvs.com/display/framework/DFRM1-38351+DT+Emitir+alerta+ao+identificar+SpecialKeys+distintos)
