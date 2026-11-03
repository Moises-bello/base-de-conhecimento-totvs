---
content_hash: 9020571fafda2cae66d0b77668afec664a784739a8d507fa5c746c4c63cc6277
fetched_at: '2026-06-29T00:11:36.968739+00:00'
page_id: '776112878'
product: rm
source: tdn-rm
title: Eventos S-1200 e S-1210 - Autônomos do TOTVS Gestão Financeira - Como realizar
  o pagamento de uma verba com incidência exclusiva em IRRF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=776112878
version: 6
---

false

**A partir das Versões:**

* 12.1.2209.246
* 12.1.2302.170
* 12.1.2306.114

# Objetivo:

---

O objetivo deste documento é trazer informações de como enviar os eventos S-1200 (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social) e S-1210 (Pagamentos de Rendimentos do Trabalho) para Autônomos do TOTVS Gestão Financeira que possuem uma verba com incidência exclusiva em IRRF.

---

**PASSO 1**

Acesse RH | Folha de Pagamento | Configurações | Parametrizador |  06.07 - eSocial | 06.07.01 - Configurações Gerais | Autônomos e Externos 2/2, cadastre o provento com incidência exclusiva em IRRF no campo **Provento com incidência somente em IRRF utilizado na integração para autônomos de outros sistemas (S-1200).**

**PASSO 2**

Lançamento financeiro realizado para o autônomo com o tipo de documento "Gera IRRF", conforme exemplo do print abaixo:

**ATENÇÃO:**

**Para geração dessa nova verba, serão contempladas todas as categorias, EXCETO as categorias:**

* + **711 - Contribuinte individual - Transportador autônomo de passageiros) e**
  + **712 - Contribuinte individual - Transportador autônomo de carga).**

**PASSO 3**

Ao gerar o XML dos eventos periódicos S-1200 e S-1210,  sistema irá gerar da seguinte forma:

* S-1200: O valor do lançamento financeiro informado no PASSO 2 é gerado no código do evento/verba informado no parametrizador "**Provento com incidência somente em IRRF utilizado na integração para autônomos de outros sistemas (S-1200)"** PASSO 1.

* S-1210: O valor do liquido do lançamento financeiro será levado na tag <vrLiq>:
