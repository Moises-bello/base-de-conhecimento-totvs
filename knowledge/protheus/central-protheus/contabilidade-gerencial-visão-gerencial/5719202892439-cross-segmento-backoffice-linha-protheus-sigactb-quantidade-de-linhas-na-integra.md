---
article_id: 5719202892439
category: Contabilidade Gerencial - Visão Gerencial
content_hash: 5af32d3e75f9340bd862a750b20eaaa602a1dc934bf36826653dd82d6f359fb3
fetched_at: '2026-06-28T22:40:50.633167+00:00'
product: protheus
section_id: 1500001548642
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Quantidade de Linhas
  na integração de lançamentos contábeis do RM para o Protheus
type: support-article
updated_at: '2022-05-09T15:54:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5719202892439-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Quantidade-de-Linhas-na-integra%C3%A7%C3%A3o-de-lan%C3%A7amentos-cont%C3%A1beis-do-RM-para-o-Protheus
---

**Ocorrência**Quando o RM envia os lançamentos contábeis ao Protheus, no arquivo XML não contém todas as linhas do documento contábil.  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - SIGACTB - Todas as versões  
  
**Solução**Para esses casos é possível definir no RM a quantidade de partidas conforme o desejado na integração contábil:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5718398422423/mceclip0.png)

A documentação de referência, onde pode verificar esse e outros parâmetros da integração entre o RM e Protheus é a <https://tdn.totvs.com/display/public/INT/Manual_Doc_Integracao_RMLabore_BackOfficeProtheus>

Lembrando que dentro do Protheus os parâmetros **MV\_NUMLIN e MV\_NUMMAN** precisam estar configurados para receber a quantidade de lançamentos definidas no RM, por isso precisam conter um valor maior.

Ex: No RM coloquei para gerar até 999 lançamentos, assim os parâmetros precisam estar iguais a 999 ou mais.

Segue a documentação dos parâmetros: [MP - SIGACTB - MV\_NUMLIN MV\_NUMMAN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006753632-MP-SIGACTB-MV-NUMLIN-MV-NUMMAN?source=search)
