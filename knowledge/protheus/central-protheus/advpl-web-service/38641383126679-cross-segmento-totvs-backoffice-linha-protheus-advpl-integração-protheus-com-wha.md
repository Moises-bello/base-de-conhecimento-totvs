---
article_id: 38641383126679
category: ADVPL - Web Service
content_hash: 0bc601c07648fc648a12a64d38f5209100ca0c428ff4e55f1d6071c7ddb2d684
fetched_at: '2026-06-28T22:40:10.544244+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Integração Protheus
  com WhatsApp
type: support-article
updated_at: '2026-03-17T18:49:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38641383126679-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Integra%C3%A7%C3%A3o-Protheus-com-WhatsApp
---

Recomendação para criação de uma API REST customizada em ADVPL ou TL++ para trafegar dados entre Protheus e WhatsApp, permitindo adaptar as regras de negócio conforme a necessidade da empresa.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38641383119255) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Existe uma forma padrão de integrar o Protheus ao WhatsApp?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões

**Solução**  
A integração do Protheus com o WhatsApp é viabilizada por meio da criação de uma API REST customizada.  
  
O tráfego de dados entre o Protheus e ferramentas externas ocorre utilizando o protocolo REST, com serviços desenvolvidos nas linguagens ADVPL ou TL++.   
  
A construção de APIs próprias é a alternativa técnica recomendada para este cenário, pois permite que o desenvolvedor responsável aplique as regras de negócio específicas da sua empresa, garantindo que a comunicação atenda exatamente à necessidade desejada.

**Passos**

1. Estruture as regras de negócio necessárias para o envio ou recebimento de mensagens da sua empresa.
2. **Configuração do Ambiente:** Realizar a configuração do serviço REST (ou REST TLPP) no arquivo `appserver.ini` do Protheus.
3. **Desenvolvimento:** Utilizar a linguagem ADVPL ou TL++ para a criação das classes e métodos (ex: ***GET***, ***POST***) que disponibilizarão os dados para a integração que será realizada com o WhatsApp.

**Saiba mais**  
[Como criar um serviço REST no protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052976074-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-criar-um-servi%C3%A7o-REST-no-protheus)  
[Conceitos sobre WebServices](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053029654-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Conceitos-sobre-WebServices)  
[Configuração básica REST do protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Configura%C3%A7%C3%A3o-b%C3%A1sica-REST-do-protheus)  
[Criação de Web Service REST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021376912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-Web-Service-REST)  
[REST tlppCore](https://tdn.totvs.com/pages/viewpage.action?pageId=553337101)
