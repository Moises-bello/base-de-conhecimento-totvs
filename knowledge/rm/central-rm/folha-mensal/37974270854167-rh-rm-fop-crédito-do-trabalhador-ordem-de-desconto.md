---
article_id: 37974270854167
category: Folha Mensal
content_hash: 8b1dd5c9afdac8bdc11d71fcdbc824b8f329c8299e155998616752ed8c3823fc
fetched_at: '2026-06-28T22:46:57.978019+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Ordem de desconto
type: support-article
updated_at: '2026-01-28T12:12:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37974270854167-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Ordem-de-desconto
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37974307322007) Tempo aproximado para leitura: 00:10:00 min  
  
**Dúvida**  
Qual é a ordem de que o RM adota para o desconto do empréstimo quando há mais de um crédito do Trabalhador para o funcionário?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento   
  
A partir dos patches:   
  
12.1.2406.287;

12.1.2410.258;

12.1.2502.160;

12.1.2506.105 e superiores  
  
**Solução**  
Para determinar a ordem o sistema adota 3 critérios de validação:  
  
1. Primeiro critério: Data do empréstimo

A primeira validação realizada pelo sistema considera a **data de contratação do empréstimo**.  
O empréstimo **contratado primeiro** (ou seja, com data de empréstimo mais antiga) terá **prioridade no desconto** em relação aos demais.

Em outras palavras, quanto **mais antiga a data do empréstimo**, maior será sua precedência no processamento da folha.

---

2. Segundo critério: Data de início do desconto

Caso dois ou mais empréstimos possuam a **mesma data de contratação**, o sistema passa para a segunda validação: a **data de início do desconto**.

Nessa etapa, o empréstimo cujo **desconto foi programado para iniciar primeiro** terá prioridade sobre os demais, independentemente do código do evento.

---

3. Terceiro critério: Código do empréstimo

Se, após as duas validações anteriores, ainda houver empate — ou seja, se os empréstimos possuírem **a mesma data de empréstimo e a mesma data de início do desconto** —, o sistema utiliza um critério final de desempate: o **código do empréstimo**.

Nesse caso, o empréstimo com o **menor código numérico** será descontado primeiro na folha de pagamento.

Exemplo 1 – Prioridade pela data de início do desconto:   
Foram cadastrados dois empréstimos para o colaborador, ambos com a **mesma data de empréstimo**:

* Empréstimo 1:

  + Evento **1480**
  + Data de início do desconto: **01/11/2025**
* Empréstimo 2:

  + Evento **2480**
  + Data de início do desconto: **01/10/2025**

Embora os dois empréstimos tenham sido contratados na mesma data, ao processar a folha de pagamento o sistema **desconta primeiro o evento 2480**, pois sua **data de início de desconto é anterior** à do evento 1480.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37974270831127)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37974307326103)

Veja que ambos possuam a mesma data do empréstimo, mas quando lançamos a Folha de pagamento o sistema lança primeiro o evento 2480, pois a sua data de inicio de desconto é menor que a data inicio do empréstimo com código de evento 1408.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37974270832919)

Exemplo 2:

No segundo cenário, a **data do empréstimo do evento 1480** foi alterada para ser **anterior** à data do empréstimo com código **001**.

Após essa alteração, ao processar a folha de pagamento, observa-se que a **ordem de desconto é invertida**, passando a ser descontado **primeiramente o evento 1480**, uma vez que agora ele possui a **data de contratação mais antiga**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37974307327767)

Exemplo 3:

Quando as **datas de empréstimo** e as **datas de início do desconto** dos empréstimos são exatamente iguais, o sistema aplica o critério final de desempate.

Nesse cenário, o sistema **prioriza o empréstimo com o menor código**, realizando o desconto primeiro para esse evento.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37974307329431)

Importante:

Em situações de **insuficiência de saldo**, essa ordem de prioridade torna-se ainda mais relevante, pois é ela que determina **quais empréstimos serão descontados integralmente e quais poderão sofrer desconto parcial ou não serem descontados** no período.

Por esse motivo, compreender a lógica de priorização é fundamental para a correta análise dos lançamentos em folha e para a validação dos valores processados.  
  
**SAIBA MAIS**  
  
[RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
