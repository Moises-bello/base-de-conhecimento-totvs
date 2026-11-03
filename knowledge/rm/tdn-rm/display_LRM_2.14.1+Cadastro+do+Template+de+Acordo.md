---
content_hash: ee1278bed7d3ed7d972231b50d891d36194ecfc6c3402967c491c482213b2570
fetched_at: '2026-06-29T00:10:43.894348+00:00'
page_id: '551424608'
product: rm
source: tdn-rm
title: 2.14.1 Cadastro do Template de Acordo
type: documentation
url: https://tdn.totvs.com/display/LRM/2.14.1+Cadastro+do+Template+de+Acordo
version: 4
---

Neste primeiro momento, será apresentado o cadastro dos “Templates” de acordo. O “Template” é um modelo de negociação padrão que será cadastrado para ser utilizado posteriormente no momento da geração da negociação. Para realizar este processo, o usuário deve acessar “Contas a Pagar / Receber | Acordo | Template Acordo” e realiza os passos a seguir.

O usuário pode utilizar o filtro para listar os Templates de acordos desejados.

Na aba “Identificação”, o usuário deve informar os campos:

* **Descrição:** Informar uma descrição para o” Template”, para facilitar a identificação;
* **Faixa de Valores:** Informar uma faixa de valores que serão permitidos para realização do acordo.

Na aba “Defaults”, informar:

* **Impressão da Negociação do Acordo:** Informar o relatório para impressão desta negociação;
* **Meio de pagamento obrigatório: opções:** não informar/ informar/ informar obrigatório
* **Data default para baixa do acordo:** Quando o template de acordo for parametrizado para Efetivação do acordo como 'Ao Aprovar' ou 'Ao pagar primeira parcela', será possível definir a data da baixa dos lançamentos baixados por acordo que poderá ser a data geração do Acordo ou data aprovação/sistema.
* **Copiar campos complementares:** marcar esta opção caso queira copiar os campos complementares do lançamento original.
* **Informar Defaults para lançamentos na geração do acordo:** Marcando esta opção, o Sistema permitirá que no momento da geração do acordo os defaults como: Filial, Centro de Custo, Conta Caixa, etc sejam informados pelo usuário;
* **Sobrepor defaults do template sobre lançamento:** esse parâmetro terá a seguinte ação:

\* *Desmarcado:*Considera primeiramente os defaults do lançamento de origem se preenchido, caso esteja vazio irá considerar os defaults do template.   
\* *Marcado:* Sempre considera os defaults do template caso esteja preenchido, caso contrário, considera os defaults do lançamento.

* **Default para lançamentos gerados**: Informar nos campos a seguir qual será a informação default para cada um deles. Filial, Departamento, Centro de Custo, Tipo de Documento, Conta Caixa, Classificação Financeira;
* **Histórico Default:** Informar um histórico padrão para os lançamentos gerados por acordo a partir deste “Template”.

Na aba “regras” informar:

* **Usar juros futuros:**
  + **Não utiliza juros:** Marcar esta opção em caso de não utilizar juros futuros;
  + **Juros Simples:** Marcar esta opção para utilização de juros futuros simples;
  + **Juros Compostos:** Marcar esta opção para utilização de juros futuros compostos.
* **Taxa de Juros ao dia:** Informar um intervalo possível de taxa de juros futuros ao dia a ser utilizado.
  + **Permitir alterar juros:** Marcando esta opção, será permitido alterar os valores de juros durante a geração do acordo;
* **Acréscimo:**
  + **Valor Acréscimo:** Informar o valor de acréscimo permitido no acordo;
  + **Mínimo(%):** Percentual mínimo de acréscimo permitido para acordos realizados com esse “Template”;
  + **Máximo(%):** Percentual máximo de acréscimo permitido para acordos realizados com esse “Template”.
  + **Permitir alterar acréscimos:** Marcando esta opção, será permitido alterar os valores de acréscimos durante a geração do acordo;
