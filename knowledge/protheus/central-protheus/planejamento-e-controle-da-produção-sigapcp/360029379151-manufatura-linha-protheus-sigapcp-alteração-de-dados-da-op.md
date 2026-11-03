---
article_id: 360029379151
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d4a7406013a5cc8c1c0c7158cb2baa6225bcfcf3afd633a832693fa88910d8b7
fetched_at: '2026-06-28T22:42:40.772182+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Alteração de dados da OP
type: support-article
updated_at: '2021-06-11T20:26:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029379151-Manufatura-Linha-Protheus-SIGAPCP-Altera%C3%A7%C3%A3o-de-dados-da-OP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:49 min****Dúvida**Por que alguns dados como a quantidade da **OP - Ordem de produção** não podem ser alterados?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Algumas informações, como a quantidade da **OP** não podem ser editadas para garantir a integridade dos dados, pois são usadas para cálculos e registros em outras tabelas, como a tabela **SB2 - Saldos Físico e Financeiro** e **SD4 - Requisições Empenhadas.**  
  
**Saiba mais**  
Caso necessite alterar algum campo bloqueado na alteração da **OP** pode ser utilizado o ponto de entrada [MTA650ALT - Liberar campos para alteração da OP](https://tdn.totvs.com/x/ZzG4Ew).
