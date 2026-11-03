---
content_hash: 025c3d9797c84ce7eea380be4a07113216b78136755b1bd41b891eae5a7d2fa7
fetched_at: '2026-06-28T21:35:23.858996+00:00'
page_id: '266982513'
product: fluig
source: tdn-fluig
title: ECM - Mensagem "O sistema não pode encontrar o caminho especificado" ao tentar
  visualizar documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266982513
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto**: TOTVS Fluig Plataforma

**Versão:** 1.5.11

# Ocorrência

Ao abrir algum documento na plataforma ocorre o erro "null\999\1000\Documento.pdf (O sistema não pode encontrar o caminho especificado)".

No arquivo de log ocorrem os erros abaixo o erro abaixo:

xml

**Figura 1 - Erro ao visualizar documento**

# Causa

O volume da plataforma pode estar vazio.

# Solução

Acesse a plataforma com o usuário wcmadmin e acesse Painel de Controle > Gerais > Volumes.

Edite o volume cadastrado e verifique o caminho definido. Acesse o caminho e verifique se ele está de acordo com a estrutura da imagem abaixo.

Converse com o responsável pela plataforma da sua empresa para saber onde está o conteúdo do volume. Uma nova versão da plataforma pode ter sido instalada e esqueceram de mover o conteúdo do volume para o novo local.

**Figura 2 - Estrutura do volume**
