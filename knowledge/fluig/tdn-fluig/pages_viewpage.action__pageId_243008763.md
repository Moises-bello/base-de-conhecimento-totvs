---
content_hash: 3ff8776325d3e40262074cbde58f565f3e422fce99bbdfdd23a6071d15798223
fetched_at: '2026-06-28T21:35:22.949632+00:00'
page_id: '243008763'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Definir critérios de aprovação para pasta ou para documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243008763
version: 42
---

# Falando de definir critérios de aprovação para pasta ou para documento...

---

A aprovação de conteúdo publicado na plataforma pode ser efetuada tanto por pastas como por documentos.

Ao definir critérios de uma pasta para que tenham aprovadores, todo conteúdo que é publicado nela passará por essa aprovação, exceto se houverem subpastas em que a opção 'Herdar aprovadores do pai?' esteja desmarcada.

A aprovação por documento somente é possível quando ele é publicado em uma pasta que não possui aprovação. Nesse caso, os critérios são definidos no momento da criação do documento. O conteúdo publicado pelo próprio usuário aprovador da pasta também passará por aprovação, pois além de aprovador ele pode também ser publicador e incluir documentos na pasta. Essa ação é necessária para garantir maior assertividade quanto a publicação e aprovação de documentos na plataforma.

acessar

## Acessar configuração de aprovação

---

**01**. No menu principal, clique em **Documentos**.

**02**. Localize a pasta ou o documento que deve ter a aprovação configurada.

**03**. Clique em **Mais ações** referente à pasta ou ao documento e clique na opção **Propriedades**.

**04**. Clique na aba **Aprovação**.

## Adicionar nível de aprovação

---

O recurso de aprovação é configurado em 1 ou mais níveis, isto é, pode-se determinar que a publicação de uma pasta ou documento passe por vários níveis de aprovação.

******[Visualize o passo a passo](http://tdn.totvs.com/download/attachments/243008763/definir%20criterios%20de%20aprovacao.gif?version=1&modificationDate=1519149817449&api=v2)******

**01.** Clique na aba **Aprovação** conforme apresentado no item .

**02**. No campo **Nível de aprovação**, insira um nome para o nível de aprovação.

**03.** Clique em **Adicionar**.

**04.** Defina os usuários ou grupos que farão parte do nível de aprovação.

#f2f2f2#f2f2f2

Clique em **Usuários** para incluir um usuário como aprovador da pasta ou do documento. No campo **Buscar**, digite o nome do usuário e clique sobre o mesmo para incluí-lo como um aprovador.

Clique em **Grupos** para incluir um grupo de usuários como aprovador da pasta ou do documento. No campo **Buscar**, digite o nome do grupo e clique sobre o mesmo para incluí-lo como um grupo aprovador.

Para remover um usuário ou um grupo de usuários do nível de aprovação, clique no ícone .

Fique atento às configurações de segurança do documento!

É necessário que o usuário aprovador possua pelo menos a permissão de leitura no documento a ser aprovado, pois caso contrário não poderá acessar o documento para aprovação.   
Lembrando que a segurança do documento não depende de aprovação: se for retirada a permissão de um documento em aprovação, essa regra será aplicada nesse mesmo momento, bloqueando o acesso ao documento que foi enviado para aprovação.

**05.** Defina as demais informações para o nível de aprovação.

#f2f2f2#f2f2f2

**Condição de aprovação**  
Condição de aprovação para as publicações efetuadas na pasta. As opções disponíveis são:  
  
- **E**: quando selecionada, determina que devem ser levadas em consideração as opiniões de todos os aprovadores do nível, para que o documento seja publicado ou encaminhado para o próximo nível de aprovação. Caso um documento seja reprovado por algum usuário, ele não será mais exibido, pois será reprovado automaticamente;

- **OU**: quando selecionada, determina que basta receber o parecer de apenas um dos aprovadores do nível para que o documento seja publicado ou encaminhado ao próximo nível de aprovação;

#00000#f2f2f2

A diferença entre a condição **OU** e **Único** é que na OU para o documento ser reprovado, todos precisam reprovar entrando em consenso. Caso a maioria reprove, mas pelo menos um aprovar, o documento será aprovado.

- **Único aprovador**: quando selecionada, determina que, quando existe uma lista de aprovadores, a decisão do primeiro aprovador será definitiva para todo esse grupo de aprovadores. Isso tanto para a aprovação quanto para a reprovação. 

**Este nível requer assinatura digital**  
Quando assinalado, determina que a aprovação desse nível deverá utilizar assinatura digital. Essa opção só é disponibilizada caso o recurso  esteja configurado para essa empresa.

**06.** Após alterar as propriedades desejadas da pasta ou do documento, clique em **Confirmar** para gravar as alterações.

## Remover nível de aprovação

---

Antes de remover o nível de aprovação, é necessário aprovar todos os documentos que estiverem pendentes de aprovação.

**01.** Clique na aba **Aprovação** conforme apresentado no item .

**02**. Clique na aba referente ao nível de aprovação a ser removido, caso possua mais de uma.

**03**. Clique no **X** apresentado ao lado do nome do nível da aprovação. Ela será removida sem uma prévia confirmação.

oculto
$("b:contains('oculto')").parent().parent().hide();
]]>Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
