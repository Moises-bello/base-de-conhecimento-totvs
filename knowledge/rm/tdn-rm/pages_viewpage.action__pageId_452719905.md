---
content_hash: df6350fc58eb7bc33586f4a2fc5aaeff246e89a0b5413feb443eb96b07b19f61
fetched_at: '2026-06-29T00:10:10.680463+00:00'
page_id: '452719905'
product: rm
source: tdn-rm
title: Código de Cálculo 29 - INSS Outro Emprego
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719905
version: 4
---

Evento do tipo Base de Cálculo, Valor e sem incidências.. Este evento será calculado sobre o valor lançado no código de cálculo 072 (Base de INSS Outro Emprego).

**Observação**

Este código de cálculo somente poderá ser lançado quando não é necessário o cálculo do INSS proporcional.

**Exemplo**

Vamos considerar 2 casos básicos de cálculo do cód. de calc. 029:

Tabela de INSS

*Limite Superior           Percentual*  
        2,00                      8,00  
    174,86                       8,00  
    291,43                       9,00  
    582,86                     10,00  
   
**Caso 1:** Soma das incidências de todos os empregos limite tabela:  
1º emprego = 150,00 (Empresa Exemplo)   
2º emprego = 280,00 (outro emprego, valor informado no evento código de cálculo 072.  
Total = 430,00 - atinge a 4ª faixa (10%) = 43,00  
Cálculo proporcional do INSS:  
1º emprego (150,00) = 15,00 (lançado no evento de cód. de cálculo 03 - INSS)  
2º emprego (280,00) = 28,00 (lançado no evento de código de cálculo 029 - INSS Outro Emprego)  
   
**Caso 2:** Soma das incidências de todos os empregos limite tabela:  
1º emprego: 400,00 (Empresa Exemplo)  
2º emprego: 800,00 (valor lançado no evento de código de cálculo 072)  
1.200,00 - atinge a última faixa (10%) = 58,28  
Cálculo proporcional do INSS:  
1º emprego (400,00): 19,42 (lançado no evento de código de cálculo 03 - INSS)  
2º emprego (800,00): 38,86 (lançado no evento de código de cálculo 029)  
Você poderá lançar o evento com o código de cálculo 029 e o respectivo valor já calculado. Neste caso, não será preciso lançar o código de cálculo 072.   
   
**Atenção**

Quando existe mais de um evento com o código de cálculo 29, o sistema lançará o valor do cálculo no primeiro evento e lançará os demais com o valor zerado.

**Observação**

Quando é informada a Base de INSS do externo, utilizando os CC's 72 ou 181 para CLT ou o CC 418 para autônomo, o sistema calcula o desconto de INSS do externo, e não considera o valor informado pelo usuário no CC 29.   
Para utilizar o desconto do INSS do externo como referência do cálculo o correto é informar somente o CC 29.   
O CC 29 pode ser utilizado para informar o desconto do INSS de qualquer vinculo externo, seja CLT ou autônomo.  
Somente no caso de informar a Base de INSS do externo, onde o sistema que irá calcular do valor descontado, que é necessário diferenciar o número do código de cálculo, CC 418 para autônomo e CC's 72 e 181 para CLT.

[EXEMPLO LANÇAMENTO CC 29 – INSS Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=647459982)

---

Códigos de Cálculo
