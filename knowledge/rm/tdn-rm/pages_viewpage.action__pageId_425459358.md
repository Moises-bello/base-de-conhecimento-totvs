---
content_hash: 41c064038009496816adc475701d896e6f0a6e2025aa2b773484ee1e34a00c24
fetched_at: '2026-06-29T00:09:35.471543+00:00'
page_id: '425459358'
product: rm
source: tdn-rm
title: Correspondência - Sub-String
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459358
version: 2
---

**Correspondência - Sub-String**

---

A operação Sub-String recebe uma entrada e retorna somente a sub-string determinada pelos parâmetros.   
 Inicia de uma posição, determinada pelo campo Inicio, e possui um tamanho especifico, retornando o número de caracteres informado no parâmetro Quantidade.  
    
 A posição do primeiro caractere é 0 conforme exemplo abaixo:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B | U | S | I | N | E | S | S |  | C | O | N | E | C | T | O | R |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |

Início: 0  
 Quantidade: 4  
 Resultado: BUSI  
    
 Início: 5  
 Quantidade: 8  
 Resultado: ESS CONE  
    
 ***Nota:*** *A quantidade tem de estar dentro dos limites da string de entrada*

Os parâmetros para configurar esta operação são:

*Alimentação*

* **Entrada:** Ponto de entrada da operação ou campo.

*Diversos*

* **Início:** Índice da primeira letra da sub-string.
* **Quantidade:** Número de caracteres da sub-string.

*Identificação*

* **Nome:** Nome da operação.
* **Nome:** Campo somente leitura, tem como valor o tipo da operação.

---

**Recursos Adicionais**

Acesse o boletim técnico abaixo para ver um exemplo desta operação:

[Conceito utilizando Operação Sub-String](http://totvsconnect.blogspot.com/2011/06/como-fazer-conceito-utilizando-operacao_4840)
