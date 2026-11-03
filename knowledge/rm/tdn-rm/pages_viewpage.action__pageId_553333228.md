---
content_hash: d7f3143198462c98d6de6353475fdb36c5559fe90645c47a281de26b77f9328d
fetched_at: '2026-06-29T00:10:44.559323+00:00'
page_id: '553333228'
product: rm
source: tdn-rm
title: Integração Orçamentária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553333228
version: 26
---

Integração OrçamentáriaPrimeiros Passos - TOTVS Gestão de Estoque

* **Habilitar a utilização do Controle Orçamentário no TOTVS Gestão de Estoque**

Para que o TOTVS Gestão de Estoque permita que sejam enviados valores o Controle Orçamentário deve estar habilitado. A parametrização é realizada nos parâmetros do TOTVS Gestão de Estoque em "Controle Orçamentário".

Ao marcar o parâmetro "Utilizar Nova Versão", o Controle Orçamentário estará ativo e armazenará os valores recebidos utilizando a Natureza Orçamentária/Financeira.

O parâmetro "Utilizar a tabela de Grupo Orçamentário" permite que o Controle Orçamentário possa armazenar os valores recebidos de forma mais detalhada utilizando Natureza Orçamentária/Financeira e o Grupo Orçamentário.

* **Natureza Orçamentária/Financeira**

A Natureza Orçamentária/Financeira pode ser cadastrada no menu Orçamento em Tabelas de Orçamento.

* **Associar usuário ao centro de custo**

Os usuários devem ser associados ao grupo de custo em Vínculo do Usuário e Centro de Custo no menu das Tabelas de Orçamento. Ao abrir a tela, o vínculo é realizado no anexo "Vinculação Usuário a Centro de Custo".

***Obs: Os vínculos ao centro de custo devem ser cadastrados um a um. Utilizando o exemplo do centro de custo associado ao usuário na imagem acima, caso o valor de orçamento que será enviado para o TOTVS Gestão de Estoque utilize o centro de custo 01 mas utiliza rateio nos centro de custo 01.1 e 01.2, o usuário deverá cadastrar além do vínculo para o centro de custo 01 o vínculo para os centros de custos 01.1 e 01.2.***

* **Vinculação de Centro de Custo a Natureza Orçamentária/Financeira**

Os centros de custo que serão utilizados para o orçamento devem estar vinculado as suas respectivas Naturezas Orçamentárias. As naturezas só poderão receber valores dos centros de custo que possuem vínculos.

***Obs: Os vínculos a Natureza Orçamentária/Financeira devem ser cadastrados um a um. Seguindo o mesmo exemplo citado, caso o valor de orçamento que será enviado para o TOTVS Gestão de Estoque utilize o centro de custo 01 mas utiliza rateio nos centro de custo 01.1 e 01.2 e os valores enviados sejam de Naturezas Orçamentárias diferentes como as do exemplo na imagem acima 001, 001.001, 002 e 003, o usuário deverá cadastrar além do vínculo das 4 naturezas para o centro de custo 01 o vínculo das 4 para os centros de custos 01.1 e 01.2.***

Pedido Extra 

No Processo de Pedido Extra, quando no tipo de movimento o campo de Natureza Orçamentária estiver configurado como Edita ou Mostra o sistema não irá validar a Natureza da Tarefa.

* **Cadastro de Grupo Orçamentário**

Caso o parâmetro de utilização da Tabela de Grupo Orçamentário estiver habilitado, devem ser cadastrados os grupos orçamentários que serão utilizados.

Primeiros Passos - TOTVS Construção Obras e Projetos

* **Utilizar Controle Orçamentário**

A Integração Orçamentária poderá ser utilizada quando o sistema estiver parametrizado no TOTVS Gestão de Estoque. Caso a integração orçamentária esteja ativa, o parâmetro poderá ser habilitado nos parâmetros de projeto(F6) em Parâmetros de projeto/Integração/Orçamento.

***Obs: A fórmula do valor unitário da tarefa para o Orçamento é opcional para definir o valor da tarefa que será enviado ao Orçamento. Caso a fórmula não estiver preenchida o valor unitário da tarefa será enviado e caso estiver preenchida o valor unitário da tarefa será o valor retornado pela fórmula ao executar o processo de envio para o Orçamento.***

Quando habilitada, a Integração Orçamentária poderá ser controlada por períodos do cronograma ou pelo projeto. A utilização dos grupos orçamentários também poderá ser habilitada e controlada por Grupo de Custo/Insumo ou Tarefa.

