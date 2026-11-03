---
article_id: 10273949483031
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 5067c705870885b4eebb170fd56a93d81e540536cb92e6cf825d4f59038fefb9
fetched_at: '2026-06-28T22:38:48.212541+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - É possível
  ter um PE que apresente visualização de uma interface durante a jornada de fechamento?
type: support-article
updated_at: '2025-03-12T12:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10273949483031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-%C3%89-poss%C3%ADvel-ter-um-PE-que-apresente-visualiza%C3%A7%C3%A3o-de-uma-interface-durante-a-jornada-de-fechamento
---

**Dúvida**Desenvolvi um ponto de entrada acionado em uma rotina executada pelo Acompanha Custos, como o recálculo do Custo Médio (MATA330), que possui a exibição de uma interface. Esse ponto de entrada continuará funcionando?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33.  
  
**Solução**Os pontos de entrada existentes nas rotinas de fechamento continuam disponíveis, porém por conta da tecnologia utilizada, não permitem mais a apresentação de interface.

**PO-UI** utiliza a execução de um JOB para a montagem e apresentação dos dados em tela, sendo assim, não é possível realizar a montagem de qualquer tipo de tela através de pontos de entrada em rotinas PO-UI, caso o faça será apresentando a mensagem de erro por exemplo:

**JOB Threads doesn't support remote/visual components.**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10273778464023)

Caso você utilize algum ponto de entrada com abertura de tela, será necessário adaptá-lo para que ele trabalhe considerando que o processamento da rotina ocorrerá **sem possibilidade de exibição de interface, como se fosse uma execução via schedule ou execauto.**

**Saiba mais**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que é a rotina Acompanha Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065773526039)*

*[Clique aqui e veja mais artigos sobre o Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-MONITOR-DE-CUSTOS)*
