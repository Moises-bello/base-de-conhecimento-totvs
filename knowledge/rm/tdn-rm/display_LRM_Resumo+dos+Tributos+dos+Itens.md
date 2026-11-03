---
content_hash: 075eb5e3bc2c33c03590526dd2fe0f8f596fb9397edae4497512687b26ad7edc
fetched_at: '2026-06-29T00:10:58.960634+00:00'
page_id: '608169904'
product: rm
source: tdn-rm
title: Resumo dos Tributos dos Itens
type: documentation
url: https://tdn.totvs.com/display/LRM/Resumo+dos+Tributos+dos+Itens
version: 11
---

## Valor contábil ICMS S.T

O parâmetro "Soma ICMS S.T Valor Contábil" tem como objetivo fazer com que a rotina responsável por exibir o resumo dos tributos do movimento considere o parâmetro "Soma ICMS S.T. Valor Contábil", contido nas regras de ICMS vinculadas a natureza de operação.

* Com o parâmetro marcado, o sistema realiza os cálculos e apresenta o valor com a descrição "VALOR ICMSST"

* Com o parâmetro desmarcado, o sistema realiza os cálculos, mas apresenta o mesmo em tela com a descrição "VALOR ICMSST informativo".

* Na mesma nota podem existir itens com parametrizações diferentes, e neste caso os dois valores deverão ser informados.

**Importante:**

A partir da versão 12.1.33 o sistema irá seguir a seguinte sequência de cálculo para definir os valores de integração fiscal do movimento:

1º ISS  
2º ICMS  
3º ICMS ST  
4º DIFAL  
5º Simples Nacional  
6º PIS/Pasep  
7º COFINS  
8º PIS Importação  
9º COFINS Importação

Os tributos abaixo seguirão a ordem que for definida na parametrização do movimento, etapa Fis - Tributação - Item:  
IRRF  
IRPJ  
CSLL  
INSS
