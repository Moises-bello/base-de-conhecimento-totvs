---
article_id: 1500010638982
category: Materiais - Compras (SIGACOM)
content_hash: e5755e2fdc1b450079305e61680b273143cdd31f5bbd05c16bb91bc0fa3601fe
fetched_at: '2026-06-28T22:41:16.029385+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar uma Devolução
  de Vendas na rotina de Documento de Entrada ?
type: support-article
updated_at: '2026-02-12T13:13:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010638982-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-uma-Devolu%C3%A7%C3%A3o-de-Vendas-na-rotina-de-Documento-de-Entrada
---

**Dúvida**  
Como realizar uma devolução de Vendas na rotina de Documento de Entrada ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões

**Solução**

Para se realizar na rotina de Documento de entrada (MATA103) uma devolução de uma Venda que foi feita e no módulo de Faturamento pode-se se seguir os passos abaixo:

**Opção 1:** Através da opção "Incluir:

Na rotina de Documento de Entrada, utilizar as opções da imagem abaixo:

* "Tipo da Nota" = "Devolução" (Perceber que ao escolher esta opção é mudada a opção de escolha de "Fornecedor" para "Cliente" )
* "Form. Próprio" / "Numero" / "Série" = Conforme a necessidade
* "Cliente" = conforme a NF de Saida que deseja realizar a devolução
* Nos Itens, preencher "Produto" e "TES" = Produto da NF que se deseja devolver e TES a ser utilizada

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017374721)

Clicar em "Outras Ações -> Origem" ou na tecla "F7" do teclado e será aberta uma tela com a lista de NFs de Saída conforme as informações que foram preenchidas até aqui:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017114242)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017375001)

Ao selecionar a NF desejada e confirmar conforme imagem acima, serão preenchidas as demais informações de "Quantidade" e "Valor" do Item da NF, conforme a NF Selecionada bem como as informações dos campos de "Docto", "Serie" e "Item" da NF Origem :

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017375041)

Ao confirmar, a NF é incluída ficando com o status de "Docto de Devolução" conforme a sua característica:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017114322)

**Opção 2:** Através da opção Outras Ações->Retornar

Para esta opção, a TES utilizada na NF de Venda no Faturamento, necessita estar com a amarração da TES de Entrada/Devolução  a ser utilizada na Devolução no campo "TES Devol" (F4\_TESDV) conforme imagem abaixo:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017115842)

No Browse da rotina de Documento de Entrada, utilizar a opção "Retornar":

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017115082)

Na tela aberta, preencher o código do Cliente referente à NF que deseja realzar a Devolução da Venda e Confirmar:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017115122)

Apção Tipo de Seleção conforme escolha, será possível vincular uma única origem, opção Documento ou pela opção Cliente/Fornecedor haverá a possibilidade de se vincular mais de uma nota de origem, pois há casos que há recebimento de uma única nota de entrada de devolução com mais de uma nota de origem ( venda/remessa ).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38352790174231)

São listadas as NFs de Saída referente a este cliente, pela opção Documento só conseguimos vincular uma única nota de origem ( venda/remessa )

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017115182)

Utilizando a opção Cliente/Fornecedor.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38352797078807)

O sistema exibirá um browser sendo possível escolher mais uma de nota de origem. Sendo possível clicar em cada quadradinho e escolher as origens.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38352790176279)

Ao selecionar a NF desejada e Confirmar, é aberta a tela padrão da rotina de Documento de Entrada, com as informações do item já preenchidas, a TES de Entrada que havia sido amarrada na TES da NF de Venda, e também as informações do "Docto", "Serie" e "Item Origem", podendo assim ser confirmada a inclusão.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017376461)

**Observações:**

**1-)** Caso sua nota fiscal de Venda tenha sido **recusada pelo cliente** basta fazer o processo acima de devolução porém utilizar a opção **formulário próprio = SIM**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414611085207)

Nesse caso, você estará retornando sua saída e deverá transmiti-la (com a sua sequência de numeração interna) para que seja fechado o processo de retorno.

**2-)** Para notas de devolução de vendas, o sistema padrão somente gera títulos a receber, pois o sistema utiliza o cadastro de clientes. Não conseguimos gerar um título a pagar nesse processo, pois títulos a pagar no sistema utilizam o cadastro de fornecedores.

Caso deseje customizar o processo em seu ambiente, segue abaixo a lista dos Pontos de entrada que temos disponíveis na rotina MATA103:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de entrada do Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-entrada-do-Documento-de-Entrada-MATA103?source=search)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
