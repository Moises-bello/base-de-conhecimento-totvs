---
content_hash: 62b468133faebf409157b51d3a7952894034b43250e4c2cd2c3a5c724c801281
fetched_at: '2026-06-29T00:09:48.480673+00:00'
page_id: '435105166'
product: rm
source: tdn-rm
title: Identificação - Regra - Tratamento do Desconto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105166
version: 4
---

**Tratamento do Desconto**

---

Devido à necessidade de contabilização dos descontos, em contas específicas, e em alguns casos de forma linearizada, o desconto foi tratado no contrato de locação.

* **TIPO** - Irá definir o tipo de desconto a ser considerado:
  + **Valor fixo:** Irá habilitar os campos "Valor do desconto" e "Aplicar Reajuste", além de desabilitar o campo "Percentual de desconto", que será preenchido com o percentual correspondente do valor do desconto sobre o valor total do contrato.
  + **Percentual:** Irá habilitar o campo "Percentual de desconto" além de desabilitar os campos "Aplicar Reajuste" e "Valor do desconto", onde este último será preenchido com o valor correspondente ao percentual do desconto aplicado sobre o valor total do contrato.

*Observação: Será exibida mensagem ao usuário, informando que o valor final do contrato pode divergir do padrão (valor final - valor desconto) caso esteja sendo aplicada alguma fórmula para calcular o valor final do contrato.*

* Para os campos "Percentual de desconto" e "Valor de desconto", apenas serão válidos os valores maiores ou iguais a 0 (zero).
* O campo "Percentual de desconto" não permitirá valor maior que 100%.
* O campo "Valor de desconto" não permitirá valor maior que o "Valor total do contrato".
* A opção "Aplicar reajuste" apenas ficará habilitada se o desconto for do tipo "valor fixo".
* O cálculo do valor final do contrato, caso não seja definido via fórmula, passará a considerar o desconto, sendo calculado internamente: Valor Final = Valor total do contrato – Desconto.
* O desconto do contrato não será aplicado no escalonamento, que possui campos próprios e específicos para isto.
* Os históricos existentes serão atualizados com valor 0 para os campos criados (valor e percentual de desconto).

**Reajuste**

* **Aplicar reajuste:** irá tratar e reajustar os descontos dos contratos que possuírem a opção "Aplicar Reajuste" marcada, aplicando a mesma regra de reajuste do Contrato de Locação.
  + O reajuste irá atualizar o percentual de desconto nas situações em que a opção "Aplicar Reajuste" estiver desmarcada. O reajuste deverá recalcular o percentual correspondente do valor do desconto sobre o valor total do contrato reajustado.
  + Se a opção "Aplicar Reajuste" estiver marcada, o percentual de desconto será mantido e calculado o novo valor de desconto, se a opção "Aplicar Reajuste" estiver desmarcada, o valor de desconto será mantido e calculado o novo percentual de desconto.
* **Desfazer reajuste:** deverá voltar o percentual e desconto para os valores anteriores ao reajuste aplicado.
* Os históricos serão criados sempre que for reajustado ou desfeito o reajuste do contrato.
* Será gravado o histórico do desconto, assim como é feito com o valor do contrato. Sempre que houver alteração do valor, seja por reajuste ou por aditivo de renegociação, o valor de desconto e percentual de desconto serão gravados na mesma tabela de histórico, da mesma forma que, quando for alterado o valor ou percentual de desconto, será gravado o histórico do valor do contrato.

**Aditivo**

* **Aditivo de renegociação:** Permitirá que sejam alterados, além do valor por imóvel, os campos "tipo de desconto", "Percentual de Desconto", "Valor do Desconto" e "Aplicar Reajuste".
  + O Aditivo permitirá que o usuário altere apenas os dados de desconto, sem a necessidade de alterar o valor de qualquer imóvel.
  + Na tela de aditivo, foram incluídos os campos "valor total" e "valor final" do contrato contendo os valores anteriores os novos valores após o aditivo, considerando também os valores de desconto.
* **Desfazer aditivo:** retornará a mesma configuração, valor e percentual do desconto anteriores ao aditivo em questão.
* Será gravado o histórico do desconto, assim como é feito com o valor do contrato. Sempre que houver alteração do valor, seja por reajuste ou por aditivo de renegociação, o valor de desconto e percentual de desconto serão gravados na mesma tabela de histórico, da mesma forma que, quando for alterado o valor ou percentual de desconto, será gravado o histórico do valor do contrato.
* Os históricos serão criados sempre que for Efetivado ou cancelado algum aditivo de renegociação do contrato.

Voltar

Veja Também

---

Aditivos

Dados do Reajuste
