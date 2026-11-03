---
content_hash: 4c088fb99f559051bd151a97d0e3108528e23e110b7772d03b1dccad6adb50c3
fetched_at: '2026-06-29T00:11:12.465405+00:00'
page_id: '653558097'
product: rm
source: tdn-rm
title: Configuração do Go-Global - Totvs News e Esocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=653558097
version: 51
---

Neste artigo estou descrevendo um problema encontrado no uso pelos clientes em relação ao acesso ao RM com travamento da tela do Totvs News e da tela de acesso aos

relatórios de conferencia do INSS/FGTS do Esocial.

## Guia passo a passo

Juntamente com o time de SO realizamos as seguintes configurações:

1. Atualização da versão do RM a partir do release 12.1.31
2. Atualização da versão do Go-Global para 6.2.0.31099
3. Ajuste de um parâmetro no caminho do executável do Go-Global criado na maquina local do cliente, adicionar o parâmetro -krm 3 este processo se faz necessário somente para uso do relatório do Esocial por conta do período ficar inibido.

Em alguns casos, para conseguir preencher o campo "período" tem que ajustar o atalho do Go-Global, adicionando o parâmetro -krm 3  
  
​  
  

## Artigos relacionados

Os artigos relacionados aparecem aqui baseados nos rótulos que você selecionar. Clique para editar a macro e adicionar ou alterar os rótulos.

false5LRMfalsemodifiedtruepagelabel in ("totvs","news","goglobal","esocial") and type = "page" and space = "LRM"TOTVS NEWS ESOCIAL GoGlobal

true

|  |  |
| --- | --- |
| Ocorrências relacionadas |  |
