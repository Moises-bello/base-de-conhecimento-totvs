---
article_id: 14469408055191
category: Encargos
content_hash: 114cef02791bb7ca50e705d329aae1a019542ed38a5e55066fd591e5920dd0c7
fetched_at: '2026-06-28T22:46:52.347332+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP -  Geração do encargo TIPO 2 Base: incidência de FGTS'
type: support-article
updated_at: '2024-10-09T20:15:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14469408055191-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-encargo-TIPO-2-Base-incid%C3%AAncia-de-FGTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como gerar o encargo TIPO 2 Base: incidência de FGTS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para o cadastro do encargo deve-se observar que o campo código **alfanumérico - limite: 4 posições**, que deve ser único e Descrição **limite: 40 posições.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14468894312087)

O tipo de encargo deverá constar na tabela dinâmica **INT01**. Os tipos de encargos 2 é padrão do sistema:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14469002662551)

O Encargo Contábil com informação de rateio que o encargo segue, não seguirá o Rateio Fixo definido no cadastro de funcionários e SIM, seguirá ocorrência dos eventos que foram cadastrados no Rateio por Evento para que ele seja calculado. Ele só seguirá o Rateio Fixo definido no cadastro de funcionários, se os eventos cadastrados no Rateio por Evento não existirem na movimentação do funcionário. O código do rateio é definido no cadastro de Rateio de Eventos.  
   
Preenchendo o campo **Rateio que o Encargo segue** será obrigatório preencher também o **Período para Cálculo de Rateio** com um dos os seguintes períodos:  
  
**1 – Mês Atual -** Rateia conforme os rateios fixos informados no cadastro do funcionário.  
**2 – Período Aquisitivo –** Rateia conforme os rateios realizados durante o período aquisitivo de Férias.  
**3 – Ano de Competência –** Rateia conforme os rateios realizados durante o ano de competência atual.  
**4 - Mês Anterior –** Rateia de acordo com o rateio por centro de custo utilizado no mês anterior, tomando como base, a ficha financeira por centro de curto. Quando essa movimentação não existir o sistema deverá buscar o centro de custo do **Rateio Fixo** do funcionário.

O parâmetro **Aplicar arredondamento sobre o valor total do encargo** será utilizado quando o cálculo do encargo para cada funcionário é realizado sem arredondamento então, somente ao gerar o lançamento contábil será aplicado o arredondamento sobre a soma dos valores individuais de cada funcionário.  
Dessa forma, a diferença entre a soma dos valores dos funcionários e do valor final arredondado geral do lançamento é apurada. Essa diferença é adicionada tanto ao lançamento contábil quanto no histórico de encargos.  
Este parâmetro garante, por exemplo, que os valores gerados na GPS sejam idênticos àqueles gerados na contabilização, desde que as quebras entre os lançamentos contábeis sejam os mesmos da Guia de INSS.  
   
**Importante:**  
O parâmetro **Arredonda FGTS conforme SEFIP** nos parâmetros de cálculo do RM Labore, interfere nos cálculos de arredondamento dos encargos de FGTS. O parâmetro **Arredonda FGTS conforme SEFIP** marcado têm prioridade sobre o parâmetro **Aplicar arredondamento sobre o valor total do encargo**, também marcado, durante a contabilização. Os tipos de encargos afetados são:  
2 - Base: incidência de FGTS  
5 - Provisão de FGTS de férias  
8 - Provisão de FGTS de 13o. salário  
M - Base: incidência de FGTS de 13o. salário

Verificar o código ativo associado ao encargo para no momento da geração do encargo selecionar o mesmo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14469084734999)

O calculo é a base de FGTS da competência informada multiplicado pelo percentual do cadastro do encargo/ 100:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14469296840215)

Log da geração do encargo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14469243029015)

**Saiba mais**  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
