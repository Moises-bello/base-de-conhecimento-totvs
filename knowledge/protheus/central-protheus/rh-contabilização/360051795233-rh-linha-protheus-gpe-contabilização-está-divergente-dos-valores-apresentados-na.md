---
article_id: 360051795233
category: RH - Contabilização
content_hash: 1f7b7609e6af280df40b49fc7117cc284463fe861682dab254f24f493f65e86f
fetched_at: '2026-06-28T22:43:46.108219+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização está divergente dos valores apresentados
  na tabela SRT
type: support-article
updated_at: '2021-06-07T13:37:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051795233-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-est%C3%A1-divergente-dos-valores-apresentados-na-tabela-SRT
---

**Dúvida**GPE - Contabilização está divergente dos valores apresentados na tabela SRT  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**1) Para conferir os valores de contabilização, será necessário utilizar o relatório de provisão.  
Os valores apresentados em tela , conforme print abaixo e consequentemente na tabela SRT são os valores acumulados da provisão e não a provisão do Mês (competência):  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079476514/mceclip0.png)  
  
2) Tabela SRT:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079476774/mceclip1.png)  
  
3) Acessar **Relatórios->**Provisões->Provisão de Férias/13º **ou**  
**Miscelânea ->**Provisão de Férias/13º -> Outras ações -> Imprimir férias/Imprimir 13º  
  
Tanto na provisão de férias, o valor apresentado na linha "No Mês", é o valor correto referente à provisão mensal e o valor que deverá ser apresentado no lançamento contábil:   
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080567433/mceclip3.png)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080569793/mceclip4.png)  
  
4) Acessar **Miscelânea-> Fechamentos -> Contabilização.**  
Após o processamento , verifique os lançamentos contábeis de acordo com o relatório:   
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080573273/mceclip6.png)
