---
article_id: 21076832799255
category: Integração RM
content_hash: 4db4082b91fb5b81a1055dc83ff6e007341adf4eb4e2359f262df36c73e983b5
fetched_at: '2026-06-28T22:42:36.868384+00:00'
product: protheus
section_id: 360012117913
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Controle de Numeração - Manutenção de Ativos
  x RM BackOffice
type: support-article
updated_at: '2024-02-05T14:30:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21076832799255-Manufatura-Linha-Protheus-MNT-Controle-de-Numera%C3%A7%C3%A3o-Manuten%C3%A7%C3%A3o-de-Ativos-x-RM-BackOffice
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21076832748311)** Tempo aproximado para leitura: **00:00:55 min** **Dúvida**Como funciona o controle de numeração automática no **Manutenção de Ativos** integrado ao **RM BackOffice**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integração RM - Todas as versões  
  
**Solução**Para geração de numeração sequêncial de **Ordem de Serviço - STJ**, **Solicitação Armazém - SCP** e **Solicitação de Compras - SC1**, respectivamente para os campos **Número da ordem de serviço - TJ\_ORDEM**, **Número da solicitação de armazém - CP\_NUM** e **Número da solicitação de compra - C1\_NUM**, quando o **Manutenção de Ativos** **- SIGAMNT** está integrado ao **BackOffice RM**, não são utilizados os controles de numeração automática do **Protheus**, cadastrados no **Configurador - SIGACFG**. O controle é feito de forma sequencial com base no maior código encontrado  nos registros já cadastrados, somando mais 1.   
Isto ocorre, pois a regra de negócio do **BackOffice RM** requer sempre um sequencial e nunca realiza *rollback* de numeração, já no processo de controle de numeração ocorre este processo de reutilização de numeração ao cancelar e deletar os registros.
