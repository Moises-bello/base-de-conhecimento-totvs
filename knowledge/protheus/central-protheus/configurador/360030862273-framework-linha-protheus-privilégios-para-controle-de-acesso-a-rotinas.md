---
article_id: 360030862273
category: Configurador
content_hash: 64d4850269909f6a39c41e57425cfd4e0d00be73127562b81e5326415cce47a5
fetched_at: '2026-06-28T22:42:19.293621+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus - Privilégios para controle de acesso a rotinas
type: support-article
updated_at: '2024-05-08T11:54:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030862273-Framework-Linha-Protheus-Privil%C3%A9gios-para-controle-de-acesso-a-rotinas
---

**Dúvida**Como configurar os Privilégios para controlar o acesso às rotinas?  
   
 **Ambiente**Protheus - Configurador - a partir da Versão 11  
  
**Solução**A rotina Privilégios do Protheus permite definir regras de acessos a rotinas para usuários e grupos, facilitando a administração e manutenção de direitos.  
  
Para configurar a rotina Privilégios, existem 2 opções:  
1. **Inclusão manual de rotinas**: você cria um novo privilégio e inclui apenas as rotinas que deseja configurar.  
- Acesse Configurador > Usuário > Senhas > **Privilégios**  
- Clique em **Incluir**  
- Defina um nome (campo **Regra**) e descrição (campo **Comentário**) para o Privilégio  
- Clique 2 vezes abaixo da coluna **Transação/Rotina**, e digite o nome do objeto da rotina que deseja configurar (MATA010 por exemplo)  
- Para incluir outras rotinas, pressione **seta para baixo** no teclado

|  |
| --- |
| **Informação** Para a maioria das rotinas, é possível visualizar o nome do objeto pressionando a tecla **SHIFT+F6** na tela da rotina. Algumas rotinas, como a rotina **Spool** do menu **Miscelânea**(que possui o nome de objeto OURSPOOL), podem não exibir o nome real do objeto no SHIFT+F6. Nestes casos, recomendamos entrar em contato com a equipe de suporte responsável pelo módulo para verificar o nome a ser utilizado. |

![PR_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042108694)

|  |
| --- |
| **Nota** A partir da lib com label 20170208 será permitido controlar o acesso de **funções de usuário**. Para isso, faça o cadastro informando o "U\_" e sem o "()", como no exemplo: U\_CUSTFUNC.  Para funções de usuário que queriam ter suas **funcionalidades** controladas é necessário que a mesma esteja compilada em um fonte de mesmo nome e que possua implementada a função estática MenuDef() que é responsável pela definição do menu de funcionalidades.  Exemplo de Fonte: custfunc.prw User Function CustFunc Private aRotina := MenuDef() //... restante do código. Return  Static Function Menudef Local aRotina := { {"Pesquisar" ,"AxPesqui",0,1} ,; {"Visualizar" ,"AxVisual",0,2} ,; {"Incluir" ,"AxInclui",0,3} ,; {"Alterar" ,"AxAltera",0,4} ,; {"Excluir" ,"AxDeleta",0,5}} Return aRotina |

2. **Inclusão de todas as rotinas de um menu**: você cria um novo privilégio baseado em um menu. Todas as rotinas desse menu serão carregadas para configuração.  
- Acesse Configurador > Usuário > Senhas > **Privilégios**  
- Clique em **Incluir**  
- Clique em **Outras Ações** (Ações Relacionadas) e selecione **Menu**![PR_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042108714)  
  
- Clique em **Avançar**, clique na **Lupa** e localize o arquivo .xnu do menu que deseja configurar os privilégios  
  
![PR_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042956273)  
  
- Clique em **Finalizar.** As rotinas do menu serão carregadas  
  
![PR_04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042956253)  
  
- Após incluir as rotinas na seção **Regras por transação/rotina**, clique sobre cada rotina para exibir os itens de menu na seção **Funcionalidades das transações/rotinas**  
- Ao lado de cada rotina na seção **Regras por transação/rotina**, na coluna **Acesso**, é possível definir o acesso à rotina como: **Negado, Permitido** ou **Não Permitido**.  
- Ao lado de cada item de menu na seção **Funcionalidades das transações/rotinas**, na coluna **Acesso**, é possível definir o acesso ao item de menu como: **Negado**, **Permitido** ou **Não Permitido**.  
  
![PR_05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042956293)

|  |
| --- |
| **Dica** O conceito para as opções **Permitido** / **Não Permitido** / **Negado** é utilizado quando se utiliza mais de um privilégio para um usuário ou grupo. Desta forma, na listagem de privilégios, se for detectada uma mesma rotina, e em um dos privilégios ela estiver como **Negado**, ela sobrepõe qualquer outro privilégio desta rotina que esteja como **Permitido** ou como **Não Permitido**. Se uma rotina tem um privilégio como **Não permitido**, é feita uma verificação desta rotina em outros privilégios neste usuário, se não tiver como **Permitido** em nenhum abaixo, fica como **Não Permitido**, mas se tiver como **Permitido** em algum privilégio, fica como **Permitido**. Desta forma, a ordem de prioridade desta configuração é: **Negado** > **Permitido** > **Não Permitido**. |

- Após concluir a configuração das rotinas do Privilégio, clique em **Confirmar  
  
  
Associando Privilégios a um usuário ou grupo de usuários**Com o privilégio configurado, para que ele entre em vigor, você deve associá-lo a um Usuário ou Grupo de Usuários.  
- Acesse Configurador > Usuário > Senhas > **Usuários** (ou **Grupos**)  
- Clique no usuário (ou grupo) e clique em Outras Ações > **Ações Relacionadas**  
- Clique em **Privilégios  
  
![PR_06.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042108754)**- Clique 2 vezes abaixo da coluna **Regra**e clique na **Lupa**  
- Selecione o privilégio que deseja associar a este usuário/grupo e clique em **OK**  
- Caso queira que este privilégio tenha efeito apenas em determinada Empresa/Filial, digite o código destas nas colunas **Grupo de Empresas** / **Filial do Sistema**. Caso queira que este privilégio tenha efeito para todas as empresas/filiais que o usuário tem acesso, deixe estes campos **em branco**![PR_07.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042108734)  
  
- Clique em **Confirmar**. A Regra de Privilégio está configurada.

|  |
| --- |
| Maiores informações sobre a configuração de usuários: [Configurar usuários](http://tdn.totvs.com/pages/viewpage.action?pageId=271186036) Maiores informações sobre a configuração de grupos: [Criar um Grupo de Usuários](http://tdn.totvs.com/pages/viewpage.action?pageId=271388115) |
