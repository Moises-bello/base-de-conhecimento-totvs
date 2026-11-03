---
content_hash: e0ace359ad804d83cc8ee5354739301bdd41b27ac96fc01a178557bbf1cbe3cd
fetched_at: '2026-06-29T00:09:28.517999+00:00'
page_id: '423938696'
product: rm
source: tdn-rm
title: Aprovação de Movimentos por Workflow no Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938696
version: 5
---

Através da integração do Fluig com o TOTVS Gestão de Estoque, Compras e Faturamento é possível realizar a aprovação de movimentos para faturamento ou utilização em Cotação. Nesse processo ao incluir ou alterar um movimento será gerado um workflow no Fluig com os dados do movimento, onde um usuário com papel de aprovador deve acessar o Formulário no Fluig e conforme análise dos dados aprovar ou não o workflow.  
   
**Parametrização de Integração Fluig**

Para a utilização da integração com o Fluig é necessário configurar em Ambiente | Parâmetros | Parâmetros Globais | Aba Integração Fluig informar o Endereço do Servidor do Fluig, Usuário/Senha do administrador do Fluig e Id da Empresa do Fluig.

Em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetro Gerais | Definições Gerais | Etapa Definições Gerais 3/3 informe o Id da Empresa Centralizadora do Workflow do Fluig com o mesmo valor definido no campo Id da Empresa do Fluig nos parâmetros globais.

Importante: Para maiores informações sobre a instalação e configuração do Fluig.

**Parametrização de Tipo de Movimento**

Para um tipo de movimento gerar workflow no Fluig o mesmo deve estar parametrizado na etapa "Workflow Fluig" conforme as seguintes opções:

**Aprovação**

Este parâmetro define o tipo de aprovação do Fluig utilizada pelo Tipo de Movimento. As opções disponíveis são:

* Não Utiliza: a aprovação pelo Fluig não é habilitada.
* Utiliza no Faturamento: a aprovação pelo Fluig é habilitada para que somente itens aprovados no Fluig possam ser faturados.
* Utiliza na Cotação: a aprovação pelo Fluig é habilitada para que somente itens aprovados no Fluig possam ser selecionados ao se criar uma nova cotação.
* Utiliza em Ambos: é habilitada aprovação pelo Fluig para Faturamento e Cotação.

**Aprovação no Faturamento/Aprovação na Cotação**

* Processo: este parâmetro define o processo do Fluig que será utilizado para a inclusão do Workflow. Para aprovações de movimento no TOTVS Gestão de Estoque Compras e Faturamento estão disponíveis dois workflows de exemplo: "WorkflowNucleus" e "WorkflowItem".

**Importante**: Os WorkFlows de exemplo, são exclusivos para bases de dados em SQL. Não sendo homologados para bases de dados em Oracle.

* Agrupamento: este parâmetro define o tipo de agrupamento utilizado. As opções disponíveis são:
  + Movimento: é gerado um único workflow por movimento, contendo os dados de todos os itens de movimento, quando aprovado este workflow todos os itens do movimento estarão liberados para serem utilizados.
  + Item de Movimento: é gerado um workflow para cada item de movimento, possibilitando ao usuário que cada item seja aprovado de forma individual.
* Estados de Aprovação: devem ser informados os estados de aprovação possíveis para o processo selecionado. Os estados de aprovação são as etapas do workflow em que o movimento/item do movimento serão considerados aprovados. Exemplo: "Aprovado"; "Aprovação Automática".

***Observação***: não é possível informar estados repetidos na lista de Estados de Aprovação.  
***Atenção!*** é possível utilizar somente um tipo de aprovação por Tipo de Movimento, ou seja, se estiver parametrizada a aprovação de workflow no Fluig não é possível utilizar aprovação no TOTVS Gestão de Relacionamento com o Cliente ou Aprovação por Fórmula.  
***Importante***:!se o Processo selecionado no Faturamento e na Cotação forem iguais é obrigatório que os tipos de agrupamento sejam iguais. Nesta situação de Processo e Agrupamento idênticos é gerado apenas um workflow no Fluig.   
   
