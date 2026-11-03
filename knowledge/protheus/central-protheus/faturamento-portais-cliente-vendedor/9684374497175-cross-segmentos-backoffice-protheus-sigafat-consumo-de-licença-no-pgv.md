---
article_id: 9684374497175
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: acf2815ed03baf06e1977d3a25760ce2cb3f6772d15cad5d03a195113128ac20
fetched_at: '2026-06-28T22:38:23.922493+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Consumo de Licença no PGV
type: support-article
updated_at: '2025-11-27T19:49:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9684374497175-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Consumo-de-Licen%C3%A7a-no-PGV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16479148185623) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Consumo de Licença no Portal Gestão de Vendas?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Portal Gestão de Vendas - a partir da release 12.1.33  
  
**Solução**  
**Consumo de Licenças no Portal Gestão de Vendas (PGV).**  
O consumo de licenças no Portal Gestão de Vendas segue a mesma regra aplicada ao Protheus. Cada nova conexão estabelecida por meio de uma tela aberta no PGV consome uma licença (**Thread**).

Para o correto funcionamento do Portal Gestão de Vendas (PGV), é indispensável que o ambiente esteja licenciado com quantidade suficiente de licenças em, pelo menos, uma das seguintes modalidades:

1. ID da Aplicação: **0217 - APP TOTVS Gestão de Vendas (TGV)**

* **3004** - APP BACKOFFICE VENDAS
* **4001** - TOTVS I - Acesso a Portal, WS, BI, T-REPORTS e outros...
* **4000** - TOTVS FULL

**Importante: Sobre as licenças 4001 – TOTVS I e 4000 – TOTVS FULL**

A licença **4001 – TOTVS I** é destinada a integrações com rotinas e ferramentas do Protheus através de API. Caso o ambiente esteja licenciado **exclusivamente** com a licença **4001 - TOTVS I**, devem ser observados os seguintes pontos:

A licença **4000 – TOTVS FULL** é mais abrangente, permitindo acesso completo às funcionalidades do ambiente, abrangendo recursos avançados, integrações e operações que demandam permissões mais amplas dentro do Protheus.

* **Compartilhamento da licença**: verifique se outras aplicações do ambiente também utilizam essa mesma licença, pois isso pode impactar a disponibilidade de acesso.
* **Configuração do WebServices REST**: é necessário configurar a chave `Stateless` com o valor **1** para o correto funcionamento.

**Exemplo:**

*[URIHTML]*  
*URL=/vendas/*  
*PrepareIn=All*  
*Instances=1,2*  
*CORSEnable=1*  
*AllowOrigin=\**  
***Stateless=1***

Para maiores informações sobre consumo de licenças por demanda, acesse a página: [Consumo de Licença por demanda no REST do Protheus](https://tdn.totvs.com/x/NGR2Hw)