Caso o sistema esteja parametrizado para não utilizar integração orçamentária o parâmetro não poderá ser marcado no TOTVS Construção Obras e Projetos e a utilização dos grupos orçamentários também estará bloqueada.

***Observação: Caso a base de dados esteja integrada com o BACKOFFICE PROTHEUS, a integração orçamentária não poderá ser ativa.***

* **Utilizar Natureza Orçamentária/Financeira**

A utilização da Natureza Orçamentária poderá ser definida nos parâmetros de projeto(F6) em Parâmetros de projeto/Integração/Orçamento. O usuário pode parametrizar para utilização da natureza nas opções Projeto ou Tarefa.

A utilização do grupo orçamentário será utilizada para que o valor enviado para o TOTVS Gestão de Estoque possa ser discriminado pela Natureza Orçamentária/Financeira e pelo Grupo Orçamentário informados. Os valores serão discriminados no TOTVS Gestão de Estoque por Natureza Orçamentária e por Grupo Orçamentário.

**Restrições:**

1. Caso o usuário utilize a natureza orçamentária por Projeto, o usuário poderá utilizar o grupo orçamentário para Grupo de Custo/Insumo e Tarefa;
2. Caso o usuário utilize a natureza orçamentária por Tarefa, o usuário poderá utilizar o grupo orçamentário por Grupo de Custo/Insumo;
3. A opção Grupo de Custo/Insumo somente poderá ser utilizada se "Utilizar controle orçamentário" estiver desmarcado:

* **Projeto deve possuir período informado nos Parâmetros de Projeto(F6)**

Para enviar os valores ao Controle Orçamentário o período do projeto deve estar preenchido.

* Caso o Controle Orçamentário esteja habilitado e a opção de controle for "Período", o sistema irá discriminar nos períodos do Controle Orçamentário os valores por período de acordo com o preenchimento do cronograma previsto..
* Caso o Controle Orçamentário esteja habilitado e a opção de controle for "Todo o Projeto", o sistema irá enviar para o Controle Orçamentário o valor total.

***Observação: Deve ser realizado um cálculo full (cronograma + projeto) para o correto preenchimento dos valores no TOTVS Construção Obras e Projetos antes que a Integração Orçamentária seja executada.***

* **Filial e centro de custo informadas**

O centro de custo pode ser informado no cadastro de projeto ou nos rateios de centro de custo das tarefas.

***IMPORTANTE: Cada projeto deve ter o seu centro de custo associado para que a integração orçamentária funcione corretamente.***

* **Local de Estoque informado no SubProjeto**

O local de Estoque deve estar informado no SubProjeto. Para acessar as informações do SubProjeto deve-se abrir a Planilha de Atividades e acessar o Menu "Funções Principais".

Parametrização do Sistema - TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária no Projeto e Não Utilizando Grupo Orçamentário - Controle por Período**

 

* Os **valores enviados para o Orçamento** terão a mesma **Natureza Orçamentária** informada no cadastro de **Projeto**
* Os **valores enviados para o Orçamento** serão enviados para os períodos do TOTVS Gestão de Estoque com as mesmas quantidades dos períodos do TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária no Projeto e Não Utilizando Grupo Orçamentário - Controle Todo o Projeto**

 

* Os **valores enviados para o Orçamento** terão a mesma **Natureza Orçamentária** informada no cadastro de **Projeto**
* Os **valores enviados para o Orçamento** serão enviados para o TOTVS Gestão de Estoque com a quantidade total do TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária na Tarefa e Não Utilizando Grupo Orçamentário - Controle Período**

* Os **valores enviados para o Orçamento** terão a mesma **Natureza Orçamentária da Tarefa selecionada**. Os valores terão a Natureza Orçamentária **discriminada por Tarefa**.
* Caso as tarefas selecionadas possuam **Naturezas Orçamentárias diferentes**, os valores enviados serão discriminados pela**Natureza Orçamentária** de sua respectiva Tarefa.
* Caso as tarefas selecionadas possuam **Naturezas Orçamentárias iguais**, os valores enviados serão agrupados pela**Natureza Orçamentária**.
* Os **valores enviados para o Orçamento** serão enviados para os períodos do TOTVS Gestão de Estoque com as mesmas quantidades dos períodos do TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária na Tarefa e Não Utilizando Grupo Orçamentário - Controle Todo o Projeto**

