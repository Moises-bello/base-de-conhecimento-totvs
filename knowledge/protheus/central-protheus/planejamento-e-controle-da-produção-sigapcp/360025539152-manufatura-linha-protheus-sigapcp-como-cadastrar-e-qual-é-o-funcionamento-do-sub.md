---
article_id: 360025539152
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c240d78e5c36036399cf695bf6d678ca546ed8faeeec4fceec1430a052da540b
fetched_at: '2026-06-28T22:42:41.067830+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como cadastrar e qual é o funcionamento
  do subproduto
type: support-article
updated_at: '2025-09-11T20:17:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025539152-Manufatura-Linha-Protheus-SIGAPCP-Como-cadastrar-e-qual-%C3%A9-o-funcionamento-do-subproduto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34878656071831)**Tempo aproximado para leitura: **00:02:20 min**  
**Dúvida**Durante o processo produtivo, ocorre a geração de outro produto que pode ser comercializado ou consumido em outro processo, como cadastrá-lo? E qual é o funcionamento desse **subproduto**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O **subproduto** é cadastrado por meio da rotina **PCPA200 - Estrutura**,e ele é identificado pela quantidade negativa na estrutura, o Sistema verifica o parâmetro **MV\_NEGESTR - Permite incluir itens negativos na estrutura, sendo que estes itens gerarão devoluções no arquivo de movimentos nos módulos de Estoque/PCP**, para permitir cadastrar itens negativos na estrutura. O **subproduto** é utilizado quando ao produzir um produto principal, ocorre a geração de outro produto através do resíduo. Este **subproduto** pode ser comercializado ou utilizado em outro processo produtivo, ou somente para manter um controle de estoque.  
  
Por exemplo, o processo produtivo do queijo, no qual temos como matéria-prima o leite e como **subproduto** o soro, sendo que o soro pode ter controle de estoque, ser comercializado ou utilizado na estrutura de outro produto. Suponhamos que para a produção de 1 kg de queijo precisamos de 2 litros de leite e tenhamos como resultado 0,200 litros de soro, então poderíamos ter a seguinte estrutura:  
  
Produto Queijo;  
|\_leite - 2 litros;  
|\_soro - -0,2 litros - **subproduto**.  
  
Então neste caso, ao produzir o queijo teremos a entrada em estoque da quantidade produzida, a saída do leite consumido e a entrada em estoque do soro do leite. Para uma **OP - Ordem de produção** de 20 quilos, teríamos portanto:

* Entrada em estoque de 20 quilos de queijo;
* Saída do estoque de 40 litros de leite;
* Entrada em estoque de 4 litros de soro.

Porém, caso falte soro em estoque para atender alguma demanda, ao identificar a necessidade deste material, será aberta uma **OP** para o produto queijo, pois produzindo o queijo é que a necessidade do soro será atendida. Caso tenha identificado a necessidade de 8 litros de soro, o Sistema abrirá uma **OP** de 40 quilos de queijo, havendo desta forma:

* Entrada em estoque de 40 quilos de queijo;
* Saída do estoque de 80 litros de leite;
* Entrada em estoque de 8 litros de soro, atendendo a demanda.
