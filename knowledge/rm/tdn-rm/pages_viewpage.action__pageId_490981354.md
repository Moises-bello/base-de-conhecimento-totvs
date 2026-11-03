---
content_hash: c24cf83cf1a94524132195f29cd46d0d17e69da45dcc2ae2d07cd6023c6ee812
fetched_at: '2026-06-29T00:10:21.305237+00:00'
page_id: '490981354'
product: rm
source: tdn-rm
title: Retificação 13°
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490981354
version: 26
---

## **ÍNDICE**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01.****VERSÕES**

* 12.1.24.259
* 12.1.25.199
* 12.1.26.140
* 12.1.27.000

## **02.****VISÃO GERAL**

Através deste processo é possível realizar a retificação do décimo terceiro salário de anos anteriores. A retificação será através da digitação de evento(s) que se deseja acrescentar, alterar valor, e/ou quando houver um aumento salarial que não seja por dissídio.

**Observação:**

* O processo de retificação fará o cálculo dos valores de INSS e IRRF conforme tabela da época.
* Os períodos de lançamento da retificação serão criados no mês de dezembro e seu cadastro será a partir do numero 10000 ou conforme parametrizado no campo "Período Inicial" existente em: **Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/6**.

## **03. EXEMPLO DE UTILIZAÇÃO**

1true2ParametrizaçãoParametrização

Acesse o menu Serviços Globais | Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 02.02.03 Retificação 13°

Acesse o menu RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/5

Cadastre o período inicial que será apresentado na tela do processo de retificação da folha de pagamento.

Cadastre os eventos com os códigos de cálculo.

[383 - Líquido Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718720) 

[384 - Pagamento Líquido Retificação](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718780)

3Retificação do 13° SalárioRetificação do 13° Salário23-1CalculoCalculo

Acesse o menu RH | Folha de Pagamento | Folha Mensal | Retificação 13°

Selecione Quebra de Seção, Seleção de Funcionários, Mês, Ano e Período que deseja realizar a retificação; Clique em avançar.

Cadastre o(s) evento(s) que deseja incluir ou alterar no período selecionado. Clique em avançar e depois Executar.

Observação: O evento lançado tem que possuir o CC 102.

Após executar o processo de cálculo parametrizado conforme acima será gerado um gatilho do evento S-1200 no período anual de apuração original como retificação do envio anterior.

Será gerado o gatilho para retificar o evento S-1210 - Pagamentos de Rendimentos do Trabalho no mês de apuração referente ao mês de pagamento.

E na ficha financeira do mês de dezembro original é inserido um período de acordo com o parametrizado no processo de retificação do 13° com a data de pagamento do lançamento do 13°.

Os valores do liquido são lançados no período atual, deverá ser gerado os eventos S-1200 e S-1210 para esse período.

4Cancelamento da RetificaçãoCancelamento da Retificação

Acesse o menu RH | Folha de Pagamento | Folha Mensal | Cancelamento

Marque o parâmetro "Retificação folha/rescisão",  selecione o período e a competência de retificação do decimo terceiro que deseja cancelar. Clique em avançar e depois executar.

## **04. TABELAS UTILIZADAS**

* PFFINANC, PFRETIFICACAOPERIODO.

]]>