* **Desconto:**
  + **Valor Desconto:** Informar o valor de desconto permitido no acordo;
  + **Mínimo(%):** Percentual mínimo de desconto permitido para acordos realizados com esse “Template”.
  + **Máximo(%):** Percentual máximo de desconto permitido para acordos realizados com esse “Template”.
  + **Permitir alterar desconto:** Marcando esta opção, será permitido alterar os valores de desconto durante a geração do acordo;
* **Primeira Parcela (%):** Pode-se definir o percentual a ser considerado na geração da primeira parcela do acordo. O percentual informado será aplicado sobre o total da negociação para o valor da primeira parcela;
* **Manter Dia de Vencimento:** Marcando essa opção, acordos registrados com esse “Template” e tiverem mais de uma parcela, sempre terão as parcelas vencendo no mesmo dia de cada mês de vencimento;
* **Intervalo em Dias:** Quando não marcada a opção anterior, o Sistema obedece o intervalo em dias para cada parcela;
* **Prazo:** Informar o prazo para vencimento da primeira parcela do acordo;
* **Quantidade máxima de Parcelas:** Informar a quantidade máxima de parcelas permitidas para acordos que utilizarem este “Template”;
* **Permitir alterar número de parcela:** Marcando esta opção, será permitido alterar o número de parcelas a serem gerados pelo acordo;
* **Permitir acordo de lançamentos a vencer:** Marcando esta opção, o Sistema permitirá que seja feito acordo de lançamentos que ainda não estão vencidos;
* **Exibir soma valores lançamentos:** Marcando esta opção, o Sistema exibirá a soma dos valores dos lançamentos acordados;
* **Permitir alterar Cliente/Fornecedor:**Marcando esta opção, na geração do acordo será exibido um campo para informar o cliente/fornecedor, que será utilizado na geração dos lançamentos financeiros do acordo.
* **Informar opções para gerar número de documento:** Marcando esta opção, no momento da geração do acordo, o Sistema exibirá opções para geração do número de documento dos lançamentos gerados pelo acordo;
* **Permite acordo para lançamentos com boleto Registrado ou Remetido:** Permite que seja gerado acordo para lançamentos Registrados e/ou Remetidos.
* **Permite acordo para lançamentos gerados por acordo:** Quando marcado será permitido a geração do acordo para lançamentos gerados por acordo. Caso desmarcado o sistema fará a validação do mesmo durante o processo de geração de acordo e caso algum dos lançamentos de origem seja oriundo de um outro acordo, será emitida mensagem e o acordo não será gerado.

Na aba “efetivação” informar:

* **Efetivação do Acordo:**
  + **Ao Criar:** Acordo estará ativo assim que criado;
  + **Ao Aprovar:** Acordo estará ativo ao ser aprovado;
  + **Ao pagar a primeira parcela:** Acordo estará ativo apenas no pagamento da primeira parcela do mesmo;
* **Utiliza Aprovação:**
  + **Não Utiliza:** Marcando esta opção, não será solicitada aprovação para o acordo;
  + **Aprovação Simples:** Marcando esta opção, será solicitada a aprovação simples do acordo dentro do Sistema;
  + **Workflow CRM:** Esta opção não será utilizada inicialmente. Marcando esta opção, o usuário tem que informar quais os processos de *workflow* a serem utilizados do Módulo Gestão de Relacionamento com o cliente.
  + **Workflow Fluig:** Esta opção não será utilizada inicialmente. Marcando esta opção, o usuário tem que informar quais os processos de *workflow* a serem utilizados do Fluig.
* **Obter aceite dos Termos do Acordo:** Informar o relatório de aceite do termo de acordo.

Na aba “Meio de Pagamento” o usuário pode informador quais os possíveis meios de pagamento que serão utilizados no acordo, clicando no botão “Incluir”, para inserir meios de pagamento no “Template”.

Em um dos meios de pagamento utilizados no Template é possível marcar a opção “Obrigatório para primeira parcela” que serve para definir a forma de pagamento default para o lançamento, no processo de baixa esse meio de pagamento pode ser alterado.

Após definição dos dados e permissões do Template o mesmo será gerado e poderá ser utilizado nas negociações dos Lançamentos Financeiros através da Visão de Lançamentos ou através da Negociação Online.
