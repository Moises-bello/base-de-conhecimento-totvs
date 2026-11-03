---
content_hash: 78efeeaf2f846f35911da524afd8fae1ae74590150417d3cb6e8de3b9d424beb
fetched_at: '2026-06-29T00:11:34.007234+00:00'
page_id: '765344367'
product: rm
source: tdn-rm
title: Eventos S-1200 e S-1210 - Autônomo Externo - Como realizar o pagamento de uma
  verba com incidência exclusiva em IRRF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=765344367
version: 11
---

false

**A partir das Versões:**

* 12.1.2205.273
* 12.1.2209.230
* 12.1.2302.153
* 12.1.2306.100

# Objetivo:

---

O objetivo deste documento é trazer informações de como enviar os eventos S-1200 (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social) e S-1210 (Pagamentos de Rendimentos do Trabalho) para Autônomo Externo que possuem uma verba com incidência exclusiva em IRRF.

---

**PASSO 1**

Acesse RH | Folha de Pagamento | Configurações | Parametrizador |  06.07 - eSocial | 06.07.01 - Configurações Gerais | Autônomos e Externos 2/2, cadastre o provento com incidência exclusiva em IRRF no campo **Provento com incidência somente em IRRF utilizado na integração para autônomos de outros sistemas (S-1200).**

**PASSO 2**

Preencha o campo VALORREMUNFRETEINCIDEIRRF na tabela PPAGTOAUTONOMOEXT conforme sua integração (exemplo: Webservice, conceito, etc...)

**ATENÇÃO:**

**Para geração dessa nova verba, serão contempladas todas as categorias, EXCETO as categorias:**

* + **711 - Contribuinte individual - Transportador autônomo de passageiros) e**
  + **712 - Contribuinte individual - Transportador autônomo de carga).**

**PASSO 3**

Ao gerar o XML dos eventos periódicos S-1200 e S-1210,  sistema irá gerar da seguinte forma:

* S-1200: O valor informado no PASSO 2 no campo "**Valor remuneração com incidência em IRRF**" é gerado no código do evento/verba informado no parametrizador "**Provento com incidência somente em IRRF utilizado na integração para autônomos de outros sistemas (S-1200)"** PASSO 1.

* S-1210: O valor desse evento/verba será somado no liquido, tag <vrLiq>:
