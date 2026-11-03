---
article_id: 26789534231063
category: Financeiro
content_hash: caf82633f248f4eb831c6f25aa9e083abe712bec60b103cfc8f290896db68797
fetched_at: '2026-06-28T22:38:01.179345+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - Configurar privilégios para gerenciar
  o acesso às rotinas
type: support-article
updated_at: '2024-10-03T13:12:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26789534231063-Cross-Segmentos-Backoffice-Linha-Protheus-Configurar-privil%C3%A9gios-para-gerenciar-o-acesso-%C3%A0s-rotinas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26806219727255) Tempo aproximado para leitura: 00:13:00 min**

**Dúvida**  
Como definir restrições para o usuário?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

A rotina de **Privilégios do Protheus** permite definir regras de acesso às rotinas para **usuários e grupos**, facilita a administração e manutenção dos direitos de acesso.

Para configurar a rotina de Privilégios, há duas opções disponíveis:

1. **Inclusão manual de rotinas**: você pode criar um novo privilégio e incluir apenas as rotinas que deseja configurar.
   * Acesse: **Configurador** **> Usuário > Senhas > Privilégios**
   * Clique em "**Incluir**"
   * Defina um nome (campo "**Regra**") e uma descrição (campo "**Comentário**") para o privilégio.
   * Clique duas vezes na coluna "**Transação/Rotina**" e digite o **nome do objeto** da rotina que deseja configurar (por exemplo, **MATA010**).
   * Para incluir outras rotinas, pressione a seta para baixo no teclado.

**Importante**

Para a maioria das rotinas, é possível visualizar o nome do objeto pressionando a tecla **SHIFT+F6** na tela da rotina. No entanto, algumas rotinas, como a rotina *Spool* do menu **Miscelânea** (que possui o nome de objeto *OURSPOOL),* podem não exibir o nome real do objeto ao utilizar o **SHIFT+F6**. Nesses casos, recomenda-se entrar em contato com a equipe de suporte responsável pelo módulo para verificar o nome a ser utilizado.

![Gravar_2024_10_02_15_09_31_668.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26789534219799)

**Nota:**

A partir da lib com label 20170208 será permitido controlar o acesso de funções de usuário. Para isso, faça o cadastro e informe o "**U\_**" e sem o "**()**", como no exemplo: **U\_CUSTFUNC**

Para funções de usuário que queriam ter suas funcionalidades controladas é necessário que a mesma esteja compilada em um fonte de mesmo nome e que possua implementada a função estática **MenuDef()** que é responsável pela definição do menu de funcionalidades.

**Exemplo de Fonte: custfunc.prw**

`User``Function` `CustFunc`

`local aRotina := MenuDef()`

`//... restante do código.`

`Return`

`Static``Function` `Menudef`

`Local aRotina :=``{ {"Pesquisar" ,"AxPesqui",0,1}` `,;`

`{"Visualizar" ,"AxVisual",0,2}` `,;`

`{"Incluir" ,"AxInclui",0,3}` `,;`

`{"Alterar" ,"AxAltera",0,4}` `,;`

`{"Excluir" ,"AxDeleta",0,5}``}`

`Return aRotina`

**2. Inclusão de todas as rotinas de um menu:** você pode criar um novo privilégio baseado em um menu, permitindo que todas as rotinas desse menu sejam carregadas para configuração.

* Acesse: C**onfigurador > Usuário > Senhas > Privilégios**
* Clique em **"Incluir"**.
* Clique em **"Outras Ações"** (Ações Relacionadas) e selecione **"Menu".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26789731203991)

Clique em **"Avançar"**, em seguida, clique na **Lupa** e localize o **arquivo .xnu** do menu para o qual deseja configurar os privilégios.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26789731205911)

Clique em "**Finalizar**". As rotinas do menu serão carregadas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26790685461143)

