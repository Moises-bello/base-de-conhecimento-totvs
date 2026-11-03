---
content_hash: beb1181645c33b20cbe7080d575665dda8127bbf183c339229a3ae40f566ccd6
fetched_at: '2026-06-29T00:11:54.790205+00:00'
page_id: '857905605'
product: rm
source: tdn-rm
title: DT - Rescisão - Data de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=857905605
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cadastro de Rescisão |
| País: | Brasil |
| Issue: | [DRHCALCRM-6742](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6742) |

## **02. VERSÃO**

Versão disponível a partir de:

* 12.1.2402.195
* 12.1.2406.122
* 12.1.2410 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao cadastrar um rescisão, o campo data de pagamento está preenchendo com a mesma data de desligamento/demissão. O cliente deseja que a data de pagamento seja preenchida automaticamente com até 10 dias após o desligamento do funcionário, considerando que a data de pagamento seja em um dia útil bancário.

## **04. SOLUÇÃO**

Implementar no produto a sugestão de preencher automaticamente a data de pagamento da rescisão nos Processos/Cadastro de Rescisão Individual, Rescisão Global e Rescisão Coletiva considerando o prazo de 10 dias para pagamento da rescisão após o desligamento: 

* Foi criado no parametrizador o parâmetro 'Calcular a data de pagamento de último movimento considerando a quantidade de dias’ e o campo 'Quantidade de dias'.
* O campo 'Quantidade de dias' só ficará habilitado se o parâmetro estiver marcado.
* A quantidade de dias informada será parametrizada com um limite de até 10 dias, conforme a legislação.
* Quando o parâmetro estiver marcado, nos processos/cadastros de Rescisão Individual, Coletiva e Global deverá preencher o campo Data de Pagamento e Data do último movimento considerando a data de desligamento + quantidade de dias informado no campo Quantidade de dias.
* Quando o funcionário tem aviso prévio trabalhado (campo DTAVISOPREVIOTRAB preenchido) ou para o tipo de demissão do tipo 5 e 6 (transferência), o parâmetro não será considerado.
* Quando a data de pagamento for em um sábado, domingo ou feriado irá retroceder, até o dia útil anterior a este.

## **05.** **ASSUNTOS RELACIONADOS**

* [Cálculo - Rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719617)
