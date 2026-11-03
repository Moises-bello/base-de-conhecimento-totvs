---
content_hash: c1f35fb479969dabea136cd70444a79d6e8b1aee4c72d829cde4eab8d9e290e4
fetched_at: '2026-06-29T00:09:48.634290+00:00'
page_id: '435105209'
product: rm
source: tdn-rm
title: Contratos de Venda - Plano de Financiamento - Condições de Financiamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105209
version: 13
---

Tela onde é possível inserir os componentes dentro de grupos, onde serão representados como regras do Plano de Financiamento do Contrato.   
Nela possui os seguintes processos:

* **Copiar Grupo:** Onde é possível realizar a cópia de um grupo selecionado.
* **Copiar Modalidade:** Através desse processo é possível copiar os grupos e componentes da Modalidade da Venda, caso tenha um componente cadastrado ele será sobrescrito pelos componentes da modalidade.
* **Gerar Plano de Financiamento:** Processo para realizar a geração do Plano de Financiamento, criando assim os lançamentos financeiros.
* **Exclusão do Plano de Financiamento:** Processo para realizar a exclusão do Plano de Financiamento, excluindo os lançamentos financeiros do contrato.
* **Limpar as condições de financiamento em aberto:** Processo que excluir as condições de financiamento que não possui valor.

Atualizar Dados de Integração Financeira na Regra de Venda

**Sobre : Atualizar Dados de Integração Financeira na Regra da Venda.**

**Observação Importante :**

Esse processo é Irreversível.

Este processo após executado , é **responsável por atualzar os campos de Integração Financeira dos Componentes geradores das Parcelas**

**Prioridade Primeira :**  Paramentros por Coligada  
**Prioridade Segunda :** Empreendimento  
**Prioridade Terceira :** Unidade  
**Prioridade Quarta :** ParametroTipoParcela  
**Prioridade Quinta :** TipoParcelaModalidade  
**Priorioridade Sexta e útlima :** Venda  
**Exemplo:**  
Esse processo busca a **filial no parametro**, e se nao encontrar no mesmo , vai buscar esta informação no c**adastro do emprendimento** e assim será até encontrar a Filial informada para preencher o componente gerador de parcela.

Os processos acima são habilitados a partir das permissões dos perfis do TIN. Para isso basta acessar o módulo de serviços globais e perfis. Os processos existem tanto no Contrato da venda, no aditivo e também no distrato. Cada opção com sua permissão própria.

**Inclusão, edição e exclusão de componentes**  
Para o cadastro de um Componente nas Condições da venda, preencha corretamente os campos em branco apresentado na pasta de Identificação.  
Campos a serem preenchidos:

* **Grupo:** Informe o número do grupo que este componente fará parte. Os componentes de reajustes somente terão efeito sobre os componentes de mesmo grupo.

Uma modalidade de venda pode conter vários grupos de financiamento, ou seja, um mesmo componente poderá ser usado em grupos distintos, com regras diferentes.

* **Componente:** Informe o componente a ser cadastrado.

Os componentes podem ser dos seguintes tipos abaixo:

* + - ;
    - ;
    - ;
    - ;
    - ;
    - ;
    - ;
    - ;
    - ;
    - ;
    - ;
    - ;
    - .

Importante

* : Será apresentado se o Tipo de Componente for Entrada, Principal, Resíduo, Seguro ou Alíquota
* : Será apresentado se o Tipo de Componente for Desconto de Juros de Contrato
* : Será apresentado se o Tipo de Componente for Desconto na Correção Monetária

* ****Prioridade de cálculo:****Ao habilitar este parâmetro e estiver utilizando fórmula configurada na condição de financiamento dos componentes de Juros e Correção Monetária, o cálculo do reajuste irá reajustar esses componentes, em ordem crescente, por essa prioridade. Somente para componentes que tenham a fórmula preenchida. Se o CM depende do juros, então o juros tem que ser 0 e o CM tem que ser 1, ou vice-versa.

* **Parâmetros:**

* + **Situação ativa**: Marque este campo quando o Componente estiver ativo. Se o campo estiver desmarcado este Componente não poderá ser usado na Modalidade de Venda.

Nos componentes de reajustes, com ação antes da entrega do empreendimento, este campo será desmarcado após a sua utilização, ou seja, enquanto a venda estiver antes da entrega do empreendimento, o componente estará ativo, após a entrega do empreendimento, o componente será desativado.

* + **Comprador**: Cliente que será informado para ter o nome registrado nos lançamentos do Fluxus. Caso este campo esteja em branco, as parcelas do Fluxus serão registradas com o cliente informado na Identificação da Venda/Aluguel.
  + **Endereço** para envio de boleto: Endereço que será informado para ter o endereço registrado nos lançamentos do Fluxus.

Se o parâmetro "Consistir Saldo Devedor c/ Valor Sub-Unidade", através do Menu Opções | Parâmetros | RM SGI, estiver marcado, o sistema irá comparar o valor da Sub-unidade com o valor total do plano de financiamento, se não for igual, será negado a geração do plano de financiamento.false

Veja Também

---
