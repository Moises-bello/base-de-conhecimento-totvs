---
content_hash: da2989c690736daa8de093bd3686821bfc5f0ee6c49a648ac07f64c3d42b0210
fetched_at: '2026-06-29T00:05:55.795646+00:00'
page_id: '146182940'
product: rm
source: tdn-rm
title: Segurança - Perfis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146182940
version: 73
---

## **01. VISÃO GERAL**

    O cadastro de Perfil fica localizado **em:** Serviços Globais | Segurança | Perfis"  se tratando de um item essencial do sistema, pois restringe ou permite o acesso aos módulos do sistema.

       Somente os usuários que possuírem o acesso de Supervisor do **módulo utilizado** poderão editar, excluir e alterar um perfil. Ao incluir ou editar um perfil é exibido os seguintes menus para edição:

## **02. EXEMPLO DE UTILIZAÇÃO**

### **IDENTIFICAÇÃO**

Menu **"Identificação****"** na visão de cadastro de perfil

       

        A aba **"Identificação"** é utilizada para o controle dos perfis criados, onde é necessário preencher os campos **Cód. Perfil**, **Identificação** e **ativo**.

**Campos disponíveis:**

**Cód. Perfil:** Uma vez que o perfil foi criado não é possível alterar o campo Cód. Perfil.

**Identificação:** Este campo serve para identificar o perfil criado, pois podemos ter mais de um perfil com o mesmo Cód.Perfil, porém em **módulos** diferentes.

**Ativo:** Esta opção serve para ativar e desativar o perfil.

**Perfis compartilhados entre módulos**

Atenção

Disponível a partir das versões **12.1.31** , **12.1.29 e 12.1.28.**

Nas versões **12.1.28.227** e **12.1.29.158** é necessário executar o script **CP.2020.11\_02** para que a funcionalidade seja habilitada.

Atenção

A partir das versões abaixo o compartilhamento de Perfil entre Módulos será desabilitado, pois a funcionalidade será revista em versões futuras.

| Versões |
| --- |
| 12.1.34 |
| 12.1.33.145 |
| 12.1.32.218 |
| 12.1.31.272 |

Para quem já tem perfis compartilhados entre módulos, a funcionalidade continuará funcionando.

Não será permitido editar e incluir novos perfis compartilhados.

Os perfis compartilhados são um novo conceito para criação de perfis no RM. Agora podemos criar um perfil em um módulo, e conceder também acesso a vários outros módulos usando o mesmo perfil. Esta funcionalidade está disponível a partir dos patches mais recentes da versão 12.1.28.

Dessa forma, por exemplo, é permitido criar um perfil "Admin", que tem permissões no módulo de Serviços Globais e Educacional ao mesmo tempo. O perfil irá aparecer em ambos os módulos, quando selecionados na tela de cadastro de perfil, para que sejam cadastradas as permissões relativas a acesso a campos e menus de cada módulo.

No **cadastro de perfil**é possível selecionar os módulos que o perfil em edição terá acesso, além do módulo de origem, que é o que está selecionado na Action.

Apensas usuários supervisores do módulo poderão editar e visualizar a lista de cadastro dos módulos em que o perfil terá acesso. 

Na listagem de seleção dos módulos, não é possível editar o módulo de origem. Da mesma forma, os módulos que já foram marcados anteriormente não poderão ser editados. Veja a imagem abaixo como exemplo.

O perfil da figura acima (DBA\_G) , tem origem no módulo Integração (sigla G), mas também tem acesso ao Educacional e Processo seletivo. Ou seja, o perfil DBA além de ser visível em globais, também será visível no módulo educacional.

Indisponibilidade de desvinculação

Tenha certeza ao adicionar outro módulo ao perfil. Por questões de segurança e integridade, após dar permissão em um módulo não é possível desvincular o mesmo do perfil.

RM Reports

Por questões de segurança, a funcionalidade de "Perfil compartilhados entre módulos" não se aplica para relatórios, portanto na tela de Relatórios só serão apresentados os relatórios do módulo de origem do perfil.

