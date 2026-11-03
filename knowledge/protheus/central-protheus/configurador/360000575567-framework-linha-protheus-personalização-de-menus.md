---
article_id: 360000575567
category: Configurador
content_hash: 40bf80a157fddb43a12290991f3c8e5cd5fb9b8f509bb8badf5a757281d627e8
fetched_at: '2026-06-28T22:42:19.109027+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Personalização de Menus
type: support-article
updated_at: '2024-05-08T11:53:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000575567-Framework-Linha-Protheus-Personaliza%C3%A7%C3%A3o-de-Menus
---

**Dúvida**Como personalizar um menu, adicionando ou removendo itens?  
  
**Ambiente**Protheus - Configurador - A partir da versão 11.8  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:1. No Configurador, acesse Ambiente / Cadastros / **Menus**  
2. Clique no rodapé em **Todos os menus** para desmarcar todas as caixinhas, e marque **apenas** a caixinha do módulo desejado. Clique em **OK**;  
3. Na coluna do meio, clique em **Adicionar**.  
4. **Para INCLUIR um item:**- Do lado direito, clique sobre a pasta e na subpasta que deseja adicionar o item de menu, e clique em **Novo item**;  
- Preencha a **Descrição**, o **Programa**, o **Módulo** e as **Tabelas** conforme orientação do Módulo, clique em **OK**;  
  
5. **Para ALTERAR um item:**  
- Do lado direito, clique sobre a pasta e na subpasta, clique sobre o nome da rotina, e clique em **Detalhes**;  
- Faça as alterações necessárias e clique em **OK**.  
  
6. Após concluir as inclusões/alterações, clique em **Gerar**.  
7. Em **Arquivo**, preencha com o nome do menu:  
- Se for salvar sobrescrevendo o menu padrão, digite o nome do módulo (por exemplo, SIGACFG) e clique em **Gerar**;  
- Se for salvar um **novo** menu, digite o nome do menu a ser criado, e clique em **Gerar**.  
  
8. Clique em **Fechar**Após criar o menu, você pode atribuí-lo diretamente a um usuário, ou se ele pertencer a um grupo, atribuir ao grupo.  
  
**Atribuindo menu a um USUÁRIO:**  
1. Acesse o menu Usuário / Senhas / **Usuários**;  
2. Clique sobre o usuário, e clique em **Alterar**;  
3. Clique na aba Restrições de acesso / **Ambientes**;  
4. Localize o módulo que utilizará este menu, então, na coluna **Arquivo**, clique 2 vezes no caminho do arquivo .xnu;  
5. Altere o **nome do arquivo**, indicando o nome do menu que você criou na etapa anterior.  
Obs.: Você pode, ao invés de digitar o nome, clicar no rodapé da página, em **Arquivo**, no botão de "..." e selecionar o caminho onde está o arquivo.  
6. Após a alteração, clique em **Confirmar.****Atribuindo menu a um GRUPO:**  
1. Acesse o menu Usuário / Senhas / **Grupos**;  
2. Clique sobre o grupo, e clique em **Alterar**;  
3. Clique na aba Restrições de acesso / **Ambientes**;  
4. Localize o módulo que utilizará este menu, então, na coluna **Arquivo**, clique 2 vezes no caminho do arquivo .xnu;  
5. Altere o **nome do arquivo**, indicando o nome do menu que você criou na etapa anterior  
Obs.: você pode, ao invés de digitar o nome, clicar no rodapé da página, em **Arquivo**, no botão de "..." e selecionar o caminho onde está o arquivo  
6. Após a alteração, clique em **Confirmar.**
