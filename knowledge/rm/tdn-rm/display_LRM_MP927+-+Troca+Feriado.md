---
content_hash: bbb651efa9b4b2d60c0c7457abe07eacd4fc0e744b976f40490f0f6d7dedd094
fetched_at: '2026-06-29T00:10:38.719013+00:00'
page_id: '544712014'
product: rm
source: tdn-rm
title: MP927 - Troca Feriado
type: documentation
url: https://tdn.totvs.com/display/LRM/MP927+-+Troca+Feriado
version: 6
---

***Capítulo V - DO APROVEITAMENTO DA ANTECIPAÇÃO DE FERIADOS***

**1. Descritivo:**

Art. 13.  Durante o estado de calamidade pública, os empregadores poderão antecipar o gozo de feriados não religiosos federais, estaduais, distritais e municipais e deverão notificar, por escrito ou por meio eletrônico, o conjunto de empregados beneficiados com antecedência de, no mínimo, quarenta e oito horas, mediante indicação expressa dos feriados aproveitados.

1º Os feriados a que se refere o **caput** poderão ser utilizados para compensação do saldo em banco de horas.

2º O aproveitamento de feriados religiosos dependerá de concordância do empregado, mediante manifestação em acordo individual escrito.

**2. Procedimentos a serem executados:**

**IMPORTANTE: Este recurso só está disponível a partir da release 12.1.26 (mediante execução de script específico) e nativamente na 12.1.27.**

Para utilização da troca de feriado não é necessária parametrização inicial. Ao abrir o RM, contexto de aplicativo RH | Automação de Ponto, no menu “Cadastros | Troca de Feriado”, é possível efetuar a troca de um feriado pré-determinado no cadastro de calendários para a data desejada.

**Exemplo:**

O funcionário de chapa 00004 (veja prints abaixo) possui em seu calendário feriado no dia 07/09/2011 que será trocado pelo dia 12/09/2011. As duas datas possuem marcações. No dia 07/09 estão sendo geradas extras:

No dia 12/09 foi gerada movimentação normal de trabalho:

Ao executar a troca e recálculo as ocorrências são trocadas, ou seja, ocorrência de extra para o dia 12/09 e normal para o dia 07/09:

**Importante:** É necessário executar este procedimento para cada feriado a ser trocado.
