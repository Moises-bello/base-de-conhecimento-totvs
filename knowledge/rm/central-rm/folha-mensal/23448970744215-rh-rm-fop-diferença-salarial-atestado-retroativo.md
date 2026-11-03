---
article_id: 23448970744215
category: Folha Mensal
content_hash: 09fbfbd0cef9cb2aa3c2179fb25697092bf3941578b493f8e60ab2adeae65dd2
fetched_at: '2026-06-28T22:46:58.153090+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Diferença Salarial - Atestado retroativo
type: support-article
updated_at: '2025-02-12T18:03:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23448970744215-RH-RM-FOP-Diferen%C3%A7a-Salarial-Atestado-retroativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23448925737623) Tempo aproximado para leitura: 00**:01:35 min** **Dúvida**Como será o lançamento de diferença Salarial quando houver atestado médico retroativo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento -

12.1.2402.117   
12.1.2310.182  
12.1.2306.240 e superiores  
  
**Solução**

Ao realizar o cálculo da diferença salarial quando há inclusão de atestado médico de forma retroativa, haverá o recálculo dos eventos de CC2 - DIAS TRABALHADOS e CC145 - ATESTADO MÉDICO, verificando a soma dos códigos de cálculo e subtraindo o valor calculado no envelope original.

Quando há inclusão de atestado médico sem incidência de INSS de forma retroativa, haverá o recálculo dos eventos de CC2 - DIAS TRABALHADOS e CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS, verificando a soma dos códigos de cálculo e a subtração do valor calculado do valor original.

**Importante**Quando houver lançamento retroativo de atestado médico com CC445 - ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS deverá primeiro existir o cálculo da retificação para ser feita a restituição do INSS descontado no envelope original antes do cálculo da diferença salarial.

Para obter informações adicionais e exemplos de utilização, por favor, [CLIQUE AQUI](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718616#1-3)  
  
**Saiba mais**

[RH - RM - FOP - Códigos de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo?source=search)
