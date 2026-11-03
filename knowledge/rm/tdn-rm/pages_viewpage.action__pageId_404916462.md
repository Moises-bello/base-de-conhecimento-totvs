---
content_hash: e087e356b7955ccdf847728afd64a2249e47b4cfcdcdaabe1e26a874c934d0b5
fetched_at: '2026-06-29T00:09:11.474120+00:00'
page_id: '404916462'
product: rm
source: tdn-rm
title: Como_Fazer_Venda_Parcelamento_de_Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=404916462
version: 4
---

| Produto | : | TOTVS Incorporação |
| --- | --- | --- |
| **Processo** | : | Comissão |
| **Sub Processo** | : | Parcelamento de Comissão |

#### Este documento visa explicar o funcionamento do parcelamento de comissões geradas pelo TOTVS Incorporação e integrada com Gestão de Estoque, Compras e Faturamento e também com a folha de Pagamento.

A partir da versão 12.1.22 será possível realizar o parcelamento do valor da comissão. Este processo é habilitado tanto para a geração da comissão para o Fornecedor (Gestão de Estoque, compras e faturamento) quanto para o Funcionário (Folha de Pagamento).

Para utilizar a comissão temos que primeiramente definir os parâmetros para a integração com o Backoffice. Estes parâmetros podem estar no Empreendimento, na Unidade ou como Default nos parâmetros do TOTVS Incorporação.

 **Após realizar toda a parametrização, é necessário criar uma venda e incluir um vendedor. O Vendedor pode ser tanto um fornecedor, quanto um Funcionário.**

Ao acessar a comissão, que está no anexo de vendedores, os campos que aparecem são de acordo com o tipo de vendedor, como podemos ver a seguir:

Quando o vendedor é um Funcionário os campos são diferentes, porém também é possível criar o parcelamento.

* A tela de cadastro foi alterada para que seja possível definir o valor da comissão e quantas parcelas serão geradas. As parcelas podem ser incluídas manualmente, ou então, ao salvar a comissão são calculadas quantas parcelas foram definidas criadas automaticamente.

* As parcelas são integradas com os respectivos sistemas gerando Movimento ou então um item no Envelope de pagamento do funcionário.

* Foi criado um novo campo de Fórmula para a validação da integração das parcelas da comissão. Com esta fórmula será possível escolher quais parcelas serão integradas e também canceladas da integração.

Observação

As parcelas podem ser tanto incluídas, quanto editadas e excluídas, isto, enquanto a comissão não estiver integrada ao BackOffice. O valor da comissão e o número de parcelas devem coincidir com a quantidade de parcelas incluídas na comissão e o valor deve ser igual ao somatório das parcelas criadas.

---

## Detalhes e validações

No detalhe da parcela podemos ver quais são os campos existentes.

**Quando a comissão é para um fornecedor:**

**Quando a comissão é para um funcionário:**

Observação

As parcelas podem ser editadas, e seu valor ou número de parcela alterada. Porém devemos sempre respeitar o valor total da comissão e não ultrapassar esse valor, ou a quantidade de parcelas estipulada.

**IMPORTANTE**

Ao cadastrar a comissão, existem as seguintes validações:

1. 1. O número de parcelas da comissão deve ser igual ao somatório da quantidade de parcelas incluídas na comissão.
   2. O valor total da comissão deve ser o mesmo do somatório dos valores das parcelas incluídas na comissão.
   3. Não pode existir parcela com valor zerado ou negativo na comissão.

---

## Processos de Comissão

Após as validações, podemos realizar o processo de Gerar a comissão, fazendo assim a integração com o Backoffice Respectivo.

 Quando a comissão é integrada à Gestão de Estoque, compras e Faturamento, é gerado um movimento para cada parcela da comissão, conforme vemos a seguir:

 Quanto integrada à Folha de Pagamento, a comissão irá gerar um item no Envelope de Pagamento do Funcionário. Para cada competência, um item é gerado.

---

## Fórmula de Validação da Integração da Comissão

Outra forma de gerar a comissão é utilizando a fórmula de Validação da integração. Foi criada uma função de fórmula para acessar todos os dados da tabela XCOMISSAOPARCELAMENTO. Essa função é a **TABCOMISSAOPARCELA.**

Segue abaixo um exemplo de como utilizar a fórmula.

**No exemplo acima, a fórmula irá integrar apenas as parcelas 2 e 4 da comissão. As outras parcelas não serão integradas.**

Ao executar o processo da geração da comissão, o parcelamento ficará da seguinte forma:

**Perceba que apenas as parcelas 2 e 4 foram integradas ao backoffice. Isto por causa da fórmula utilizada para validação.**

No cancelamento da comissão (Integração da comissão com o Backoffice), será possível escolher se apenas 1 parcela será retirada da integração ou todas as parcelas. Veja a seguir:

**Após executar o processo, caso escolher pelo Número da parcela, apenas esta votará a situação de Não integrada.**