**Inclusão de Movimento**

Ao incluir um movimento será criado no Fluig o workflow conforme parametrização. O usuário aprovador deve acessar seu painel de tarefas no Fluig e movimentar o workflow gerado para alguma das etapas possíveis. Por exemplo: aprovar solicitação, reprovar solicitação, transferir solicitação, entre outras.  
***Observação***: Os workflows são customizáveis, sendo assim possível criar as etapas do mesmo conforme necessidade da empresa.   
Os workflows gerados para o movimento podem ser visualizados a partir da visão de movimento em "Anexos|Itens de Movimento – Workflow Fluig", nessa visão é possível verificar o Identificador do workflow no Fluig, o Tipo de Aprovação (Faturamento ou Cotação) e o Status de Aprovação (Aprovado ou Não Aprovado).   
Na visão de movimentos são disponibilizados os botões "Aprovados Fluig" e "Não Aprovados Fluig", para filtrar na visão os movimentos com workflow aprovado no Fluig e movimentos com workflow não aprovado, respectivamente.   
   
**Alteração de Movimento**

Ao alterar um movimento que gerou workflow se o item já foi faturado ou utilizado em Cotação (Campo ITEMUTILIZADO = 1 na tabela TITMMOVWFLUIG) será mantido o workflow gerado incialmente e será gerado um novo workflow para aprovação. Se o item ainda não foi utilizado em faturamento ou Cotação, ao realizar a alteração, o workflow já gerado será excluído e em seguida é incluído um novo workflow com os valores atualizados.  
   
**Permissão**

A alteração de movimentos que geraram workflow no Fluig é permitida conforme permissão concedida no cadastro do perfil do usuário.  
Para que um usuário possa alterar um movimento com workflow em aprovação deve estar habilitada a permissão "Alterar Movimentos em Aprovação por Workflow" no menu de movimentos no cadastro do perfil do usuário.  
Para que um usuário possa alterar um movimento com workflow já aprovado deve estar habilitada a permissão "Alterar Movimentos Aprovados por Workflow do Fluig" no menu de movimentos no cadastro do perfil do usuário.   
   
**Faturamento**

Ao realizar o Faturamento do Movimento é realizada a consulta no estado do *workflow,* e de acordo com a parametrização se a aprovação for por Item, somente serão faturados os Itens aprovados e o movimento ficará com o Status de Parcialmente Faturado caso apenas um Item de Movimento estiver aprovado. Caso a aprovação seja por Movimento todos os itens serão faturados se o *workflow* estiver aprovado e o Status do será alterado para Faturado.  
Os Itens faturados são marcados como utilizados (Campo ITEMUTILIZADO = 1 na tabela TITMMOVWFLUIG).  
Somente é permitido o Faturamento do Movimento/Item de Movimento que estiverem aprovados no *workflow* em que está vinculado no Fluig.   
   
**Conclusão de Pedido**

Ao executar o processo de conclusão de pedido as quantidades dos itens serão zeradas no workflow assim como no movimento.   
   
**Estorno de Item não Recebido**

Ao executar o processo de "Estornar item não recebido" em um movimento de destino gerado a partir de um movimento que gerou workflow de aprovação, o Item será alterado para como não utilizado (Campo ITEMUTILIZADO = 0 na tabela TITMMOVWFLUIG)  no movimento de origem relacionado. Não haverá alteração nos workflows existentes para o movimento de origem.   
   
**Cancelamento de Movimento**

