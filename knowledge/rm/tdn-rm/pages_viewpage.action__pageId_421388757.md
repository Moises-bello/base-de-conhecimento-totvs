---
content_hash: 6f39b14b426b53a68a90eb049612b1f916ac3ff4370631e73997497e31bb59c7
fetched_at: '2026-06-29T00:09:18.702290+00:00'
page_id: '421388757'
product: rm
source: tdn-rm
title: Reajuste utilizando o serviço de Integração Bancária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388757
version: 2
---

No Retorno Bancário os Valores de Integração deverão ser reajustados para que o serviço de cálculo do valor líquido receba os Valores de Integração já com o reajuste para calcular o valor líquido do Lançamento.  
No retorno da Integração Bancária, existem chamadas diferentes no sistema para retorno de Cobrança Registrado e Não Registrado. Na utilização do  retorno modelo CNAB 240, é possível parametrizar a informação na tela do retorno de cobrança. Dessa forma, temos a definição do tipo de carteira utilizada.

Boleto Carteira Não Registrada

* No  retorno bancário para realização da baixa será chamado o cálculo de reajuste onde o sistema irá apresentar o valor do título até a data de pagamento que consta no arquivo bancário.
* Será comparado o valor calculado pelo sistema e o valor do arquivo de retorno, verificando se há divergência entre tais valores.
* A partir desta comparação o financeiro assume o comportamento atual, que pode ser não permitir a baixa de valores divergentes caso assim esteja parametrizado.
* A efetivação dos valores calculados pelo reajustes devem ser efetivados somente se a baixa for confirmada.

Boleto Carteira Registrada

* No Retorno Bancário o sistema não irá atualizar o valor da parcela. Não será realizado nenhum cálculo do reajuste, pois o valor correto será enviado pelo arquivo de cobrança.
* No Retorno Bancário é validado o tipo de retorno e não a situação do Boleto, pois mesmo tendo um título de carteira registrada o cliente pode optar por gerar segunda via de boleto que não necessariamente será também um título de carteira registrada.

Boleto Pagamento em Carteiras

Não será realizado nenhum tratamento em relação ao reajuste na Remessa Bancária.
