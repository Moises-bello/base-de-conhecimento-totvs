---
article_id: 360024673534
category: Materiais - Compras (SIGACOM)
content_hash: 8f7fa2d77051320a3d970deb8046938b72ebb56030ac5b7012b00b84a0cf7ae2
fetched_at: '2026-06-28T22:41:24.243907+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a Funcionalidade
  da rotina Eliminar de Resíduo (MATA235)
type: support-article
updated_at: '2026-06-23T19:17:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024673534-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-Funcionalidade-da-rotina-Eliminar-de-Res%C3%ADduo-MATA235
---

**Dúvida**

Qual a Funcionalidade da Eliminação de Resíduo (MATA235)  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Quando a empresa recebe entradas parciais de materiais, muitas vezes os registros (pedidos de compras, autorizações de entrega , contratos de parceria e solicitações de compras) ficam em aberto por quantidades muito pequenas, insuficientes para que se faça uma nova entrega. São resíduos que devem ser eliminados para que não haja reserva em estoque, o que pode atrapalhar o atendimento de novos pedidos, visto que o estoque vai tentar primeiro atender a este.

Essa funcionalidade pode ser utilizada para se encerrar uma SC que foi feita compra a menor do que foi solicitado.

A eliminação de resíduos é um cancelamento das pequenas quantidades que sobram nos pedidos de compras, autorizações de entrega , contratos de parceria e solicitações de compras.

***Procedimentos***  
*Para efetuar a eliminação de resíduos:*

*Em "Compras->Atualizações->Pedidos->Eliminar Residuos":*

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102391473)*

1. **Em Eliminação de Resíduos, clique em Parâmetros.**
2. **Preencha os dados conforme orientação do help de campo.**
3. **Confira os dados e confirme a operação de eliminação de resíduos.**

***Importante:***  
**No processamento desta rotina, são efetuados os seguintes ajustes:**  
*\*\*   Os saldos dos pedidos de compra, autorizações de entrega, contratos de parceira ou solicitações de compra são analisados, e os registros com saldo inferior ao percentual informado são encerrados pelo*  
*\*\*   Sistema, indicando a eliminação por resíduos.*  
*\*\*   Os saldos previstos de entrada são recalculados na tabela de Saldos Físicos e Financeiros.*  
*\*\*   Os saldos dos aprovadores são recalculados;*

*\*\* Os documentos com alçadas são eliminados, ou seja, o registro da alçada é "apagado" na tabela SCR*

**Para executar a rotina para eliminação de resíduo de pedidos de compras de forma efetiva seguir os passos abaixo:**

• Percentual Máximo = 100%

• Data de emissão (De/Até) = Informar um intervalo abrangente, sendo que os pedidos (caso a necessidade seja eliminar PC, senão informar conforme a necessidade) que serão eliminados devem estar dentro deste período.

• Pedido (De/Até) = Informar o intervalo ou numero especifico do pedido a eliminar

• Produto (De/Até) = Caso desejar poderá informar um intervalo ou produto especifico que deve ser eliminado do pedido. Para eliminar o resíduo do pedido independente do produto, informar "branco" a "ZZZZZZ".

• Eliminar Resíduo Por = Pedido de Compra (caso a necessidade seja eliminar PC, senão informar conforme a necessidade)

• Fornecedor (De/Até) = Caso desejar poderá informar um intervalo ou fornecedor especifico que deve ser eliminado. Para eliminar o resíduo do pedidos independente do fornecedor, informar "branco" a "ZZZZZZ".

• Data de entrega (De/Até) = Informar um intervalo abrangente, sendo que os pedidos que serão eliminados devem estar dentro deste período.

• Item (De/Até) = Informar o intervalo ou numero especifico do pedido a eliminar

• Produto (De/Até) = Caso desejar poderá informar um intervalo ou item especifico que deve ser eliminado do pedido. Para eliminar o resíduo do pedido independente do item, informar "branco" a "ZZZZZZ".  
Após a execução do processo, o pedido terá sido eliminado o resido se na rotina de pedido de compras sua legenda estiver "cinza" e na tabela SC7 o campo C7\_RESIDUO estiver marcado com 'S'.

**Observação 1 :**:

Não orientamos e nem sugerimos alterar o campo C7\_RESIDUO colocando "S" direto na rotina do Pedido de Compras (MATA121), pois inserir "S" altera a cor da legenda do Pedido na rotina, mas não há como mensurar o impacto dessa alteração manual dentro do sistema, dessa forma, recomendamos **sempre utilizar a rotina Eliminação de Resíduos (MATA235)**.

**Observação 2 :**

Uma vez que os registros sejam finalizados pela rotina de eliminação de resíduos, não temos como reverter o processo pelo padrão do sistema. Será necessário incluir um novo registro, seja solicitação de compras, pedido de compras, etc com o saldo que foi eliminado para ocorrer os vínculos.

**Observação 3 :**

Itens que estão em processo de Cotação não serão eliminados o resíduo pela rotina MATA235 , para não perder integridade e histórico com a cotação já gerada.

**Observação 4 :**

Pedidos de compras que foram gerados pelo módulo do SIGAEIC ( PO´s, **Purchase Order** ) devem ter o resíduo eliminado diretamente no módulo do EIC. Vide documentação abaixo :

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025888952-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Elimina%C3%A7%C3%A3o-de-Saldo-da-Purchase-Order>

