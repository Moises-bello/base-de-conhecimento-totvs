---
article_id: 21645638243095
category: Evento S-2240
content_hash: d3490ded4a5caf3207b95e95e8f06630b92b6a5a8b804dc65c1f5ad065c66b5f
fetched_at: '2026-06-28T22:45:23.471163+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - É possivel realizar geração
  de evento S-2240 em lote
type: support-article
updated_at: '2024-02-28T12:01:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21645638243095-RH-Linha-Protheus-MDT-eSocial-S-2240-%C3%89-possivel-realizar-gera%C3%A7%C3%A3o-de-evento-S-2240-em-lote
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21645638224663) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível realizar geração de evento S-2240 em lote?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Os eventos do SST são gerados no momento do cadastro, contudo existem algumas situações em que é possível gerar essa carga do S-2240 em lote. Abaixo descrevo algumas circunstancias sobre o disparo do S-2240.  
  
**1.** No processo de implantação é necessário gerar a **carga de riscos**, este processo faz com o sistema  gere o evento para todos os funcionários que possuem risco e para todos funcionários que possuem ausência de risco.  
  
Para saber mais sobre a **Carga de Risco** para Empresa/Filial, consulte a documentação abaixo  
  
[RH - Linha Protheus - MDT - eSocial - S-2240 - Como gerar a Carga de Risco de uma filial específica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4479141016983-RH-Linha-Protheus-MDT-eSocial-S-2240-Como-gerar-a-Carga-de-Risco-de-uma-filial-espec%C3%ADfica)  
**2.** Quando existe exposição de risco para o(s) funcionario(s) ao realizar o cadastro do risco **(MDTA180)** ou alguma alteração, o evento S-2240 pode ser enviado em lote para aqueles funcionários expostos ao risco. Conforme exemplo abaixo:  
  
![gif risco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/21645638229015)  
  
**3.** Para funcionários que não tem exposição a risco, não temos uma forma padrão de fazer esse disparo em lote, visto que no momento da admissão já é gerado o evento quando **não existe exposição a risco**. Pode ocorrer a necessidade de reenvio do evento, necessidade essa que deve ser avaliada pelo cliente de acordo com cenário em que se encontra, para esses casos deve ser reprocessado a rotina **Gerar Carga de Riscos** para disparo em lote onde o sistema irá processar todos os riscos/ausências de riscos existentes no disparo do evento S-2240.  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
