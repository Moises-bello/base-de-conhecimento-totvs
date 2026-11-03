---
content_hash: 12c1b894f1a913e1ea83e74e3818a6879c6dd4fbb36898aca2d582612f377505
fetched_at: '2026-06-29T00:09:14.114306+00:00'
page_id: '421385129'
product: rm
source: tdn-rm
title: Adiantamento de Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Adiantamento+de+Contrato
version: 19
---

O TOTVS Construção Obras e Projetos permite associar Adiantamentos aos contratos, bastando clicar em "Controle | Contrato | Anexos | Adiantamento de Contrato" e incluir um novo Adiantamento.  
No cadastro do Adiantamento é necessário definir:

* **Centro de Custo:** Centro de Custo de onde será feito o adiantamento;
* **Descrição (meramente informativo):** Descrição do adiantamento;
* **Data de Vencimento:** Data de vencimento do adiantamento;
* **Valor:** Valor do adiantamento;
* **Saldo:** Apresenta o saldo atualizado do adiantamento;

Ao salvar um adiantamento de contrato o sistema irá verificar e efetuar as seguintes consistências;

* Não irá permitir a criação de um adiantamento de contrato cujo valor seja superior ao valor do contrato;
* Não irá permitir a criação de um adiantamento de contrato cujo valor seja superior ao saldo do contrato;
* Não irá permitir a criação de um adiantamento de contrato cujo valor seja superior ao valor do saldo do contrato deduzindo o saldo dos adiantamentos já existentes para o contrato;
* O valor do adiantamento somente poderá ser alterado caso ainda não tenha sido efetuada nenhuma liberação para o adiantamento;
* Somente poderá ser alterado se não tiver assinatura eletrônica pendente ou assinada;
* Um adiantamento somente pode ser excluído se não tiver sido liberado.
* "Se o código do centro de custo não for informado, será vinculado ao contrato o centro de custo utilizado no projeto. Se o projeto não conter nenhum centro de custo, será necessário informá-lo manualmente no cadastro de adiantamento"

A data de vencimento do Adiantamento deve ser maior ou igual à data da sua liberação e ao ser enviada para o movimento será enviada para o campo DATAEXTRA1.

*Observação: O campo do movimento que receberá a Data de Vencimento do Adiantamento pode ser configurado no movimento.*

#### Liberação de um Adiantamento de Contrato

Após ter sido cadastrado o Adiantamento, é possível liberá-lo através do processo **Liberar Adiantamento,** que libera o valor do adiantamento para o Suprimento e Faturamento, caso a base esteja integrada ao Protheus este valor também é liberado para o Núcleos, no qual o TOTVS Construção Obras e Projetos irá verificar e efetuar as seguintes consistências:

* Não permitir a liberação de um adiantamento de contrato cujo valor seja superior ao saldo do contrato, gerando mensagem específica;
* Não permitir a liberação de um adiantamento de contrato cujo valor seja superior ao valor do saldo do contrato deduzindo o saldo dos adiantamentos já existentes para o contrato, gerando mensagem específica;
* Bloquear o campo "Valor do Adiantamento";
* Atualizar o campo relativo à data de liberação do adiantamento;
* Atualizar o campo relativo ao Saldo do adiantamento;
* Alimentar a aba Detalhes do Adiantamento com as informações relativas à liberação efetuada;
* Gravar o usuário que efetuou a liberação do adiantamento;
* Ao ser efetuada uma liberação de adiantamento, o TOTVS Obras e Projetos irá gerar o respectivo título financeiro no backoffice.

#### Aba Detalhes do Adiantamento

No anexo de Adiantamentos de Contrato, ao editar um contrato, será apresentada a aba "Detalhes do Adiantamento" que estará disponível somente após a liberação do adiantamento.

Esta aba não permite edição e irá conter as seguintes informações:

* Data: Data em que foi liberado o adiantamento ou o período;
* Usuário: Deverá ser preenchido com o código do usuário que efetuou a Liberação do Adiantamento ou do Período;
* Operação: Deverá ser preenchido com "Liberação do Adiantamento", "Liberação do Período XXX" ou "Estorno da Medição do Período XXX" conforme o caso;
* Valor: Na liberação do adiantamento será atualizado com o próprio valor do adiantamento e na liberação do período será atualizado com o valor de dedução de adiantamento constante da mesma.

#### Liberação de Período (Processo de Liberar Período / Processo de Gerar Integração com Suprimentos/Faturamento)

Da mesma forma que para a retenção, o adiantamento passa a tem grid específica com os mesmos campos da Retenção e Dedução. Assim, na grid do detalhamento das Deduções devem estar disponíveis somente detalhamentos do tipo D e na grid do detalhamento do Adiantamento devem estar disponíveis somente detalhamentos do Tipo A.

