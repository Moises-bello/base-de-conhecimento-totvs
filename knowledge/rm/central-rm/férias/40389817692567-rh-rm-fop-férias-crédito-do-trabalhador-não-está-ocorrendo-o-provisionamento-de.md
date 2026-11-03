---
article_id: 40389817692567
category: Férias
content_hash: c955704a6abef0168902ce2fb16a4d3b854c8bf307ce3d3e6f8344f1c752a0f0
fetched_at: '2026-06-28T22:46:56.099483+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Crédito do Trabalhador - Não está ocorrendo o provisionamento
  de férias'
type: support-article
updated_at: '2026-05-11T19:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40389817692567-RH-RM-FOP-F%C3%A9rias-Cr%C3%A9dito-do-Trabalhador-N%C3%A3o-est%C3%A1-ocorrendo-o-provisionamento-de-f%C3%A9rias
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40389794949783) Tempo aproximado para leitura: 00:15:00min  
  
**Dúvida**  
No calculo das férias não está ocorrendo o provisionamento de férias. Como resolver?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches: 12.1.2406.287; 12.1.2410.258; 12.1.2502.160; 12.1.2506.105 e superiores  
  
**Solução**  
Para este tipo de situação, recomenda-se realizar as seguintes validações para identificar a causa do problema relacionado ao provisionamento do Crédito do Trabalhador em férias:

### 1. Validar o cadastro do empréstimo

Acesse o caminho: **Funcionário | Anexos | Folha de Pagamento | Empréstimo**

O primeiro passo consiste em confirmar se o cadastro do empréstimo está corretamente preenchido:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40389794950935)

Inicialmente, é necessário identificar se o empréstimo em questão se trata de um **Crédito do Trabalhador**. Para isso, deve-se verificar o campo **Modalidade do Empréstimo**.

Além disso, os seguintes campos devem ser validados:

* **Data do Empréstimo** e **Início do Desconto**: ambos devem possuir datas anteriores à data de início das férias. Caso contrário, o provisionamento não será realizado.
* **Comp. Final Desc.**: a competência final do desconto deve ser posterior ao término das férias. Caso esteja configurada para encerrar no mês de início das férias, o provisionamento poderá ocorrer apenas no primeiro mês, pois no segundo mês o empréstimo já estará finalizado.
* **Valor da Parcela**: este campo deve estar preenchido com valor superior a zero, pois sem valor de parcela não haverá desconto.
* **Competência Atual**: deve corresponder ao mês das férias ou, no máximo, ao mês imediatamente anterior ao início das férias.
* **Observação:** Como um empréstimo pode ser quitado, renegociado ou sofrer alterações devido a multas e ajustes, o sistema não realiza o provisionamento quando a competência da parcela estiver dois ou mais meses anterior à competência de início das férias.
* Exemplo: se as férias iniciam em junho/2026 (06/2026) e a competência da parcela estiver em abril/2026 (04/2026) ou anterior, o provisionamento não será realizado, pois o Manual do Crédito do Trabalhador prevê que o provisionamento ocorra apenas com a parcela do mês imediatamente anterior.

Observação: Como um empréstimo pode ser quitado, renegociado ou ajustado com as multas, o provisionamento não vai ocorrer se a competência da parcela for 2 ou mais meses antes da competência de inicio destas férias.   
Por exemplo, se as férias iniciam em Junho (06/2026) e a competência da parcela é a 04/2026 ou inferior, o provisionamento não ocorrerá pois o Manual do Crédito prevê que o provisionamento possa ocorrer somente com a parcela do mês anterior.

2. Validar os parâmetros de Férias relacionados ao Crédito do Trabalhador

Acesse o caminho:

**Folha de Pagamento | Configuração | Parametrizador | Férias | Empréstimo**

Com o cadastro do empréstimo validado, é necessário conferir se os parâmetros relacionados ao Crédito do Trabalhador estão corretamente configurados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40389817672855)

#### 

* #### Lança provisionamento do empréstimo do Crédito do Trabalhador nas Férias

  Este parâmetro deve estar marcado para que o provisionamento seja realizado automaticamente nas férias, respeitando as regras de datas e competências.
* #### Período para lançar o provisionamento do empréstimo Crédito do Trabalhador nas férias

  Quando preenchido, este parâmetro separa o lançamento do provisionamento das férias. Sem essa configuração, o provisionamento ocorre no mesmo período em que as férias são lançadas. Quando preenchido, o lançamento será realizado separadamente no período informado.

  **Observação:** Recomenda-se utilizar o período da folha de pagamento, pois dessa forma o provisionamento será devolvido no mesmo período em que ocorrerá o desconto efetivo do evento 480.
* #### Lança Provisionamento no adiantamento e no Recibo de férias da mesma competência

  Caso já tenha ocorrido provisionamento no adiantamento ou no recibo de férias dentro da mesma competência, este parâmetro permite que o sistema realize novo provisionamento nas férias, independentemente de já ter ocorrido desconto anterior.

  **Importante:** Caso o parâmetro esteja desmarcado e o provisionamento não tenha ocorrido, um teste válido é marcá-lo e recalcular o recibo de férias para verificar se o provisionamento será realizado corretamente.

3. Validar se já houve lançamento do evento 480 na competência

Acesse novamente o cadastro do empréstimo e consulte o anexo de **Desconto**.

É necessário verificar se já houve o lançamento do evento **480** na competência atual.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40389794953495)

**Importante:** Caso já tenha ocorrido desconto na competência vigente, o sistema não realizará novo provisionamento, exceto em situações onde o desconto não deveria ter sido processado.

Nesses casos, deve-se verificar:

* Se o evento consta lançado no envelope, será necessário cancelar o movimento;
* Caso o evento não esteja no envelope, pode ter ocorrido o cancelamento da movimentação da folha sem a marcação da opção **Atualizar cadastro do Empréstimo**.

Quando isso acontece, será necessário acessar manualmente o anexo de desconto e remover o lançamento existente, permitindo que o desconto seja gerado automaticamente quando a folha do mês for processada novamente.

### 4. Validar Eventos Adicionais de Férias

O provisionamento do Crédito do Trabalhador deve ocorrer de forma automática pelo sistema.

Por esse motivo, se algum dos eventos relacionados ao Crédito do Trabalhador — seja o evento de desconto ou os códigos de cálculo do provisionamento — estiver configurado como **Evento Adicional de Férias**, poderão ocorrer falhas no desconto ou desrespeito às regras automáticas de validação.

Para essa conferência, acesse:

* **Folha de Pagamento | Configuração | Parametrizador | Férias | Eventos Adicionais Globais**

e também:

* **Período Aquisitivo | Anexos | Eventos Adicionais**

### 5. Validar possíveis conflitos de importação e competências

Como última possibilidade, pode haver algum conflito relacionado às datas das parcelas ou ao processo de importação das competências.

Nessa situação, recomenda-se realizar a reimportação do arquivo da competência atual e, após esse procedimento, efetuar um novo teste para validar se o provisionamento passará a ocorrer corretamente.

**Saiba Mais:**

[RH - RM - FOP - Férias - Provisionamento de Empréstimo: Férias Partidas com Finalização da Parcela na Competência Atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40337837448343-RH-RM-FOP-F%C3%A9rias-Provisionamento-de-Empr%C3%A9stimo-F%C3%A9rias-Partidas-com-Finaliza%C3%A7%C3%A3o-da-Parcela-na-Compet%C3%AAncia-Atual)

[RH - RM - FOP - Crédito do Trabalhador - Provisionamento de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32319832741527-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Provisionamento-de-F%C3%A9rias)
