---
article_id: 36092806199831
category: SIGAEST - SALDOS
content_hash: a98e56ced2cb2239f294c1c275054c8db49e64398162a3597828d15f9eeaa9ec
fetched_at: '2026-06-28T22:39:14.916429+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Parâmetro MV_ESTNEG
  por Filial, é possível criar um parâmetro para cada Filial com conteúdos distintos?
type: support-article
updated_at: '2025-11-04T16:49:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36092806199831-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Par%C3%A2metro-MV-ESTNEG-por-Filial-%C3%A9-poss%C3%ADvel-criar-um-par%C3%A2metro-para-cada-Filial-com-conte%C3%BAdos-distintos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36092748196759) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**

É possível utilizar o parâmetro **MV\_ESTNEG**  Exclusivo para cada Filial com os conteúdos distintos?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  - Todas as versões   
  
**Solução**

É possível sim, pode ser criado um para cada Filial, reforçando que deve constar o parâmetro para cada Filial com o conteúdo desejado. Veja o exemplo abaixo.

![MV_ESTNEG filial.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/36093446730647)

**Nesse exemplo como devem ficar os parâmetros no Configurador:**

![MV_ESTNEG .jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/36093437857047)

***Observação:***Nesse caso, ***não deve existir*** o parâmetro com o ***campo Filial em Branco***, pois o sistema entende que deve seguir a regra para o parâmetro Compartilhado para todas as Filiais e desconsidera os parâmetros que estão destinados a cada Filial.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre SALDOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)

[SIGAEST - MA240NEGAT - Principais situações que podem apresentar esse help](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058347413-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MA240NEGAT-Principais-situa%C3%A7%C3%B5es-que-podem-apresentar-esse-help)

[SIGAEST - Como descobrir a origem dos saldos na consulta com comando [F4] no Produto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto)
