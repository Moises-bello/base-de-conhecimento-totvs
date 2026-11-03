---
article_id: 360016126271
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: daabb8dacf599fc11b0f813931f5a8cc65224cff3b2dde51c03ff5465a38ef87
fetched_at: '2026-06-28T22:38:41.005193+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Uso de Opcionais no Faturamento
type: support-article
updated_at: '2025-04-10T11:03:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016126271-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Uso-de-Opcionais-no-Faturamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16032152842775) Tempo aproximado para leitura: **00:01:00 min****

**Dúvida**

Como Uso de Opcionais no Faturamento - Pedido de Vendas (**MATA410**) e Orçamento (**MATA415**)?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Para utilização do Opcionais no Faturamento é necessário realizar a seguinte configuração;

* (1) Parâmetro MV\_SELEOPC = S;

* (2) Cadastro de Produto **(MATA010)** Exemplo: Produto PAI **"PA"** - Produtos Opcionais **"MP";**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21239948233879)**

* (3) Cadastro do Grupo de Opcionais **(MATA256)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21239930028567)

* (4) Cadastro da Estrutura **(PCPA200);**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21239930037399)

**OBSERVAÇÃO 1:**Na linha dos componentes, preencher o **"Grupo Opcio."** e **"Item Opcion."**, para a abertura da tela de **Opcionais** no Orçamento / Pedido de Vendas;

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21239948251031)**

**OBSERVAÇÃO 2:**Uma vez configurado o uso de Opcionais para o produto, aparecerá nas rotinas do faturamento (além das rotinas e módulo de PCP (Planejamento e Controle da Produção):

* Pedidos de Venda (MATA410)
* Orçamentos de Venda (MATA415)

**OBSERVAÇÃO 3:**O cadastro do campo Opcionais - **C6\_OPC,** por padrão tem o tamanho de 80 caracteres, tendo a possibilidade de aumento do campo até 254 caracteres que é o tamanho do limite no Banco para gravação de informação. Caso selecione mais que o limite o sistema vai gravar o restante das informações no C6\_MOPC.    
  
Para o produto pai da Estrutura de Produtos, ao mudar a linha de item, o sistema abrirá a janela de seleção dos componentes "Opcionais" para a escolha na venda..

Para que essa janela não apareça, tem de desativar o parâmetro (MV\_SELEOPC == N), porém nativamente ou fica habilitado em todas as rotinas e módulos ou desativado em todas.

Para que a janela de Opcionais não apareça apenas nos Pedidos de Venda ou Orçamentos de venda, deve-se utilizar o ponto de entrada:[MTSELEOP - Exibição da tela de seleção de opcionais do produto](https://tdn.totvs.com/x/oeRc).A composição do ponto de entrada é:

```
lSeleOpc: = ExecBlock (" MTSELEOP ", .F.,. F., {CRet, cProd , cProg})  
  
# A variável  cProg irá conter o nome do programa chamado, como por exemplo,  
# MATA650 para ordens de produção e MATA410 para os pedidos de venda.
```

**Saiba mais:**

[FAT0066 Uso de Opcionais no Pedido de Vendas](https://tdn.totvs.com/display/public/PROT/FAT0066+Uso+de+Opcionais+no+Pedido+de+Vendas)