Ao cancelar um movimento, caso o tipo de movimento esteja parametrizado para utilizar o Workflow de Aprovação no Fluig para Faturamento, será realizado exclusão do Workflow de Aprovação no Fluig   
Ao cancelar um movimento gerado a partir de um movimento que gerou workflow de aprovação, o Item será alterado para como não utilizado (Campo ITEMUTILIZADO = 0 na tabela TITMMOVWFLUIG) no movimento de origem relacionado. Não haverá alteração nos workflows existentes para o movimento de origem.

**Inclusão de Cotação**

Durante o processo de inclusão de uma nova Cotação, somente serão apresentados Itens de Movimentos que tenham sido aprovados no processo de Workflow de Aprovação no Fluig, nos casos em que o Tipo de Movimento selecionado para a Cotação estejam parametrizados para utilizarem Workflow de Aprovação no Fluig para a Cotação.  
Os Itens utilizados em Cotação são marcados como utilizados (Campo ITEMUTILIZADO = 1 na tabela TITMMOVWFLUIG).

**Cancelamento de Cotação**

Ao cancelar uma Cotação, os Itens da Cotação serão alterados para como não utilizado (Campo ITEMUTILIZADO = 0 na tabela TITMMOVWFLUIG) no movimento que originou a Cotação. Não haverá alteração nos workflows existentes para o movimento de origem.

**Exclusão de Item de Cotação**

Ao excluir um item da cotação, o Item será alterado para como não utilizado (Campo ITEMUTILIZADO = 0 na tabela TITMMOVWFLUIG) no movimento que originou a Cotação. Não haverá alteração nos workflows existentes para o movimento de origem.

**Workflows de Exemplo**

São disponibilizados dois workflows de exemplo: Workflow por Movimentos e Workflow por Item de Movimento.

**Workflow por Movimento**

Ao movimentar o Workflow por Movimento é possível realizar as seguintes ações:  
   
**Aprovação Automática**

No workflow de exemplo está predefinido que movimentações com valor até 10.000 são aprovadas automaticamente, ou seja, se o valor do movimento é até 10.000 ao movimentar o workflow o mesmo é avançado automaticamente para "Aprovado", se for o valor for superior a 10.000 o workflow é avançado para a etapa de "Aprovação", onde será analisado por um usuário definido como aprovador se a solicitação deve ser aprovada ou reprovada.   
Para que seja feito o avanço automático, conforme o valor de 10.000, deve-se realizar a importação da Consulta SQL"NUCSQL0004 -  Fluig - WorkFlow Movimento" e marcar no momento da importação o parâmetro "Código de Consulta SQL = Fixo" (Menu Gestão | Visões de Dados | Importação de Consulta SQL). A Consulta SQL se encontra disponível na Pasta *C:\Totvs\CorporeRM\ObjetosGerenciais\Consultas SQL* (Caminho padrão de instalação da Biblioteca RM, que pode ser alterado conforme necessidade no momento da instalação).  
 ***Importante!*** por padrão, o sistema realiza o avanço automático do WorkFlow para o estado de Aprovação, para que o avanço automático NÃO seja realizado, ou seja, para que o WorkFlow seja mantido em seu estado inicial é necessário:

* Realizar a importação da  Fórmula Visual "MOVWKF0023 - Fluig - Manter WF no Estado Inicial" e marcar no momento da importação a opção "Importar Gatilhos [Menu Gestão | Fórmula Visual | Fórmula Visual | Importação de Fórmula Visual](http://tdn.totvs.com/pages/viewpage.action?pageId=63278047). A Fórmula Visual se encontra disponível na Pasta *C:\Totvs\CorporeRM\ObjetosGerenciais\Fórmulas Visuais* (Caminho padrão de instalação da Biblioteca RM, que pode ser alterado conforme necessidade no momento da instalação).

**Aprovado:**Ao escolher essa ação o workflow é Aprovado e nenhuma ação é realizada no movimento que o gerou.

**Aprova e Fatura Movimento:**Ao escolher essa ação o workflow é aprovado e o movimento que o gerou é faturado automaticamente. Para execução do faturamento automático é necessário que o movimento que gerou o workflow esteja parametrizado para realizar faturamento automático e seja informado um tipo de movimento default na Etapa Compra/Venda - Características na parametrização do tipo de movimento.

