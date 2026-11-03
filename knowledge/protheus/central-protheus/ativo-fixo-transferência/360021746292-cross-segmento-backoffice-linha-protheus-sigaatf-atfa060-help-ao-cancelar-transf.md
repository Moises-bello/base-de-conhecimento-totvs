---
article_id: 360021746292
category: Ativo Fixo - Transferência
content_hash: 45c9ca02f7169294db7c2a336f09d76d60db578f60f00ad9e9688622d777c447
fetched_at: '2026-06-28T22:41:52.179957+00:00'
product: protheus
section_id: 1500001536061
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA060 - HELP ao cancelar
  transferência: AF060RECNO'
type: support-article
updated_at: '2023-01-26T14:50:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021746292-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA060-HELP-ao-cancelar-transfer%C3%AAncia-AF060RECNO
---

**Ocorrência**Ao efetuar um cancelamento de uma transferência manual é apresentado o seguinte **HELP** em tela:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018676731/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões

**Causa**Esta mensagem é apresentada devido ao fato do sistema estar tentando localizar o ativo na filial que está sendo feito o cancelamento da transferência, porém este cancelamento está sendo efetuado diretamente pela filial de origem do cancelamento ao invés da filial destino.

Quando ocorrer a mensagem AF060RECNO na tentativa de cancelamento da transferência de um bem, será necessário verificar a filial que o usuário está logado. A rotina somente permite que seja feito o cancelamento pela filial de destino, ou seja, a filial em que o bem está ativo no momento.

Quando tentamos fazer o cancelamento pela filial de origem, é exibida a mensagem AF060RECNO, pois a rotina não encontra o bem na filial posicionada.

**Solução**1- Acessar a rotina **ATFA060(Transferências)** com a filial de destino.  
2- Optar por Outras Ações > Canc. Transf.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018677871/mceclip0.png)

3- Verifique  qual  transferência foi realizada e selecione o cancelamento

* Transferência Física : Entre filial
* Transferência contabil : Entre Grupo  e ou entidades (Contas, item conta, centro de custo e ou Classe de Valor)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11955040789911)

4-**Selecionar a filial de destino** da transferência feita:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018802792/mceclip0.png)

5- Parametrizar conforme os dados do bem e confirme.

Verifique outros artigos que podem ser utilizados como base para o processo de cancelamento de Transferência:  
[MP - SIGAATF -ATFA060 - CANCELAMENTO DE TRANSFERENCIA DE FILIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019903231-MP-SIGAATF-ATFA060-CANCELAMENTO-DE-TRANSFERENCIA-DE-FILIAL?source=search)[MP - SIGAATF -ATFA060 - Lançamento padrão para Cancelamento de Transferência de Filial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019667932-MP-SIGAATF-ATFA060-Lan%C3%A7amento-padr%C3%A3o-para-Cancelamento-de-Transfer%C3%AAncia-de-Filial?source=search)

Saiba mais: [MP-SIGAATF - COMO FUNCIONA ROTINA ATFA060 TRANSFERÊNCIA DE ATIVO?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015091671-MP-SIGAATF-COMO-FUNCIONA-ROTINA-ATFA060-TRANSFER%C3%8ANCIA-DE-ATIVO-?source=search)
