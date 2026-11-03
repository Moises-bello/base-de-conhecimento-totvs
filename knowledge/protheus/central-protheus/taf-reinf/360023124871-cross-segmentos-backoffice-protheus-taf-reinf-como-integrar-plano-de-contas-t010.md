---
article_id: 360023124871
category: TAF - REINF
content_hash: d9cc004fa8492940e570758baf143271e03396227bb7087a7dfd489fca58f578
fetched_at: '2026-06-28T22:41:33.533388+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Como integrar Plano
  de Contas - T010
type: support-article
updated_at: '2023-04-04T12:14:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023124871-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-Plano-de-Contas-T010
---

**Dúvida**Procedimentos para integrar as CONTAS CONTÁBEIS do Protheus para o TAF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020849592/mceclip0.png)  
  
**Ambiente**Microsiga Protheus - Extrator Fiscal – A partir da versão 11.80  
  
**Solução**

Por gentileza, executar os procedimentos de forma rigorosa.  
  
1º Caso seu ambiente estiver desatualizado, aplicar os pacotes dos links abaixo, senão ir para a **etapa 4**:  
  
Pacote periódico

[MP - TAF - REINF - Atualização Completa REINF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-MP-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-REINF?source=search)

2º.Ir no parâmetro **MV\_VAUTCON**, apagar o conteúdo em **"POR"** e em seguida executar o **Wizard de Configuração do TAF**.

[TAF - CONFIGURAÇÃO - Atualização das tabelas autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034479973-TAF-CONFIGURA%C3%87%C3%83O-Atualiza%C3%A7%C3%A3o-das-tabelas-autocontidas?source=search)

3º - Avaliar o compartilhamento das tabelas C1O (TAF) e CT1 (PROTHEUS).

**Compartilhada**: Se a tabela CT1 estiver compartilhada, a C1O também deverá estar.

**Exclusiva**: Se a CT1 estiver exclusiva, a C1O também deverá estar.

4º Avalie se há alguma conta Bloqueada, pois o extrator só irá levar as contas desbloqueadas. Caso haja contas bloqueadas, efetue o desbloqueio e prossiga para a extração.

5º Executar a opção de carga inicial no extrator fiscal.

[MP - TAF/REINF Carga inicial.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420378223639-MP-TAF-REINF-Carga-inicial-?source=search)

Executar o extrator e validar se possui algum erro no gerenciador de integração.

[TAF - REINF - Como consultar o gerenciador de integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043361753-TAF-REINF-Como-consultar-o-gerenciador-de-integra%C3%A7%C3%A3o?source=search)
