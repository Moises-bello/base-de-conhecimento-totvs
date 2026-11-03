---
content_hash: 80e85e5849c0ba777c5107376655fed779099bff2f7d92d8d4d3e82f07e88962
fetched_at: '2026-06-29T00:06:10.626278+00:00'
page_id: '203765549'
product: rm
source: tdn-rm
title: 5. Configuração do menu html
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203765549
version: 5
---

Os serviços do Corpore RM com as funcionalidades para utilização do TOTVS | HTML Framework estarão disponíveis em 2016. No momento versões controladas serão disponibilizadas para as equipes de Segmentos envolvidas no projeto de Experiências de Uso.

Versão

 Disponível à partir da versão 12.1.8 da linha RM.

Definição do Menu HTML

A estrutura de menu html é definida em banco de dados (GMENUHTML) com os seguintes campos:

ID - identificação do menu  
PARENTID - identificação do pai  
CODSISTEMA - código do sistema onde o mesmo está sendo criado.  
CAPTION - Descrição para o mesmo  
PATH - caminho virtual, somente deve ser setado para as rotinas, agrupadores não devem contar conteúdo.  
SECURITYID - Id de segurança da rotina, similar à tag de segurança da action.  
EXECUTIONID - id se execução, utilizado nos casos de policy, como por exemplo: incluir/excluir/editar

O modelo de permissão é similar ao que temos no portal, portanto cada produto possui um "XxxPofileRibbonControl" com a estrutura de menu do portal e "XxxActionModuleController" que possui as tags de segurança.

Ou seja devemos inserir nosso menu html nesse mesmo modelo para que os itens sejam disponibilizados na treeView de segurança do respectivo modulo na edição do perfil em globais.

É necessário que o modelo definido no "XxxProfileRibbonControl" esteja coerente com o modelo definido na GMENUHTML

# Exemplo de criação de menu

O correto é, ao ser disponibilizada uma nova tela, ser gerado um script de inserção na GMENUHTML, de qualquer forma existe um CRUD para inserção dos itens de menu conforme print abaixo

Regras para geração do registro:

        \* O registro "root" é default e somente pode ser alterado a descrição.

        \* O registro que representa o módulo têm como parentID = root

        \* Os registros que são rotinas estão com a coluna "caminho absoluto da página" preenchido.

        \* Os registros que são policies do lado do RM, estão com Id de execução preenchido.

        \* Todos os registros seguem uma estrutura de árvore, ligada pelo parentID.

        \* A estrutura deve conter o mesmo conceito do RM de Page/Group/Item/Policy

Adicione no "XxxProfileRibbonControl" do seu respectivo módulo os itens seguindo a estrutura definida acima

Adicione no "XxxActionModuleController" do seu respectivo módulo as tags/policies definida na estrutura acima.

Adicione as tags de segurança nos respectivos dataServers, pois por se tratar de chamadas rest, o CheckPermission é executado no DataServer.

# Utilização do menu HTML

O serviço que disponibiliza a estrutura de menu html utiliza o alias do banco de dados definido na tag **DefaultDB**. Portanto,  é necessário que esta tag esteja definida no Host

# Exemplo do RM.Host.exe.config

]]>

A tela do frame já irá contemplar todos os menus cadastrados acima.

Para que os menus sejam disponibilizados no fluig será necessário executar o sincronismo com o Identity através do onClickConfiguration,