* Os **valores enviados para o Orçamento** terão a mesma **Natureza Orçamentária da Tarefa selecionada**. Os valores terão a Natureza Orçamentária **discriminada por Tarefa**.
* Caso as tarefas selecionadas possuam **Naturezas Orçamentárias diferentes**, os valores enviados serão discriminados pela**Natureza Orçamentária** de sua respectiva Tarefa.
* Caso as tarefas selecionadas possuam **Naturezas Orçamentárias iguais**, os valores enviados serão agrupados pela**Natureza Orçamentária**.
* Os **valores enviados para o Orçamento** serão enviados para o TOTVS Gestão de Estoque com a quantidade total do TOTVS Construção Obras e Projetos

* + **Utilizando Natureza Orçamentária no Insumo/Grupo de Custo e Não Utilizando Grupo Orçamentário - Controle Por Período**
  + Os **valores enviados para o Orçamento**terão as Naturezas Orçamentárias respectivas ao Insumo ou ao grupo de custo que está associado nas tarefas.
  + Caso as tarefas possuam **Insumos/Grupos de Custo com Naturezas Orçamentárias diferentes**, os valores enviados serão discriminados**para cada Natureza Orçamentária** e o **Rateio**discriminado **por Grupo de Custo/Insumo**.
  + Caso as tarefas possuam **Insumos/Grupos de Custo com Naturezas Orçamentárias iguais**, os valores enviados serão agrupados**pela Natureza Orçamentária** e o **Rateio**discriminado **por Grupo de Custo/Insumo da Tarefa**.
  + Os **valores enviados para o Orçamento**serão enviados para os períodos do TOTVS Gestão de Estoque com as mesmas quantidades dos períodos do TOTVS Construção Obras e Projetos
  + **Utilizando Natureza Orçamentária no Insumo/Grupo de Custo e Não Utilizando Grupo Orçamentário - Controle Todo Projeto**
  + Os **valores enviados para o Orçamento**terão as Naturezas Orçamentárias respectivas ao Insumo ou ao grupo de custo que está associado nas tarefas.
  + Caso as tarefas possuam **Insumos/Grupos de Custo com Naturezas Orçamentárias diferentes**, os valores enviados serão discriminados**para cada Natureza Orçamentária** e o **Rateio**discriminado **por Grupo de Custo/Insumo**.
  + Caso as tarefas possuam **Insumos/Grupos de Custo com Naturezas Orçamentárias iguais**, os valores enviados serão agrupados**pela Natureza Orçamentária** e o **Rateio**discriminado **por Grupo de Custo/Insumo da Tarefa**.
  + Os **valores enviados para o Orçamento**serão enviados para o TOTVS Gestão de Estoque com a quantidade total do TOTVS Construção Obras e Projetos

* Os **valores enviados para o Orçamento**terão as Naturezas Orçamentárias respectivas ao Insumo ou ao grupo de custo que está associado nas tarefas.
* Caso as tarefas possuam **Insumos/Grupos de Custo com Naturezas Orçamentárias diferentes**, os valores enviados serão discriminados**para cada Natureza Orçamentária** e o **Rateio**discriminado **por Grupo de Custo/Insumo**.
* Caso as tarefas possuam **Insumos/Grupos de Custo com Naturezas Orçamentárias iguais**, os valores enviados serão agrupados**pela Natureza Orçamentária** e o **Rateio** discriminado **por Grupo de Custo/Insumo da Tarefa**.
* Os **valores enviados para o Orçamento** serão enviados para o TOTVS Gestão de Estoque com a quantidade total do TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária por Projeto e Grupo Orçamentário por Tarefa - Controle Por Período**

* Os **valores enviados para o Orçamento** terão a Natureza Orçamentária informada no Projeto e o Grupo Orçamentário será definido pela Tarefa selecionada.
* Caso as tarefas possuam **Grupos Orçamentários diferentes**, os valores enviados serão agrupados por natureza orçamentária e no **Rateio** será visualizado o valor e a quantidade **separado por Grupo Orçamentário e Tarefa**.
* Caso as tarefas possuam **Grupos Orçamentários iguais**, os valores enviados serão agrupados por natureza orçamentária e no **Rateio** a quantidade será **separada por Tarefa**.
* Os **valores enviados para o Orçamento** serão enviados para os períodos do TOTVS Gestão de Estoque com as mesmas quantidades dos períodos do TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária por Projeto e Grupo Orçamentário por Tarefa - Controle Todo o Projeto**

