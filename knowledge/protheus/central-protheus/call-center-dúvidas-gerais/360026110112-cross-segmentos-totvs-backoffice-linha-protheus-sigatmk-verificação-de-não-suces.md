---
article_id: 360026110112
category: Call Center - Dúvidas Gerais
content_hash: 0df0dcc0811e4c5637993070fe6ead84a3ea460655acf39bce776fb20e437b63
fetched_at: '2026-06-28T22:41:26.809299+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - Verificação de
  não sucesso de ligação via agenda do operador
type: support-article
updated_at: '2022-06-17T14:59:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026110112-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Verifica%C3%A7%C3%A3o-de-n%C3%A3o-sucesso-de-liga%C3%A7%C3%A3o-via-agenda-do-operador
---

**Dúvida**

Quando o operador tenta entrar em contato com o cliente e não é obtido o sucesso na ligação exite algumas opções para o operador informar qual foi o motivo do não sucesso da ligação, neste ponto, existe algum relatório que contenha a tentativa de contato do operador com os motivos que foram informados?

**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - todas as versões.  
  
**Solução**Não há um relatório que traga o motivo pelo o qual a ligação não foi atendida, quando acessado a agenda do operador (**TMKA380**),pois, as informações do Status da Discagem, são gravadas  em um tabela de histórico, **SU8**, porém, o relatório mais próximo que pode ser verificado é o **TMKR025** - Ligações Realizadas.

Neste relatório é apresentado as ligações que foram realizadas e informa qual será a data e hora para um contato de retorno ao cliente, esses contatos podem ser comparados comas pendências existentes na agenda do operador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025538531/mceclip0.png)

Uma opção é utilizar a consulta genérica relacional das tabelas SU6 e SU8, onde será mostrado o atendimento que tentou o contato com o cliente, a data e o horário de ligação, e qual foi o motivo de não conseguir contato com o cliente.

![Consulta_su6_x_su8.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360025553252/Consulta_su6_x_su8.gif)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025552452/mceclip1.png)
