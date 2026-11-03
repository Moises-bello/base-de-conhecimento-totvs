---
content_hash: 619676f9bef8a734332f124f4090f474328146a0e9a7771374d3f96bcd3cfb74
fetched_at: '2026-06-29T00:11:54.036205+00:00'
page_id: '853280161'
product: rm
source: tdn-rm
title: Contratos de Venda - Dados Gerais - Adiantamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Adiantamento
version: 14
---

**LIBERADO NA VERSÃO 12.1.2410 EM DIANTE!**

Para que se possa registrar um **[Adiantamento de Sinal](https://tdn.totvs.com/pages/viewpage.action?pageId=865405461)** no *[Portal de Imóveis](https://tdn.totvs.com/pages/viewpage.action?pageId=435105077)* e garantir a venda do imóvel que o cliente tem interesse, foi criada a nova aba Adiantamento no cadastro de Vendas.

Esta funcionalidade tem como objetivo confirmatório, sendo que o sinal de compra confirmatório, visa confirmar a sua intenção de comprar a propriedade, abatendo assim, o valor pago, do seu valor total, ocorrendo a efetivação total da negociação.

Com esta implementação, é possível de se gerar a parcela de adiantamento de sinal, para a venda em questão, mesmo sem que haja um Plano de Financiamento gerado para a mesma.

Atenção!

O sistema não irá controlar o adiantamento com propósito indenizatório.

Para acessar esta funcionalidade, aplique a Permissão de Acesso na opção *[01.1.02.29] Contratos: Adiantamento de Sinal*, do agrupador de Contratos:

Nesta aba, o sistema apresenta os seguintes campos:

* **Data de Vencimento do Adiantamento:** informe a data de vencimento do lançamento de adiantamento associado a esta venda. A data informada neste campo pode ser anterior à data da venda;
* **Valor do Adiantamento:** informe o valor da parcela de adiantamento, sendo que este valor deve ser exatamente o mesmo valor da parcela de sinal ([Tipo de Componente 1 - Entrada](https://tdn.totvs.com/display/LRM/Tipos+de+Componentes+-+Entrada)), informado nas condições de financiamento do PI. Sendo ainda que a parcela deste componente deve obrigatoriamente, ser única.

Importante!

Caso a condição acima não seja atendida, o sistema apresentará uma exceção semelhante à abaixo ao se realizar a validação da VPL, no PI ou ao gerar o Plano de Financiamento no TCGI:

*Na venda [###] existe o lançamento de adiantamento de sinal e não existe nenhuma condição de financiamento no valor [R$ 51.000,00] para o tipo de componente [Tipo Entrada]. Favor ajustar a condição ou excluir o adiantamento*

Também é importante que o parâmetro [Efetivar venda e desbloquear lançamentos no TOTVS Gestão Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=435104791), do TCGI esteja marcado, para permitir que a parcela do sinal com crédito de adiantamento seja baixada antes da Efetivação do Contrato de Venda:

*Na venda [num\_venda] tem adiantamento de sinal [idlan] e o parâmetro geral deve ficar marcado para que o processo de efetivar realize a baixa da parcela do sinal com o crédito de adiantamento. Parâmetro Geral=> Contrato de Venda =>Integração Financeira =>Integração Financeira 3/4 => Efetivar Venda e Desbloquear Lançamentos.*

* **Id. Lanc do Adiantamento:** este campo é preenchido automaticamente, na tabela de venda, com o identificador do lançamento de adiantamento gerado pelo módulo financeiro e também é gravado o código da coligada deste lançamento em um campo próprio, desta mesma tabela. Este lançamento de adiantamento é gerado de acordo com o Tipo de Documento de Adiantamento informado no cadastro do [Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105033#:~:text=Tipo%20de%20Documento%20de%20Adiantamento%3A);
* **Agrupador de Tipo de Adiantamento:** Neste agrupador pode ser informar se o lançamento de adiantamento será gerado com a forma de pagamento via Boleto ou via PIX;

Atenção!

Caso a parcela de Adiantamento de Sinal gerada não esteja baixada, no momento da [efetivação do contrato da venda](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Processo+-+Efetivar+Contrato), o sistema exibirá uma exceção semelhante à abaixo ao usuário:

*A venda [num\_venda] possui um lançamento de adiantamento de sinal [idlan] que não se encontra baixado, favor realizar a baixa ou excluir esse adiantamento para efetivar o contrato*

Gerando o crédito ao Efetivar o contrato de venda.

Neste exemplo acima , foi gerado um Adiantamento no valor de R$500,00 Reais , mesmo valor da condição de Financiamento R$500,00 Reais.

Feita a baixa do Lançamento de Adiantamento.

Ao Efetivar o contrato de venda - o lançamento é baixado automaticamente e ocorre o vínculo ao Lançamento de Adiantamento.

Valor da Baixa : R$0,00

Pois mostra o Crédito de Adiantamento no valor do SINAL de R$500,00 Reais.

Feito o vínculo com o Crédito Financeiro gerado ao baixar o Adiantamento.

Adiantamento via PI = [Clique Aqui !](https://tdn.totvs.com/display/LRM/Pagamento+de+Adiantamento+via+PI)

Consulte a documentação sobre [Adiantamento](https://tdn.totvs.com/display/LRM/Adiantamento), do módulo financeiro.
