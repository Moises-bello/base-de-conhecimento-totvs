---
content_hash: e6e4cfdfcfbd46b4e026471cac1d538ac8d3d240492fae4322c9ef0896aa326c
fetched_at: '2026-06-29T00:10:58.794259+00:00'
page_id: '606860113'
product: rm
source: tdn-rm
title: Log da ADRC-ST
type: documentation
url: https://tdn.totvs.com/display/LRM/Log+da+ADRC-ST
version: 7
---

Foi implementado junto a geração da Rotina Estadual ADRC-ST um Log para que o cliente posso verificar algumas inconsistências antes de enviar o Arquivo.

Para utilizar este recurso basta utilizar um layout a partir da data 23/03/2021 da rotina disponibilizado em nosso portal.

falseO que foi implementadoPrincipalRegistro 1000false

Quando o Código CEST não informado para o Produto:

Imagem

Quando a Alíquota Interna do ICMS estiver zerada ou sem preenchimento.

ImagemRegistro 1200false

Quando o Código CST vazio:

Imagem

Quando a flag "Operação com Consumidor Final" estiver desmarcada a seguinte mensagem irá aparecer:

Imagem

O arquivo de Log é gerado em forma de um arquivo de texto no mesmo diretório de destino que o arquivo da rotina.

Exemplo:

ImagemNota

Disponível a partir da biblioteca 12.1.29.224 e 12.1.31.126