**Reprovado Somente**: Ao escolher essa ação o workflow é reprovado e nenhuma ação é realizada no movimento que o gerou.

**Reprova e Cancela o Movimento**: Ao escolher essa ação o workflow é reprovado e o movimento que o gerou é Cancelado. Caso, o workflow tenha sido gerado a partir de um movimento de Ordem de Compra gerado através de uma Cotação, a mesma é reaberta.

**Reprova e Conclui o Movimento**: Ao escolher essa ação o workflow é reprovado e o movimento que o gerou é Concluído.  
   
*Fluxo do Workflow de Exemplo por Movimento:*  
  
    
**Workflow por Item de Movimento**

Ao movimentar o Workflow por Item de Movimento é possível realizar as seguintes ações:  
   
**Aprovação Automática:**No workflow de exemplo está predefinido que movimentações com valor até 10.000 são aprovadas automaticamente, ou seja, se o valor do item é até 10.000 ao movimentar o workflow o mesmo é avançado automaticamente para "Aprovado", se for o valor for superior a 10.000 o workflow é avançado para a etapa de "Aprovação", onde será analisado por um usuário definido como aprovador se a solicitação deve ser aprovada ou reprovada.  
Para que seja feito o avanço automático, conforme o valor de 10.000, deve-se realizar a importação da Consulta SQL"NUCSQL0004 -  Fluig - WorkFlow Movimento" e marcar no momento da importação o parâmetro "Código de Consulta SQL = Fixo" (Menu Gestão | Visões de Dados | Importação de Consulta SQL). A Consulta SQL se encontra disponível na Pasta *C:\Totvs\CorporeRM\ObjetosGerenciais\Consultas SQL* (Caminho padrão de instalação da Biblioteca RM, que pode ser alterado conforme necessidade no momento da instalação).  
***Importante**!*** por padrão, o sistema realiza o avanço automático do WorkFlow para o estado de Aprovação, para que o avanço automático NÃO seja realizado, ou seja, para que o WorkFlow seja mantido em seu estado inicial é necessário:

* Realizar a importação da Fórmula Visual "MOVWKF0023 - Fluig - Manter WF no Estado Inicial" e marcar no momento da importação a opção "Importar Gatilhos [Menu Gestão | Fórmula Visual | Fórmula Visual | Importação de Fórmula Visual](http://tdn.totvs.com/pages/viewpage.action?pageId=63278047). A Fórmula Visual se encontra disponível na Pasta *C:\Totvs\CorporeRM\ObjetosGerenciais\Fórmulas Visuais* (Caminho padrão de instalação da Biblioteca RM, que pode ser alterado conforme necessidade no momento da instalação).

**Aprovado**: Ao escolher essa ação o workflow é Aprovado e nenhuma ação é realizada no movimento que o gerou.

**Reprovado Somente**: Ao escolher essa ação o workflow é reprovado e nenhuma ação é realizada no movimento que o gerou.

**Reprova e Estorna Item**: Ao escolher essa ação o workflow é Reprovado e o item é estornado no movimento.  
   
*Fluxo do Workflow de Exemplo por Item de Movimento:*  
  
**Aprovação via Aplicativo Mobile**  
   
O processo de aprovação de movimentos por workflow está disponível também via aplicativo mobile. Disponível para as plataformas IOS e Android.

**Pré Requisitos:**

* **Android**

Versão: 4.1 ou superior  
Dispositivos suportados: Smartphones ou tablets

* **IOS**

Versão: 8 ou superior  
Dispositivos suportados: IPhone  4 ou superior, IPad 2 ou superior  
Para maiores informações sobre o Fluig Mobile [clique aqui.](http://tdn.totvs.com/pages/releaseview.action?pageId=107940624)
