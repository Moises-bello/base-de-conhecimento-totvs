---
content_hash: bd9bf7d886a3d5d9cc46b1defa8bf962d699a7bf9a1ae52ff0418fffb2142442
fetched_at: '2026-06-28T21:35:27.686409+00:00'
page_id: '568921366'
product: fluig
source: tdn-fluig
title: Cache em navegador no TOTVS Fluig Plataforma
type: documentation
url: https://tdn.totvs.com/display/fluig/Cache+em+navegador+no+TOTVS+Fluig+Plataforma
version: 6
---

# Índice

4true.\*ndicenone

# Objetivo

Esse guia tem o objetivo de detalhar o uso da técnica de cache em navegador, passando pelos benefícios da técnica e exemplos.

## O que é Cache?

Cache é uma técnica utilizada para guardar uma cópia do dado recurso e quando requisitada, essa cópia do dado é apresentada. Quando temos um web cache com um recurso requerido anteriormente armazenado, ele intercepta a solicitação devolvendo sua cópia não sendo necessário fazer o download novamente do servidor original, facilitando em vários pontos como por exemplo: o balanceamento do servidor não precisando servir todos os *clients* sozinho, proximidade com o *client* levando menos tempo para transmitir o recurso de volta.

São muitas vantagens ao se utilizar a técnica de cache, porém precisa essa técnica precisa de uma configuração correta pois os recursos armazenados podem mudar ao longo do tempo, isso faz com que seja retornado um recurso obsoleto. O importante é sempre lembrar: um recurso só cabe no cache somente até que ele sofra alterações.

Ao utilizar cache, a performance de aplicações e websites podem melhorar significativamente pois o reuso de recursos buscados previamente diminui bastante o tempo de retorno da resposta.

## Benefícios

**Redução do tráfego**Menos requisições e respostas precisam trafegar na rede. O objeto é recuperado do servidor somente uma vez, reduzindo a quantidade de banda usada pelo cliente. Pode-se conseguir taxas de acerto de até 60%.

**Redução de carga dos servidores**Menos requisições para o servidor WWW atender. Exemplificando, alguns sites ficam extremamente congestionados quando do lançamento de novos produtos. Um servidor proxy pode resolver o problema.

**Redução da latência**As respostas de requisições aos objetos "cacheados" são feitas a partir do cache local, não pelo servidor WWW original, ou seja, o acesso tende a ser bastante rápido.

## Uso do cache na plataforma

### Imagem na timeline - API de Thumbnail antiga

### Resources de Widgets - JavaScript e CSS

Atualização de uma widget e/ou layout através da Central de Componentes ou via Fluig Studio

### Imagem de perfil

## Como forçar a limpeza?

Existem algumas formas de forçar a limpeza do cache nos navegadores, confira a seguir:

* Limpeza manual via configuração dos browsers:
  + Google Chrome: Pressionar ao mesmo tempo as teclas **CTRL + Shift + R** ou pressionar **CTRL + Shift + Del** e, na pop-up aberta, marcar a opção **Cookies e outros dados do site** e acionar **Limpar dados**.
  + Mozilla Firefox: Pressionar ao mesmo tempo as teclas **Ctrl + Shift + Del**e, na pop-up aberta, marcar a opção **Cookies e Cache** e acionar **Limpar agora**.
  + Internet Explorer: Pressionar ao mesmo tempo as teclas **Ctrl + Shift + Del** e, na pop-up aberta, marcar a opção **Arquivos de Internet Temporários e Cookies**e acionar **Excluir**.

Também é possível acessar a plataforma sem cache, para isso é necessário autenticar-se a partir de uma **janela anônima**. Nesse caso, o cache é mantido no navegador habitual.

Dica!

Recomendamos a leitura da documentação oficial do Mozilla® sobre [Cache](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/HTTP).
