---
content_hash: e4359cd2b2617a1050a15209b49260eb15dc817764c75ffa89442025bebb5ac8
fetched_at: '2026-06-29T00:09:35.488405+00:00'
page_id: '425459366'
product: rm
source: tdn-rm
title: Correspondência - Lista de Decodificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459366
version: 8
---

**Correspondência - Lista de Decodificação**

---

Na operação Lista de Decodificação, valores de origem são convertidos para um valor de destino específico através de uma lista de conversão.  
    
 Essa lista contém o valor origem e qual valor destino ele representa. Por Exemplo:

|  |  |  |
| --- | --- | --- |
| **Origem** | **Destino** | **Lista** |
| Sexo: M ou F | Sexo: 0 ou 1 | M=0 e F=1 |

Nesse exemplo, os valores e os tipos de dados são diferentes. Com a montagem da lista, quando for recebido da origem um valor M, o mesmo será convertido para 0 (da mesma forma para o valor F).  
    
 Os parâmetros para configurar esta operação são:

*Alimentação*

* **Entrada:** Ponto de entrada da operação ou campo.

*Identificação*

* **Nome:** Nome da operação.
* **Nome:** Campo somente leitura, tem como valor o tipo da operação.

*Parâmetros*

* **Valor Padrão:** Valor a ser utilizado caso o valor de origem não corresponda a nenhum dos valores mapeados na propriedade Valores.
* **Valores:** Valores de comparação.

Ao clicar no lookup do campo Valores, uma visão é aberta onde deve ser criada a lista com os valores de origem e destino.  
 No lado esquerdo da visão estão as relações de valores referente ao campo.   
    
 Abaixo estão disponíveis os botões Add e Remove, para adicionar uma relação ou remover a relação selecionada, respectivamente.   
    
 No lado direito estão os parâmetros para configuração, que são:

* + **Código:** Informe o valor do campo na origem.
  + **Valor:** Informe o valor que o campo deverá ter no destino.

---

**Recursos Adicionais**

Acesse o boletim técnico abaixo para ver um exemplo desta operação:

[Conceito utilizando Operação Lista de Decodificação](http://totvsconnect.blogspot.com/2011/06/como-fazer-conceito-utilizando-operacao_01)
