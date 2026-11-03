---
content_hash: 6dd8e5da4fb4a04120dff269495034bc0635e2d87aeefec22a5bdcee6f381ec9
fetched_at: '2026-06-29T00:10:13.908547+00:00'
page_id: '458769352'
product: rm
source: tdn-rm
title: Para que serve o código de cálculo 398 - Base de Abono Férias Envelope?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458769352
version: 89
---

Quando o evento de Abono de Férias NÃO incidia IRRF Férias, ocorria duplicidade de valores no evento S-5002, isso acontecia devido o recibo de férias e o envelope de pagamento utilizarem os mesmos eventos de abono. Com isso ao gerar o evento S-1210 as verbas eram levadas em duplicidade, pois as verbas eram enviada no S-1210 (tipo de pagamento **7-Recibo de férias)**e também no S-1200, fazendo com que a incidência de IRRF de Abono (****75-IRRF de Abono)****ficasse duplicada no eSocial.

Para tratar essa situação foi implementado o código de cálculo **[398-Base de Abono Férias Envelope](http://tdn.totvs.com.br/pages/viewpage.action?pageId=463821314)****.**

**O usuário deverá:**

* + Recalcular o movimento para que o sistema crie o novo código de cálculo na tabela dinâmica (**398-Base de Abono Férias Envelope****).**  
    **Obs.:** Esse recalculo poderá ser apenas para um funcionário.
  + Cadastrar um evento com código de cálculo **[398-Base de Abono Férias Envelope](http://tdn.totvs.com.br/pages/viewpage.action?pageId=463821314)****.**

* Após a criação do evento, ao lançar as férias o evento de código de cálculo 398-Base de Abono Férias Envelope será visualizado no envelope do funcionário, conforme tela a seguir:

**Importante:**

Caso o usuário não tenha criado um evento com o código de cálculo **398-Base de Abono Férias Envelope**, ao realizar o processo de lançamento das férias através do processo ou diretamente no cadastro de férias será apresentada a mensagem de erro abaixo impedindo o processo.

****Atenção!****

Caso existam funcionários que tenham férias lançadas antes da criação do evento com código de cálculo **398-Base de Abono Férias Envelope,** deverá inserir manualmente o evento na movimentação destes funcionários e em seguida realizar recálculo.

Erros e AçõesO usuário que deseja ajustar as competencias já enviadas

1) Após cadastrar o evento acima mencionado, o sistema irá gerar automaticamente o gatilho S-1010. O usuário deverá acessar o menu eSocial | Fila de Eventos e editar esse evento e alterar o campo "Competência" preenchendo com a data de obrigatoriedade do eventos de tabela.

2) Deverá acessar a ficha financeira do funcionário nos mês que ocorreram férias com pagamento de abono, e:

* inserir o evento com código de cálculo **398-Base de Abono Férias Envelope,** com a soma dos valores dos eventos relacionados a abono de férias e que NÃO tenham incidência ou estorno de IRRF de Férias
* Alterar o valor do evento com código de calculo 381, deduzindo o valor informado no código de cálculo 398.

3) Retificar os eventos S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social  e  S-1210 - Pagamentos de Rendimentos do Trabalho.

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.24 |
| 12.1.23 |
| 12.1.22 |
| 12.1.21 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
