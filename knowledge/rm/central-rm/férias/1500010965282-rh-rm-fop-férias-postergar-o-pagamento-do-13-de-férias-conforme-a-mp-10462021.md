---
article_id: 1500010965282
category: Férias
content_hash: a8b67e8478ebfb695dfbd27075661da222372f08a9774d46d36f08fabaf5844d
fetched_at: '2026-06-28T22:46:56.406954+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Postergar o pagamento do 1/3 de férias conforme a
  MP 1.046/2021'
type: support-article
updated_at: '2024-10-18T15:39:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010965282-RH-RM-FOP-F%C3%A9rias-Postergar-o-pagamento-do-1-3-de-f%C3%A9rias-conforme-a-MP-1-046-2021
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:36 min  
  
Dúvida**Como pagar as férias sem o pagamento do adicional de férias (1/3) conforme Art. 7º da MP 1406  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Conforme a MP 1.046/2021, Art. 7º, o adicional de um terço relativo às férias concedidas durante o período a que se refere o art. 1º poderá ser pago após a sua concessão, a critério do empregador, até a data em que é devida a gratificação natalina prevista no [art. 1º da Lei nº 4.749, de 12 de agosto de 1965](http://www.planalto.gov.br/ccivil_03/leis/l4749.htm).  
  
Para atender a determinação do Art 7º, o Módulo TOTVS Folha de Pagamento disponibiliza o recurso de fórmulas que pode ser configurado pelo usuário para que não seja calculado 1/3 de férias caso seja opção do empregador:   
  
1. Deve-se criar a fórmula conforme o exemplo abaixo e vincular no evento de código de cálculo 40:

**Fórmula - Cálculo 1/3 de Férias**

|  |
| --- |
| `SE PROCESSO="FERIAS"`  `ENTAO 0`  `SENAO`  `VALORCODCALCULO(40)`  `FIMSE` |

![](https://tdn.totvs.com/download/attachments/615912658/image2020-3-24_19-6-1.png?version=1&modificationDate=1620303715220&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/615912658/image2021-5-6_9-26-58.png?version=1&modificationDate=1620304018660&api=v2)  
  
2. Criar uma fórmula para incluir um evento de base para armazenar o valor de 1/3 de férias que será pago posteriormente.

**Fórmula - Base 1/3 de Férias**

|  |
| --- |
| `SE PROCESSO="FERIAS"`  `ENTAO VALORCODCALCULO(40)`  `SENAO`  `0`  `FIMSE` |

![](https://tdn.totvs.com/download/attachments/615912658/image2021-5-6_9-30-25.png?version=1&modificationDate=1620304225427&api=v2)  
  
3. O evento pode ser incluído no parametrizador como evento adicional para ser lançado automaticamente no recibo de férias:

![](https://tdn.totvs.com/download/attachments/615912658/image2021-5-6_9-29-12.png?version=1&modificationDate=1620304152407&api=v2)

![](https://tdn.totvs.com/download/attachments/615912658/image2021-5-6_9-36-4.png?version=1&modificationDate=1620304564517&api=v2)  
  
4. Calculando as férias, no recibo de férias o evento de CC 40 não será lançado e o evento de Base será lançado com o valor correspondente:

![](https://tdn.totvs.com/download/attachments/615912658/image2021-5-6_9-31-56.png?version=1&modificationDate=1620304316727&api=v2)

5. lançar as férias, o evento de Base também será lançado no envelope de pagamento:

![](https://tdn.totvs.com/download/attachments/615912658/image2021-5-6_9-37-53.png?version=1&modificationDate=1620304673853&api=v2)

Saiba Mais em: [Pagamento de férias sem 1/3 para pagamento posterior conforme MP 1046](https://tdn.totvs.com/pages/releaseview.action?pageId=615912658)
