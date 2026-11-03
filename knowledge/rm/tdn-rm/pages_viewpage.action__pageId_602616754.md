---
content_hash: a36eec667af3ae09ddf840417317ab790a76a4f45e9b2f38654785417dc510a0
fetched_at: '2026-06-29T00:10:57.987629+00:00'
page_id: '602616754'
product: rm
source: tdn-rm
title: DT- Integração Contábil RM X Protheus - Gerar lote contábil para todas as filiais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=602616754
version: 23
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Folha de Pagamento |
| Função: | Parâmetro da contabilização |
| Ticket: | N/A |

## **02. SITUAÇÃO**

Possibilitar a geração do lote contábil de todas as filiais de uma única vez.

**1) Geração da Contabilização**

Marcar o parâmetro "Gravar lote separado por filial" para que o sistema concatene o código do lote informado na tela + o código da filial no momento da geração do lote.

Exemplo:

Na tela foi informado o Lote "555" e o parâmetro "Gravar lote separado por filial" foi marcado.

Após a geração, os  lançamentos contábeis foram gerados para todas as filiais, separadamente para filial 1 e filial 2:

**Atenção:** Caso ocorra erro na integração com o Protheus em uma das filiais, o usuário terá duas opções:

* Gerar somente para aquela filial que ocorreu o erro, informando o mesmo código preenchido no campo "Lote".
* Gerar novamente o lote para todas as filiais, neste caso o serviço irá deletar os dados que foram integrados e gravar os novos.
