---
article_id: 6296851624727
category: Folha Mensal
content_hash: 16085a10bab08c3c43e8c0c06456daebfcf7a3c4534af4e944e57611ca21e4b6
fetched_at: '2026-06-28T22:46:59.173820+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Como excluir adiantamento salarial
type: support-article
updated_at: '2025-01-20T14:23:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6296851624727-RH-RM-FOP-Como-excluir-adiantamento-salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Dúvida**  
Como realizar a exclusão do lançamento de adiantamento salarial?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6296323847959/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
**01.** Acesse **Folha Mensal - Cancelamento;**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6296321320855/mceclip1.png)  
  
**02.** Realize os filtros;  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6296393087895/mceclip2.png)

* **Seleção de Funcionários:** O cancelamento pode ser coletivo, não selecionando chapa de funcionário ou poderá fazer de forma individual selecionando a chapa de um funcionário. No exemplo abaixo, a seleção de funcionários não tem chapa ou filtro atribuído, e todos os tipos, situação e recebimento estão confirmados, ou seja, a rotina será global.
* **Quebra de Seção:** Informe a quebra desejada.
* **Cancela Movimento:** No momento da seleção do período haverá a possibilidade de cancelar a movimentação do período atual ou cancela todos os períodos. Selecionando a primeira opção, serão cancelados todos os eventos de um determinado período.
* **Cancela verbas com Insuficiência de Saldo:**Marque este parâmetro para realizar o cancelamento dos eventos com insuficiência de saldo para os funcionários que utilizam o campo **Controle de Saldo de Verbas** no cadastro de funcionários.
* **Incrementa Códigos Fixos:**Quando há o lançamento de um código fixo cadastrado no funcionário o número de vezes para lançamento é decrementado. Utilizar o parâmetro para incrementar o número de vezes do Código Fixo do funcionário quando se realiza o cancelamento, sendo que, somente será incrementado o número de vezes quando este for diferente de 999.
* **Cancela Movimentação por Centro de Custo** e **Todos os Centros de Custos:** Cancelam todos os centros de custo, inclusive os editados manualmente dentro da ficha financeira. O campo **Cancela Movimentação por Centro de Custo** somente cancela um centro de custo, quando editado manualmente, ficando inconsistente com o envelope de pagamento, já que existem centros de custos que não foram cancelados na ficha financeira, e o evento no envelope existe apenas com os centros de custos restantes, isto é, que ainda não foram cancelados. Se não estiver editado, o cancelamento por apenas um centro de custo cancelará todos os centros de custos existentes.  
    
  ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6296502201111/mceclip3.png)
* **Seleção de eventos a cancelar:**Nesta pasta, terá a opção de cancelar eventos isolados, ou poderá cancelar todo o movimento marcando a flag **Cancela todos os eventos.** Deixando marcada essa opção, todos os eventos do envelope serão cancelados, caso tenha outras movimentações e não deseje cancelar, faça a seleção dos eventos.
* **Grava movimento digitado:**Ao final da rotina para que a movimentação cancelada seja preservada em um arquivo que respeita o layout de importação de movimento. Caso seja necessário reimportar o movimento, basta utilizar a rotina **Folha Mensal | Importação | Importação do Movimento**.  
    
  ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6296571786647/mceclip4.png)  
    
  **Saiba mais**  
  [RH - RM - FOP - Cancelamento do Movimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057701274-RH-RM-FOP-Cancelamento-do-Movimento)  
  [RH - RM - FOP - Adiantamento Salarial](https://totvssuporte.zendesk.com/knowledge/articles/4420403003287/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F4420403003287)
