---
content_hash: 8cea970f3a3f3d2312db4d0e51e96fe772009ebbac3f1a4aaad75cd0a4835019
fetched_at: '2026-06-29T00:06:00.233586+00:00'
page_id: '195300058'
product: rm
source: tdn-rm
title: ER_ux_design_thinking_copia_de_itens
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_ux_design_thinking_copia_de_itens
version: 21
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Cópia de Itens |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6030 |
| **Requisito1** | PCREQ-6031 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Aplicar as soluções propostas pela a equipe de Desing Thinking da TOTVS no processo de Cópia de Itens visando uma melhor usabilidade e agilidade do processo como um todo.

## Definição da Regra de Negócio

A proposta é aplicar as soluções indicadas pela a equipe de Desing Thinking da TOTVS no processo de Cópia de Itens, de forma que o mesmo se torne mais ágil em relação à definição dos itens que deverão ser copiados e todas as suas respectivas configurações para que o usuário esteja seguro do que realmente ocorrerá ao executar o processo.

1. Novas opções de Interface  
     
   A tela do processo deverá ser modificada para que o usuário tenha mais facilidade nas definições do mesmo, três novas abas na tela do processo serão criadas:  
     
   1. **Cópia Simplificada:** Deverá permitir a cópia de todo o projeto desejado de forma simplificada, sem distinção de itens por entidade (Protótipo 01):   
      * + Estará disponível para o usuário apenas as entidades que deverão ser copiadas e não os itens de cada uma e ficará a critério do usuário selecioná-las, porém, as relações deverão ser consideradas, como por exemplo a relação "grupo de custo x insumos";
        + A descrição de cada opção deverá apresentar a relação dos itens relacionados à cópia selecionada, como por exemplo:
          - Planilha de Atividades (Todas as Atividades inclusive Composições, Insumos e Grupos de Custo utilizados);
        + A possibilidade de cópia da Planilha de Serviços somente estará disponível se o parâmetro de projeto "Utiliza Planilha de Serviço" do projeto origem estiver marcado;
        + A possibilidade de cópia de Cenários somente estará disponível se o parâmetro de projeto "Utiliza Cenários" do projeto origem estiver marcado.
   2. **Cópia Detalhada**: Receberá todas as funcionalidades que atualmente existem no processo:  
      * + Na aba de cada entidade (Sub-Projetos, Tarefa, Composições, etc) deverá ser exibido quais entidades estarão relacionadas com a cópia (Protótipo 02);
        + Na barra de cada visão das respectivas entidades deverá ser incluído uma nova opção de filtro que permite com que os itens a serem copiados, possam ser filtrados por código utilizando a vírgula ou a quebra de linha como separadores (Protótipo 03);
        + As abas deverão ser reorganizadas, de acordo com a prioridade de utilização, seguindo a seguinte ordem: Parâmetros, Insumos, Composições, Sub-Projetos, Tarefas, Disciplinas, Grupos de Custo, Modelos de Taxa, Curvas de Distribuição, Equipes do Projeto, Cenário.
   3. **Cópia por Planilha:** Deverá possibilitar uma cópia (importação) a partir de uma planilha em Excel para as planilhas de atividade e(ou) serviço (Protótipo 04):  
      * + Inicialmente o usuário deverá definir o projeto de origem pois as informações de recursos (composições e insumos) associados às tarefas serão copiadas desse projeto;
        + O usuário poderá selecionar o cenário no qual receberá a importação, este somente estará habilitado se o parâmetro de projeto "Utiliza Cenários" estiver marcado;
        + O usuário terá a possibilidade de selecionar duas planilhas Excel, uma para cada tipo de planilha do projeto, porém para a Planilha de Serviços somente será possível definir o arquivo se o projeto fizer utilização da mesma (parâmetro de projeto "Utiliza Planilha de Serviço");
        + A importação em Excel depende de um layout pré definido e para isso será disponibilizado o layout semelhante ao processo de importação de tarefas considerando, também, as preferências de usuário salvas anteriormente no processo;
        + Ao solicitar a cópia a partir das planilhas, primeiramente será verificado a existência dos recursos (composições e insumos) do arquivo em relação ao projeto origem pré-definido, então, a cópia será realizada e em seguida, a importação das tarefas existentes nas respectivas planilhas;
        + Nessa opção de cópia o usuário terá a possibilidade de também copiar os parâmetro do projeto origem, selecionando a opção "Copiar parâmetros do projeto origem".
2. Alterações no processo de Importação de Tarefas em Excel  
     
   O processo de Importação de Tarefas em Excel deverá ser alterado permitindo, também, a importação da Planilha de Serviços e uma nova opção deverá ser incluída no layout que é a coluna na qual existirá o vínculo do serviço a atividade, sendo que o mesmo somente será considerado ao importar a planilha de atividades (Protótipo 05). A possibilidade de cópia da Planilha de Serviços somente estará disponível se o parâmetro de projeto  "Utiliza Planilha de Serviço" do projeto estiver marcado.

 **Importante:**

* + **As demais regras de cópia do processo que não foram citadas neste documento não terão seu comportamento alterado;**
  + **Existirá um controle de segurança para a utilização da aba "Copia por Planilha", pois assim como o processo de Importação de Tarefas em Excel que possui um controle, é necessário o mesmo tratamento para essa nova funcionalidade;**
  + **A Copia por Planilha somente será permitida se a permissão de cópia de Insumos e Composições estiver habilitada;**
  + **Existirá um controle de segurança para a utilização da aba "Copia Simplificada";**
  + **O controle de segurança existente para as funcionalidades da aba "Cópia Detalhada" deverá ser considerado nas demais abas de acordo com a entidade a ser copiada, como por exemplo: se não existir permissão para a cópia de parâmetros, esta não deverá ser permitida nas três abas;**
  + **A utilização das abas do menu deverão ser consideradas na preferência de usuários sendo que inicialmente, caso a preferência ainda não esteja definida (primeiro acesso à nova tela), a aba padrão deverá ser a "Cópia Detalhada".**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Cópia de Itens] | [Alteração] | [Orçamento -> Cópia de Itens] | Melhoria de Usabilidade |
|  |  |  |  |
|  |  |  |  |

## 

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

****Protótipo 03****

**Protótipo 04**

****Protótipo 05****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
