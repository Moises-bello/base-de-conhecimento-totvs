---
article_id: 39555511913495
category: Integrações Outros BackOffice
content_hash: 6f1be523c4ff63c656349e9908476f9fede570b31b80e217bcf93e777261f264
fetched_at: '2026-06-28T22:46:42.091353+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RH - RM - FOP - Integração RM Labore x BackOffice Protheus - Erro ao gerar
  WSDL do endereço http://localhost:8050/EAISERVICE.apw?WSDL
type: support-article
updated_at: '2026-04-09T12:37:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39555511913495-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Erro-ao-gerar-WSDL-do-endere%C3%A7o-http-localhost-8050-EAISERVICE-apw-WSDL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39555481284631) Tempo aproximado para leitura: **00:03:25 min**  
  
**Ocorrência**  
Ao tentar realizar integrações entre RM e Protheus, ocorre o erro: "Erro ao gerar WSDL do endereço http://localhost:8051/EAISERVICE.apw?WSDL  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
O erro indica que o a URL do Webservice do RM está informado errado no Protheus, especificamente no parâmetro MV\_EAIURL2 do Protheus.  
  
**Solução**  
Para solucionar essa ocorrência, você deve acessar o endereço do Webservice do RM, geralmente com o final wspageindex (exemplo: <http://localhost:8051/wsPageIndex/)> e acessar o menu EAIService.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39555511850135)

Muitos usuários se confundem copiando a URL desta página para informar no parâmetro MV\_EAIURL2 ou no Configurador do EAI 2.0, mas o endereço correto está no fim dessa página com o final IConWSEAIService (exemplo de URL: <http://localhost:8051/EAIService/IConWSEAIService>)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39555481287959)

**Observação**

Esse endereço exemplo de URL: <http://localhost:8051/EAIService/IConWSEAIService> não irá abrir no navegador que muitos utilizam como teste pois o é um endpoint.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39555511859479)

Outro possível motivo para a ocorrência do erro, mesmo com a URL correta, é a falha de comunicação entre o servidor do RM e o servidor do Protheus.

Nesses casos, é importante validar a conectividade entre os ambientes, acessando via navegador, a partir do servidor do RM, os serviços (Webservice e REST) do Protheus, e, da mesma forma, acessar o Webservice do RM a partir do servidor do Protheus.

Essa validação ajuda a identificar possíveis bloqueios de rede. Caso sejam encontrados impedimentos, será necessário acionar a equipe de infraestrutura para liberação da comunicação entre os servidores
