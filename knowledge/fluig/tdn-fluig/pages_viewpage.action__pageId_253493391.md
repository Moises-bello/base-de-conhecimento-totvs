---
content_hash: 9fb54f78bae1206fcc6ddfbed366bc859710ec261f61b432be5c8e04514d07e6
fetched_at: '2026-06-28T21:35:23.435845+00:00'
page_id: '253493391'
product: fluig
source: tdn-fluig
title: SOC - Como incluir permissão de gravação na galeria da comunidade para usuários
  específicos?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=253493391
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Gostaria de adicionar a permissão para que um usuário comum possa administrar a galeria de imagens na comunidade, mas apenas para um determinado usuário; os demais não devem poder criar galerias ou inserir imagens.

# Solução

Para permitir que determinados usuários criem galerias na comunidade, sem que essa permissão seja aplicada aos demais membros, você deve configurar as permissões de segurança diretamente na pasta em que as imagens da comunidade são armazenadas.

0.5falsesamplesfadetrue1Passo 1

* O primeiro passo é identificar a pasta que em as imagens da comunidade são salvas. Acesse a comunidade com um administrador e clique no botão **Administrar** → **Editar comunidade**.

Passo 2

* Na tela de administração da comunidade, desça a página até a área de **Conteúdo e segurança**.

* Na coluna Pasta, será exibido o caminho da pasta onde as imagens da comunidade são armazenadas. Na imagem abaixo, o caminho seria Raiz/Comunidades/Espanhol Básico.

**No exemplo acima, os membros da comunidade possuem permissão de Leitura, ou seja, apenas podem visualizar as imagens das galerias.**

3Passo 3

* Acesse o menu lateral **Documentos** e navegue até o diretório onde encontra-se a pasta com as imagens da comunidade.

* No final da linha, clique sobre o menu **Mais opções** → **Propriedades**

Passo 4

* Na aba Segurança, adicione os usuários que deverão receber permissão para inclusão de imagens nas galerias. Para isso clique em **Colaborador**, selecione o usuário, e defina o nível de segurança para, no mínimo, **G** (Gravação).

* Uma vez finalizadas as configurações, clique em **Confirmar**.

**No exemplo acima, a usuária Anna Smyth, que é membro da comunidade Espanhol Básico (mas não é moderadora) agora poderá incluir imagens nas galerias desta comunidade.**
