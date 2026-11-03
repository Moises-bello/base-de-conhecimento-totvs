---
article_id: 360022024032
category: Faturamento - Cadastros
content_hash: babc43111c0e441a5880f6a4681337363b46df09edceb5339259419aa7144c22
fetched_at: '2026-06-28T22:38:35.608376+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: MP-FAT-Condição de Pagamento Tipo C
type: support-article
updated_at: '2021-04-28T15:14:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022024032-MP-FAT-Condi%C3%A7%C3%A3o-de-Pagamento-Tipo-C
---

**Dúvida**Como utilizar a condição do tipo C?  
   
 **Ambiente**

Microsiga Protheus - versões 8 e 10  
  
**Solução**

Essa condição tinha como característica a utilização de “**dia fixo**” para a geração das parcelas. Com isso, no campo “Cond. Pgto.” (E4\_COND), devia-se informar apenas a quantidade de parcela(s).

Exemplo:

|  |  |
| --- | --- |
| Campos | Valores |
| Tipo (E4\_TIPO) | C |
| Cond. Pgto. (E4\_COND) | 3 |
| Dias da Condição (E4\_DDD) | D = Data do Dia |
| IPI (N/J/S) (E4\_IPI) | N = Normal |

Resultado:

Considerando a emissão da Nota em 21.01.19 e valor da nota de R$ 300,00, teremos:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Documento | Série | Parcela | Vencimento | Valor |
| 000000001 | UNI | A | 21.01.19 | 100,00 |
| 000000001 | UNI | B | 21.02.19 | 100,00 |
| 000000001 | UNI | C | 21.03.19 | 100,00 |

 A condição de pagamento do **tipo C** ainda possui a sua codificação ativa no fonte **MatxfunC**, por legado de sistema, podendo ser utilizada e sem causar nenhum erro no sistema, mas como essa condição pode ser atendida nas demais existentes (**[MP - FAT - Condições de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017468312-MP-FAT-Condi%C3%A7%C3%B5es-de-Pagamento?source=search)**), a mesma foi ***descontinuada de uso*** e inclusive, a documentação do help on line encontra-se atualizada desde a versão 11, onde já não consta a sua chamada, conforme link :**[Help on line Faturamento](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/portuguese/sigafat.htm)** **(Faturamento/Atualizações/Cadastros/Condições de Pagamento/Condições de Pagamento / tipos).**
