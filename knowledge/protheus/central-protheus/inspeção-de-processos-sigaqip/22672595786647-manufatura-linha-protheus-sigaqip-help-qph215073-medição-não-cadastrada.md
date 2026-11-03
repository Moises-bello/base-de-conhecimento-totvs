---
article_id: 22672595786647
category: Inspeção de Processos (SIGAQIP)
content_hash: 4aeed9610e3f329ecc43767e37d7706c543537597432cdf296c897e3f6ef4052
fetched_at: '2026-06-28T22:42:25.785505+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help QPH215073 - Medição não cadastrada
type: support-article
updated_at: '2024-04-10T15:58:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22672595786647-Manufatura-Linha-Protheus-SIGAQIP-Help-QPH215073-Medi%C3%A7%C3%A3o-n%C3%A3o-cadastrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22672595759639) Tempo aproximado para leitura: **00:01:05 min****Ocorrência**Na rotina QIPA215 - Resultados, ao selecionar a aba **Laudo de Laboratório,** é retornado o *help* QPH215073 - Existem campos obrigatórios que não foram preenchidos na medição atual.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**O *help* **QPH215073** ocorre quando o ensaio está definido como obrigatório na rotina **QIPA010 - Especificação de Produtos** e não possuí medição cadastrada**.**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Na rotina **QIPA215 - Resultados**, realizar o apontamento de medição no ensaio obrigatório;
2. Ou validar o parâmetro **MV\_QPGESMD - Define se irá ignorar ensaios sem medições mesmo que estes estejam definidos como Obrigatórios 1 = Sim / 2 = Não.**

**Observação**Para cenário similar, verifique também o artigo [Manufatura - Linha Protheus - SIGAQIP - Help QPH215013 - Ensaio obrigatório sem medição](https://totvssuporte.zendesk.com/knowledge/editor/01HV1ESMRG31Q78AXFGNBVGDCS/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F360061646214)
