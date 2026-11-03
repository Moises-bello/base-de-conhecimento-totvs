---
content_hash: d1704a0684469cddce4ce5a491ac7f5f5ce33663be56c6cf175ac3041a32fa1b
fetched_at: '2026-06-29T00:11:02.778386+00:00'
page_id: '61934230'
product: rm
source: tdn-rm
title: Grupos de Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61934230
version: 59
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é explicar o que são e como trabalhar com Grupos de Relatórios.

# Introdução:

---

**Trabalhando com Grupos de Relatórios****:** 

       A opção para cadastramento de Grupos de Relatórios permite organizar e relacionar os relatórios disponíveis por grupos. Para isso, em cada relatório deverá ser informado, no campo Grupo de Relatórios, o grupo pelo qual ele pertencerá.

**Por que criar Grupos de Relatórios?** 

        Os Grupos de Relatórios devem ser criados para que somente usuários que tenham permissão de acesso ao grupo possam visualizar o relatório. Essas permissões serão definidas na guia de **Acesso à Relatórios/Planilhas**, no menu do formulário de cadastro de perfil.

# Criação dos Grupos por Perfil

---

**Formulário de edição do Perfil** 

       Através do formulário de edição de Perfis pode-se acessar a guia de **Acesso à Relatórios/Planilhas** onde serão apresentados os Grupos de Relatórios/Planilhas já cadastrados para o perfil selecionado, com seus respectivos níveis de alteração e emissão.

       O usuário logado no sistema poderá criar/alterar os Grupos desde que ele seja supervisor do módulo em questão. Após criar os grupos de relatórios/planilhas, todos os usuários que estiverem associados ao perfil pertencerão aos grupos dele também. Para cada grupo será cadastrado o nível de permissão de alteração e emissão dos relatórios/planilhas.

# Atribuição de Grupo ao Relatório:

---

         Para atribuir um nível de acesso ao relatório, acesse a guia **Gestão | Ferramentas de Análise | RM Reports**. Selecione o relatório desejado na listagem de relatórios e clique no ícone “Editar”, ou tecle “Control + Enter”. No formulário das propriedades do relatório, na opção “Grupo”, pesquise e selecione o grupo desejado.

         Para alterar o nível de acesso do relatório, modifique o valor do campo “Nível de Acesso” de acordo com o nível de segurança planejado.

Observações

Serão listados para escolha de “Grupo” somente os grupos de relatório que estiverem associados ao perfil do usuário que estiver configurando esta segurança. Caso o usuário seja supervisor, serão listados todos os grupos de relatórios que estiverem vinculados em todos os perfis do módulo corrente.

O sistema não permitirá que seja atribuído ao “Nível de Acesso” valor maior que o “Nível de Alteração” definido no grupo selecionado associado ao perfil do usuário que estiver configurando esta segurança.

# Exemplos

---

Abaixo estão descritos dois exemplos distintos para melhor entendimento da aplicabilidade de Grupos de Relatórios/Planilhas.

falseExemplosExemplo 1Exemplo 1Exemplo 1

O usuário João possui um perfil como acesso a relatórios do grupo “Listagens” com nível de alteração um (01) e emissão dois (02).

**Situações:**

1)    Relatório sem grupo - João poderá alterar e emitir esse relatório. Pois este relatório está desprotegido.

2)    Relatório com grupo diferente do grupo “Listagens” - João não poderá alterar e emitir esse relatório. O relatório não será exibido na visão de relatórios para João porque ele não possui permissão de acesso a este outro grupo.

3)    Relatório do grupo “Listagens” com nível de acesso igual a um (01) - João poderá alterar e emitir esse relatório porque o nível de acesso ao relatório é menor ou igual aos níveis de alteração e emissão no perfil.

4)    Relatório do grupo “Listagens” com nível de acesso igual a dois (02) - João poderá apenas emitir esse relatório porque o nível de acesso ao relatório é menor ou igual ao nível de emissão. Ele não poderá alterar porque o relatório possui um nível de acesso maior que o nível de alteração atribuído ao grupo “Listagens” do seu perfil.

5)    Relatório do grupo “Listagens” com nível de acesso igual a 3 - João não poderá alterar e emitir esse relatório. O relatório nem será exibido na visão de relatórios para João, porque o nível de acesso ao relatório é maior que os níveis de alteração e emissão.

Exemplo 2Exemplo 2Exemplo 2

**Situação:**

Simulação da aplicação de Grupos de Relatórios/Planilhas em perfis distintos:

1) Criamos um perfil no módulo "Folha de pagamento" e vinculamos esse perfil a um grupo 'Teste' e definimos o nível de acesso como 5, para editar e visualizar.

2) Criamos um usuário e vinculamos ao perfil criado no passo 1 sem configurá-lo como supervisor.

3) Criamos um relatório no módulo "Folha de pagamento" e vinculamos esse relatório ao grupo do passo 1 e definimos o nível de alteração como 6.

4) Logamos com o usuário cadastrado no passo 2 e ele **não** visualizou o relatório (procedimento correto).

5) Alteramos o usuário para supervisor e ele passou a visualizar o relatório do passo 3 (procedimento correto pois usuário supervisor pode visualizar relatórios do seu módulo).

6) Criamos um perfil no módulo "Automação de Ponto" e vinculamos ao mesmo grupo 'Teste' utilizado para o "Folha de pagamento" com os mesmo níveis de acesso.

7) Vinculamos o usuário do passo 2 no perfil criado no passo 6 e **não** definimos como supervisor.

8) Criamos um relatório no módulo "Automação de Ponto" e **não** vinculamos ao grupo 'Teste', que foi vinculado ao perfil.

9) Logamos com o usuário e ele visualizou os relatórios da folha de pagamento e da automação de ponto.

10) Vinculamos o relatório da automação de ponto ao grupo 'Teste', que estava vinculado ao perfil, e definimos o nível de alteração como 6. Ao logar com o usuário novamente ele somente visualizou o relatório da folha de pagamento, ou seja, o fato de ser supervisor no folha de pagamento não fez com que ele visualizasse o relatório da automação de ponto.

11) Alteramos o usuário para supervisor no automação de ponto e ele passou a visualizar os dois relatórios.

Observação

Um usuário cadastrado como supervisor em um módulo não consegue acessar aos relatórios de outros módulos quando **há segurança** aplicada no relatório.

Essa segurança não é feita somente mediante a definição do nível de acesso, deve-se também vincular o relatório ao grupo definido no perfil.

---

 

Para maiores informações:

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.1.XX

false

**Processo:** Grupos de Relatórios

falsefalse

**Status:** Finalizado

false

**Data:** 01/07/2016

false

**Autores:**
