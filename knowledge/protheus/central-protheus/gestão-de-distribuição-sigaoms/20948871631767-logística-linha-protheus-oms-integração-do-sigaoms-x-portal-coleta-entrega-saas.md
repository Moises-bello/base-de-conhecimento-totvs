---
article_id: 20948871631767
category: Gestão de Distribuição (SIGAOMS)
content_hash: c3fb6ce69e4b3c932ebb874660782999b5eca5ae3a9648dd52abeb86d30644f3
fetched_at: '2026-06-28T22:45:49.862457+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Integração do SIGAOMS x Portal Coleta Entrega
  SAAS
type: support-article
updated_at: '2024-01-30T20:50:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20948871631767-Log%C3%ADstica-Linha-Protheus-OMS-Integra%C3%A7%C3%A3o-do-SIGAOMS-x-Portal-Coleta-Entrega-SAAS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20948871597719) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como utilizar a Integração do **SIGAOMS** x **Portal Coleta Entrega SAAS**?   
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Solução**A integração do **SIGAOMS** x **Coleta Entrega**, consiste no **envio da Carga** gerada pela rotina **OMSA200-Montagem de Carga**, localizada no **Módulo 39-SIGAOMS**.   
O **envio de uma carga do SIGAOMS**, irá gerar uma **viagem** para controle e planejamento no **Coleta Entrega**.Com a integração ativa, possibilitará maior proximidade entre Motoristas e Planejadores por meio de automações e troca de mensagens em tempo real.  
Esta funcionalidade/integração será liberada no **Dicionário Oficial da Release 12.1.2310**.  
Para acessar detalhes do processo de integração do **SIGAOMS** x **Coleta Entrega**, no **Saiba Mais** desse artigo, indicamos as documentações associadas a este tema.  
  
Para uso desta funcionalidade, deve ser atualizado seu ambiente na seguinte ordem:

1. **Pacote: 010555** - Para atualização de dicionário de dados, criação de novas tabelas, campos, índices e gatilhos.
2. **Pacote: 011015** - Utilizado na integração do **TOTVS Logística TMS** x **Portal Logístico**.
3. **Pacote: 011339** - Utilizado na integração do **SIGAFAT - Faturament**o x **TOTVS Logística TMS**
4. **Pacotes DLOGTMS02-22574** com os fontes atualizados das rotinas envolvidas da versão 12.1.2210.

O *layout* **padrão**, poderá ser baixado automaticamente pela rotina **TMSAI88B-Importa Layout.** Para o **SIGAOMS**, escolha o *layout* **03.**

**Saiba mais**Mais informações poderão ser acessadas nos *links*:  
[Integração OMS x Coleta Entrega](https://tdn.totvs.com/pages/releaseview.action?pageId=759939874)   
[Montagem de Carga](https://tdn.totvs.com/pages/viewpage.action?pageId=551446517)  
[Guia de Uso - TOTVS Coleta e Entrega](https://tdn.totvs.com/display/MOBILE/Guia+de+Uso+-+TOTVS+Coleta+e+Entrega#tudo-sobre-instalacao)  
  
**Anexos**
