---
article_id: 38583182557079
category: ADVPL - Web Service
content_hash: 5317e1516444613be4b29a7ef5ddaa2ec6f1b8d74d4d8e7f141934403f5e99d8
fetched_at: '2026-06-28T22:40:10.540407+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Integração PowerBI
  ao Protheus
type: support-article
updated_at: '2026-02-24T19:08:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38583182557079-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Integra%C3%A7%C3%A3o-PowerBI-ao-Protheus
---

Para integrar o Protheus ao Power BI é necessário desenvolver APIs customizadas utilizando ADVPL ou TL++ e o protocolo REST. A responsabilidade pela integração é do cliente, e, em ambientes Cloud, é preciso validar a viabilidade junto ao suporte. Consulte a documentação oficial para detalhes técnicos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38583182547351) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Existe uma forma padrão de integrar o Protheus ao PowerBI?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões

**Solução**  
A integração direta com o Power BI requer o desenvolvimento de uma estrutura customizada, visto que não há uma ferramenta padrão para este processo.

A TOTVS concentra o suporte técnico direto e a homologação em suas próprias soluções de BI nativas. Dessa forma, a implementação, configuração e manutenção de conexões com ferramentas de mercado externas são de responsabilidade exclusiva do cliente.

Como alternativa técnica para viabilizar esse cenário, é possível construir APIs próprias. O tráfego de dados entre o Protheus e as ferramentas de análise ocorre por meio da utilização do protocolo REST, desenvolvido através das linguagens ADVPL ou TL++.

**Passos**   
Para a construção de uma estrutura de consumo de dados via API (REST), devem ser seguidas as seguintes etapas técnicas:

1. **Configuração do Ambiente:** Realizar a configuração do serviço REST (ou REST TLPP) no arquivo `appserver.ini` do Protheus.
2. **Desenvolvimento:** Utilizar a linguagem ADVPL ou, preferencialmente, TL++ para a criação das classes e métodos (ex: GET) que disponibilizarão os dados para o consumo do Power BI.

**Importante**  
Caso o banco de dados esteja hospedado em ambiente **Cloud**, é necessária a validação prévia junto à equipe de atendimento **Cloud** sobre a viabilidade, compatibilidade e liberação de acessos para este tipo de conexão externa.

**Saiba mais**  
Para detalhes técnicos sobre a criação de serviços REST em ambas as linguagens, consulte a documentação oficial no TDN:

[Como criar um serviço REST no protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052976074-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-criar-um-servi%C3%A7o-REST-no-protheus)  
[Conceitos sobre WebServices](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053029654-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Conceitos-sobre-WebServices)  
[Configuração básica REST do protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Configura%C3%A7%C3%A3o-b%C3%A1sica-REST-do-protheus)  
[Criação de Web Service REST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021376912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-Web-Service-REST)  
[REST tlppCore](https://tdn.totvs.com/pages/viewpage.action?pageId=553337101)
