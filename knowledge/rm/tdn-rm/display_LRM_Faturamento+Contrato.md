---
content_hash: 7dee4d0e4a15962f809bddad61f7c7cc6cb50b3f7150ff1c02bae1c81ef7b1ab
fetched_at: '2026-06-29T00:09:25.459959+00:00'
page_id: '423938157'
product: rm
source: tdn-rm
title: Faturamento Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Faturamento+Contrato
version: 15
---

O termo faturamento de contratos refere-se a criação dos movimentos, que por meio das parametrizações, poderão, através da integração com os demais sistemas gerar os lançamentos financeiros, a contabilização dos valores, o recolhimento das retenções e obrigações fiscais, entre outros.  
O faturamento poderá ser para o cliente ou representante do contrato cadastrado através da opção Manutenção de Contrato, você é quem determinará no cadastro do representante, através do campo "Fatura Cliente Direto" para quem o contrato será faturado.  
Os Contratos inclusos podem ser faturados por três formas distintas.

* Faturamento pela tela principal
* Faturamento por Lotes
* Faturamento de medições

Na primeira, o faturamento é feito com base nos contratos (Periódicos ou não periódicos) selecionados na visão e gera todas as parcelas dos contratos selecionados. Esse processo gera um lote de faturamento que pode armazenar os logs do faturamento dos contratos.  
O segundo tipo é feito com base em um filtro criado pelo usuário na inclusão do lote. Durante a criação do Lote são especificados dados como o intervalo datas, filiais, natureza, tipo de destinatário, tipo de faturamento, movimento a ser gerado, entre outros, que serão utilizadas para filtrar os itens de contratos que serão faturados no processo de faturamento de lotes.   
Para faturar itens do tipo medição é utilizado o faturamento de medições acessado através do anexo "Medições" na tela de manutenção de contratos.

**Quebra de Notas Fiscais**

Durante o faturamento de um contrato com vários itens ou mesmo de vários contratos ao mesmo tempo, movimentos distintos podem ser gerados, de acordo com a parametrização do módulo de manutenção de contratos, ou marcando o campo "Gera nota Separada" na aba "Condições Gerais" do item de contrato.  
Além disso, alguns campos informados no contrato podem fazer com que o mesmo seja quebrado no faturamento independentemente da parametrização.   
***Observação***: Se na pasta identificação dos parâmetros do contrato, você marcou o campo representante, significa que em cada lote incluído você determinará quem será o destinatário do contrato, os representantes ou os clientes, pois podem ter vários representantes e estes efetuam vendas a vários clientes. Portanto, o destino da nota será o representante, porém é o cliente quem efetuará o pagamento e o representante é quem enviará a nota ao cliente.

Fórmula Visual

Está disponível a partir da versão 12.1.29.111 a opção de utilizar gatilho de fórmula visual por Assinantes no processo de Faturamento de Contrato.

Para adicionar o gatilho pesquise pela descrição: **Inclusão de Movimento via Faturamento de Contrato,**na janela de inclusão de gatilhos.

Integração EAI 2.0

Quando na base de dados existir algum pacote de integração que faça uso de mensagens de Lançamentos Financeiros, o envio destes lançamentos financeiros para o EAI irá ocorrer somente no final do processo de Faturamento de Contrato.

Este recurso está disponível nas versões da Biblioteca RM: 12.1.32.348 e superiores, 12.1.2205.161 e superiores,  12.1.2209.106 e superiores

Para maiores informações sobre a integração dos lançamentos financeiros com EAI consulte o documento .

---

Maiores Informações

* [Como Fazer - Reajuste de Contrato no Faturamento](http://tdn.totvs.com/display/LRM/Reajuste+de+Contrato+por+Faturamento)
* [Como Fazer - Previsão Financeira do Contrato por Medição](http://tdn.totvs.com/pages/viewpage.action?pageId=4813050)
* [Como Fazer - Faturamento de Itens de Contrato sem Vigência Definida](http://tdn.totvs.com/pages/viewpage.action?pageId=4813162)
* [Como Fazer - RSS de Contratos a Vencer nos próximos 30 dias](http://tdn.totvs.com/pages/viewpage.action?pageId=4813114)
