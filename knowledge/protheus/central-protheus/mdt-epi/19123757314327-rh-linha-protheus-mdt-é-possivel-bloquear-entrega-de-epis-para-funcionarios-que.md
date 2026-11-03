---
article_id: 19123757314327
category: MDT - EPI
content_hash: a7d58a679971de0588930fca6fb9f7c306529e5b911703e751c809ea33ac82ff
fetched_at: '2026-06-28T22:44:25.235981+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - É possivel bloquear entrega de EPI's para funcionarios
  que não estejam com situação ativa
type: support-article
updated_at: '2025-03-03T12:26:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19123757314327-RH-Linha-Protheus-MDT-%C3%89-possivel-bloquear-entrega-de-EPI-s-para-funcionarios-que-n%C3%A3o-estejam-com-situa%C3%A7%C3%A3o-ativa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19123746160023) Tempo aproximado para leitura: **00:02:00min** **Dúvida**É possível bloquear entrega de EPI's para funcionários que não estejam com situação ativa?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução****Requisitos:** Estar com o parâmetro do configurador do Protheus **(SIGACFG)** de integração entre MDT e GPE habilitado **(MV\_MDTGPE = S)** e no caso do funcionário estar afastado ou em férias, o mesmo deve possuir cadastro na rotina **Ausências** **(GPEA240).**  
Para bloquear entregas de EPI que ocorrerem para funcionários que estejam com situação não ativa (demitido, afastado ou em férias) é necessário que o parâmetro do configurador Protheus **MV\_NGEPIEN** esteja configurado como **N**. Acesse a rotina de parâmetros através do caminho, **Ambiente > Cadastros > Parâmetros** e realize a alteração.  
  
![Bloqueio Entrega.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19123770559895)  
 **Saiba mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-BR/sections/9198712823575-Assistente-Virtual-Carolina)
