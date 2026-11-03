---
article_id: 4413704495895
category: eSocial
content_hash: fcda29c46123bebabfee5477ef22c2673688d3dd0e9bf22bfb755740ebda21c9
fetched_at: '2026-06-28T22:47:39.122662+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - Evento S-2220: Erro na validação do campo ''dtAso'':Deve ser
  uma data válida'
type: support-article
updated_at: '2025-09-25T14:50:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413704495895-RH-RM-SMT-Evento-S-2220-Erro-na-valida%C3%A7%C3%A3o-do-campo-dtAso-Deve-ser-uma-data-v%C3%A1lida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035245336855) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao gerar o XML do evento S-2220 aparece a mensagem: Erro na validação do campo 'dtAso':Deve ser uma data válida, igual ou anterior à data atual e igual ou posterior à data de início da obrigatoriedade deste evento para o empregador no eSocial, o que fazer ?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM- Segurança e Saúde Ocupacional - 12.1.28 e superiores.  
  
**Solução**Serão considerados somente as consultas e exames realizados (Asos) realizados a partir da data de obrigatoriedade de envio dos eventos, conforme o cronograma do eSocial, exames anteriores a data não devem ser enviados ao eSocial. 

![](https://totvssuporte.zendesk.com/attachments/token/9JHT13OQ3PrFOrwhekViRJadK/?name=inline-56460573.png)

Por exemplo: Data de obrigatoriedade de envio dos eventos de SST do primeiro grupo é 13/10/2021. Assim a data de emissão do ASO deve ser após a data obrigatoriedade, como do dia 15/11/2021.   
  
Dessa forma acesse o menu **PCMSO** | **Prontuário Medico** e edite a consulta desejada e avalie o campo **'Data de emissão do ASO'**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35193484790935)

**Saiba Mais**

Para maiores informações, acesse: 

- [RH - RM - SMT - Gerar o evento S-2220 - Monitoramento da Saúde do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010325282)
