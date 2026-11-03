---
article_id: 4402638800279
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 0ded62be9bf0b80122cc624e20f80a4ab25f8b24125fca9b36c93cd62f20f3bb
fetched_at: '2026-06-28T22:45:21.124233+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - Configuração - Como realizar o ajuste manual na
  TAFST2
type: support-article
updated_at: '2026-06-26T12:17:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402638800279-RH-Linha-Protheus-TAF-Configura%C3%A7%C3%A3o-Como-realizar-o-ajuste-manual-na-TAFST2
---

**Ocorrência**  
Quando os eventos do e-Social são enviados para o TAF, o sistema ERP indica que o evento está aguardando processamento e fica registrado no gerenciador de integração.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**  
Os eventos ficam retidos na tabela de integração através do TAFST2 e não são exibidos na tabela TAFXERP, resultando na ausência dos eventos na tela de monitoramento para transmissão ao e-Social.  
  
**Solução**

1. Acesse o seguinte menu: Miscelânea ► Ajuste de Base ► Ajuste Manual TAFST2 x TAFXERP.  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402645743767)
2. Insira as informações nos campos conforme indicado abaixo:  
     
   **Exemplo:** Os campos Data Dê e Data Até: deve ser a data que os eventos foram integrados e o TAFKEY e o TAFTICKET caso não tenha certeza sobre o que deveria informa, pode deixar os valores vazios:  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39333124450711)
3. Em seguida, acesse a rotina de processamento do TAF e execute novamente o processamento dos eventos. [RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - INTEGRAÇÕES - Como processar os eventos e verificar os status no Gerenciador de Integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049713414-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-INTEGRA%C3%87%C3%95ES-Como-processar-os-eventos-e-verificar-os-status-no-Gerenciador-de-Integra%C3%A7%C3%A3o)  
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402638799895)
