---
content_hash: 5e43e27e2512fd11eaa06ebd26044cb16666bf5e5944451d29755e37fc9acf07
fetched_at: '2026-06-29T00:09:54.801218+00:00'
page_id: '445647388'
product: rm
source: tdn-rm
title: Aba Dados adicionais
type: documentation
url: https://tdn.totvs.com/display/LRM/Aba+Dados+adicionais
version: 20
---

Nesta pasta são apresentadas informações adicionais do lançamento financeiro.

Centro de Custo/Natureza Orçamentária Financeira

Defina o centro de custo para o lançamento.

É possível incluir informações do Rateio por Centro de Custo/Natureza Orçamentária Financeira do lançamento através do botão *Rateio*. Esse botão estará disponível apenas quando for definido no parâmetro "Rateio – Centro de Custo/Natureza Orçamentária" em A*mbiente | Parâmetros | Gestão Financeira | Contas a Pagar | Recursos adicionais* a utilização de rateio, obrigatório ou não.

Departamento

Defina o departamento da filial escolhida para o lançamento.

É possível incluir informações de Rateio por Departamento do lançamento através do botão *Rateio*. Esse botão estará disponível apenas quando for definido no parâmetro "Rateio – Departamento" em *Ambiente | Parâmetros | Gestão Financeira | Contas a Pagar | Recursos adicionais* a utilização de rateio, obrigatório ou não.

Contabilização

Defina o tipo contábil do lançamento.

Caso haja alterações nos dados originários do lançamento, ao salvar, a contabilização poderá ser regerada. Para isso, é necessário marcar o parâmetro "Regerar Contabilização" e definir quais campos do lançamento que irão afetar a contabilização em *Ambiente | Parâmetros | Gestão Financeira | Contas a Pagar | Manutenção de lançamentos | Contab. Lançamento.*

Observações:

* Quando algum dos campos que afeta a contabilidade é alterado (via tela de edição) a contabilização será regerada automaticamente somente ao salvar o registro.
* Quando o campo parametrizado como default para o evento contábil é alterado, será validado com o usuário se o evento contábil será atualizado. Se a resposta a pergunta for "Sim", os ajustes no evento e na contabilização serão feitas somente ao salvar o registro; para resposta "Não", a contabilização continua como estava.

Rateio Gerencial

O **rateio gerencial na contabilização** pode ser configurado por meio do **Evento Contábil**. No entanto, no **TOTVS Gestão Financeira**, em *Ambiente > Parâmetros > Gestão Financeira > Integração Contábil > Contab. Lançamento*, existe o parâmetro **“Rateio c. custo default para rateio contábil”**.

Quando esse parâmetro está **marcado**, o sistema define que o **rateio contábil** será gerado com base no **rateio por centro de custo informado no lançamento**.

Dessa forma, caso exista uma configuração de **rateio gerencial** no evento contábil e, simultaneamente, um **rateio por centro de custo** no lançamento, **o rateio do lançamento terá precedência**, sobrescrevendo o definido no evento contábil.

Livro Caixa Digital do Produtor Rural

* **Classificação do lançamento no LCDPR:** nesse campo será configurado a classificação do lançamento que está sendo incluído no sistema.

1. Nota Fiscal
2. Fatura
3. Recibo
4. Contrato
5. Folha de Pagamento
6. Outros

* **Tipo de lançamento no LCDPR:** nesse campo o tipo de documento a ser selecionado, deve acompanhar a classificação de despesa ou receita do lançamento.

1. Receita de Atividade Rural
2. Despesas de Custeio e investimentos
3. Receita de produtos entregues no ano referente a adiantamento de recursos financeiros.

* **CPF/CNPJ do contribuinte sujeito passivo do tributo:** o preenchimento desse campo é opcional e quando preenchido deve ter um CPF ou CNPJ válido. Na rotina geradora do livro caixa  o registro Q100 irá buscar dados desse campo quando preenchido.

Observação

Caso o default para o campo "Classificação do lançamento no LCDPR" esteja preenchido no Tipo de Documento será carregado quando da inclusão de um novo registro, assim como para o campo "Tipo de lançamento no LCDPR" preenchido de acordo com o tipo (A pagar ou A Receber).

Veja Também
