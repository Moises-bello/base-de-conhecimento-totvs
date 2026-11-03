---
article_id: 360054152334
category: Configurações
content_hash: 469cc045c0fc10250011423c651b889bf0d402e47224b12d2ad90e693f40e43e
fetched_at: '2026-06-28T22:46:49.603389+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - Alteração da Data de Pagamento '
type: support-article
updated_at: '2025-03-13T10:02:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054152334-RH-RM-FOP-Altera%C3%A7%C3%A3o-da-Data-de-Pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao lançar a folha de pagamento, verificou que a data do pagamento estava incorreta. Dessa forma, como alterar a data de pagamento?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, segue abaixo orientações:  
  
1. Para realizar a alteração da data de pagamento, deverão ser realizados dois processos. Ambos os processos apresentados abaixo necessitam que a data de pagamento seja alterada no caminho: **Configurações | Locais | Dia de Pagamento.**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4446675088791/mceclip0.png)​  
  
2. Após alterar a data de pagamento, realize uma das opções abaixo:

* **1ª Opção:** A primeira opção de processo é a mais intuitiva. Será necessário cancelar o movimento do envelope dos funcionários através do caminho: **Folha Mensal | Cancelamento** e posteriormente lança-los novamente. Lembrando que, com os parâmetros locais alterados, o sistema passará a validar o novo Dia do Pagamento.
* **2ª Opção:** A segunda opção também demanda o cancelamento do movimento do envelope dos funcionários através do caminho: **Folha Mensal | Cancelamento.** Mas, neste caso é importante que, no final da rotina seja marcada opção **Gravar o Movimento Digitado.**

![](https://totvssuporte.zendesk.com/attachments/token/wO1DpTfqwvGE8vFFWsnyII2VV/?name=inline2109172482.png)​  
  
Feito isso, o sistema gerará um arquivo em *txt*, que nada mais é que um layout contendo todas as informações que estavam no envelope. Este arquivo deve ser importado em **Folha Mensal | Importação | Importação do Movimento**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4446711074839/mceclip1.png)  
  
Os eventos serão importados para o envelope dos funcionários, considerando a data informada na rotina. A alteração da data, neste caso, se dá ao preenchimento do campo **Informar data de pagamento**, conforme demonstrado na imagem abaixo.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093493133/mceclip0.png)  
  
Nesta segunda opção, os eventos do layout respeitarão a nova data, não se valendo da data original quando os eventos ainda estavam no envelope ou na data informada nos parâmetros locais demonstrados acima. No entanto, sugere-se que os parâmetros locais sejam alterados mesmo assim para o caso em que seja necessário lançar novos eventos no envelope.  
  
**Saiba Mais**[RH - RM - FOP - Cancelamento do Movimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057701274-RM-FOP-Cancelamento-do-movimento#:~:text=Como%20realizar%20o%20cancelamento%20do%20movimento%20dos%20funcion%C3%A1rios%3F&text=A%20movimenta%C3%A7%C3%A3o%20do%20funcion%C3%A1rio%20deve,os%20per%C3%ADodos%20de%20um%20m%C3%AAs.)  
[RH - RM - FOP - Importação do Movimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001485501-RH-RM-FOP-Importa%C3%A7%C3%A3o-do-Movimento#:~:text=Exemplo%3A%20Ao%20importar%20o%20movimento,onde%20o%20processo%20%C3%A9%20executado.&text=Neste%20caso%20tamb%C3%A9m%20tem%20que,transfere%20arquivo%20para%20o%20servidor.)
