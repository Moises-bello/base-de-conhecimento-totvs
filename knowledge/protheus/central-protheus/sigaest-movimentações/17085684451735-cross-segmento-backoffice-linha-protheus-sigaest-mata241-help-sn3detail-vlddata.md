---
article_id: 17085684451735
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4fb0e9a579fb2aa0dc8c3538de0a6f1510a5c475fd6ca2a5195949ee762c5366
fetched_at: '2026-06-28T22:38:56.961001+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - HELP SN3DETAIL
  VLDDATA_LINEPOST ATFVALORUF ao tentar incluir uma Movimentação Interna de Ativo
  Fixo '
type: support-article
updated_at: '2023-08-28T16:47:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17085684451735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-HELP-SN3DETAIL-VLDDATA-LINEPOST-ATFVALORUF-ao-tentar-incluir-uma-Movimenta%C3%A7%C3%A3o-Interna-de-Ativo-Fixo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17085669788311) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Ao tentar incluir uma movimentação Interna de um Ativo Fixo apresenta o **HELP SN3DETAIL VLDDATA\_LINEPOST ATFVALORUF** como ajustar?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17085977324567)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Causa**O HELP é apresentado quando incluir saldo pela rotina do MATA241 e o ***parâmetro* MV\_ATFMOED esta diferente de 1**, no print de exemplo acima, observe que indica a MOEDA 3, portanto o parâmetro esta com 3.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17086288019735)

**Solução**

Nesse cenário, significa que o valor do Ativo será valorizado na MOEDA 3, sendo necessário informar a cotação do dia na MOEDA 3 na rotina ***cadastro de MOEDAS (MATA090)***, para assim conseguir incluir o Documento de Entrada ou Movimentação Interna. Veja os prints de exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17086474899223)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17087041803799)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17087053121303)

Caso, o valor do Ativo seja na MOEDA 1, é necessário apenas alterar o parâmetro MV\_ATFMOED para 1, assim o documento será integrado normalmente, não apresentando a mensagem em questão. Verificar em qual cenário a empresa se aplica e efetuar os ajustes conforme necessário.

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[SIGAEST - Funcionalidade do campo F5\_GERAATF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411465903383-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Funcionalidade-do-campo-F5-GERAATF-)
