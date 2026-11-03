---
content_hash: 361f38b528ebceb69b49dc7a3432f9e31957fa2febc95be18ce09d42f29ae463
fetched_at: '2026-06-29T00:11:17.411294+00:00'
page_id: '680234913'
product: rm
source: tdn-rm
title: Grupos.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680234913
version: 44
---

## O que são?

Grupos são funcionalidades do TOTVS Automação de Testes utilizadas para organizar e controlar o acesso dos usuários às atividades criadas no sistema. Eles permitem uma gestão eficiente das permissões, assegurando que cada usuário tenha acesso somente às atividades relevantes para seu papel ou projeto.

## Para que servem?

Os Grupos permitem que usuários se organizem conforme a necessidade das equipes, facilitando o controle de acesso e a gestão das atividades relacionadas a um produto ou projeto específico. Isso ajuda a manter a segurança e a integridade dos dados, além de simplificar a administração do sistema.

## Exemplo de Uso

Criação de um grupoComo Cadastrar1. Início do Cadastro

1. Após o login, um usuário administrador deve adicionar você a um grupo específico para que você possa acessar as atividades criadas pelos membros desse grupo. Se o grupo não existir, basta navegar até a seção **"Grupos"** na barra de menu do TOTVS Automação de Testes e clicar no ícone de pasta verde para criá-lo.

2. Definir Nome e Descrição do Grupo

Descreva o nome e a descrição desse Grupo. O nome do grupo deve representar para qual finalidade esse grupo está sendo criado, seja por produto ou para um projeto específico.

3. Adição de novos membros e definição do seu nível de acesso

Para adicionar um novo membro ao grupo, basta digitar o nome desse novo integrante na seção **"Membros"**e selecioná-lo dentre as sugestões apresentadas.

Após esse passo, selecione a permissão do usuário.

**- Administrador:** Tem acesso total às atividades criadas pelo grupo.  
**- Membro:** Tem acesso somente de leitura às atividades criadas pelo grupo.

4. Configurações de Notificações

Caso queira receber notificações sobre o grupo em questão via e-mail, você pode adicioná-lo clicando no seguinte ícone em questão.

5. Uso do sistema após a adição do usuário a um grupo

Após o usuário ser adicionado em um grupo, será possível para o mesmo criar, editar e executar atividades no TOTVS Automação de Testes.

*Exemplo de uma atividade que envolve a configuração de permissões para Grupos.*

Exemplo PráticoGestão de Equipes Diferentes

Tenho 2 times que atuam em sistemas diferentes. No Financeiro e no Educacional. Um time não pode ter acesso as automações criadas do outro time e nem podem executar as automações.

Neste caso, deve-se criar dois grupos filho do grupo todos e colocar cada membro das equipes em seus respectivos grupos.

Novo Integrante na Equipe

Suponha que entrou um novo integrante na equipe de Automação da Engenharia. Porém, esse usuário ao realizar login na ferramenta se deparou com a seguinte mensagem:

*"Você ainda não foi adicionado em nenhum grupo e por isso não conseguirá visualizar, editar ou executar nenhuma atividade.*

*Peça para que seu time te adicione em algum grupo."*

Além disso, o mesmo não obteve êxito ao tentar acessar qualquer atividade do seu time, visualizando uma lista em branco, e nem criar qualquer atividade. Diante dessa situação, o usuário deve solicitar a alguém do seu time, com permissão de administrador, para adicioná-lo ao grupo do time em questão.

Para isso, o usuário com permissão de administrador deve entrar no TOTVS Automação de Testes, navegar ao menu **Grupos**e editar esse grupo em questão.

Após clicar em editar esse grupo, deve-se adicionar pesquisar pelo **NOME** do usuário, na caixa de pesquisa **Membros**e selecionar na caixa de diálogo pelo usuário correspondente. Ele será adicionado ao final da lista de membros.

Após isso, deve-se ajustar a permissão do usuário.

E finalmente, clicar em salvar.

Com isso, irá aparecer uma mensagem de sucesso e será possível visualizar esse usuário na lista de membros

Após ser adicionado, o usuário poderá entrar novamente no TOTVS Automação de Testes e agora, conseguirá visualizar, editar e executar as atividades do seu time.

Além disso, agora o usuário também conseguirá criar uma nova atividade, associando essa atividade ao grupo em questão.

---

# Saiba mais

Os Grupos são definidos de acordo com a necessidade das equipes. Aconselha-se a definição de grupos por produto.

Grupos podem ser alterados ou excluídos pelos administradores. No entanto, a exclusão de um grupo resultará na exclusão de todas as atividades pertencentes a esse grupo.A exclusão de usuários é permitida apenas para membros administradores.Cada grupo deve ter pelo menos um usuário administrador para garantir a transferência de atividades quando necessário.

# FAQ

**P: O que acontece quando um grupo é excluído?**  
R: Todas as atividades pertencentes ao grupo serão automaticamente excluídas.

**P: É possível excluir todos os usuários de um grupo?**  
R: Não. Pelo menos um usuário administrador deve permanecer no grupo. Quando um usuário é excluído, as atividades pertencentes a ele são transferidas automaticamente para o primeiro usuário administrador.

**P: Quem pode excluir ou alterar grupos?**  
R: Apenas os administradores podem excluir ou alterar grupos.

**P: É possível visualizar, editar e executar alguma alguma atividade se meu usuário não pertencer a nenhum grupo?**  
R: Não. É necessário solicitar o seu time para que te adicione em algum grupo.

**P: Eu consigo ver as automações que foram criadas em outro grupo?**  
R: Não. O usuário só consegue visualizar as automações criadas no grupo em que ele pertence.

**P: Estou tentando adicionar um novo integrante, porém ele não aparece na pesquisa para adicionar usuários, o que pode ser?**  
R: O usuário deve estar cadastrado no Fluig Identity e ter permissões para visualizar o TOTVS Automação. Além disso, ele deve fazer o primeiro login na ferramenta. A partir desse momento será possível adicioná-lo aos membros de um grupo.
