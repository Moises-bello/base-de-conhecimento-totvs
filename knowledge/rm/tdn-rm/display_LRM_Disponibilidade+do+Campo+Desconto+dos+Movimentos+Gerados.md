---
content_hash: 6d9ac357c0a88cf3c4abb959dcd499ddf379191f9d0ed843fb07063efac4896b
fetched_at: '2026-06-29T00:09:14.307117+00:00'
page_id: '421385192'
product: rm
source: tdn-rm
title: Disponibilidade do Campo Desconto dos Movimentos Gerados
type: documentation
url: https://tdn.totvs.com/display/LRM/Disponibilidade+do+Campo+Desconto+dos+Movimentos+Gerados
version: 2
---

---

O ajuste do campo foi realizado com o objetivo de identificar os movimentos gerados que contenham dedução e discriminação de valor de dedução e retenção na liberação do período do contrato. Não será permitido modificar o Desconto do movimento no módulo Suprimento/Faturamento.

* **Regra de Negócio** Quando o movimento é gerado a partir de uma liberação de período de um contrato com dedução e discriminação de valor de dedução e retenção o somatório das deduções é enviado para o campo "Desconto" do movimento no módulo Suprimentos/Faturamento. Quando o movimento é gerado e possui dedução no contrato discriminando o valor de dedução e retenção o valor será identificado no módulo Suprimentos/Faturamento e assim, o campo "Desconto" do movimento terá sua edição bloqueada.

A geração do movimento pode apresentar 3 cenários diferentes:

* **Cenário 1 - Gerar movimento com parâmetro "Discriminar valores de retenção e dedução" marcado** Nesse cenário o campo "Desconto" do movimento terá sua edição bloqueada Ao gerar o movimento com essa parametrização os valores de dedução e de retenção serão enviados ao Suprimentos/Faturamento e terão o seguinte comportamento: - O somatório das deduções vai para o campo "Desconto" do movimento no módulo Suprimentos/Faturamento. - O somatório das retenções vai para o campo "Valor Retido" do movimento no módulo Suprimentos/Faturamento.

* **Cenário 2 - Gerar movimento com parâmetro "Enviar retenção como desconto na liberação do período" marcado** Ao gerar o movimento com essa parametrização os valores de dedução e de retenção serão enviados ao Suprimentos/Faturamento e terão o seguinte comportamento: - O valor do campo "Valor total retido/deduzido" da liberação do período será enviado para o campo "Desconto" do movimento no módulo Suprimentos/Faturamento.

* **Cenário 3 - Gerar movimento com parâmetro 'Discriminar valores de retenção e dedução' e parâmetro 'Enviar retenção como desconto na liberação do período' desmarcados.** Ao gerar o movimento com essa parametrização nenhum valor será enviado para os campos "Desconto" e "Valor retido" do movimento no módulo Suprimentos/Faturamento.
