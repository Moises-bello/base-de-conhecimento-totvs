---
content_hash: 9671ddea59c535ba4f15f245fdad34cd02bcf7e1e5bfc39f18e720850a35bb8d
fetched_at: '2026-06-29T00:09:35.453656+00:00'
page_id: '425459356'
product: rm
source: tdn-rm
title: Cadastro Empréstimos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459356
version: 2
---

**Cadastro Empréstimos**

---

A Integração Cadastrar Empréstimos do TOTVS Folha de Pagamento x Gestor AVB (TOOLS) tem como objetivo oferecer uma solução para o empréstimo consignado em folha (Averbação).  A averbação do contrato na folha de pagamento poderá ser feita no cadastro do financiamento logo após a aprovação da proposta, impedindo que a margem disponível para os empréstimos sejam tomadas por outras financeiras. No momento da averbação o serviço "Cadastrar Empréstimo" será chamado pelo Gestor AVB e todas as informações necessárias para conclusão do processo serão enviadas através de um XML para o TOTVS Folha. O TOTVS Business Conector receberá esse XML e entregará a inclusão do empréstimo ao TOTVS Folha que fará o cadastro do mesmo.

|  |  |
| --- | --- |
| **CAMPO** | **OBRIGATÓRIO** |
| CNPJ (coligada) | SIM |
| CPF | SIM |
| Matrícula (chapa) | SIM |
| Código Empréstimo | SIM |
| Tipo de Empréstimo | SIM |
| Data do Empréstimo | SIM |
| Valor Original | SIM |
| Saldo Devedor | SIM |
| Número de Parcelas | SIM |
| Início do Desconto | SIM |
| Observação | NÃO |
| Usuário | SIM |
| Senha | SIM |

Uma das informações que será recebida é a data inicial do desconto. Esta permitirá que seja feito o desconto em folha automaticamente, evitando o risco atual de não inclusão dos contratos de averbação no processamento da folha de pagamento. Caso ocorra algum erro na tentativa de inclusão de um empréstimo o sistema deverá retornar uma mensagem em formato XML referente ao log do erro. Existem algumas condições para o cadastro/solicitação da averbação (empréstimo consignado em folha), veja:

- O funcionário não poderá estar com a situação igual a demitido. Caso esteja o empréstimo não será feito.

- O tipo de empréstimo deverá ser sempre AVBTOTVS. Caso seja diferente o empréstimo não será feito.

- O conjunto Coligada, Chapa (Matrícula) e Código do Empréstimo não poderão ser duplicados.Caso tente incluir mais de uma vez com os mesmos códigos o sistema não irá permitir que o empréstimo seja feito.

- O número de parcelas deverá ser no máximo 99.

- O código do empréstimo deverá ter exatamente 9 dígitos.

- A descrição do Evento utilizado nos empréstimos deverá obrigatóriamente ter a seguinte informação: "Empréstimo Consignado TOOLS".

- O código de cálculo desse evento deverá ser o de número 36. Caso contrário o sistema não cadastrará o empréstimo, pois não terá nenhum evento de desconto vinculado ao AVBTOTVS.
