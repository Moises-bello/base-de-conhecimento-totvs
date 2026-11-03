---
content_hash: 247e2ad38a300a7ef99ce65ec144e52afeacfa3d2f307bbf82e1ecd0be6a9a46
fetched_at: '2026-06-29T00:11:56.668788+00:00'
page_id: '868222489'
product: rm
source: tdn-rm
title: DT - Rescisão - Restituição de INSS/IRRF 13 Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=868222489
version: 17
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo da rescisão |
| País: | Brasil |
| Tickets | [10487880](https://totvssuporte.zendesk.com/agent/tickets/10487880 "View ticket on the Zendesk portal"); [11411010](https://totvssuporte.zendesk.com/agent/tickets/11411010 "View ticket on the Zendesk portal"); [13059367](https://totvssuporte.zendesk.com/agent/tickets/13059367 "View ticket on the Zendesk portal"); [13143952](https://totvssuporte.zendesk.com/agent/tickets/13143952 "View ticket on the Zendesk portal"); [13236281](https://totvssuporte.zendesk.com/agent/tickets/13236281 "View ticket on the Zendesk portal"); [13238189](https://totvssuporte.zendesk.com/agent/tickets/13238189 "View ticket on the Zendesk portal"); [13213338](https://totvssuporte.zendesk.com/agent/tickets/13213338 "View ticket on the Zendesk portal"); [13259708](https://totvssuporte.zendesk.com/agent/tickets/13259708 "View ticket on the Zendesk portal"); [13294355](https://totvssuporte.zendesk.com/agent/tickets/13294355 "View ticket on the Zendesk portal"); [13306219](https://totvssuporte.zendesk.com/agent/tickets/13306219 "View ticket on the Zendesk portal"); [13450879](https://totvssuporte.zendesk.com/agent/tickets/13450879 "View ticket on the Zendesk portal"); [13455421](https://totvssuporte.zendesk.com/agent/tickets/13455421 "View ticket on the Zendesk portal"); [13524052](https://totvssuporte.zendesk.com/agent/tickets/13524052 "View ticket on the Zendesk portal"); [10592899](https://totvssuporte.zendesk.com/agent/tickets/10592899 "View ticket on the Zendesk portal"); [10568224](https://totvssuporte.zendesk.com/agent/tickets/10568224 "View ticket on the Zendesk portal"); [10683676](https://totvssuporte.zendesk.com/agent/tickets/10683676 "View ticket on the Zendesk portal"); [13546178](https://totvssuporte.zendesk.com/agent/tickets/13546178 "View ticket on the Zendesk portal") |
| Issue: | [DRHCALCRM-5582](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5582); [DRHCALCRM-154](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-154) |

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2402.238
* 12.1.2406.172
* 12.1.2410.107
* 12.1.2502 e Superiores

## **02. SITUAÇÃO/REQUISITO**

Quando o funcionário é demitido na primeira quinzena de Dezembro e já houve o cálculo da 2º parcela de 13º Salário integral, o sistema está gerando um valor de restituição de INSS/IRRF na rescisão referente ao 13º Salário. Isto ocorre, porque na rescisão é considerado um avo a menos de 13º Salário devido a data de desligamento ser antes do dia 15/12. Com isto, ao enviar o S-2299 é retornando erro, pois no e-Social não é permitido enviar uma rubrica de restituição de INSS/IRRF com valor maior que o desconto de INSS/IRRF e neste cenário não é lançado valores de desconto de INSS/IRRF de 13º na rescisão pois o mesmo não é devido. Para contornar a situação, o usuário tem que fazer alterações manuais na Ficha Financeira, inserindo os valores de restituição no período de cálculo de 13º Salário e recalcular a rescisão em seguida.

## **03. SOLUÇÃO**

Foi adequado no cálculo da rescisão para que gere o período 10000 com os valores de restituição de INSS/IRRF para que o mesmo não fosse gerado na rescisão e assim o usuário conseguir integrar os eventos S-1200 e S-2299 sem erros no eSocial.

Para que o cálculo ocorra conforme o esperado foi criado o um parâmetro global “Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão” em [13º salário - Rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719912)para gerar retificação de 13º Salário quando existir restituição de IR e INSS na rescisão referente ao 13º salário. 

Foram criados também quatro códigos de cálculo novos que devem ser cadastrados previamente conforme orientado na documentação:

* [Código de Cálculo 473 - Pagamento da Restituição de INSS 13º Retificado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873209051)
* [Código de Cálculo 474 - Estorno na Base de INSS 13º Retificado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873209115)
* [Código de Cálculo 475 - Pagamento da Restituição de IRRF 13º Retificado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873209187)
* [Código de Cálculo 476 - Estorno na Base de IRRF 13º Retificado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873209231)

Assim, quando existir restituição, o sistema:

* Criará o período de retificação (10000) com os valores restituídos e dois eventos de base de cálculo da diferença encontrada entre o valor calculado para 13º na rescisão e o desconto de 13º adiantado.
* Serão lançados também dois eventos de pagamento no período de cálculo da rescisão com os valores de restituição de INSS 13º e IRRF 13º como provento Estes eventos não devem ter incidência.
* No período retificado será  lançando o evento com o código de cálculo 383 - Líquido retificação para zerar o período 10000

IMPORTANTE

[FAQ - Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873208316)

## **04. DEMAIS INFORMAÇÕES**

* O período retificado (10000) é vinculado na tabela PFRETIFICACAOPERIODO no campo PERIODOORIGEMRETIF ao período do 13º Salário e a data de pagamento será a mesma do 13º Salário.
* Para que ocorra o correto envio dos valores restituídos no eSocial é necessário que a base esteja parametrizada para [Unificar período na retificação](https://tdn.totvs.com/pages/viewpage.action?pageId=811714715)
* Para identificar qual período é de pagamento de 13º Salário, será verificado a existência de evento de código de cálculo 102 - 2ª parcela de 13º salário.
* Caso o parâmetro esteja desmarcado ou o cálculo não encontre período de pagamento de 13º Salário, ou seja, não encontre o evento com  código de cálculo 102 - 2ª parcela de 13º salário, então será lançado os valores de restituição como ocorre atualmente na rescisão e irá retornar a mensagem: ”O sistema identificou restituição de INSS e/ou IRRF para o funcionário de chapa XXXXX. Porém, para o eSocial não é permitido ter restituição em período onde não consta o desconto com valor igual ou superior.  
  Para criar um período de Retificação com os valores restituídos é necessário marcar o parâmetro "Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão", no Parametrizador, aba Rescisão/13º Salário.”
* Não iremos fazer a retificação automática em casos de pagamento do 13º Salário integral (código de cálculo 102 - 2ª parcela de 13º salário) antes de Dezembro. Neste caso, como isto geralmente é customizado pelo usuário, o tratamento também deve ser customizado caso não queira lançar restituição na rescisão.  Em competências diferentes de dezembro seguirá o comportamento atual.

## **05. ASSUNTOS RELACIONADOS**

* [13º salário - Rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719912)
* [FAQ - Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873208316)
* [Código de Cálculo 473 - Pagamento da Restituição de INSS 13º Retificado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873209051)
* [Código de Cálculo 474 - Estorno na Base de INSS 13º Retificado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873209115)
* [Código de Cálculo 475 - Pagamento da Restituição de IRRF 13º Retificado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873209187)
* [Código de Cálculo 476 - Estorno na Base de IRRF 13º Retificado](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873209231)
* [FAQ - Quando ocorrer uma rescisão após o pagamento da 2ª parcela e o valor do 13º Salário lançado em rescisão é menor do que o pago em 2ª parcela, gerando uma restituição de inss 13º, como proceder?](https://tdn.totvs.com/pages/viewpage.action?pageId=654942683)