* Os **valores enviados para o Orçamento** terão a Natureza Orçamentária informada no Projeto e o Grupo Orçamentário será definido pela Tarefa selecionada.
* Caso as tarefas possuam **Grupos Orçamentários diferentes**, os valores enviados serão agrupados por natureza orçamentária e no **Rateio** será visualizado o valor e a quantidade **separado por Grupo Orçamentário e Tarefa**.
* Caso as tarefas possuam **Grupos Orçamentários iguais**, os valores enviados serão agrupados por natureza orçamentária e no **Rateio** a quantidade será **separada por Tarefa**.
* Os **valores enviados para o Orçamento** serão enviados para o TOTVS Gestão de Estoque com a quantidade total do TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária por Projeto e Grupo Orçamentário por Grupo de Custo/Insumo - Controle Período**

* Os **valores enviados para o Orçamento** terão a Natureza Orçamentária informada no Projeto e o Grupo Orçamentário será definido pelo Insumo associado as Tarefa selecionadas.
* Caso as tarefas selecionadas possuam **Grupo Orçamentário informado no Insumo/grupo de custo** **diferente**, os valores serão agrupados por Natureza Orçamentária e no **Rateio** será visualizado o valor e a quantidade **separado por Grupo Orçamentário e Tarefa**.
* Caso as tarefas selecionadas possuam **Grupo Orçamentário informado nos Insumos/grupos de custos** **iguais**,
* Os valores serão agrupados por Natureza Orçamentária e no **Rateio** a quantidade será **separada por Tarefa**.
* Os **valores enviados para o Orçamento** serão enviados para os períodos do TOTVS Gestão de Estoque com as mesmas quantidades dos períodos do TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária por Projeto e Grupo Orçamentário por Grupo de Custo/Insumo - Controle Todo o Projeto**

* Os **valores enviados para o Orçamento** terão a Natureza Orçamentária informada no Projeto e o Grupo Orçamentário será definido pelo Insumo associado as Tarefa selecionadas.
* Caso as tarefas selecionadas possuam **Grupo Orçamentário informado no Insumo/grupo de custo** **diferente**, os valores serão agrupados por Natureza Orçamentária e no **Rateio** será visualizado o valor e a quantidade **separado por Grupo Orçamentário e Tarefa**.
* Caso as tarefas selecionadas possuam **Grupo Orçamentário informado nos Insumos/grupos de custos** **iguais**,
* Os valores serão agrupados por Natureza Orçamentária e no **Rateio** a quantidade será **separada por Tarefa**.
* Os **valores enviados para o Orçamento** serão enviados para os períodos do TOTVS Gestão de Estoque com as mesmas quantidades dos períodos do TOTVS Construção Obras e Projetos
* Os **valores enviados para o Orçamento** serão enviados para o TOTVS Gestão de Estoque com a quantidade total do TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária por Tarefa e Grupo Orçamentário por Grupo de Custo/Insumo - Controle Período**

* Os **valores enviados para o Orçamento** terão a Natureza Orçamentária definida pela Tarefa respectiva selecionada e o Grupo Orçamentário será definido pelo Insumo associado.
* Caso as tarefas selecionadas possuam **Tarefas com Naturezas Orçamentárias diferentes**, os **Insumos selecionados sejam iguais** e os **Grupos Orçamentários dos Insumos sejam iguais**, ao gerar o **Orçamento**, serão gerados **um Item para cada natureza** e o**Rateio de cada Item irá conter o Grupo Orçamentário por Insumo**.
* Caso as tarefas selecionadas possuam **Tarefas com Naturezas Orçamentárias diferentes**, os **Insumos selecionados iguais** e os **Grupos Orçamentários dos Insumos sejam diferentes,** ao gerar o **Orçamento**, serão gerados **um Item para cada natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário por Insumo.**
* Caso as tarefas selecionadas possuam **Tarefas com Naturezas Orçamentárias iguais**, os **Insumos selecionados iguais** e os **Grupos Orçamentários dos Insumos sejam diferentes**, ao gerar o **Orçamento**, os**Itens serão agrupados por natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário por Insumo**.
* Caso as tarefas selecionadas possuam **Tarefas com Naturezas Orçamentárias diferentes**, os **Insumos selecionados diferentes**, ao gerar o **Orçamento**, serão gerados **um Item para cada natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário do seu respectivo Insumo**.
* Os **valores enviados para o Orçamento** serão enviados para os períodos do TOTVS Gestão de Estoque com as mesmas quantidades dos períodos do TOTVS Construção Obras e Projetos

* **Utilizando Natureza Orçamentária por Tarefa e Grupo Orçamentário por Grupo de Custo/Insumo - Controle Todo o Projeto**