[Saiba mais em "RM Reports"](https://tdn.totvs.com/x/a4NMBQ)

Relatório de permissão 

O processo de "Relatório de Permissões aos Itens de Menu" só exibem as permissões do módulo de qual o perfil é o originado.

Na tela de perfis temos duas novas colunas, a coluna "Cód. Sistema" que irá confirmar a sigla de origem do perfil, e a "Aplicações" que guarda as siglas de todos os módulos em que o perfil tem acesso

Quando a coluna "Aplicações" estiver preenchida é um indicativo que é um perfil compartilhado, e tem acesso aos módulos indicados.

Saiba mais sobre como atribuir estes perfis aos usuários: 

## **03.** **ACESSO A****CAMPOS**

Menu **"Acesso a Campos"** na visão de cadastro de perfil

       

        A aba **"Acesso a Campos"** é utilizada para restringir e/ou permitir que o perfil possa **consultar** ou **alterar**, no sistema, o campo da base selecionado, na árvore de acesso.

**Exemplo:**

        Os campos que possuírem o ícone o perfil vai poder **consultar** e **alterar** o campo no sistema.

        Os campos que possuírem o ícone o perfil poderá somente **consultar** o campo no sistema, ficando como **somente leitura**.

        Os campos que possuírem o ícone o perfil não poderá **consultar** nem **alterar** o campo no sistema, o campo ficará **invisível.**

**Cache de Segurança de campos**

A partir dos patches 12.1.23.196, 12.1.24.127 e versão 12.1.25, quando uma tabela tem restrição na GAUTZTAB e o usuário altera essa restrição, as alterações nas permissões em campos **serão propagadas após no máximo 2 minutos estando o usuário usando ou não o sistema**, não tendo a necessidade da reinicialização do Host.

Nas versões **anteriores** aos patches **12.1.24.127 e 12.1.23.196** as alterações de restrição serão propagadas após 2 minutos de **inatividade** do usuário em questão, não tendo a necessidade da reinicialização do Host. 

**Obs:** Estes acessos são setados em cada campo da base na opção de permissões.

Reforçamos que a ***restrição de um campo prevalecerá*** nos casos onde haja perfis diferentes, do mesmo produto ou não, associados ao usuário.

## **04.** **ACESSO A MENUS**

        Menu **"Acesso a Menus"** na visão de cadastro de perfil

             

       A aba **"Acesso a Menus"** serve para **permitir** ou **proibir** o acesso do perfil aos **menus** e **operações**do sistema**.**

**Permissões**serão adicionadas através da opção

       Os itens que possuírem o ícone **poderão**acessar o(s) menu(s) ou a(s) operação(ões) do sistema.

**Restrições**serão adicionadas através da opção

       Os itens que possuírem o ícone  **não** poderão acessar o(s) menu(s) ou a(s) operação(ões) e **nenhum** outro módulo do sistema será afetado nesta permissão.

       Os itens que possuírem o ícone  **compartilham** da mesma opção com outros módulos. Indicando que o(s) menu(s) ou a(s) operação(ões) de outros módulos **serão** afetados nesta permissão.

       No caso das **restrições** o menu ou a operação do sistema poderão ser exibidos de duas formas: **visível e desabilitado** ou **invisível** para o perfil.

* **Cada módulo do sistema possuí sua árvore de menus.**

Permissão

* **O item da árvore de menu pode ser permitido  em apenas um módulo em que o usuário tiver acesso para que a permissão seja aplicada.**

**Exemplo:**O item da árvore do módulo "Folha de Pagamento" possui a permissão e o item da árvore de menus do módulo "Serviços Globais" possui a restrição .Neste caso irá prevalecer a permissão . O Usuário terá acesso a funcionalidade devido a permissão que ele possui no módulo "Folha de Pagamento".

 

Restrição

* **Para que a restriçãoseja aplicada, todos os perfis, do mesmo produto ou de outros outros, deverão estar configurados com a proibição, Havendo a possibilidade de um perfil divergente a restrição não será efetiva.**

**Exemplo:**O item da árvore de menus do módulo "Folha de Pagamento" possui a restriçãoe o item da árvore do módulo "Gestão de Pessoas" possui a restrição irá prevalecer a restrição. O Usuário não terá à permissão pois é restrito em todos os módulos que possui acesso.

                           O item da árvore de menus do módulo "Folha de Pagamento - Perfil DBA" possui a restrição e o item do mesmo produto, porém do perfil "Perfil DP" possui permissão. Irá prevalecer a . O Usuário continuará com permissão pois existe restrição somente em um dos perfis do mesmo módulo atribuídos ao mesmo usuário.

Veja como criar [relatórios customizados de Permissão aos itens de Menu](https://tdn.totvs.com/pages/viewpage.action?pageId=272431175).

## **05.** **ACESSO A RELATÓRIOS / PLANILHAS:**

        Menu **"Acesso à Relatórios/Planilhas"** na visão de cadastro de perfil

        

        A aba **"Acesso à Relatórios/Planilhas"** serve para criar um grupo de relatórios/planilhas, que serão acessados **somente** pelos perfis que possuírem este grupo.

        Para maiores informações acesse: ["Acesso à Relatórios/Planilhas"](http://tdn.totvs.com/x/lgqxAw)

false

**Versão:** 11.82.44 ou Superiores

## **06. PERMISSÃO DE SEGURANÇA PARA WIZARD DE PARAMETRIZAÇÃO**

No menu anexos, selecione o item para abrir a tela de permissão de segurança...

Nesta tela é possível configurar as permissões de segurança de cada item referente ao Wizard de configuração. Pode-se selecionar toda uma árvore ou apenas um único item.

* + Pode Consultar  
    Permite apenas visualizar, realizando o bloqueio dos campos apresentados na tela.
  + Pode Alterar  
    Permite visualizar e alterar os campos. Esta é a opção padrão, onde as duas caixas de seleção são marcados.
  + Bloqueio total  
    Remove o item da tela de Wizard. Deve-se desmarcar ambas caixas de seleção.

Legenda dos ícones:

* + Apresentam dois Checks, indicando que as duas caixas de seleção estão marcadas.
  + Apresenta apenas um Check, indicando que somente a opção Pode Consultar, esta marcada.
  + Apresenta um X, indicando que nenhuma opção foi marcada.
