---
article_id: 5095503812375
category: Folha Mensal
content_hash: ffa83bfc2bdb0048f123cf0d524dcfdfa1361872a0f51d47c5c0280084e34d3c
fetched_at: '2026-06-28T22:46:59.228758+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Cálculo de Insalubridade
type: support-article
updated_at: '2025-01-20T21:49:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5095503812375-RH-RM-FOP-C%C3%A1lculo-de-Insalubridade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:30 min** **Dúvida**Como se faz o cálculo do adicional de insalubridade no sistema?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O sistema possibilita o cálculo de insalubridade através do [Código de Cálculo 22 - Insalubridade](https://tdn.totvs.com/pages/releaseview.action?pageId=452718304). Trata-se de um evento tipo Provento, sendo dia ou hora a depender de como os funcionários recebem. O percentual de incidência do evento deve ser igual a 10, e o valor informado para o evento deve ser o número que, multiplicado por 10, corresponderá ao percentual de insalubridade pago pela empresa.  
  
O cálculo se dá da seguinte forma:  
  
**- Tipo Hora**:  
  
((SAL. MIN. \* PORC. INC. INSAL.) / 100) \* (H/INF. NA INSAL. / No. H/MES) \* No. DE H/NOR.  
  
**- Tipo Dia**:  
  
(((SAL. MIN. / 30) \* POR INCID.) \* No. HORAS INF.) \* Número. HORAS NORMAIS  
  
Por exemplo, tenho o evento de insalubridade cadastrado como Provento e Dia, e percentual de incidência igual a 10, conforme explicado acima:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5095075989911/mceclip1.png)  
  
Adiciono o evento no Grupo de Eventos que desejo lançar para o funcionário com o valor 2, a fim de calcular 20% de insalubridade  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5095081682199/mceclip0.png)  
  
O funcionário deste exemplo tem salário de R$8.200,00, e o salário mínimo desta base é igual a R$1.212,00. Seu envelope fica da seguinte forma:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5095225149079/mceclip2.png)  
  
Por fim, para conferir o cálculo conforme a fórmula descrita acima, o log de cálculo demonstra:  
  
*Calculando evento: 0022 - INSALUBRIDADE*  
*Código de Cálculo 22 - Prioridade 1*  
  
*Horas trabalhadas no mês : 30,00 \* 1,0000 (%inc.) \* (220 (Jornada) / 30) = 220,00*  
*Salário Mínimo: 1212,0000*  
*Valor da Insalubridade: 1212,0000 (Salário Mínimo) / 30 \* 10,0000 (%inc.) / 100 \* 2,00 \* 220,00 (Horas Trab.) = 1.777,600000*  
*Valor do evento: 1.777,60***Importante**- As empresas que têm como rotina agregar o valor da Insalubridade ao salário para outros cálculos, como por exemplo Hora Extra, deverão marcar a opção **Incide em Salário** na aba **Inc. Proventos** do evento de Insalubridade;  
- O exemplo acima descreve o uso do código de cálculo 22 sem a necessidade de fórmulas. Portanto, é necessário que o funcionário tenha o evento de código de cálculo 1 - hora normal ou código de cálculo 2- dias trabalhados, e o evento de insalubridade deve ter prioridade maior. Fora este cenário, faz-se necessário operar o cálculo utilizando fórmula.
