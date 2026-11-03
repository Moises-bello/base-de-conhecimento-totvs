---
content_hash: 22d16ae7d92f86745ba4f0dec61dfa0a5f3b3a0c4527836ea8377c9f15a29667
fetched_at: '2026-06-29T00:09:24.549798+00:00'
page_id: '423937958'
product: rm
source: tdn-rm
title: Contrato e Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937958
version: 6
---

O processo de integração do módulo de Contrato com o Controle Orçamentário funciona basicamente da mesma forma que o controle orçamentário do movimento. Possui a funcionalidade de realocação de valores orçamentários entre Centros de Custos e consulta aos valores do Orçamento por Centro de Custos, Períodos do Orçamento e Natureza Orçamentária/Financeira.

**Pré-requisitos**

É obrigatório informar Centro de Custo no Item de Contrato ou Rateio de Centro de Custo no Item do Contrato (parametrização);   
É obrigatório informar Natureza Orçamentária / Financeira no Item de Contrato;   
É obrigatório que existam períodos orçamentários cadastrados para todas as datas de faturamento dos contratos que irão afetar o Orçamento;.

**Parametrização**

Acessar  **Parâmetros | Gestão de Estoque, Compras e Faturamento | Contratos**

**Etapa - Orçamento**

* **Efeito no Orçamento Item: I**ndica o saldo orçamentário que o contrato irá afetar - opção única para todos os Tipos de Contrato): Nenhum efeito orçamento (default), Aumenta Real, Diminui Real, Aumenta Opcional 1, Diminui Opcional 1, Aumenta Opcional 2, Diminui Opcional 2.
* **Ação ao Exceder Orçamento: I**ndica quando o Valor Previsto de Gasto do Orçamento' exceder o saldo orçamentário. Opções válidas:  Avisa, Barra, Bloqueia.
* **Utiliza Rateio no Orçamento: I**ndica que o orçamento irá utilizar o rateio de CCUSTO do item de contrato

 **Etapa – Definições Gerais**

**Rateios:** Marcar Usa Rateio de Centro de Custo no Item do Contrato;   
  
**Parâmetros específicos para o processo**

Na tabela de 'Tipo de Contrato' será criado o seguinte campo:  
**Afetar Orçamento:**  Tem como objetivo indicar os contratos que irão afetar o orçamento;

Quando um tipo de contrato definido para afetar orçamento, e um contrato desse tipo afeta o orçamento, esse parâmetro não pode mais ser desmarcado no tipo de contrato. Na parametrização de Contratos, serão criados os seguintes campos:

**Efeito no Orçamento:** Tem como objetivo indicar o saldo orçamentário que o contrato irá  afetar (essa opção é única para todos os Tipos de Contrato).Opções válidas:

* Nenhum efeito orçamento (default)
* Aumenta Real
* Diminui Real
* Aumenta Opcional 1
* Diminui Opcional 1
  + Aumenta Opcional 2
  + Diminui Opcional 2

**Ação ao Exceder Orçamento:** tem como objetivo indicar o comportamento do sistema quando o 'Valor Previsto de Gasto do Orçamento' exceder o saldo orçamentário. Opções válidas:

* Avisa
* Barra
* Bloqueia

**Utiliza Rateio no Orçamento:** tem como objetivo indicar que o orçamento irá utilizar o rateio de custo do item de contrato.  
  
**Processos**  
  
**Inclusão:**Ao incluir novo contrato e respectivo(s) item(s), será possível informar os dados que afetarão o Controle Orçamentário do Contrato. Esta opção está disponível no item de contrato, Informações Adicionais, Orçamento, onde o usuário deverá informar a condição de pagamento para geração da(s) parcela(s), assim, os campos Status, data e valor serão automaticamente preenchidos. As opções de Status possíveis são:

* **A Faturar:** será utilizado para indicar que o 'Valor Previsto de Gasto do Orçamento' foi afetado no período indicado na parcela e a mesma ainda não foi vinculada a faturamento;
* **Faturado:** será utilizado para indicar que o 'Valor Previsto de Gasto do Orçamento' foi afetado no período indicado na parcela e a mesma já foi vinculada a um faturamento;
* **Bloqueado:** será utilizado para indicar que o 'Valor Previsto de Gasto do Orçamento', excedeu o saldo Orçamentário disponível referente ao respectivo Centro Custo / Natureza Orçamentária / Período. A parcela com esse status estará bloqueada para vinculação a faturamento até que seu saldo seja desbloqueado.

***Importante!***

