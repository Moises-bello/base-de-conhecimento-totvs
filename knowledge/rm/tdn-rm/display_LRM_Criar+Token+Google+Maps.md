---
content_hash: f178f07e57cc1f0eaaa35835aa8762e94a7d5287ce2f3eaaa98965d52b3144b4
fetched_at: '2026-06-29T00:11:13.191513+00:00'
page_id: '658237358'
product: rm
source: tdn-rm
title: Criar Token Google Maps
type: documentation
url: https://tdn.totvs.com/display/LRM/Criar+Token+Google+Maps
version: 7
---

Funcionalidade disponível a partir da versão 12.1.32

O processo de criação do token para acesso a API do Google Maps começa ao acessar este [link](https://console.cloud.google.com/apis/).

Ao acessar clique em Criar Projeto

Escolha o nome do Projeto e o Local como mostra a figura abaixo e clique em criar

Ao criar vai abrir o projeto, então selecione no menu a esquerda a opção Credenciais ao clicar vai aparecer a tela abaixo

Então clique em Criar Credenciais e escolha a opção Chave de API

A chave será gerada

Após clique no menu de navegação e vá em APIs e serviços e selecione Biblioteca

Em Biblioteca encontre Maps JavaScript API e ative.

Agora é necessário vincular uma conta de faturamento, no menu de navegação clique em Faturamento ao abrir a tela clique em Vincular Conta de Faturamento, caso não tenha uma conta de faturamento clique em criar conta de faturamento.

Siga os passos e ao final faça o cadastro dos dados solicitados

Ao finalizar o cadastro vai aparecer a seguinte informação, que fala que você tem 3 meses de teste gratuito, porém ao acabar este período o Google libera um crédito mensal e você só é cobrado caso passe deste limite.

Para maiores informações sobre veja [aqui](https://cloud.google.com/free/docs/gcp-free-tier)

Para finalizar vá até o backend do seu portal e adicione o token que foi gerado
