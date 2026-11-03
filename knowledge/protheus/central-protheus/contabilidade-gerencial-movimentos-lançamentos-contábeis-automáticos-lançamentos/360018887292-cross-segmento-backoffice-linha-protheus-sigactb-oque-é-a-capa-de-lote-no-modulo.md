---
article_id: 360018887292
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: a8736f14447995bcd62390189a9704783254d256d3809f8710f53808ea4c9d8e
fetched_at: '2026-06-28T22:40:32.397288+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus  - SIGACTB: Oque é a capa de lote
  no modulo contábil?'
type: support-article
updated_at: '2022-07-18T20:28:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018887292-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Oque-%C3%A9-a-capa-de-lote-no-modulo-cont%C3%A1bil
---

**Dúvida**Oque é a capa de lote no modulo contábil?

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

 capa do lote é o identificador do lançamento contábil. As informações nela digitadas, são utilizadas para localizar o lançamento contábil posteriormente.

Seguem abaixo alguns detalhes importantes sobre os campos da capa de lote:

Data

Deve existir pelo menos um Calendário Contábil válido para a data informada.

Consulte o tópico Calendário contábil.

Deve existir pelo menos uma Moeda Contábil válida para a data informada

Consulte os cadastros Moedas contábeis e Moeda x Calendário

Para evitar digitação em data indevida, configure o status do período como Bloqueado na opção de Calendário contábi[l](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/ctba010.htm).

Lote

Conteúdo do parâmetro MV\_LOTECON = T. O número do lote será gerado a partir da Tabela 09.

Conteúdo do parâmetro MV\_LOTECON = U. O número do lote será o último número disponível no arquivo de Lançamentos Contábeis mais 1 para a data informada.

Sublote

Este campo é um classificador de operações para o lançamento contábil, pois pode ser gerado na contabilização de integração entre sistemas.

Exemplo:

No Lançamento-padrão 500 (Contas a Receber), o número do Sublote poderá ser 001, no Lançamento-padrão 510 (Contas a Pagar) o número do Sub-Lote poderá ser 002,  etc.

Dessa forma, por essa numeração consegue-se identificar rapidamente qual foi a operação do sistema que gerou aquele lançamento contábil.

Ele só estará disponível para a digitação manual caso o parâmetro MV\_SUBLOTE não esteja preenchido. Caso contrário, o conteúdo informado nesse parâmetro será exibido na tela e gravado sem a intervenção do usuário.

Documento

Este número é sugerido pelo sistema, sendo que é o último número digitado mais 1.

**Importante**

A chave de procura de um lançamento contábil obedece a seguinte forma: Data+Lote+Sublote+Documento.

Para maiores detalhes sobre os campos, verifique o help de campo

|  |  |
| --- | --- |
| |  | | --- | |  | |