**Observação 5 :**

O usuário consegue identificar na SC se o item teve resíduo eliminado através da opção Visualizar, **no campo Elim.Resíduo,** pois o sistema o preenche com conteúdo **S,** quando o resíduo do item for eliminado.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21648996299415)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21648951174167)**

**Observação 6 :**

Ao realizar a Eliminação de Resíduo de um Pedido que teve Aprovação por Alçada, o Saldo do aprovador utilizado é retornado.

**Observação 7 :**

Solicitações de Compra originadas no módulo PIMS, por conceito do sistema no funcionamento padrão da rotina, não podem ter seu resíduo eliminado através da utilização da funcionalidade de Eliminação de Resíduos.

**Observação 8 :**

A MATA235 pode ser executada via Smart Schedule a partir da release 2410 do sistema.

[**Execução da MATA235 via Smart Schedule**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018783772-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-executar-a-rotina-Elimina%C3%A7%C3%A3o-de-Res%C3%ADduos-MATA235-de-forma-autom%C3%A1tica)

**Observação 9 :**

**Quando a rotina é executada e o sistema não elimina o resíduo o que fazer ?**

**A rotina de eliminação de resíduos precisa ser executada na filial do registro que precisa ter o resíduo eliminado. O sistema também valida e verifica todas as perguntas dos parâmetros da rotina.**

***9A-) Se o registro a ser eliminado é de um pedido de compras.***

Por padrão o sistema posiciona na tabela SC7 e verifica os campos **:**

**C7\_QUANT (quantidade comprada)**,

**C7\_QUJE (quantidade já recebida, NFE já classificada)** ,

**C7\_QTDACLA (quantidade a classificar, NF em pre nota),**

**C7\_RESIDUO (quando o resíduo do item já foi eliminado, ele fica gravado com S)  e**

**C7\_ENCER (quando o item do PC já está totalmente encerrado é gravado com E).**

Se a soma do **QUJE com o QTDACLA for menor que o QUANT**, ai o sistema entende que há resíduo a ser eliminado, aí na sequência ele verifica o ENCER e o RESIDUO, se ambos estão em branco, o resíduo será eliminado normalmente e o campo C7\_RESIDUO gravado com S e o C7\_ENCER gravado com E.

Para saber se há residuo a eliminar, ele faz a conta C7\_QTDACLA + C7\_QUJE. Essa soma precisa ser menor que o conteúdo do campo C7\_QUANT.

Quando o pedido de compras é oriundo de uma medição de contrato ( módulo GCT ), o sistema verifica o parâmetro **MV\_CNRESID.**Veja mais detalhes na documentação:[**https://tdn.totvs.com/pages/releaseview.action?pageId=272417737**](https://tdn.totvs.com/pages/releaseview.action?pageId=272417737)

Quando o pedido de compras é oriundo do EIC ( Easy Import Control ), a eliminação de resíduos deve ocorrer em rotina no módulo de origem ( EIC ).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41436934664087)

***9B-) Se o registro a ser eliminado é uma solicitação de compras.***

Por padrão o sistema posiciona na tabela SC1 e verifica os campos **:**

**C1\_QUANT (Quantidade solicitada),**

**C1\_QUJE (Quantidade recebida, ou seja, quantidade vinculada à um pedido de compras),**

**C1\_RESIDUO (Resíduo Eliminado. Quando o resíduo do item já foi eliminado, ele fica gravado com S),**

**C1\_COTAÇÃO(se preenchido e diferente de XXXXXX).**

O conteúdo do C1\_QUJE precisa ser menor que o C1\_QUANT, para que o sistema entenda que há saldo no item da SC, para ser eliminado como resíduo. O C1\_RESIDUO também precisa estar em branco e o C1\_COTAÇAO em branco ou diferente de XXXXXX.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41436886395415)

***9C-) Se o registro a ser eliminado é uma Autorização de Entrega.***

As validações que ocorrem são basicamente as mesmas do pedido de compras, no tocante a poscionar na tabela SC7 e validar os campos. Pois a Autorização de Entrega também é gerada na tabela SC7.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41436934666519)

***9D-) Se o registro a ser eliminado é um Contrato de Parceria.***

Por padrão o sistema posiciona na tabela SC3 e verifica os campos **:**

**C3\_QUANT (Quantidade contratada),**

**C3\_QUJE (Quantidade Entregue, quantidade vinculada à uma autorização de entrega),**

**C3\_ENCER (Item encerrado) e**

**C3\_RESIDUO** **(Resíduo Eliminado. Quando o resíduo do item já foi eliminado, ele fica gravado com S).**

**O conteúdo do C3\_QUJE precisa ser menor que o C3\_QUANT, para que o sistema entenda que há saldo no item do contrato para ser eliminado como resíduo. O C3\_RESIDUO e o C3\_ENCER, também precisam estar em branco.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41436934667159)

***Saiba Mais :***

[*C7\_QTDACLA*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028009671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Eliminar-Res%C3%ADduos-n%C3%A3o-ocorre-no-Pedido-de-Compras-Rela%C3%A7%C3%A3o-com-campo-C7-QTDACLA?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
