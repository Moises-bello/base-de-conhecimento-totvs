---
content_hash: 6b43dd24fadfa4f421e45f416282bb57a21d3fe0d7c73d99d7228326565af84b
fetched_at: '2026-06-29T00:10:58.335642+00:00'
page_id: '605848545'
product: rm
source: tdn-rm
title: Relatórios - Informe de pagamentos - IR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=605848545
version: 7
---

Novidades!

A partir da versão 12.1.2205.156, o IR contém informação do saldo devedor no tempo, esse valor é o mesmo que utilizamos na nossa ficha financeira. Portanto, para clientes que utilizam a ficha financeira com data base terá essa informação no IR também. Favor atualizar o relatório TINREL0065 no [TOTVS Compartilhamento](https://tdn.totvs.com/display/public/LRM/TOTVS+Compartilhamento). Veja o exemplo no final dessa página.

A partir do Release 12.1.2506 é possível parametrizar os componentes que serão ignorados na geração do *Informe de Pagamentos - IR* , para configurar esta opção informe os componentes a serem ignorados no parâmetro [*Componentes a serem ignorados no IP*](https://tdn.totvs.com/pages/viewpage.action?pageId=435105113#:~:text=Componentes%20a%20serem%20ignorados%20no%20IP).

Retorna os valores que foram pagos para o contrato de acordo com o(s) comprador(es). Caso o contrato possua mais de 1 comprador por default os valores apresentados serão de acordo com o % do contrato que cada comprador, desta forma será dividido o valor recebido igualmente considerando o % dos compradores. É possível parametrizar o sistema para que considere exatamente o valor que foi pago(valor baixado) para cada comprador com o parâmetro '**Utilizar o comprador do lançamento Financeiro para o Gerar o IP'**.

Para gerar o relatório selecione o contrato desejado vá ao menu Processos>>Relatório>>Informe de pagamentos - IR.

## Exemplo de geração do relatório:

* O contrato de venda a seguir que será utilizado para a ilustração da geração do relatório possui 2 compradores com 50% cada, e possuem valores de pagamento diferentes.

* Componentes do plano de financiamento.

* O contrato possui lançamentos financeiro para ambos os compradores.

* Para a geração do relatório é necessário selecionar o contrato e ir em Processos>>Relatórios.

* Selecione o relatório(caso não apareça nenhum é necessário importar o mesmo da pasta de instalação do sistema Objetos Gerenciais>>Relatórios), informe o ano base e confirme a execução.

* O relatório a seguir foi gerado da forma padrão o sistema considerou o valor pago e dividiu conforme o % do contrato dos compradores.

Ao habilitar o parâmetro **Utilizar o comprador do lançamento financeiro para gerar o IP** o comportamento do sistema será alterado e o sistema irá considerar o valor que foi pago.

Após a alteração do parâmetro foi feito uma nova baixa para o cliente F12928 e o relatório irá considerar os valores pagos por comprador vinculado ao lançamento que está sendo baixado.

Importante:

* Para que o parâmetro **Utilizar o comprador do lançamento financeiro para gerar o IP**seja considerado é preciso gerar lançamentos para cada comprador do contrato.

### Saldo Devedor no IR

A partir da versão 12.1.2205.156, o IR contém informação do saldo devedor no tempo, esse valor é o mesmo que utilizamos na nossa ficha financeira. Portanto, para clientes que utilizam a ficha financeira com data base terá essa informação no IR também

**Exemplo do IR com saldo devedor**
