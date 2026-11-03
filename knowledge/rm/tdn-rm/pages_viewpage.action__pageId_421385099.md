---
content_hash: d40c661224bcf35c90b8dfa764d3b2dc8241362c02f68ffca05cae50ed30addd
fetched_at: '2026-06-29T00:09:13.741555+00:00'
page_id: '421385099'
product: rm
source: tdn-rm
title: Apropriação (F6) 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385099
version: 32
---

***Apropriação de Serviços/Insumos***

**Cronograma de destino da apropriação:**  
Informe para qual cronograma você deseja exportar o percentual ou quantidade apropriada da tarefa.  
Previsto:   
Nesse caso, será acumulado no cronograma previsto o percentual ou quantidade apropriada da tarefa.  
Realizado:   
Nesse caso, será acumulado no cronograma realizado o percentual ou quantidade apropriada da tarefa.  
Medido:   
Nesse caso, será acumulado no cronograma medido o percentual ou quantidade apropriada da tarefa.

Todos os cronogramas.

***Folha de Pagamento:***

**Aplica leis sociais no preço do sistema de folha de pagamento (RM Labore):**  
Caso esta opção esteja habilitada, no cadastro da apropriação vinculada a um funcionário é aplicada a lei social. A lei social aplicada é a lei definida no cadastro do grupo de custo ao qual o insumo está vinculado. A lei social é sempre aplicada, independente da forma de aplicação (sobre o custo unitário ou sobre o total do grupo).  
**Origem do Preço da Apropriação:**  
Valor Mão de Obra do sistema de folha  (RM Labore)  
Marque esta opção caso você queira que o Preço Unitário da apropriação seja lançado de acordo com o valor hora do funcionário do RM Labore apropriado no Totvs Obras e Projetos.  
Valor Insumo Totvs Obras e Projetos   
Marque esta opção caso você queira que o Preço Unitário da apropriação seja lançado de acordo com o valor do Insumo com leis no Totvs Obras e Projetos.

**Data mínima para Apropriação:**  
Informe a data limite para apropriação de serviços/insumos.  
O sistema não permitirá cadastrar uma apropriação onde a "Data de Apropriação" seja inferior a esta data.

**Permite apropriar apenas serviço**

**Permite apropriar apenas serviço**  
Quando este parâmetro estiver marcado será permitido realizar apropriações somente em tarefas tipo serviço, ou seja, não será possível apropriar em uma obra ou etapa.

**Permite editar preço unitário da apropriação:**  
Permite a alteração de preço unitário das Apropriações, exceto apropriações de Mão de Obra.

**Permite editar preço unitário da apropriação de mão de obra.**

Permite Alterar preço unitário das apropriações de Mão de Obra, quando estiver integrado com RH.

   
***Apropriação BackOffice***

Apropriação BackOffice - RM

**Utiliza processo de importar apropriações no BackOffice**

Este parâmetro habilita a apropriação com o BackOffice RM.

Quando habilitado desabilita o parâmetro "ConsultaSQL Personalizada para dados de Apropriação"

**Data da Apropriação**

* Movimentos : Define - se o movimento considerará a data da emissão , ou a data de entrega , ou a data de entrega do item ou a data da saída do movimento.
* Lançamentos Financeiros: Define -se o lançamento considerará a data de emissão ou a da baixa ou vencimento ou previsão , criação ou pagamento.

****Intervalo de períodos para processamento****

Define os períodos que serão submetidos ao processamento ou reprocessamento.

Campo: APROPPERINI e APROPPERFIM

* Automático

Quando atualizado o cronograma de todo o projeto o período inicial é atualizado conforme a data de fechamento contábil do, desta forma será identificado no projeto um período compatível que será adicionado ao período inicial, ajustando também o período final de acordo com o deslocamento do inicial. Considere deslocamento a diferença entre o período inicial antes do processamento e o identificado pela data de fechamento contábil.

Exemplo:

Evolução dos parâmetros de período inicial e final:

¹Campo APROPPERAUTO

* Início

Será informado manualmente o período inicial da apropriação

* Final

Será informado manualmente o período final da apropriação

Caso o usuário opte pela definição manual dos períodos, serão feitas as seguintes consistências:

* Valida a sequência dos períodos e não permite gravar.

**Adicionado o controle de segurança para este processo. Quando o sistema não está parametrizado é exibida uma mensagem mesmo com permissão para o usuário.**

****ConsultaSQL Personalizada para dados de Apropriação****

Mais detalhes sobre informações especificas referente ao BackOffice ou parametrização necessárias de acordo com o BackOffice em:  [BackOffice Protheus](https://tdn.totvs.com/x/davxIQ) - [BackOffice Nucleus](https://tdn.totvs.com/x/ZavxIQ)

Apropriação BackOffice - Protheus

**Apropriar liberação de período de contratos em:**

* **Medição**: O sistema considera como valor apropriado o valor informado na medição do período do contrato. Ao solicitar os valores apropriados no BackOffice sendo desconsideradas as movimentações originadas destas medições.
* **Nota Fiscal**: O sistema considera como valor apropriado o valor retornado pelo BackOffice para os documentos de entrada, desconsiderando os valores de medição.

**Tipos de documento:**

Define os tipos de documento que serão considerados na pesquisa da apropriação, bem como a data que poderá ser utilizada identificação do período da incidência da apropriação no cronograma.

|  |  |
| --- | --- |
| **Tipo de Documento** | **Datas de Apropriação** |
| Notas fiscais | Data de Criação |
| Data de Emissão |
| Baixas de estoque | Data de Emissão |
| Contas a pagar | Data de Emissão |
| Data de Vencimento |
| Data de Vencimento Real |

**Valor Apropriado:**

* Considerar o valor do frete: Se marcado, o sistema soma o valor do frete no total do item. Default: 1.

Campo: MPARAMETRO - APROPFRETE

* Considerar o valor do seguro: Se marcado, o sistema soma o valor de seguro no total do item. Default: 1.

Campo: MPARAMETRO - APROPSEGURO

* Considerar o valor da despesa: Se marcado, o sistema soma o valor de despesa no total do item. Default: 1.

Campo: MPARAMETRO - APROPDESPESA

* Considerar o valor de IPI: Se marcado, o sistema soma o valor de IPI no total do item. Default: 1.

Campo: MPARAMETRO - APROPIPI

OBS.: Para o Mercado internacional este parâmetro é utilizado para o IVA. Se marcado considera o mesmo como Desconto no total do item na apropriação e se desmarcado o valor total não é subtraído ou seja contem o IVA.

**Intervalo de períodos para processamento**

Define os períodos que serão submetidos ao PROTHEUS para processamento ou reprocessamento.

Campo: APROPPERINI e APROPPERFIM

* Automático

Quando atualizado o cronograma de todo o projeto o período inicial é atualizado conforme a data de fechamento contábil do PROTHEUS, desta forma será identificado no projeto um período compatível que será adicionado ao período inicial, ajustando também o período final de acordo com o deslocamento do inicial. Considere deslocamento a diferença entre o período inicial antes do processamento e o identificado pela data de fechamento contábil.

Exemplo:

Evolução dos parâmetros de período inicial e final:

¹Campo APROPPERAUTO

* Início

Será informado manualmente o período inicial da apropriação

* Final

Será informado manualmente o período inicial da apropriação

Caso o usuário opte pela definição manual dos períodos, serão feitas as seguintes consistências:

* Valida a sequência dos períodos e não permite gravar.

Adicionado o controle de segurança para este processo. Quando o sistema não está parametrizado é exibida uma mensagem mesmo com permissão para o usuário.