* O Status orçamentário será atualizado automaticamente pelo sistema, ou seja, sua edição não está liberada para manutenção por parte do usuário;
* Os 'Valores Previstos de Gastos do Orçamento' e suas respectivas datas de afetação do orçamento poderão ser calculados automaticamente utilizando-se de uma condição de pagamento para os tipos de faturamento de contrato Medição e Não Periódico;
* Para os contratos do Tipo Periódico, o sistema irá calcular e preencher as informações dessa interface de acordo com a quantidade de faturamento e o Valor da Parcela;
* Para os contratos do tipo Medição e Não Periódico, a soma de todos os 'Valores Previstos de Gastos do Orçamento' informados nessa interface deverá fechar com o Valor Total do item de contrato;
* As informações dessa interface serão obrigatórias para salvar os Contratos cujo Tipo de Contrato está parametrizado para afetar orçamento;
* Na geração do orçamento, se alguma Parcela exceder o valor orçado no período, esta parcela terá o 'Status do Orçamento' alterado para 'Bloqueado'. Essa parcela deverá passar pelo processo de Realocação Orçamentária, para que seu faturamento seja liberado;
* Estorno do Valor Previsto de Gasto do Orçamento: O estorno de 'Valor Previsto de Gasto do Orçamento acontecerá somente na execução dos processos: 'Exclusão/Cancelamento de Contrato' e 'Exclusão de Item de Contrato', que serão descritos posteriormente.

**Reprocessar Parcela de Item de Contrato Bloqueada para o Orçamento:**Neste processo, o sistema irá verificar se a parcela Bloqueada pode ser desbloqueada em função de haver recebido uma verba, seja através de transferência ou de inclusão de Valores Orçados. Esse processo poderá ser executado para todos os contratos com parcelas bloqueadas, ou individualmente quando o usuário poderá selecionar o contrato no qual deseja que suas parcelas sejam desbloqueadas.

**Realocação Orçamentária de Parcelas de Item de Contrato Bloqueadas para o Orçamento:**Quando o parâmetro 'Ação ao exceder Orçamento' estiver parametrizado como bloqueia e na execução do processo 'Gerar Orçamento' o 'Valor Previsto de Gasto do Orçamento' (parcela) exceder o saldo do orçamento do respectivo período, a parcela ficará com Status Orçamento igual a Bloqueado.  Será criada uma nova visão de Realocação Orçamentária para apresentar essas parcelas com 'Status Orçamento' igual a bloqueado.

**Faturamento de Contrato** : O faturamento de contrato, seja Periódico, Não Periódico e de Medição, estorna o primeiro Valor Previsto de Gasto com o Orçamento que estiver em aberto, por data crescente de orçamento, ou seja, o primeiro Valor (registro) que ainda não foi vinculado a faturamento.

**Exclusão de Contrato:**Processo responsável por excluir o 'Valor Previsto de Gasto do Orçamento' de todos os itens. Neste caso, o saldo orçamentário não poderá ficar negativo.

**Cancelamento de Contrato:**Processo responsável por excluir o 'Valor Previsto de Gasto do Orçamento' das parcelas não faturadas. Não é permitido saldo orçamentário negativo.

**Desfazer Cancelamento de Contrato:**Ao Desfazer o Cancelamento de Contrato, ou seja, o mesmo é reativado, o sistema gera o orçamento considerando os mesmos critérios descritos no processo 'Geração do Orçamento'.

**Exclusão de Item de Contrato:**A exclusão de um Item de Contrato é permitida somente para itens de contratos não faturados. Esse processo exclui todos os 'Valores Previstos de Gastos do Orçamento' (de todos os períodos) afetados pelo Item de Contrato. O saldo orçamentário não poderá ficar negativo.

**Alteração de Item de Contrato:**Ao efetivar a alteração de um item de contrato, o sistema exclui todos os 'Valores Previstos de Gasto do Orçamento' (de todos os períodos) afetados pelo item de contrato e gera novamente o orçamento de acordo com as novas informações.

**Aditivo de Contrato:**O Aditivo de Contrato para itens com tipo de faturamento Periódico e Não Periódico exclui os 'Valores Previstos de Gastos do Orçamento' das parcelas não vinculadas ao faturamento e regera os valores com base nos novos valores das parcelas. Para Aditivo de Contrato com itens do tipo de faturamento por Medição é necessário que seja refeita a distribuição dos 'Valores Previstos de Gastos do Orçamento' das parcelas não vinculadas ao faturamento considerando o valor do aditivo.

**Reajuste de Contrato / Desfazer Reajuste de Contrato:**Processo que excluem os Valores Previstos de Gastos com Orçamento das parcelas não faturadas e refaz o orçamento considerando o novo valor das parcelas. Os valores de Orçamento do Item de Contrato serão ajustados automaticamente na execução do processo de Reajuste/Desfazer Reajuste.
