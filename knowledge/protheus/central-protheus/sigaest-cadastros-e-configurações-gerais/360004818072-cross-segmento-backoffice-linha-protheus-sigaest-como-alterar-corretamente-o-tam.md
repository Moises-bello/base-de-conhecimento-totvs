---
article_id: 360004818072
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 8cab0085cec58bb1b75171eb52c855c50115d8c77f7fb578f385fc487c43a58f
fetched_at: '2026-06-28T22:39:07.825457+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como alterar corretamente
  o tamanho dos campos referentes a código de produtos?
type: support-article
updated_at: '2025-03-12T12:26:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004818072-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-alterar-corretamente-o-tamanho-dos-campos-referentes-a-c%C3%B3digo-de-produtos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22720837156887) Tempo aproximado para leitura: 00:02:30 min**

**Dúvida**Como alterar corretamente o tamanho dos campos referentes a código de produtos?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para alterar o tamanho dos campos referente ao código de produtos é necessário o uso do Grupo de Campos, pois o tamanho do campo B1\_COD, que é o cadastro principal do código de produtos é replicado para diversos outros campos e tabelas.

Para realizar a alteração o usuário deve logar-se no módulo Configurador: **SIGACFG > Base de Dados > Dicionário > Base de Dados**

Selecionar a **Empresa > Base de Dados > Grupo de Campos**

**![](http://tdn.totvs.com/download/attachments/271861828/image2017-3-2%2016%3A26%3A4.png?version=1&modificationDate=1488482913000&api=v2)**

Clicar em "Alterar", alterar seu tamanho conforme necessidade e não ultrapassando 30 caracteres e atualizar a base de dados.

## **Por que não ultrapassar 30 caracteres?**

O Grupo de campos do "*tamanho do produto*" pode ter seu tamanho no mínimo de 15 e máximo de 30 no padrão.Este tamanho é limitado por vários aspectos, separando abaixo alguns exemplos:

* Um código de produto maior de 30 poderá mudar significativamente o layout de telas e relatórios.
* Índice de tabelas, performance do sistema em índices onde o código do produto faz parte de uma composição de chave.
* Poderá truncar seu conteúdo em aplicações como coletor de dados onde a tela tem limite de caracteres.
* Pode obrigar a revisão de possíveis integrações com outros sistemas.
* Em alguns bancos de dados não é recomendado chaves e índices grandes.

## **E se eu aumentei acima de 15 e agora quero reduzir, qual impacto?**

* Uma vez que você tem a necessidade de aumentar o tamanho do campo, é porque o seu cadastro em algum momento necessita que o codigo tem aquele tamanho, por exemplo:
* **MATERIALFORA001** (Aqui tem o tamanho maximo padrão que é 15) mas voce deseja acrescentar digamos um codigo do produto como **MATERIALFORA001-TIPOA** (aqui voce aumento para 21). E por alguma razão, você agora precisa reduzir o tamanho para 15. **Não é recomendado**, pois os produtos cadastrados acima desse tamanho minimo não terão uso correto.

É importante enfatizar que, apesar da NFE poder chegar ate 60 posições, vale observar que na NFE o código pode ser um produto ou um serviço assim como a descrição que pode chegar ate 120 posições.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
