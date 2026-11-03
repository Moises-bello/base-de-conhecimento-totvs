---
article_id: 360026422171
category: Configurador
content_hash: 01008a500b63d08403cbe5d7b787a5be9759b583c74e0206f06cd8a5b4eb9d6b
fetched_at: '2026-06-28T22:42:19.016971+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Criação de Filtros Inteligentes
type: support-article
updated_at: '2024-05-08T11:43:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026422171-Framework-Linha-Protheus-Cria%C3%A7%C3%A3o-de-Filtros-Inteligentes
---

**Dúvida**Como criar filtros inteligentes no Protheus?  
   
 **Ambiente**Protheus - Configurador - A partir da versão 11  
   
**Solução**Os Filtros Inteligentes servem para que sejam criados filtros que possam ser utilizados por vários usuários, ao invés de cada usuário ter que criá-los individualmente. Devem ser criados no Configurador, por um usuário Administrador do sistema. Após ser criado, deve-se selecionar quais usuários terão esse filtro disponibilizado nessa tabela quando a acessarem. Se não for atribuído nenhum usuário, o filtro ficará disponível para todos.  
  
Para criar um filtro inteligente, seguem os passos abaixo:  
1. Acesse Configurador > Base de Dados > Dicionário > **Bases de Dados**  
  
2. Selecione a tabela que você deseja acrescentar o **Filtro Inteligente** e clique em **Editar**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025573732)  
  
3. Expanda a tabela (+) e clique em **Filtro(s)**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025573852)  
  
4. Na barra superior, clique em **Incluir  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025589131)**

5. Na tela Gerenciador de Filtros, clique em **Criar Filtro** para criar um novo

6. Preencha um **Nome do Filtro**, selecione o **tipo de Filtro** (Padrão, Expressão ou Função), selecione o Campo, Operador e Expressão que fará parte do Filtro e clique em **Adicionar**

7. Monte o Filtro da maneira desejada e então clique em **Salvar  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025574392)**8. Na tela de seleção de filtros, marque o filtro criado e clique em **Aplicar filtros selecionados**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025574432)  
  
9. Após criado o filtro, se quiser deixar disponível para todos, apenas clique em Confirmar (pule esta etapa). Caso queira atribuir usuários específicos, deve-se selecionar quais usuários terão esse filtro nesta tabela. Clique no botão **Usuários**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025589611)  
  
10. Selecione cada usuário que utilizará este filtro em vá clicando em **Adicionar  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025574692)**11. Após finalizar, clique em **Salvar**, depois em **Confirmar**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025574712)  
  
12. Será necessário atualizar a **Base de Dados** com essas informações para que elas tenham efeito. Este processo deve ser feito em modo **exclusivo**, ou seja, nenhum usuário poderá estar utilizando a tabela em que o filtro foi criado. Clique em **Atualizar Base de Dados**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025589951)

13. Clique em **Avançar**, serão processadas as informações, então clique em **Finalizar**

14. Acesse a rotina que utiliza a tabela do filtro criado, com um dos usuários que foi atrelado a esse filtro

15. Clique em **Filtrar**, e o filtro criado será exibido na listagem, podendo ser aplicado no browse  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025590091)  
  
  
**Informações**  
Para outras opções do Filtro Inteligente, como Editar e Excluir filtros, acesse o link abaixo:  
<http://tdn.totvs.com/display/PROT/Filtros+Inteligentes+-+Como+criar>
