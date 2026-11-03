---
article_id: 4414029760023
category: SIGAEST - CUSTOS
content_hash: e5fa56c0b381802d974ccb7bc4e39a241f628a04e5eee616497cd4cf0e2306e8
fetched_at: '2026-06-28T22:39:02.213693+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Qual o significado
  da Pergunta "% de Aumento da MOD"?
type: support-article
updated_at: '2023-11-16T19:16:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414029760023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Qual-o-significado-da-Pergunta-de-Aumento-da-MOD
---

**Dúvida**Qual o conceito, e validação para utilização do pergunte **% de Aumento da MOD?** na rotina MATA330?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O pergunte "**% de Aumento da MOD?" (.MTA33005.)** vai valorizar o custo do seu produto MOD**,** de acordo com o valor preenchido, após recalculo do custo médio, por padrão é configurado como 50, mas vai de acordo com a necessidade do usuário.  
  
Um exemplo: você possui um produto PA e um produto MOD+CC (mod com centro de custo) no cadastro de uma estrutura.  
  
Ao efetuar a criação de uma OP, e apontar a mesma, após recalculo do custo médio, para que seja calculado o custo do produto MOD de acordo as configurações de calculo com "integração contábil", sua MOD vai ser valorizada.  
  
Note no seguinte exemplo abaixo, o valor do centro de custo do produto MOD utilizado é de **3135.**

Ao efetuar o apontamento da produção, e recalculo do custo médio:

Sem percentual: 2 \* 3135 = 6270  
![](https://totvssuporte.zendesk.com/attachments/token/YLhI7TzzDDhZlBdg6oSJTZFSt/?name=inline-208440402.png)​  
  
Com percentual de 50%, no caso: 3135 + 50% = 4.702,5  
2 \* 4.702,5 = 9.405  
![](https://totvssuporte.zendesk.com/attachments/token/qnF8M0zaf9J3Zc8Cu8IlIqdiV/?name=inline-47685169.png)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Processo de configuração de MOD e GGF com e sem integração contábil*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-configura%C3%A7%C3%A3o-de-MOD-e-GGF-com-e-sem-integra%C3%A7%C3%A3o-cont%C3%A1bil)

*[MP - SIGAEST - Como fazer uma análise de Custos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
