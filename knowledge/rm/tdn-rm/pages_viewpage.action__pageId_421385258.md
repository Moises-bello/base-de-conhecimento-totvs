---
content_hash: 26fc28f37f29e5d5e20601ca0c5a7dc5eedfc792c16242ff4e5e797f4ed042fb
fetched_at: '2026-06-29T00:09:14.798698+00:00'
page_id: '421385258'
product: rm
source: tdn-rm
title: ETO Relatórios 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385258
version: 1
---

**ETO - Relatórios** ----   
Por ser considerado um processo crítico, o ETO necessita de alguns relatórios que possam proporcionar ao usuário um controle de suas ordens de produção, como por exemplo, produtos que necessitam de fabricação ou produtos manufaturados. Para realizar este controle foram desenvolvidos três relatórios que são do tipo ETO – Engenharia sob Demanda. São eles:  
   
**Relatório de Tarefas com produtos manufaturados**  
O principal objetivo deste relatório é exibir todas as tarefas que possuem produtos que necessitam de fabricação. Através deste relatório é possível visualizar as demandas de produção do projeto, compará-las com as datas planejadas das tarefas e verificar o que já foi pedido e quando será entregue.  
Neste relatório são apresentados os seguintes campos:  
**Código da tarefa:** código da tarefa ligada ao produto que necessita de fabricação. Ex:  001.01.01  
**Descrição da tarefa**: descrição da tarefa ligada ao produto que necessita de fabricação. EX: Escavação de tubulões  
**Unid.:** unidade de medida da tarefa. Ex.: UN  
**Data início:** data Inicio programada no PERT. Ex: 25/01/2014  
**Data Fim:** data fim programada no Pert. Ex: 01/07/2014  
**Produto vinculado:** descrição do produto associado ao insumo que está vinculado na tarefa ou composição. Ex: Computador  
**Data Prevista de Fabricação:** data média prevista do produto. EX: 25/06/2014  
**Quantidade Pedida:** quantidade solicitada via pedidos  
**Status do Item da Ordem**: status da ordem (criada, aguardando recursos, pronta para iniciar, parcialmente concluído, interrompida, concluída ou cancelada). Com base no status e na quantidade acima, para momentos em que a demanda não for totalmente solicitada em um único pedido, o planejador poderá calcular o saldo a solicitar.  
**Código da OP**: Código da Ordem de Produção  
**Número de Série**: quando houver, listará os números de serie produzidos para esta tarefa.  
   
Para gerar este relatório:  
1) Acessar o menu: RELATÓRIOS | RELATÓRIOS (GERADOR.NET) | PLANILHA DE TAREFAS;  
2) Informar os campos RELATÓRIO, TAREFA INICIAL e TAREFA FINAL;  
3) Gerar o Relatório.  
   
**Relatório de Composições com produtos manufaturados**  
O principal objetivo é exibir todas as composições que possuem produtos que necessitam de fabricação. Através deste relatório é possível consultar os serviços (composições) que são afetados pela manufatura.  
Neste relatório são apresentados os seguintes campos:  
   
**Código da Composição:** código da composição ligada ao produto que necessita de fabricação. Ex: C0001  
**Descrição da Composição:** descrição da composição ligada ao produto que necessita de fabricação. EX: Escavação de Tubulões  
**Und.**: unidade de Medida da Composição. Ex.: UN  
**Código do Insumo:** código do Insumo manufaturado  
**Descrição do Insumo:** descrição do Insumo Manufaturado   
   
Para gerar o relatório:  
1) Acessar o menu: RELATÓRIOS | RELATÓRIOS (GERADOR.NET) | COMPOSIÇÕES DO PROJETO;  
2) Informar os campos RELATÓRIO, TAREFA INICIAL e TAREFA FINAL;  
3) Gerar o Relatório  
   
**Relatório de Pedidos com produtos Manufaturados**  
O principal objetivo deste relatório é exibir todos os produtos manufaturados no pedido com custo e data atualizada de fabricação, por pedido e tarefa.  
Neste tipo de relatório é apresentado os seguintes campos:  
**Código do produto:** código do pedido de Produção. Ex:  0002  
**Código da Tarefa**: código da tarefa ligada ao pedido. EX: 001.01.01  
**Descrição da tarefa:** Descrição da tarefa ligada ao pedido. Ex.: Escavação de Tubulões  
**Und. da Tarefa:** Unidade de Medida da tarefa. Ex.: UN  
**Código:** Código do Produto manufaturado. Ex.: 01.01  
**Produto:** descrição do produto manufaturado. Ex.: Computador  
**Insumo:** descrição do Isumo ao qual o produto esta associado. Ex.: Areia  
**Quantidade Pedida:** quantidade pedida no envio de movimento. Ex.: 10  
**Unidade:** unidade de medida do produto solicitado. Ex.: UN  
**Custo de Fabricação:** custo para a fabricação do produto. Ex.: 1,10  
**Data Programada:** data programada para a finalização do produto. Ex.: 09/04/14  
**Insumo:** Insumo ao qual o produto está associado  
**Quantidade Pedida:** Quantidade pedida no envio de movimento  
**Unidade:** Unidade do produto solicitado  
**Custo de fabricação:** é exibido o custo para a fabricação do produto  
**Data programada:** é exibido a data programada para a finalização do produto.  
   
Para gerar o relatório:  
1) Inserir o relatório através do menu: OPÇÕES | GERAÇÃO DE PEDIDOS EM SUPRIMENTOS/FATURAMENTO|ANEXOS | RELATÓRIO |  INSERIR RELATÓRIO;  
2) Na tela de seleção do Relatório, selecionar o relatório ETO.003 PEDIDOS COM PRODUTOS MANUFATURADOS;   
3) Na tela Vinculo de Campos preencher os campos  COLIGADA = COLIGADA; IDENTIFICADOR DO PROJETO = PROJETO e IDENTIFICADOR DO PEDIDO = PEDIDO;   
4) Na tela Definição de Grupo de Visualização selecionar a opção TODOS;  
5) Após inserir o relatório, acessar: ANEXOS | RELATÓRIOS | PEDIDOS COM PRODUTOS MANUFATURADOS