* Após incluir as rotinas na seção **"Regras por transação/rotina"**, clique em cada rotina para exibir os itens de menu na seção **"Funcionalidades das transações/rotinas"**.
* Ao lado de cada rotina na seção **"Regras por transação/rotina"**, na coluna "**Acesso**", é possível definir o nível de acesso à rotina como: **Negado, Permitido ou Não Permitido.**
* Ao lado de cada item de menu na seção **"Funcionalidades das transações/rotinas"**, na coluna **"Acesso"**, é possível definir o nível de acesso ao item de menu como: **Negado, Permitido ou Não Permitido.**

`![Gravar_2024_10_02_15_30_26_562.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26790663599767)`

**Dica:**

O conceito para as opções **Permitido / Não Permitido / Negado** é utilizado quando se utiliza mais de um privilégio para um usuário ou grupo.

Desta forma, na listagem de privilégios, se for detectada uma mesma rotina, e em um dos privilégios ela estiver como **Negado**, ela sobrepõe

qualquer outro privilégio desta rotina que esteja como **Permitido** ou como **Não Permitido**. Se uma rotina tem um privilégio como **Não permitido**,

é feita uma verificação desta rotina em outros privilégios neste usuário, se não tiver como **Permitido** em nenhum abaixo, fica como **Não Permitido**,

mas se tiver como **Permitido** em algum privilégio, fica como **Permitido**. Desta forma, a ordem de prioridade desta configuração é: **Negado > Permitido > Não Permitido.**

**Importante**

Quando um usuário estiver associado a mais de um grupo e a regra não estiver configurada para desconsiderar grupos, os privilégios dos grupos serão sempre somados.

O campo da **grade de grupos**, configurado como "**Priorizar igual a Sim**", não será levado em consideração. Em caso de conflito de privilégios, será aplicada a regra de

hierarquia mencionada anteriormente.

* Após concluir a configuração das rotinas do **privilégio**, clique em "**Confirmar**"

**Associando Privilégios a um Usuário ou Grupo de Usuários**

Com o privilégio configurado, para que ele entre em vigor, é necessário associá-lo a um Usuário ou Grupo de Usuários.

* Acesse: **Configurador > Usuário > Senhas > Usuários (ou Grupos)**
* Selecione o usuário (ou grupo) e clique em **"Outras Ações"** (Ações Relacionadas).
* Clique em **"Privilégios"**.

![Gravar_2024_10_02_15_37_18_621.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26790685469335)

* Clique duas vezes na coluna "**Regra**" e em seguida, clique na **Lupa**.
* Selecione o privilégio que deseja associar a este **usuário** ou **grupo** e clique em "**OK**".
* Se desejar que esse privilégio tenha efeito apenas em uma determinada **Empresa/Filial**, insira o código correspondente nas colunas "**Grupo de Empresas**" > "**Filial do Sistema**"
* Se preferir que o privilégio seja aplicado a todas as **empresas/filiais** às quais o usuário tem acesso, mantenha esses campos em branco.

**Visualizando Usuários Relacionados ao Privilégio**

Após associar o privilégio a **usuários** ou **grupos de usuários**, é possível visualizar quais usuários estão relacionados a ele:

* Acesse: **Configurador > Usuário > Privilégios > Localize o privilégio desejado > Clique em "Alterar" > "Outras Ações" > "Usuários Relacionados"**

![Gravar_2024_10_02_15_46_54_408.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26790685470359)

A coluna **"Definição do Privilégio"** indica a origem do privilégio:

* **"Usuário"**: utilizado quando o privilégio é associado diretamente ao usuário por meio de seu cadastro.
* **"Grupo"**: utilizado quando o privilégio é associado ao usuário por meio do cadastro de grupo.
* **"Ambos"**: utilizado quando o privilégio é associado ao usuário tanto pelo cadastro de usuário quanto pelo cadastro de grupo.

**Importante**:   
Os usuários que pertencem a um grupo e têm a opção "**Regra de acesso por grupo**" configurada como "**Desconsiderar**" não são exibidos nessa lista.

A coluna "**Definição do Privilégio**" está disponível a partir da versão 20220905.

**Saiba mais**

[Privilégio](https://tdn.totvs.com/pages/releaseview.action?pageId=271389653)
