---
article_id: 115011811428
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 327fb391b0789511573c2be5909d6e7e413a4d7167ad2c6ba74ec4de145effb1
fetched_at: '2026-06-28T22:38:41.216843+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Ao tentar gerar a nota , gera erro no campo C5_NATUREZ
type: support-article
updated_at: '2021-04-28T15:51:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011811428-MP-FAT-Ao-tentar-gerar-a-nota-gera-erro-no-campo-C5-NATUREZ
---

**Ocorrência**

Ao tentar gerar a nota, gera o erro no campo c5\_naturez:

variable does not exist C5\_NATUREZ on MAFISINI(MATXFIS.PRX)

**Causa**

De acordo com o erro, a variável que recebe o conteúdo do parâmetro mv\_1dupnat, está recebendo a seguinte instrução, conforme trecho retirado do mesmo abaixo:

CMVDUPNAT(C) :C5\_NATUREZ​

Desta forma, o sistema não consegue enxergar o alias da tabela para procurar a informação, gerando o erro de que o campo não existe.

**Ambiente**

Microsiga Protheus a partir da versão 12

**Solução**

1 - Acesse o Configurador, Base de dados, Dicionário, Base de Dados, Parâmetros.

2- Selecione o parâmetro MV\_1DUPNAT e edite.

3-Coloque a seguinte instrução no parâmetro: SC5->C5\_NATUREZ

Colocando o alias da tabela , SC5, o sistema saberá a quem o campo pertence e de onde precisa buscar a informação , fazendo com que o erro deixe de ocorrer.
