---
article_id: 360057701274
category: Folha Mensal
content_hash: b9ff8d40ed6cb483cc88d80dae7d1f37cf6ae596f1c80a77c4f1607d13cd590c
fetched_at: '2026-06-28T22:46:59.490392+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Cancelamento do Movimento
type: support-article
updated_at: '2025-01-20T14:29:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057701274-RH-RM-FOP-Cancelamento-do-Movimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como realizar o cancelamento dos valores do envelope de pagamento dos funcionários?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A movimentação do funcionário deve ser lançada mensalmente no envelope de pagamento, e neste caso, deve existir a possibilidade de cancelar um ou vários eventos lançados, ou seja, toda a movimentação do último período ou de todos os períodos de um mês. A seguir, estão descritas as principais funções da rotina de cancelamento.  
  
Primeiramente, acesse: **Folha mensal | Cancelamento,** crie um perfil de parâmetros e parametrizo o de acordo com necessidade da empresa.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097866674/mceclip3.png)  
  
![mceclip2.png](https://totvssuporte.zendesk.com/hc/article_attachments/360100132173/mceclip2.png)  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097867194/mceclip8.png)

* **Seleção de Funcionários:** O cancelamento pode ser coletivo, não selecionando chapa de funcionário ou poderá fazer de forma individual selecionando a chapa de um funcionário. No exemplo abaixo, a seleção de funcionários não tem chapa ou filtro atribuído, e todos os tipos, situação e recebimento estão confirmados, ou seja, a rotina será global.
* **Quebra de Seção:** Informe a quebra desejada.
* **Cancela Movimento:** No momento da seleção do período haverá a possibilidade de cancelar a movimentação do período atual ou cancela todos os períodos. Selecionando a primeira opção, serão cancelados todos os eventos de um determinado período.
* **Cancela verbas com Insuficiência de Saldo:** Marque este parâmetro para realizar o cancelamento dos eventos com insuficiência de saldo para os funcionários que utilizam o campo **Controle de Saldo de Verbas** no cadastro de funcionários.
* **Incrementa Códigos Fixos:** Quando há o lançamento de um código fixo cadastrado no funcionário o número de vezes para lançamento é decrementado. Utilizar o parâmetro para incrementar o número de vezes do Código Fixo do funcionário quando se realiza o cancelamento, sendo que, somente será incrementado o número de vezes quando este for diferente de 999.
* **Cancela Movimentação por Centro de Custo** e **Todos os Centros de Custos:** Cancelam todos os centros de custo, inclusive os editados manualmente dentro da ficha financeira. O campo **Cancela Movimentação por Centro de Custo** somente cancela um centro de custo, quando editado manualmente, ficando inconsistente com o envelope de pagamento, já que existem centros de custos que não foram cancelados na ficha financeira, e o evento no envelope existe apenas com os centros de custos restantes, isto é, que ainda não foram cancelados. Se não estiver editado, o cancelamento por apenas um centro de custo cancelará todos os centros de custos existentes.
* **Competência da Retificação:** No caso de cancelar o período em que foi lançada uma retificação de desligamento, deve ser marcado o parâmetro Retificação folha/rescisão e informar a competência e o período que se quer cancelar.
* **Seleção de eventos a cancelar:** Nesta pasta, terá a opção de cancelar eventos isolados, ou poderá cancelar todo o movimento marcando a flag **Cancela todos os eventos**.
* **Grava movimento digitado:** Ao final da rotina para que a movimentação cancelada seja preservada em um arquivo que respeita o layout de importação de movimento. Caso seja necessário reimportar o movimento, basta utilizar a rotina **Folha Mensal | Importação | Importação do Movimento**.

**Saiba Mais**  
[RH - RM - FOP - Importação do Movimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001485501-RH-RM-FOP-Importa%C3%A7%C3%A3o-do-Movimento#:~:text=Exemplo%3A%20Ao%20importar%20o%20movimento,onde%20o%20processo%20%C3%A9%20executado.&text=Neste%20caso%20tamb%C3%A9m%20tem%20que,transfere%20arquivo%20para%20o%20servidor.)
