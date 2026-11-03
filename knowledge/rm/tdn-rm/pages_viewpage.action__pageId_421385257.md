---
content_hash: 9bebcf3b40ad196b7ba0590ff4d1414b08ca2aae704220631b4f40693af4c0f6
fetched_at: '2026-06-29T00:09:14.793113+00:00'
page_id: '421385257'
product: rm
source: tdn-rm
title: 'ETO – Engenharia sob Demanda: Gerar OP ou Compra'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385257
version: 2
---

Produtos produzidos precisam emitir uma ordem de produção para que inicie a fabricação, este processo está relacionado a todos os componentes e as etapas de fabricação determinadas pela estrutura do produto, além disso, é essencial na geração das requisições dos materiais. Para que o processo de ordem de produção seja solicitado é necessário que algumas premissas sejam feitas, como:  
 Projeto calculado  
 Curva ABC calculada  
 Cronograma previsto devidamente planejado  
 Cronograma calculado  
 Pert datas de início e fim programadas das tarefas preenchidos  
 Histograma calculado  
 O processo de ETO utiliza o modulo de "Geração de pedido" e "Geração de pedido extra", para emitir a ordem de produção dos produtos produzidos associados a tarefa, assim como é feito para pedidos de requisição de compra.  
    
 **Pedido de Material**  
 Para criar uma solicitação de ordem de produção utiliza-se a estrutura de pedido de material, mas devido as suas especialidades foi realizada algumas modificações na inclusão de um novo pedido para atender o processo, assim no cadastro de pedido foi criada uma nova opção chamada "Requisição de Produção".  
 Quando se estiver cadastrando um pedido de material, e este pedido estiver selecionado como Requisição de Produção será demonstrado no passo de seleção de insumos, apenas insumos que possuem "produtos manufaturados" associados.   
 O pedido de material irá conter apenas produtos manufaturados que serão fabricados. Para saber sobre os produtos fabricados, datas previstas de fabricação e custo médio de fabricação, foi criado o relatório para requisição de produção e na visão de pedido são apresentados todos os produtos que precisam ser produzidos por tarefa e as datas e custos previstos para a finalização da produção.  
 O processo de geração de ordem de produção pelo pedido de material, é realizado de acordo com a quantidade da necessidade prevista na carteira do pedido, mas para que o processo ocorra normalmente, é necessário parametrizar o tipo de movimento do RMNucleus, que tem vínculo com o RMFactor. A solicitação de ordem de produção para o produto manufaturado é feita pelo processo "Envia pedido para Suprimentos/Faturamento gerando apenas 1 (um) movimento" ou "Envia pedido para Suprimentos/Faturamento gerando apenas 1 (um) mov. por data de entrega".    
 Quando um dos processos for executado e finalizado, é necessário realizar a associação do movimento gerado no TOP a ordem de produção, com esse vínculo o RMFactor inicia a produção do produto manufaturado, e o mesmo será responsavel por todo o acompanhamento e controle da produção.  
    
 Abaixo segue os passos de como utilizar o processo de produção:  
 1) Acessar o Totvs Obras e Projetos;  
 2) Selecionar o Projeto I0001 - ETO - Engenharia sob Demanda;  
 3) Acessar o menu: CADASTROS|INSUMOS e editar o insumo do Totvs Obras e Projetos que será associado ao produto manufaturado cadastrado no RMFactor;  
 4) Acessar a aba 'PRODUTOS DE SUPRIMENTOS/FATURAMENTO', clicar no botão NOVO e associar o Insumo Manufaturado cadastrado no Factor ao Insumo do Totvs Obras e Projetos;  
 5) Acessar o menu OPÇÕES|GERAÇÃO DE PEDIDOS EM SUPRIMENTOS/FATURAMENTO;  
 6) Gerar  um pedido de REQUISIÇÃO DE PRODUÇÃO;  
 7) Selecionar o pedido criado e acessar o menu PROCESSOS|ENVIA PEDIDO PARA O SUPRIMENTOS/FATURAMENTO GERANDO APENAS (1) UM MOVIMENTO ou ENVIA PEDIDO PARA O SUPRIMENTOS/FATURAMENTO GERANDO (1) UM MOV. POR DATA DE ENTREGA;  
 8) Após enviar o pedido para o Suprimentos/Faturamento acessar o RMFACTOR;  
 9) Acessar o menu PRODUÇÃO|ORDEM DE PRODUÇÃO|PROCESSOS|GERAR ORDENS A PARTIR DE PEDIDOS DO NUCLEUS;  
 10) Filtrar pela data do pedido que foi criado no Totvs Obras e Projetos e enviado para o RMNucleus;  
 11) No campo ORDEM DE PRODUÇÃO clicar com o botão direito e selecionar a opção CRIAR NOVA ORDEM;  
 12) Clicar no Pedido e arrastá-lo para a ordem que acabou de ser criada;  
 13) Clicar  no botão GERAR ORDENS;  
 14) Verificar o campo DATA/HORA FINAL PREVISTA com a Ordem de Produção que acabou de ser gerada.

**Observação:**  
Como sugestão para o processo, cadastre no RMNucleus um tipo de movimento do tipo "2.1.XX – Ordem de Produção (RMFactor)" e, no processo "Produção" desse movimento, marque o campo "Gera Ordem de Produção no RMFactor".  
Quando gerada a ordem de produção no RMFactor a partir do pedido do RMNucleus, ela terá seu status como "Criada". A data final prevista pelo cálculo do MRPII – via integração – será registrada na Aba "Integrações" do movimento que originou a ordem de produção, no campo "Data de programação Anterior". Quando a ordem de produção é promovida para o status "Pronta para iniciar", é gerada uma data atualizada para previsão de finalização da produção, esta data será registrada automaticamente pelo sistema na mesa aba no campo "Data de Programação".  Após a atualização de previsão de finalização do produto, o TOP irá verificar e solicitar a alteração das datas programadas do Pert de acordo com parametrização (processo melhor detalhado abaixo).  
Quando o RMFactor finalizar a fabricação do produto manufaturado, o mesmo irá disparar um movimento de entrada de estoque para o Suprimentos/Faturamento, com essa solicitação será possivel gerar o movimento de solicitação de compra do produto.

**Exclusão da Ordem de Produção**  
 Para acesso a funcionalidade, na tela de requisição de material, basta selecionar a requisição ou o item da requisição, o qual deseja excluir, acionar o botão "Excluir" ou o processo de "Excluir Movimento".

A exclusão é permitida para qualquer ordem de produção em status "Criada".   
Para ordens de produção que estejam no status "Aguardando Recursos", somente é permitida a exclusão daquela para a qual não houve geração de solicitação de compra, já que não ocorreu movimentação de matéria-prima ou alocação da capacidade produtiva.   
Para os status pronta para iniciar, parcialmente concluída, concluída e cancelada o sistema não permite a exclusão, em função de já estarem ligadas a outros registros.
