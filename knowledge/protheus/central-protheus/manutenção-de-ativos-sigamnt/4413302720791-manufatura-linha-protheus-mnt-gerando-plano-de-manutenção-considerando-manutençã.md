---
article_id: 4413302720791
category: Manutenção de Ativos (SIGAMNT)
content_hash: 4c1c499d94372db1776277644ea4134f4eeef6ea743ec6a22198ee9b19ed24d0
fetched_at: '2026-06-28T22:42:34.072139+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Gerando plano de manutenção considerando
  manutenção atrasada
type: support-article
updated_at: '2022-03-10T11:30:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413302720791-Manufatura-Linha-Protheus-MNT-Gerando-plano-de-manuten%C3%A7%C3%A3o-considerando-manuten%C3%A7%C3%A3o-atrasada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:40 min****Dúvida**Como gerar **Plano de Manutenção** considerando **manutenções** atrasadas ou não, conforme campo **Conside Atr. - TI\_ATRASAD.**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**O campo **Conside Atr. - TI\_ATRASAD** na geração de **Plano de Manutenção ou Plano de Lubrificação - MNTA331**, irá indicar se o plano deverá considerar as manutenções atrasadas, podendo ser: **Sim** ou **Não**. Isto corresponde as **Manutenções** que devem ser feitas no período de abrangência do plano campos - **TI\_DATAINI**, **TI\_DATAFIM**.  
  
Basicamente o processo de planejamento realizado pelo Sistema é buscar todas as manutenções existente tabela **STF - Manutenções** com base dos filtros da rotina, indiferente do período de abrangência do **plano**. Posteriormente é gerado uma lista de manutenções a serem analisadas pelo plano e projetando a data da **Próxima manutenção** ou **Data Original**. Com base na **Data original** é utilizando o campo **Considera Atrasada**, que pode ser:  
  
**S - Sim**: o Sistema verifica as manutenções anteriores ao campo **Data Início - TI\_DATAINI**para gerar as ordens de serviço no período do plano para as manutenções em atraso, caso existam. Neste caso a **Data original** será a projetada e a data prevista início será a data dentro do período do plano.  
**N - Não**: o Sistema ignora as manutenções em atraso, ou seja, projetando as manutenções e gera **O.S**. apenas as que tiverem sua data original **dentro do período do plano**.  
  
A **data prevista início** poderá ser alterada em função do calendário da manutenção e conforme definido no campo **Dia Não Útil** - **TF\_NAOUTIL**.  
  
**Exemplo quando considera atrasada igual a Sim**:   
Plano trimestral: abril, maio e junho para um determinado ano considerando que o mês atual seja abril. Vamos considerar os dados do bem conforme abaixo:

| Bem | **ABC1234** |
| --- | --- |
| **Incremento da manutenção** | 1 mês |
| **Data da Última Manutenção** | 08 de Janeiro |

|  |  |  |  |
| --- | --- | --- | --- |
| **Projeção da manutenção** | | | |
| Datas | Abril | Maio | Junho |
| **Original** | 08/02 | 08/04 | 08/05 |
| **Prevista Início** | 01/04 | 01/05 | 01/06 |

**Exemplo quando considera atrasada igual a Não**:   
Plano trimestral: abril, maio e junho para um determinado ano considerando que o mês atual seja abril. Vamos considerar os dados do bem conforme abaixo:

| Bem | **ABC1234** |
| --- | --- |
| **Incremento da manutenção** | 1 mês |
| **Data da Última Manutenção** | 08 de Janeiro |

|  |  |  |  |
| --- | --- | --- | --- |
| **Projeção da manutenção** | | | |
| Datas | Abril | Maio | Junho |
| **Original** | 08/04 | 08/05 | 08/06 |
| **Prevista Início** | 08/04 | 08/05 | 08/06 |

**Importante**A **data prevista início** poderá ser alterada em função do **calendário da manutenção**, **Dia útil**, e conforme definido no cadastro.  
  
**Saiba mais**  
Para entender melhor este processo, é necessário conhecer o conceito de **Datas na Ordem de Serviço**, principalmente **Data Original** da **Ordem de Serviço**, conforme descrito no artigo: [Manufatura - Linha Protheus - MNT - Composição das datas da ordem de serviço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004649001)
