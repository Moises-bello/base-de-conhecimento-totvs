---
article_id: 4410652120215
category: Gestão de Distribuição (SIGAOMS)
content_hash: f6b6a656cba7cb42b01ee4fce851a7cdc5b05de59991fd13f9fcb1b02c0147fc
fetched_at: '2026-06-28T22:45:49.821912+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Exclusão de Documento de Saída - Carga apresenta
  mensagem de  Falta Índice 3 para tabela DK1
type: support-article
updated_at: '2023-04-10T12:02:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410652120215-Log%C3%ADstica-Linha-Protheus-OMS-Exclus%C3%A3o-de-Documento-de-Sa%C3%ADda-Carga-apresenta-mensagem-de-Falta-%C3%8Dndice-3-para-tabela-DK1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:12 min**  
**Ocorrência**Na rotina de **Exclusão de Documento de Saída - Carga - MATA521,** é apresentada a mensagem **A rotina MATA521 foi atualizada sem o pacote de dicionários correspondente. Favor criar o índice 3 para a tabela DK1 (Módulo OMS)**.  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - A partir da versão 12.1.17  
  
**Causa**A mensagem ocorre devido a falta de aplicação de dicionário correspondente da tabela **DK1 - Viagem CPL Itens**.  
  
**Solução**Na  rotina de **MATA521,** ao ser apresentada a **mensagem** abaixo, deverá ser atualizado o **Pacote Acumulado do Módulo TOTVS OMS ,** que contém **atualização de dicionário:**

**![help.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4410701761687/help.jpg)**

Para atualizar o pacote **acumulado do Módulo TOTVS OMS**, siga as instruções do artigo [Logística - Linha Protheus - OMS - Pacote Acumulado do TOTVS OMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008813881-Log%C3%ADstica-Linha-Protheus-OMS-Pacote-Acumulado-do-TOTVS-OMS)  
  
**Saiba mais**A tabela **Viagem CPL Itens - DK1** será criada ao utilizar a Integração do **TOTVS OMS** **-****Order Management System** x **TOL - TOTVS Otimização Logística**, para maiores informações poderão ser acessadas no *link*:  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-SIGAOMS-x-TOTVS-Log%C3%ADstica-Cockpit)
