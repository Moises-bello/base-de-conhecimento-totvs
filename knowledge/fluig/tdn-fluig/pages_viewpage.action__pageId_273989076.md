---
content_hash: 50ab9cc64785323ba9fde5c70d6f4810664be68ea2b4cebcd4ba6412427b2d47
fetched_at: '2026-06-28T21:35:25.072185+00:00'
page_id: '273989076'
product: fluig
source: tdn-fluig
title: Identity | Gerenciar usuários importados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273989076
version: 44
---

# Falando de gerenciar usuários importados...

---

Usuários importados do Active Directory via SmartSync são apresentados em uma lista de usuários pendentes e precisam ser aceitos pelo administrador da empresa antes de serem efetivamente criados no TOTVS Identity.

Usuários importados do Active Directory que contenham e-mails com formato inválido não terão o aceite efetivado e permanecerão na lista de Usuários Pendentes. O endereço de e-mail do usuário em questão deverá ser corrigido no Active Directory para que o aceite possa ser realizado.

Não é possível reverter o procedimento de aceite, porém o usuário aceito poderá ser desativado pelo administrador. Usuários excluídos do contexto que venham a ser reimportados do Active Directory serão incluídos automaticamente na lista de .

Aceite Automático

É possível automatizar o processo de aceite de usuários editando o Active Directory e habilitando a opção Aceite Automático. Saiba mais em [Gerenciar Active Directories](https://tdn.totvs.com/x/W55UE).

listapendentes

## Acessar lista de usuários pendentes

---

**01.** Acionar o ícone **Configurações**no canto superior direito e selecionar a opção **Active Directory**.

**02.** Na seção , acionar o link **Gerenciar Active Directories**.

**03**. Acionar a opção **Visualizar**, localizada na coluna **Usuários pendentes** do Active Directory desejado.

oculto

Acessar lista de usuários importados

---

**01.** Acionar o ícone **Configurações**no canto superior direito e selecionar a opção **Active Directory**.

**02.** Acionar **Visualizar** localizado ao lado direito do nome do Active Directory cadastrado.

#f2f2f2#f2f2f2

Na parte de baixo da tela são apresentadas as abas **Usuários** e **Grupos**, que possibilitam uma visualização da quantidade de usuários e grupos importados por meio da sincronização com o AD em questão. Para mais detalhes sobre os grupos, consulte a documentação .

**03**. Visualizar os usuários importados.

#f2f2f2#f2f2f2

Na tela é apresentada a quantidade total de usuários importados no período, e também as quantidades de usuários em cada status: pendentes, processando, aceitos e rejeitados.

#e8f6f0#e8f6f0

![](http://tdn.totvs.com/download/thumbnails/286221066/dica.png)

**DICA!**  
Utilize os recursos da tela para trazer uma visualização mais precisa:

* **Filtrar por um período**: Utilize as opções disponíveis para visualizar os usuários importados em todos os dias, hoje, nos últimos 7 dias, nos últimos 30 dias ou por um período personalizado.  
  No período personalizado, é possível selecionar uma data inicial e final no calendário, ou selecionar a opção **Somente data inicial**, para trazer os dados até a data atual.
* **Filtrar por situação**: As situações apresentadas em destaque na tela são filtros, por meio deles é possível selecionar a situação desejada (usuários pendentes, processando, aceitos e rejeitados)
* **Buscar por usuário**: Utilize a busca para pesquisar pelo nome ou e-mail do usuário.  
  É importante notar que a busca remove a seleção dos filtros acima, trazendo todos os resultados.
