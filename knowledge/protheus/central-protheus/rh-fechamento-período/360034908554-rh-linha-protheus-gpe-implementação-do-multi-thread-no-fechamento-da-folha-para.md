---
article_id: 360034908554
category: RH - Fechamento Período
content_hash: 30d507a4e0ee76486333423169b35a5a3c93f09d58abf5ba7ff13b02096897d5
fetched_at: '2026-06-28T22:43:24.469553+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Implementação do Multi Thread no fechamento da
  folha para melhora no desempenho
type: support-article
updated_at: '2025-04-02T16:39:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034908554-RH-Linha-Protheus-GPE-Implementa%C3%A7%C3%A3o-do-Multi-Thread-no-fechamento-da-folha-para-melhora-no-desempenho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22407121696919) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Ao realizar o fechamento em uma base com muitos funcionários (acima de 300), para diminuir o tempo de processamento, qual configuração pode ser utilizada?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Foi realizado ajuste na implementação de *multi thread* no fechamento para que seja pré-definida a quantidade de threads que serão utilizadas na execução da rotina **GPEM120,** ou seja, passará a ser parametrizada a **quantidade** de ***threads*** que será utilizada e não a **quantidade** de **funcionários** por *thread* como era feito anteriormente através do parâmetro **MV\_RHQTFUN**.**Importante:**  
O parâmetro MV\_RHQTFUN deixará de ser utilizado. Em substituição ao mesmo, a rotina utilizará o parâmetro **MV\_CALCTHD**, cujo conteúdo é a **quantidade** de *threads* que será utilizada no processamento da rotina de fechamento;

* Anteriormente existia a limitação de 5 threads quando utilizado a rotina de cálculos múltiplos (GPEM020A) e fechamento mensal (GPEM120). Caso utilize binário a partir do lobo guará (será utilizada a quantidade de threads definida no parâmetro MV\_CALCTHD). Dessa forma, o número de threads poderá ser definido com base na infraestrutura disponível.
* Para **não utilizar** a implementação de *multi threads* no **fechamento** basta configurar o parâmetro com o conteúdo **0 ou 1**;
* A rotina só utilizará mais de uma *thread* caso a quantidade de funcionários que será processada for **maior que 300**;
* O parâmetro **MV\_CALCTHD** também é utilizado na rotina de **Cálculo Integrado (GPEM020A),** ou seja, a quantidade de *threads* configuradas será utilizada **nas duas rotinas;**
* Por **padrão** do **Sistema,** seu conteúdo original é =0.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22407060526999)**

**Saiba Mais:**

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
