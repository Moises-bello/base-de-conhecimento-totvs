---
content_hash: c92efa6afa6db597a0b89360bf64210ba49aacfc363e8fedc17648b3ba0b537d
fetched_at: '2026-06-29T00:09:24.076256+00:00'
page_id: '423937882'
product: rm
source: tdn-rm
title: Confirmação da Operação – Manifestação Automática (MD-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937882
version: 2
---

Este processo irá sincronizar automaticamente cada registro selecionado na visão enviando um evento de "Confirmação da Operação"  
***Observação***: Ao executar o processo o sistema irá verificar na base de dados todos as movimentações de ENTRADA que possuírem as chaves de acesso dos registros selecionados e enviar o manifesto de "Confirmação da Operação" automaticamente.  
Quando utilizado o Client Neogrid, para o evento é gerado um XML, que primeiro vai para a pasta OUT e após processamento da ferramenta, é enviado para a pasta SENT, e assim será enviado para a Neogrid.   
Essas pastas ficam no diretório onde o Client Neogrid está instalado.