Caso nos defaults do contrato exista detalhamento do tipo adiantamento cadastrado, o sistema, automaticamente deverá apresentá-lo na tela do detalhamento do Adiantamento, efetuando o devido cálculo conforme o percentual cadastrado nos defaults.

O valor total de adiantamentos constantes do detalhamento deve ser somado ao valor total das deduções e ao valor total das retenções para atualização do campo "Valor total retido/deduzido/adiantado" quando o botão "Calcular valor das retenções/deduções/adiantamentos" for acionado.

Ao ser executado o processo de liberação do período, o sistema irá efetuar as seguintes ações:

* Verificar se existe saldo de adiantamento a ser descontado no contrato, e em caso positivo, se não existir detalhamento de adiantamento informado para o mesmo, gerar mensagem em tela informando e questionando se o usuário deseja prosseguir a execução do processo;
* Não executar o processo, caso a liberação do período faça com que o saldo a ser medido no contrato seja menor do que o saldo do adiantamento. Significa dizer que o sistema bloqueará medições que, se realizadas, farão com que a dívida do fornecedor seja maior do que o valor a ser medido pela empresa;
* Atualizar os Detalhes do Adiantamento;
* Atualizar o Saldo do Adiantamento;
* Caso exista mais de um adiantamento para o contrato, e na liberação do período exista valor de adiantamento a ser deduzido, o sistema irá abatê-lo primeiramente do saldo do adiantamento mais antigo.

Da mesma forma que a Liberação do Período, tanto o Cancelamento da Liberação de Período como o Período de Estorno Automático, deverão atualizar o saldo do Adiantamento, sendo que no caso do estorno, a pasta Detalhes do Adiantamento também será atualizada.

Ao ser efetuada uma Liberação de Período na qual exista valor de adiantamento, o TOTVS Construção Obras e Projetos irá gravar o valor do adiantamento no movimento gerado no backoffice para que seja efetuado o controle financeiro do mesmo.

Ao ser executado o processo de Liberação o sistema irá verificar o saldo do Adiantamento, não permitindo deduções do tipo Adiantamento que sejam maiores que o saldo de Adiantamento. O saldo corresponde ao valor do Adiantamento abatido do valor deduzido do tipo Adiantamento nos períodos anteriores.  
   
Quando for realizada a liberação da medição do período, o sistema financeiro recebe o valor da medição. Nesse momento o sistema irá realizar o abatimento que está sendo feito do adiantamento (dedução de adiantamento) realizando a compensação do titulo do tipo Pagamento Antecipado com o titulo do valor de medição. Com base nisto o valor a ser pago será o valor cheio menos o abatimento que foi realizado do adiantamento de pagamento.  
   
Exemplo.:

|  |  |  |
| --- | --- | --- |
| Valor Lançamento Financeiro | Valor da Dedução | Valor Líquido |
| R$100,00 | R$70,00 | R$30,00 |

O abatimento dos adiantamentos de contrato, e consequentemente a alteração do saldo dos mesmos somente acontece a partir da execução do processo de "Gerar integração com Suprimentos/Faturamento". O valor a ser abatido é definido como dedução do tipo adiantamento na tela de Liberação de Período.  
O sistema permite ainda através de "Processos | Cancelar Liberação do Adiantamento" que a liberação seja cancelada, no momento do cancelamento da liberação de um adiantamento de contrato o sistema irá:

* Atualizar o campo relativo ao Saldo do Adiantamento;
* Excluir o registro da liberação do adiantamento na aba Detalhes do Adiantamento com as informações relativas à liberação efetuada e desabilitar a exibição da aba já que não haverá registros na mesma.

   
Na criação automática de um período de estorno o sistema irá aumentar o saldo do adiantamento conforme o valor do adiantamento deduzido na liberação do período que foi estornado, bem como, irá gerar o registro do estorno na aba **Detalhes do Adiantamento.**  
   
   
  Informações Complementares

Edição do Adiantamento  

   
   
  Processos

[Liberar Adiantamento](http://tdn.totvs.com/display/LRM/Liberar+Adiantamento)

[Cancelar Liberação de Adiantamento](http://tdn.totvs.com/pages/viewpage.action?pageId=441814338)

[Gerar Workflow de Aprovação](https://tdn.totvs.com/x/qsGEIg)

[Cancelar Workflow de Aprovação](https://tdn.totvs.com/x/ecKEIg)

Quando o projeto estiver integrado com o TAA (TOTVS Aprovações e Atendimento), antigo RM Agilis, e estiver parametrizada a aprovação de adiantamentos de contratos , ao criar um adiantamento estarão disponíveis nos processos do adiantamento as opções para gerar ou cancelar o workflow de aprovação.
