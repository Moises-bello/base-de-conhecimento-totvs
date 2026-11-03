---
content_hash: b6112d178daf2b8d3542fb61174f181ba99edbc4906685eba186718b7ca21ac4
fetched_at: '2026-06-29T00:12:14.649644+00:00'
page_id: '969141178'
product: rm
source: tdn-rm
title: Item de Cobrança - Anexo - Centro de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969141178
version: 7
---

## **Contexto**

Atualmente, a geração dos lançamentos de fechamento de condomínio utiliza o parâmetro de integração financeira do empreendimento, o que limita a realização de rateios específicos. Para suprir essa necessidade, foi disponibilizada uma nova funcionalidade no sistema: **cadastro de centro de custo por coligada no item de cobrança**.

Essa melhoria permite ao cliente definir, para cada coligada, e no próprio item de cobrança, qual centro de custo será utilizado no rateio dos lançamentos, proporcionando maior flexibilidade e controle sobre a gestão contábil e financeira dos empreendimentos.

---

## **Como Utilizar**

1. **Acesso à Funcionalidade:**  
   Acesse o cadastro de item de cobrança no sistema.
2. **Cadastro de Centro de Custo:**  
   No item de cobrança, utilize a nova opção de anexo para cadastrar o centro de custo desejado para cada coligada.

   * Selecione a coligada correspondente.
   * Informe o centro de custo que deverá ser utilizado nos rateios dos lançamentos desse item de cobrança.
3. **Salve as Alterações:**  
   Após cadastrar o centro de custo para cada coligada, salve o item de cobrança para que as regras passem a vigorar nos próximos lançamentos.

---

## **Restrições Importantes**

* **Centro de Custo Único por Coligada:**
  + Não é permitido cadastrar mais de um centro de custo para a mesma coligada. Cada coligada deve ter apenas um centro de custo vinculado ao item de cobrança, garantindo a consistência das regras de contabilização.
* **Definição Global do Item de Cobrança:**

  + O item de cobrança é tratado de forma global no sistema. Por isso, certifique-se de definir corretamente o centro de custo para cada coligada antes de finalizar o cadastro.

---

## **Hierarquia de Centros de Custo**

A hierarquia dos centros de custo para geração dos devidos rateios dos lançamentos é a presente abaixo:

1. Centro de custo do rateio do contrato;
2. Centro de custo do imóvel. Observação: Caso existam áreas fracionadas o sistema irá buscar o centro de custo das áreas para compor o rateio.
3. Centro de custo do item de cobrança\*
4. Centro de custo dos parâmetros financeiros do empreendimento.

\*Importante: Para a utilização do rateio de centro de custo do item de cobrança será necessário gerar os lançamentos de condomínio selecionando o agrupamento por item de cobrança nas opções de agrupamento do processo. São elas:

* Cliente/Fornecedor e Item de Cobrança;
* Cliente/Fornecedor, Subunidade e Item de Cobrança;
* Cliente/Fornecedor, Subunidade, Cálculo e Item de Cobrança.

---

## **Observações**

* Caso precise alterar o centro de custo de uma coligada, basta acessar o item de cobrança e atualizar o cadastro conforme necessário.

---

## **Veja Mais**
