---
article_id: 360053930634
category: Férias
content_hash: 9ee2ed02d69b4e48ade0850684ea7d1b3ca858e2a4a183593531f9421388f074
fetched_at: '2026-06-28T22:46:56.446594+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RM - FOP - Como fazer pagamento do 1/3 de férias relacionado à MP927?
type: support-article
updated_at: '2021-07-01T22:07:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053930634-RM-FOP-Como-fazer-pagamento-do-1-3-de-f%C3%A9rias-relacionado-%C3%A0-MP927
---

**Dúvida**

Como fazer pagamento do 1/3 de férias relacionado a MP927?

**Ambiente**

RM – Folha de Pagamento – A partir da versão 12.1.24.  
  
**Solução**

Existem três situações para pagamento de 1/3 de férias, quando o mesmo não foi realizado ao gozar férias:

**Primeira situação:** Quando o funcionário não recebeu o pagamento de 1/3 de férias e o pagamento for através da folha normal, será necessário criar um evento de 1/3 de férias em folha, onde o mesmo terá incidências de INSS/FGTS/IRRF. Nesse evento, deve ser colocada a fórmula abaixo:

|  |
| --- |
| MV (0, '2020', 'B099') |

*(Obs: Usando a função MV, o sistema irá considerar o evento de Base de Cálculo lançado no envelope durante o ano de 2020. O código do evento "B099" na fórmula acima é apenas exemplo conforme [TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=544711845). O código deve ser substituído, se for o caso, pelo código de evento cadastrado em seu sistema)*![unnamed.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090719314/unnamed.png)  
  
*(Reforça-se, portanto, que o evento B099 foi o evento do tipo Base de Cálculo criado para lançar no envelope de pagamento no mês no qual o funcionário recebeu férias).*

Após o cadastro deste evento, ele pode ser lançado como Evento Adicional, Evento do Grupo no grupo de eventos da folha normal, ou ainda lançado manualmente no envelope.  
  
**Segunda situação:** A segunda situação é quando o funcionário recebeu adiantamento de férias proporcionais sem direito aos avos, não recebeu 1/3 da mesma e foi demitido.

Deverá acessar o link abaixo e realizar o procedimento, a partir desse processo, utilizando do passo 1 até o 3 do título **"Fórmula para adicional de férias antecipado que deve ser pago de forma proporcional"**

[MP 927 - Pagamento de 1/3 de Férias na Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=545249943)  
  
**Terceira situação:** A terceira situação é quando o funcionário recebeu adiantamento de férias vencidas e não recebeu 1/3 da mesma e foi demitido.

Deverá acessar o link abaixo e realizar o procedimento, a partir desse processo, utilizando do passo 1 até o 3 do título **Fórmula para adicional de férias antecipado que deve ser pago de forma indenizadas**

[MP 927 - Pagamento de 1/3 de Férias na Rescisão](https://tdn.totvs.com/pages/releaseview.action?pageId=545249943)  
  
É necessário reforçar que deverá ser criado um evento separado para 1/3 de férias proporcionais e 1/3 de férias vencidas.  
  
Concluindo: para atender a MP 927, de acordo com o exposto acima, serão 4 eventos a serem criados:

- O evento B099 (sendo o código B099 apenas um exemplo): Tipo Base de Cálculo, para lançar o valor de 1/3 de férias na ficha financeira do funcionário;  
  
- O evento que retornará o valor do B099 para pagamento de 1/3 na folha normal;  
  
- O evento que retornará o valor do B099 para pagamento de 1/3 de férias proporcionais na rescisão; (informar o código desse evento em eventos adicionais na pasta : Configurações | Parametrizador | Rescisão | Eventos adicionais);  
  
- O evento que retornará o valor do B099 para pagamento de 1/3 de férias indenizadas na rescisão. (informar o código desse evento em eventos adicionais na pasta : Configurações | Parametrizador | Rescisão | Eventos adicionais).
