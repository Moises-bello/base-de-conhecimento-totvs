---
article_id: 16192956938647
category: Manutenção de Ativos (SIGAMNT)
content_hash: 70275d56d50e270550b0d4314cb2cfb92946bdcfd224b01b09e6fc084ccc9b33
fetched_at: '2026-06-28T22:42:34.312602+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Parâmetro MV_NGMNSFC
type: support-article
updated_at: '2025-05-26T17:50:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16192956938647-Manufatura-Linha-Protheus-MNT-Par%C3%A2metro-MV-NGMNSFC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16192973726103) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual a funcionalidade do parâmetro **MV\_NGMNSFC - Integração Manutenção - MNT com Chão de Fábrica - SFC**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Esse parâmetro indica se o módulo **SIGAMNT - Manutenção de Ativos** está integrado com o módulo **SIGASFC - Chão de Fábrica**, no que diz respeito a inclusão de **Bloqueio de recursos - MATA660** para o equipamento.  
  
As opções possíveis para esse parâmetro são:

* 1 - Não integra
* 2 - Integra *On-line*
* 3 - Integra com confirmação

**Importante**  
Para que o bloqueio seja incluído, é necessário que no cadastro de **Bem - MNTA080** o campo **T9\_FERRAME - Tipo (PCP)** esteja preenchido com o conteúdo **R - Recurso**, e no campo **T9\_RECFERR - Recur/Ferram** seja informado um recurso cadastrado na rotina **SFCA006 - Recurso**.
