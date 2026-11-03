---
content_hash: d59f01ee033bd7ea61929f605231a4e9ad0f4248ee09c5e5b19c8fbabb712a8f
fetched_at: '2026-06-29T00:09:14.700457+00:00'
page_id: '421385228'
product: rm
source: tdn-rm
title: Medição de Item de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385228
version: 12
---

Aqui será medida a quantidade dos serviços que já foram executados no período selecionado. Nesse processo, ficarão disponíveis obras e etapas dos respectivos serviços associados ao contrato. A exibição de obras e etapas é apenas informativa, ou seja, somente tarefas podem ser medidas, portanto a execução do processo desconsiderará a seleção das mesmas.  
As medições podem ser efetuadas e/ou alteradas através da visão diretamente na grade de Medição. Para isso, clique no campo "Qtde Medida", informe-o e pressione "Enter".  
As medições também podem ser efetuadas através da janela Edição. Para isso, clique no botão "Editar Medições", aparecerá uma janela com vários campos onde você poderá fazer o lançamento da medição informando a quantidade, o valor ou o percentual medido.  
Caso seja informada a quantidade, será calculado o valor medido.   
Caso seja informado o valor medido, será calculada a quantidade medida.  
Só ficam visíveis para medição os lançamentos que foram associados ao contrato.

**Observação:**

**Saldo( quantidade ) -** Considera o quantidade medida presente **Saldo( valor ) -** Considera o valor medido presente **Saldo (valor) =** valor contratado - valor medido presente

**Observação:**  
Existe um Parâmetro de Projeto "Permite Medição superior a 100% " que influência sobre o comportamento dessa funcionalidade dependendo da opção de estiver marcada.

**Selecionar Tarefas no processo de Medição:**

Quando esta desmarcado ele trás todos os itens associados ao contrato para realizar a medição.

Quando esta marcado ele não trás as tarefas na grid, o usuário deve selecionar as tarefas na medição do contrato.

Na tela logo acima, de edição do contrato, aba de parâmetros, também é possível informar a **grandeza principal de medição** do contrato em questão. Caso não seja informada a grandeza no parâmetro do contrato, será considerada a grandeza definida no parâmetro do projeto

A medição também pode ser realizada pela opção "Efetuar Múltiplas Medições"

O sistema considerará o peso de cada item do contrato no momento de realizar o rateio do valor medido.

Valor Medido é calculado com base no peso do total contratado nas tarefas selecionadas no grid, com valor medido limitado ao saldo de valor do item. Caso seja informado um valor de medição superior ao saldo de valor das tarefas não é realizado rateio.

Se a grandeza selecionada for "Percentual", informe o valor e escolha se será aplicado em "quantidade" ou "valor". A opção de ratear ficará desabilitada.   
Se a grandeza selecionada for "quantidade" informe o valor. A opção de aplicar em "quantidade" ou "valor" ficará desabilitada. A opção de ratear ficará desabilitada.   
Se a grandeza selecionada for "Valor", informe o valor. A opção de aplicar em "quantidade" ou "valor" ficará desabilitada. A opção de ratear ficará habilitada.

**Atenção:**  
Ao medir pela grandeza "percentual", o valor informado será aplicado no campo escolhido pela opção "Aplicar em"   
   
**Exemplo:**  
A grandeza selecionada foi "percentual", o valor informado foi 100, no campo aplicar em selecionei a opção "quantidade". O valor informado será apresentado no campo quantidade na medição, serão 100% sobre o valor da quantidade. Se a quantidde do item for 2, o campo quantidade da medição receberá o valor 2.  
   
Dentro do processo de medição do contrato é possível efetuar rateios para o item, tais como Rateio por Produto, Rateio por Centro Custo e Rateio por Estado e Município.

**Campo Cliente / Fornecedor**

Quando estiver parametrizado para poder utilizar mais de um fornecedor e para ser preenchido na tela de medição/consumo do contrato, terá um campo na tela para que seja escolhido qual cliente ou fornecedor será o da medição **(esse campo virá em branco e será possível escolher um dos fornecedores que estão cadastrados no contrato)**. Se tiver mais de um fornecedor por período, será preciso criar períodos complementares para os outros fornecedores. Quando o contrato tiver apenas o fornecedor principal, o sistema automaticamente preencherá  o fornecedor e não permitirá a edição.

**Última Medição do Contrato: Regras e Funcionamento**

Ao marcar a opção **"Última Medição do Contrato"** e salvar a medição, indica se aquele período será o último do contrato e que o contrato entrou em processo de encerramento. Para ativar esta função, acesse as configurações em: Contrato>Medição]]>.

### 🔒 Bloqueios e Impactos

Uma vez ativada, a função aplica restrições imediatas para garantir a integridade do encerramento:

* **Novos Períodos:** Fica bloqueado o cadastro de qualquer novo período de medição.
* **Aditivos:** Não é mais permitido criar aditivos de valor, prazo ou de qualquer outra natureza.
* **Faturamento Direto:** Impede a inclusão de novos pedidos de faturamento direto após a marcação.

> **Resumo:** Esta função é o passo definitivo para sinalizar que o contrato não sofrerá mais alterações financeiras ou cronológicas, travando a estrutura para a conclusão final.

 Informações Complementares

Liberar Medição acima de 100% por Contrato

[Avanço físico afeta medição de contrato (App Minha obra)](https://tdn.totvs.com/pages/viewpage.action?pageId=553905340)