* Os **valores enviados para o Orçamento** terão a Natureza Orçamentária definida pela Tarefa respectiva selecionada e o Grupo Orçamentário será definido pelo Insumo associado.
* Caso as tarefas selecionadas possuam **Tarefas com Naturezas Orçamentárias diferentes**, os **Insumos selecionados sejam iguais** e os **Grupos Orçamentários dos Insumos sejam iguais**, ao gerar o **Orçamento**, serão gerados **um Item para cada natureza** e o**Rateio de cada Item irá conter o Grupo Orçamentário por Insumo**.
* Caso as tarefas selecionadas possuam **Tarefas com Naturezas Orçamentárias diferentes**, os **Insumos selecionados iguais** e os **Grupos Orçamentários dos Insumos sejam diferentes,** ao gerar o **Orçamento**, serão gerados **um Item para cada natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário por Insumo.**
* Caso as tarefas selecionadas possuam **Tarefas com Naturezas Orçamentárias iguais**, os **Insumos selecionados iguais** e os **Grupos Orçamentários dos Insumos sejam diferentes**, ao gerar o **Orçamento**, os**Itens serão agrupados por natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário por Insumo**.
* Caso as tarefas selecionadas possuam **Tarefas com Naturezas Orçamentárias diferentes**, os **Insumos selecionados diferentes**, ao gerar o **Orçamento**, serão gerados **um Item para cada natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário do seu respectivo Insumo**.
* Os **valores enviados para o Orçamento** serão enviados para os períodos do TOTVS Gestão de Estoque com as mesmas quantidades dos períodos do TOTVS Construção Obras e Projetos
* Os **valores enviados para o Orçamento** serão enviados para o TOTVS Gestão de Estoque com a quantidade total do TOTVS Construção Obras e Projetos
Processo 

O processo pode ser encontrado no TOTVS Construção Obras e Projetos em Planejamento/ Básico/ Integração Orçamento e também pode ser gerado a partir dos processos da Planilha de Atividades.

* **Menu**

* **Processo "Integração Orçamento com TOTVS Backoffice" na Planilha de Atividades**

A Integração Orçamentária envia para o TOTVS Gestão de Estoque os valores de orçamento do projeto. Os valores enviados poderão ser discriminados por natureza e também por grupo orçamentário.

* **Tela do processo**

Ao executar o processo Integração Orçamentária o sistema irá utilizar a fórmula e a parametrização informada nos parâmetros de Orçamento para enviar os valores para o TOTVS Gestão de Estoque Compras e Faturamento. Existem 4 opções disponíveis no processo:

* Calcular e Integrar: os valores serão calculados para o TOTVS Construção Obras e Projetos e já serão integrados ao TOTVS Backoffice.
* Calcular: os valores serão calculados apenas para o TOTVS Construção Obras e Projetos.
* Integrar: os valores calculados serão enviados para o TOTVS Backoffice.
* Desfazer Valores Integrados: os valores integrados ao TOTVS Backoffice serão removidos.

O flag "Ignorar registros sem informação de Natureza Orçamentária e/ou Grupo Orçamentário" ignora os registros onde as informações de Natureza Orçamentária e Grupo orçamentário não estão preenchidos.

Ao fim do processo selecionado, um log será gerado contendo as atividades que falharam, junto ao seu ID, nome e razão de falha. Caso várias atividades forem selecionadas, os processos que podem ser concluídos serão executados normalmente e os que não puderem ser executados, constarão no log.

**Importante:**

* Orçamentos e Períodos de Orçamento não podem ser alterados ou excluídos no TOTVS Gestão de Estoque, pois são originários do TOTVS Construção Obras e Projetos.
Valores Integrados

Ao integrar os valores pelo processo de Integração Orçamentária, os orçamentos podem ser visualizados de duas formas no TOTVS Construção Obras e Projetos e também no TOTVS Gestão de Estoque.

1. **Visualização geral do projeto com todos os orçamentos integrados do projeto**

Acessar o Menu de Orçamento na Aba Planejamento e abrir os Detalhes de Integração Orçamentária

2. **Visualização com todos os orçamentos integrados por tarefa do projeto**

Acessar a planilha de atividades e com a atividade setada abrir o anexo Detalhes de Integração Orçamentária

3. **Consulta de Orçamento TOTVS Gestão de Estoque**

Pode ser visualizado no TOTVS Gestão de Estoque em Consulta Valores de Orçamento na aba Orçamento
