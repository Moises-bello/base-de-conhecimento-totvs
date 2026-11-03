---
article_id: 360052518913
category: RH - Ponto Eletrônico
content_hash: 3d3f9499bee31449adc96232fe37fa72b1ffb32490f992a9336b274e4a1426ed
fetched_at: '2026-06-28T22:44:58.255320+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - Troca de Turno em Lote
type: support-article
updated_at: '2026-02-16T13:03:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052518913-RH-Linha-Protheus-Troca-de-Turno-em-Lote
---

**Dúvida**  
Como executar a Troca de Turno em lote?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A **Troca de Turno em lote** nada mais é que a otimização do processo manual da troca de turno. É possível **selecionar diversas matrículas** de uma só vez para processar a troca para um mesmo Turno/Sequência/Regra de Apontamento como destino, ou seja, as matrículas selecionadas não precisam estar atualmente sob os mesmos registros, porém, no momento da troca em lote, só serão possíveis alterações para matrículas que ficarão a partir daquela data com o mesmo Turno/Sequência/Regra de Apontamento.  
  
É importante também que a data para a qual será processada a troca em lote, esteja **dentro do período de apontamento** informado no **MV\_PONMES**, por exemplo: se o período aberto for de 01 à 30.06.2020, a troca em lote só poderá ser feita em datas dentro deste período.   
Além disso, é importante que a **data base do sistema** esteja no **último dia do período de apontamento**.  
  
Para processar a troca, basta acessar a rotina de **Troca de Turno - Outras Ações - Troca em Lote** - selecionar as matrículas necessárias, preencher os parâmetros e confirmar.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406126425239)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406126449175)  
\*\*Vale ressaltar que o limite de seleção de registros na rotina é de **50 matrículas** simultaneamente.  
  
**Saiba Mais:**  
[Troca de Turno em Lote](https://tdn.totvs.com/pages/releaseview.action?pageId=778769709)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
