---
article_id: 5368261642135
category: Integrações Outros BackOffice
content_hash: cd39c7f13599142dc09aad63ad8c7d2e24d98d41f898980aa2beefe0a4a619e2
fetched_at: '2026-06-28T22:46:42.153331+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RM - FOP - Integração RM Labore x BackOffice Protheus - General Error
type: support-article
updated_at: '2025-02-10T16:40:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5368261642135-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-General-Error
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:27 min****Ocorrência**No módulo da Folha de Pagamento, ao tentar realizar qualquer tipo de integração com o BackOffice Protheus retorna o erro General Error.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro é apresentando devido à falha de comunicação entre o ambiente RM x Protheus por alguns tipos de fatores.  
  
**Solução**

O erro abaixo pode acontecer em qualquer tipo de integração realizada entre o RM x BackOffice Protheus:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5368263596695/mceclip2.png)  
  
Para solucionar essa ocorrência, podemos seguir os passos abaixo:  
  
1. Devemos verificar o endereço do Protheus que foi informado no ambiente. Caso seja utilizado **EAI 1.0**, podemos encontrar acessando o módulo **Integrações | Integrações | Mensagem Única | Integração** e editar o registro.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5367980441879/mceclip0.png)  
  
2. Caso seja utilizado o EAI 2.0, poderá localizar acessando o módulo **Integrações | EAI 2.0 | Aplicativos:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5368213717143/mceclip1.png)**

3. O tipo de integração irá determina o caminho e onde será o preenchimento, o EAI 1.0 utilizamos somente o endereço WebService do Protheus, já no EAI 2.0 também é necessário informar o  endereço REST do Protheus.

Observe exemplos de URL a serem informados:

Endereço WebService do RM:

http://ip\_da\_máquina:porta/EAIService/IConWSEAIService

Endereço WebService do Protheus:

http://ip\_da\_máquina:porta/EAISERVICE.apw?WSDL

Endereço Rest do Protheus:

http://ip\_da\_máquina:porta/rest

4. Todo endereçamento ser realizado, pode ser necessário realizar a reinicialização dos serviços **DBACESS** e **APPSERVER** por parte do **Protheus** e **Host** da aplicação **RM.**

**Saiba mais**Caso tenha interesse em conhecer ainda mais sobre a integração, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021798751).
