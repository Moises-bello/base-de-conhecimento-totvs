---
article_id: 360019073652
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 557f4f9d2b8ba8ab5d2f43b070bf1da1595fa88079dd717bd71c908d37dbebb9
fetched_at: '2026-06-28T22:40:32.479710+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102/ CTBA101 Campos
  da capa do Lote contábil
type: support-article
updated_at: '2023-12-08T17:04:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019073652-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-CTBA101-Campos-da-capa-do-Lote-cont%C3%A1bil
---

**Dúvida**

* Número do lote contábil.
* Número de lote de cada contabilização

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80 **Solução**

A capa do lote é o identificador do lançamento contábil. As informações nela inseridas, são utilizadas para localizar o lançamento contábil posteriormente.

Seguem abaixo alguns detalhes importantes sobre os campos da capa de lote:

 Conteúdo do parâmetro **MV\_LOTECON** = **T**. O número do lote é gerado a partir da Tabela 09.

• Conteúdo do parâmetro**MV\_LOTECON** = **U**. O número do lote é o último número disponível no arquivo de Lançamentos Contábeis mais 1 para a data informada.

**Sublote**

Este campo é um classificador de operações para o lançamento contábil, pois pode ser gerado na contabilização de integração entre sistemas.

**Exemplo**

No Lançamento-padrão 500 (Contas a Receber), o número do Sublote pode ser 001, no Lançamento-padrão 510 (Contas a Pagar) o número do Sub-Lote pode ser 002, etc.

Dessa forma, por essa numeração é possível identificar rapidamente a operação do sistema que gerou aquele lançamento contábil.

Este campo somente está disponível para a digitação manual caso o parâmetro **MV\_SUBLOTE** não esteja preenchido. Caso contrário, o conteúdo informado nesse parâmetro é exibido na tela e gravado sem a intervenção do usuário.

**Documento**

Este número é sugerido pelo sistema, sendo o último número digitado acrescido do valor 1. Para mais detalhe [(Clique Aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024280571-MP-SIGACTB-N%C3%9AMERO-DE-DOCUMENTO-CONT%C3%81BIL?source=search)

**Conteúdo Tabela 09 - Lotes Contabilidade :**

|  |  |
| --- | --- |
| Chave | Descrição |
| ATF | 8860 |
| CDA | 8800 |
| COM | 8810 |
| CON | 1 |
| EIC | 8800 |
| ESP | 8800 |
| ESP1 | 8800 |
| EST | 8840 |
| FAS | 8800 |
| FAT | 8820 |
| FIN | 8850 |
| FIS | 8880 |
| FRT | 8800 |
| GPE | 8890 |
| GRH | 8800 |
| JUR | 8900 |
| LOJA | 8800 |
| MNT | 8800 |
| OFI | 8800 |
| PCP | 8800 |
| PFS | 8910 |
| PON | 8800 |
| QIE | 8800 |
| QMT | 8800 |
| RPM | 8800 |
| RSP | 8800 |
| TEC | 8800 |
| TMK | 8800 |
| TRT | 8800 |
| VEI | 8800 |

Veja mais :

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Como definir a numeração inicial para o lote contábil.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16624151260439-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-definir-a-numera%C3%A7%C3%A3o-inicial-para-o-lote-cont%C3%A1bil-?source=search)

<http://tdn.totvs.com/display/public/PROT/Lotes+de+Contabilidade>

* [Tabela CTF](hthttps://tdn.totvs.com/pages/viewpage.action?pageId=654960102)
* [MV\_CTFQTD](https://tdn.totvs.com/pages/viewpage.action?pageId=544724837)
* [Remoção do Semáforo Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=630022553)
* [Help DOCINVALID Lançamento Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=666797150)
* [CTBA102 - DOCINVALID - Documento sem CTF criada](https://tdn.totvs.com/pages/viewpage.action?pageId=723817592)
