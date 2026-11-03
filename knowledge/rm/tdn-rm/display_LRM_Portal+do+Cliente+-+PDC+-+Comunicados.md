---
content_hash: 6e0b1a37a34a498738a732a5bcae2353f148632d4e031fe94fa344ed11e5ca39
fetched_at: '2026-06-29T00:09:48.341257+00:00'
page_id: '435105127'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Comunicados
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Comunicados
version: 7
---

**Comunicados**

---

**Descrição**  
Esta funcionalidade possibilita a Incorporadora de informar aos seus clientes comunicados referentes aos empreendimentos. Na visão de gestão que será utilizado pelo gestor do sistema, será permitido criar novos comunicados e associá-los aos empreendimentos. Na visão do comprador do imóvel, será exibido uma lista com todos os comunicados.

---

**Gestão**

O usuário administrador é responsável por criar e gerenciar os comunicados.

Ele consegue visualizar uma lista com todos os comunicados já criados e alguns de seus dados tais como título, descrição e datas de publicação e expiração.

A lista vem ordenada do servidor pela data de publicação, os comunicados mais recentes aparecem primeiro.

Na tela de criação de um novo comunicado, o gestor insere as informações de título, descrição, data de publicação, data de expiração, os empreendimentos e o conteúdo do comunicado, bem como o texto que irá aparecer nas notificações push dos usuários do aplicativo Meu Imóvel.

Os campos título e data de publicação são obrigatórios e devem ser preenchidos pelo usuário.

No caso de ausência de data de expiração, o comunicado não irá expirar, aparecendo sempre na visão do cliente.

No campo empreendimento o usuário pode selecionar um ou vários empreendimentos para associar ao comunicado. Caso o comunicado seja abrangente para todos os empreendimentos, então o campo deve permanecer vazio.

Para o desenvolvimento do conteúdo do comunicado, foi disponibilizado um rich editor que possibilita o usuário escolher diferentes fontes e cores para as letras, alterar cores do fundo, inserir imagens e links, entre outras funções. Também é possível inserir diretamente código em HTML. O sistema não aceita scripts.

Obs.: Pode ser incluído CSS inline para personalização do conteúdo, conforme exemplo a seguir: <img src="minha\_imagem.jpg" style="height:auto;max-width:100%;" />

O campo Texto para notificação (App Meu Imóvel) é o texto que irá aparecer nas notificações dos celulares cujo comunicado deverá será recebido pelo usuário. O campo não é obrigatório.

Ao final do processo, o sistema permite o usuário visualizar o comunicado antes de salvá-lo no banco de dados.

O conteúdo do comunicado será exibido em uma janela modal igualmente será feito para o cliente final.

O usuário terá permissão de alterar os comunicados já criados e também excluí-los.

Um campo de busca por título e/ou descrição foi criado para auxiliá-lo na busca de comunicados.

**Cliente**  
   
Os comunicados são ordenados no servidor pela data de publicação, os mais recentes aparecem no topo na lista. A data de publicação, o título e a descrição são exibidos em destaque na lista.

O sistema controla se o comunicado foi lido pelo usuário através de cookies.

Quando o usuário clica sobre o comunicado é aberto uma janela modal com o conteúdo do comunicado.

Neste momento é inserido no navegador um cookie com os detalhes do comunicado e do usuário.

Na listagem, o portal destaca através de cores diferentes quando o comunicado já foi lido ou não pelo usuário.

No topo da página, também é informado a quantidade de comunicados não lidos.

Ao clicar nesta informação, o sistema irá filtrar e exibir apenas os comunicados não lidos.

O sistema também informa a quantidade total de comunicados.

Existe um campo de pesquisa para o usuário filtrar pelo título ou descrição do comunicado.
