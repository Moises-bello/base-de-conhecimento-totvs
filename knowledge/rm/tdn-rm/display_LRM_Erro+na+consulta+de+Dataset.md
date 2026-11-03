---
content_hash: e39fe922eae78f8053097cd2f2a86f6e004307383990b9c0e0bf5de05292ece9
fetched_at: '2026-06-29T00:11:31.931284+00:00'
page_id: '741317286'
product: rm
source: tdn-rm
title: Erro na consulta de Dataset
type: documentation
url: https://tdn.totvs.com/display/LRM/Erro+na+consulta+de+Dataset
version: 11
---

## Objetivo

Este documento apresenta o motivo de erro de retorno e consulta de Datasets do Fluig no momento de enviar um arquivo para o GED.

Mais informações, :

## Introdução

Pode ocorrer que o usuário de integração do Fluig configurado no RM, tenha algum tipo de bloqueio de Datasets, ou seja, ocorreu algum problema na criação do ambiente do Fluig onde os Datasets padrões não foram criados.

Neste caso, ao realizar o envio de arquivos pelo RM, erros podem ser apresentados, reportados pela própria Api do Fluig.

Exemplo de um erro quando o usuário não possui o Dataset 'document' criado em seu ambiente.

Neste exemplo existe uma configuração de mapeamento de pasta, onde o nome da subpasta deve ser o código do usuário.

Conforme apresentado nesta imagem: Configuração (Utilizar o retorno de uma coluna do dataServer como nome da pasta)

Ao realizar o envio do arquivo, a pasta '00001' não pôde ser localizada, pois o ambiente do Fluig não possui o Dataset 'document' que oferece o serviço de consulta a pastas.  
Por esta razão, não é possível enviar o arquivo, pois para o tipo de configuração de mapeamento selecionado é necessário utilizar essa consulta de pastas.

IMPORTANTE

Deve ser reportado aos responsáveis por criar o ambiente, que a falta de qualquer Dataset padrão do Fluig, existe um problema relacionado ao ambiente.
