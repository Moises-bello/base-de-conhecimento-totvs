---
article_id: 1500008706802
category: Portal de Gestão de Capital Humano
content_hash: 1b9f87e54dcd5ac735a0c161162cc30d7f3e586968b746ca93b067f3d27aeb48
fetched_at: '2026-06-28T22:43:00.010839+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - É possível aumentar o timeout quando está
  logado no Portal Gestão Capital Humano
type: support-article
updated_at: '2021-04-29T19:53:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008706802-RH-Linha-Protheus-PORTAL-GCH-%C3%89-poss%C3%ADvel-aumentar-o-timeout-quando-est%C3%A1-logado-no-Portal-Gest%C3%A3o-Capital-Humano
---

**Dúvida**  
É possível aumentar o timeout quando está logado no Portal Gestão Capital Humano  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Sim, é possível configurar o appserver.ini incluindo a sessão **SessionTimeOut** que indica o TEMPO LIMITE, em segundos que o portal ficará aberto sem a sessão expirar.  
Caso não seja especificado, o valor padrão será 600 segundos (10 minutos).  
  
**Observação**: Esta chave deve ser configurada apenas na seção [HTTP] e é válida para todos os ambientes WEBEX configurados no servidor do Sistema (ERP).  
  
**Exemplo:**  
[HTTP]  
ENABLE=1  
PORT=8098  
PATH=C:\P12\_25\TOTVS\_12\_25\Protheus\_Data\web\pp  
**SESSIONTIMEOUT=1800** ; Especifica 30 minutos de Timeout  
  
**Importante**: A **SessionTimeOut**define o intervalo em segundos das variáveis da sessão do usuário ao utilizar uma configuração de Working threads extendes para atender através de link .APW, as solicitações de geração de páginas dinâmicas.  
  
**Saiba Mais**[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
