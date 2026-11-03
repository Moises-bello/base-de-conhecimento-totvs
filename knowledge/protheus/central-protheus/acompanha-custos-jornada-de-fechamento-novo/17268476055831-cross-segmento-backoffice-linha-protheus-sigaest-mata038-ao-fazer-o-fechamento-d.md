---
article_id: 17268476055831
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: bb7e438b83b196d5570e1691ff5d85dec53af998709d6103ce2d4f144a5d588a
fetched_at: '2026-06-28T22:38:48.160499+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Ao fazer
  o Fechamento de Estoque o Sistema não está calculando os saldos iniciais de acordo
  com a data do fechamento
type: support-article
updated_at: '2023-09-04T18:57:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17268476055831-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Ao-fazer-o-Fechamento-de-Estoque-o-Sistema-n%C3%A3o-est%C3%A1-calculando-os-saldos-iniciais-de-acordo-com-a-data-do-fechamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17268485103127) Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Ao fazer o fechamento de Estoque pela rotina Acompanha Custos, o sistema não está calculando os saldos inicias de acordo com a data de fechamento de estoque.  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Anteriormente, as rotinas de Fechamento de Estoque para calcular e gravar os saldos inicias como SB9, SBJ e SBK, era acessadas, de forma manual, as rotinas de Custo Médio e Virada de Saldos.

Hoje, com a rotina Acompanha Custos, o Sistema de forma automática vai calcular de acordo com o modo de custeio do parâmetro MV\_CUSMED.

De acordo com o fluxo da configuração do parâmetro de Custo:

<https://tdn.totvs.com/display/public/PROT/Novo+Fechamento+-+Jornada+de+Fechamento>

E caso estiver com conteúdo "O",  no parâmetro, o sistema verifica o saldo que possui atualmente em seu estoque e leva para o próximo fechamento, independentemente da data-base do Sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17268900545815)

Portanto, se o usuário utiliza o parâmetro para custo online (MV\_CUSMED = O), a Virada deve ser feita literalmente no dia que ele deseja levar o saldo final do período, ou seja, se for no fim de todos os meses, a rotina deve ser executada no ultimo dia de cada mês.

Caso deseje que a rotina Acompanha Custos faça o mesmo processo que anteriormente eram feitos de forma manual, basta alterar o parâmetro MV\_CUSMED = M para que o sistema calcule as movimentações até a data do fechamento e que leve os saldos iniciais corretamente.

Para saber sobre o roteiro da nova Jornada de Fechamento de estoque acesse nossa documentação abaixo:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/17143292484759>

**Saiba mais**:

*[Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)*
