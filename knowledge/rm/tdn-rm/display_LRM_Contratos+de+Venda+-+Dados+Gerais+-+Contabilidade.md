---
content_hash: e107b66acb9666b24597a6b86bf5f31d4b61f621e614347c2185a7b215d5ddc1
fetched_at: '2026-06-29T00:09:50.214199+00:00'
page_id: '435105445'
product: rm
source: tdn-rm
title: Contratos de Venda - Dados Gerais - Contabilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Contabilidade
version: 9
---

A tela para informar os [*Eventos Contábeis*](https://tdn.totvs.com/pages/viewpage.action?pageId=423938154) relativos à **Contabilidade** dos processos relacionados ao Contrato de Venda.

Ela está localizada na aba **Contabilidade**, no agrupador *Dados Gerais*, do painel à esquerda da tela de *edição* do Cadastro de Venda.

É possível de se contabilizar os seguintes Processos:

* **Venda/Aluguel:** Informe o Evento Contábil que será utilizado para contabilizar a **inclusão** do Contrato de Venda. Ao parametrizar um Evento Contábil para este fim, deve-se levar em consideração que o Imóvel deverá ser retirado do estoque da empresa e registradas as contabilizações para recebimento a curto e longo prazo, conforme a política de cada empresa
* **Entrega de chave:** Informe o Evento Contábil para contabilizar a **Entrega de Chaves** e também o **Valor dos Custos** relativos a esta ação. É importante ressaltar que a contabilização deste evento só é possível após a efetivação da Venda/Aluguel.
* **Eventos no reajuste:** Informe os Eventos Contábeis que serão utilizados para a contabilizar os valores calculados pelo **Processo de Reajuste da Venda**.

O TCGI trata a contabilização tanto do **Reajuste Inflacionário**, como do **Reajuste Deflacionário** de formas distintas.

O **Reajuste Inflacionário** é aquele no qual há um **acréscimo** na variação da cotação utilizada para calcular o valor da Correção Monetária da Venda, porque houve inflação no período.

Já o **Reajuste Deflacionário** é aquele no qual há um **decréscimo** na variação da cotação utilizada para calcular o valor da Correção Monetária da Venda, porque houve deflação no período.

* **Distrato:** Informe o Evento Contábil será utilizado para contabilizar as movimentações relativas ao **Distrato** do Contrato de Venda..
* **Seguro por Empreendimento:** Informe o Evento Contábil que será utilizado para contabilizar os valores Seguro por Empreendimento, calculados pelo Processo **Gerar Seguro Por Empreendimento**, disponível no menu de Processos da Venda.
* **Eventos no Aditivo:** Informe os Eventos Contábeis que serão utilizados ao se efetivar um Aditivo para o Contrato de Venda.

Assim como para o Reajuste, o TCGI permite que se contabilize os Aditivos Inflacionários e os Aditivos Deflacionários de forma distinta, conforme a política de cada empresa.

O **Aditivo Inflacionário** é aquele no qual na negociação acordada com o Comprador, há um acréscimo ao valor já contabilizado pelo Evento Contábil de Venda/Aluguel, na efetivação do Contrato de Venda.

Já o **Aditivo Deflacionário** é aquele no qual na negociação com o Cliente, há uma diminuição do valor já contabilizado pelo Evento Contábil de Venda/Aluguel, na efetivação do Contrato de Venda.

Como **exemplo** dos cenários acima, temos as situações onde o Comprador troca o seu Imóvel por outro ou realiza alguma renegociação de contrato com um valor diferente do acordado no ato da assinatura do Contrato.

* **Evento de Transferência:** Informe um Evento Contábil para tratar as movimentações realizadas pela transferência de Saldo entre [**Longo Prazo e Curto Prazo**](https://tdn.totvs.com/pages/viewpage.action?pageId=519726472), conforme a parametrização do período de cada um desses eventos.

Cabe observar, que a contabilização desses Eventos é realizada para a Venda toda, ou seja, não é detalhada contabilmente, parcela a parcela.

O TCGI permite que este [**Eventos Contábeis**](https://tdn.totvs.com/pages/viewpage.action?pageId=423938154) sejam previamente fixados na [**Modalidade de Venda**](https://tdn.totvs.com/display/LRM/Plano+-+Modalidades), como Padrão, para que os Usuários responsáveis pelo cadastro dos Contratos de Venda, não sejam obrigados a informá-los no momento deste cadastro, mitigando assim, os erros e garantido uma padronização desses processos.

É possível realizar os processos de Contabilização e de Estorno Contábil, acima, de forma assíncrona, independentemente ou em lotes (onde há a execução de mais de um registro por vez).

Para cadastrar os Eventos Contábeis no TCGI, acesse o menu *Contabilidade | Gerais | Eventos Contábeis*:
