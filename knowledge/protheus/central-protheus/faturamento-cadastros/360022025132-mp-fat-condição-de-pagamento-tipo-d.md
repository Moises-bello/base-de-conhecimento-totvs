---
article_id: 360022025132
category: Faturamento - Cadastros
content_hash: c0a3558e9793b3e41dfaf31d9d6f2d6d881e44d2616c5ca6617cb9c01c1ca004
fetched_at: '2026-06-28T22:38:36.431960+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: MP-FAT-Condição de Pagamento tipo D
type: support-article
updated_at: '2021-04-28T15:14:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022025132-MP-FAT-Condi%C3%A7%C3%A3o-de-Pagamento-tipo-D
---

**Dúvida**Como utilizar a condição do tipo D?  
   
 **Ambiente**

Microsiga Protheus - versões 8 e 10  
  
**Solução**

Essa condição tinha como característica a utilização do conceito de **meses corridos** a partir da data de emissão. Com isso, no campo “Cond. Pgto.”

Exemplo:

|  |  |
| --- | --- |
| Campos | Valores |
| Tipo (E4\_TIPO) | D |
| Cond. Pgto. (E4\_COND) | 1,2,3 |

Resultado:

Considerando a emissão da Nota em 21.01.19 e valor da nota de R$ 1000,00, teremos:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Documento | Série | Parcela | Vencimento | Valor |
| 000000001 | UNI | A | 21.02.19 | 333,33 |
| 000000001 | UNI | B | 21.03.19 | 333,33 |
| 000000001 | UNI | C | 21.04.19 | 333,34 |

 A condição de pagamento do **tipo D** ainda possui a sua codificação ativa no fonte **MatxfunC**, por legado de sistema, podendo ser utilizada e sem causar nenhum erro no sistema, mas como essa condição pode ser atendida nas demais existentes (**[MP - FAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-MP-FAT-Condi%C3%A7%C3%B5es-de-Pagamento?source=search)**), a mesma foi ***descontinuada de uso*** e inclusive, a documentação do help on line encontra-se atualizada desde a versão 11, onde já não consta a sua chamada, conforme link :**[Help on line Faturamento](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/sigafat.htm)** **(Faturamento/Atualizações/Cadastros/Condições de Pagamento/Condições de Pagamento / tipos).**
