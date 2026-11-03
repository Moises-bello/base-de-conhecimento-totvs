---
article_id: 13972932615063
category: RH - Provisão
content_hash: c54213455ff93f85f596ecf8d85153892e0925595fa32bac50e89f5f609936ad
fetched_at: '2026-06-28T22:43:56.815209+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de Médias pela Rotina de Provisão
type: support-article
updated_at: '2026-05-18T14:01:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13972932615063-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-M%C3%A9dias-pela-Rotina-de-Provis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21536779820567) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como emitir o Relatório de Médias para conferência dos valores de Adicionais de Férias e 13 Salário nas Provisões?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - À partir do release 12.1.27  
  
**Solução**  
Para facilitar na conferência dos valores de Adicionais nos cálculos de Provisão de Férias e 13º Salário, emita o relatório de Médias pela rotina de Provisão.  
  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse: Miscelânea / Provisões / Provisões Férias e 13º (GPEA070), Selecione o funcionário e o mês que está realizando a conferência e Clique em Visualizar e em seguida em Médias:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13972025774615)  
  
2. Será emitido um relatório de Médias com os valores calculados de Adicionais de Provisão de férias e 13º Salário na competência selecionada.

- A Primeira página do relatório apresentará todos os fontes, parâmetros e mnemônicos utilizados no cálculo das médias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13972167451543)

**Importante:** O Mnemônico P\_MEDDIREN define como será calculada a média de pagamento, que será aplicada tanto nos pagamentos de Férias, 13º Saláro e Rescisão, quanto na apuração das médias dos cálculos de provisão.

Para mais informações sobre o Mnemônico P\_MEDDIREN [Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=224112471) .

- Nas próximas páginas são apresentados os relatórios de Médias de Férias e 13º Salário.  
Observe que no cabeçalho do relatório de médias são destacados os Adicionais que o funcionário tem direito e o salário incorporado do funcionário.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13972390509975) 

3. Acesse: Relatórios / Provisões / Provisões de Férias (GPER070) , e preencha os parâmetros para emissão do relatório de provisão:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13972634942487)  
Neste exemplo, onde o funcionário tem Adicional de Insalubridade, este adicional deve ser proprocionalizado pelos dias de direito de Férias e somado ao valor de Média de Pagamento.

Insalubridade: 1.200 / 30 x 15 = 600  
Média de Pagamento: 291,10  
Adicional de Provisão de Férias Proporcionais: 600 + 291,10 = **891,10**A mesma regra é aplicada para conferência dos Adicionais de Provisão de 13º Salário. 

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
