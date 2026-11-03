---
article_id: 1500010091382
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 38dac89efc058878565ca11aa307efc4b6432cc202962567662576ad05049abe
fetched_at: '2026-06-28T22:38:54.421006+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como informar o lote
  ao realizar o Apontamento de Produção?
type: support-article
updated_at: '2021-05-10T14:36:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010091382-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-informar-o-lote-ao-realizar-o-Apontamento-de-Produ%C3%A7%C3%A3o
---

**Dúvida**

Como gerar o lote "automaticamente" durante o Apontamento de Produção? É possível gerar um código especifico de lote durante o apontamento de produção (MATA250)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**No Protheus, ao efetuar o Apontamento de Produção - MATA250 - de um Produto cujo controle seja Lote ou Sublote (B1\_RASTRO = L ou S respectivamente), em seu padrão, é aberta uma janela logo após o Apontamento de Produção onde é possível delegar o lote ao qual será direcionado aquele Saldo. Veja um exemplo abaixo onde o produto PA89 possui uma Ordem de Produção de 100 e ao Apontar a Produção abrirá uma janela onde é possível delegar o lote e até mesmo mudar o seu código:

![Processo_de_apontamento_de_producao_informando_lote.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015679042/Processo_de_apontamento_de_producao_informando_lote.gif)

Com relação a produto com Sublote, o comportamento é igual, porém o Protheus não permite a alteração manual do sublote no ato do Apontamento da Produção, este é gerado e gravado com um código automático.

Observações:

Existem três formas de atribuir o número de lote ao produto produzido:

1. Informado manualmente pelo usuário no momento do apontamento;
2. Através da fórmula cadastrada e indicada no parâmetro **MV\_FORMLOT - Código da formula default utilizada para preenchimento dos lotes**;
3. Fornecido automaticamente pelo Sistema. Neste caso é precedido pelas letras **AUTO**, identificando a geração automática do número do lote, podendo também ser alterado manualmente pelo usuário (conforme GIF acima).

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
