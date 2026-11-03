---
content_hash: da9472aeef8fbc54d478e563255e779ad476ec05464a9f518868560fa4de2ea6
fetched_at: '2026-06-29T00:09:26.076242+00:00'
page_id: '423938250'
product: rm
source: tdn-rm
title: Cadastro de Valores Orçados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938250
version: 10
---

Por esta opção, cadastram-se Valores Orçados para Orçamento de **Despesa** ou **Receita**.  
O campo de valor orçado possui uma consitência que impede que seja informado um valor que ultrapasse o valor real já empenhado;  
Apenas os orçamentos dentro do período de movimentação global poderão ser alterados;  
A permissão de acesso seguirá o padrão dos demais cadastros visto que a manutenção dos orçamentos é feita de forma centralizada;  
Os movimentos tipos do tipo 5.1.xx configurado para afetar o orçado, na sua inclusão irá afetar sempre o cadastro dos valores de orçamento pela data de emissão.

**Saldo disponível do Orçamento**

A fórmula para chegar ao saldo disponível do orçamento por período é a seguinte:  
**Despesa:** Saldo do Período = Valor Orçado – (Valor Opcional 1 + Valor Opcional 2 + Valor Realizado) - Valor Cedido + Valor Recebido + Valor Excedente  
**Receita:** Saldo do Período = Valor Orçado – (Valor Opcional 1 + Valor Opcional 2 + Valor Realizado) - Valor Cedido + Valor Recebido + Valor Excedente. Neste caso a coluna saldo ficará negativo até zerar o valor.  
Quando um movimento estiver configurado para utilizar o orçamento, sempre que for incluído, alterado, cancelado ou recebido, ele irá afetar o orçamento conforme sua configuração.   
Os dados que serão considerados para o orçamento são por item de movimento. Com isso um movimento poderá ter itens que afetem orçamentos diferentes centro de custo e natureza do orçamento, ou também de períodos diferentes.

A exclusão do Cadastro de Orçamento não é permitida quando existirem movimentações de  associadas ao registro.

Se houver necessidade de zerar o saldo do orçamento, o procedimento deverá ser realizado manualmente no Cadastro de Orçamento.

Exemplo para zerar o valor

Existe 2 Cadastros de Orçamento:  
1° Orçamento com valor de 1.000,00  
2° Orçamento com valor de 1.260,00

Fiz a transferência do 1° p/ 2° no valor de 260,00

Para ajustar e zerar o 1° Orçamento, seguir o seguintes passos:

* Editar o 1° Orçamento de 1.000,00 p/ 260,00
* Editar o 2° Orçamento 1.260,00 p/ 1.000,00

Quando consultar o saldo o valor do 1° estará zerado e no 2° será 1.260,00
