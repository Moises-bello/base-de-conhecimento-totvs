---
article_id: 360027628791
category: CRM - Dúvidas Gerais
content_hash: 7a4c788678a58aff8eb239edfd2b49ae18eb5be782e4874e3e3dfb60b30c0963
fetched_at: '2026-06-28T22:40:27.566073+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM-Help-NO_IX  Função de usuario não está com U_FT600EXE
type: support-article
updated_at: '2021-04-28T14:50:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027628791-MP-CRM-Help-NO-IX-Fun%C3%A7%C3%A3o-de-usuario-n%C3%A3o-est%C3%A1-com-U-FT600EXE
---

**[*Remover as instruções entre colchetes*]****Ocorrência**

Ao imprimir a proposta comercial (**fata600**), gera o Help:**Help:NO\_IX Função de usuario não está com U\_FT600EXE**

![](https://totvssuporte.zendesk.com/attachments/token/3mmdM3AdLNxxCUVj23lMbkRta/?name=proposta.JPG)  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 11.  
   
 **Causa**

O Help ocorre por que o executável da proposta comercial **FT600.EXE** não foi compilado ao RPO.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Baixe o pacote de integração Word word , onde já contém o executável **FT600.EXE**: **<http://tdn.totvs.com/pages/viewpage.action?pageId=239035266> ;**  
 2. Via TDS ou antigo IDE, complie o executável ao RPO;  
 3. Reinicie o smartclient e efetue o processo novamente.

**Obs: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
