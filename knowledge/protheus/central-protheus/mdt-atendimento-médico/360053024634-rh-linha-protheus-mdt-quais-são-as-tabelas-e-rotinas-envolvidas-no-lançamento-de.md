---
article_id: 360053024634
category: MDT - Atendimento Médico
content_hash: 783b2b1270ceef4c1bef541aef8b05fa885d5b03b1d57a6b969e3ad8510600ff
fetched_at: '2026-06-28T22:44:21.533741+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Quais são as tabelas e rotinas envolvidas no lançamento
  de Atestado Médico
type: support-article
updated_at: '2025-07-25T19:45:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053024634-RH-Linha-Protheus-MDT-Quais-s%C3%A3o-as-tabelas-e-rotinas-envolvidas-no-lan%C3%A7amento-de-Atestado-M%C3%A9dico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25844498549015)**Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Quais são as tabelas e rotinas envolvidas no lançamento de Atestado Médico?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – A partir da versão 12.1.17  
  
**Solução**Tabela: **TM0** - Ficha Médica - Rotina: MDTA005  
Tabela: **TMY** - Atestado Médico (SIGAMDT) - Rotina: MDTA695  
Tabela: **TLG** - Grupo de Doenças (CID) - Rotina: MDTA081  
Tabela: **TMR** - CID - Rotina: MDTA080  
Tabela: **TKI** - CID complementar para Atestado (não há rotina, é puxado os dados contidos na tabela MDTA081)   
Tabela: **TNP** - Emitentes de Atestados Médicos - Rotina: MDTA680  
Tabela: **SP6** - Motivo Abono/Justificativa - Rotina: PONA050      
Tabela: **RCM** - Tipos de Ausencias  - Rotina: GPEA430  
Tabela: **TYZ** - Afastamento Atestado Médico (Não há rotina, é alimentada na rotina do próprio atestado médico)    
Tabela: **SR8** - Controle de Ausências -  Rotina: GPEA240 (caso haja integração com o módulo SIGAGPE)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
