---
content_hash: 5cc3f6cf277a6a3a43b85a913a85203821dca5c9ceb18670d03fed4be324f5cd
fetched_at: '2026-06-29T00:09:14.086926+00:00'
page_id: '421385117'
product: rm
source: tdn-rm
title: Aplicar Revisão de Reprogramação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385117
version: 5
---

Antes de ser efetuada a Aplicação da Revisão de Reprogramação, recomendamos que seja executado o cálculo do Projeto da Revisão Horizontal da Revisão de Reprogramação, pois este cálculo irá garantir a utilização de recursos, quantidade prevista e valor em tarefas.  
Ao acessar o processo de Aplicação da Revisão de Reprogramação, será exibido na parte inferior da tela a data de último cálculo do projeto selecionado.   
    
Ao Aplicar a Revisão de Reprogramação o usuário poderá optar por aprová-la ou rejeitá-la, e caso tenha aprovado, o sistema exibirá duas mensagens solicitando ao usuário que confirme se deseja realmente prosseguir pois a solicitação de aprovação é um processo irreversível.  
   
Caso o usuário opte por rejeitar o projeto de Revisão de Reprogramação sua posição será modificada para cancelado e ficarão registrados na observação do seu histórico, a rejeição, o usuário que a rejeitou e o texto que o usuário informar para detalhar a rejeição. Nesta situação o projeto original não sofre nenhuma alteração.  
   
No caso de Aprovação, o status do projeto de Revisão de Reprogramação será modificado para concluído e ficarão registrados na observação do histórico, a aprovação e o usuário que a aprovou. Nesta situação o projeto original passa para a posição Revisado, sendo criada uma nova revisão que passa a ser o projeto em vigor.  
   
**Exemplo:**   
   
Venda 1    – Revisão Vertical de Venda (Principal) Venda 1.1 – Revisão Horizontal de Revisão de Reprogramação Venda 1.2 – Revisão Horizontal de Revisão de Reprogramação 2.  
   
Aplicando Revisão de Reprogramação na Venda 1.1  
   
Venda 1    – Revisão Vertical de Venda (Revisado) Venda 1.1 – Revisão Horizontal de Revisão de Reprogramação (Concluído) Venda 2    – Revisão Horizontal de Revisão de Reprogramação  
Venda 2.1 – Revisão Horizontal de Revisão de Reprogramação 2.  
   
Sendo que, a Venda 2 corresponde a um novo projeto criado que contém as informações Venda 1 e Venda 1.1 e a Venda 2.1 corresponde à Revisão de Reprogramação que não foi aplicada, portanto passa a ser "filha" do novo projeto.  
   
No caso de aprovação da Revisão Horizontal de Revisão de Reprogramação, o sistema efetuará as seguintes ações para aplicar as alterações efetuadas:

* Para as tarefas incluídas, renumeradas ou que tiveram seu código alterado, ao serem aplicadas na nova revisão ativa, irão prevalecer as informações do projeto mandatário;
* Para as tarefas que sofreram qualquer outro tipo de alteração, elas serão aplicadas na nova revisão ativa, lembrando que nas alterações para quantidade inferior serão verificados os parâmetros de consistência da Revisão de Reprogramação;
* As alterações ao Cronograma Previsto serão replicadas para a nova revisão ativa. Já os cronogramas realizado e medido, mesmo que tenham sido modificados não serão aplicados, visto sua edição ser permitida na Revisão de Reprogramação, apenas para efeito de simulações;
* Composições e Insumos alterados serão replicados para a nova revisão ativa;
* Composições e Insumos criados serão criados na nova revisão ativa;
* Se no projeto pai existir algum insumo ou composição cujo código entre em conflito com algum cadastrado na Revisão de Reprogramação, o processo será abortado e emitirá um aviso com os insumos e/ou composições que devem ser ajustados antes de se aplicar a Revisão de Reprogramação;
* Preços ativos de insumos da Revisão de Reprogramação deverão prevalecer em relação aos preços dos insumos do projeto pai;
* Se no projeto pai uma tarefa existente somente na revisão de Revisão de Reprogramação, for excluída, ela não será recriada através do processo de Aplicação.

A aplicação da Revisão Horizontal de Revisão de Reprogramação, possui ainda as seguintes características:

* Antes de iniciar o processo, o projeto pai será revisado para que seja mantida uma versão com o projeto que estava em execução;
* Todas as revisões de Revisão de Reprogramação que estavam pendentes serão vinculadas à nova revisão ativa. São consideradas revisões pendentes, aquelas para as quais não foram aplicados nem o processo de Rejeição nem o de Aprovação;
* Depois de aplicada uma Revisão de Reprogramação o sistema não irá mais permitir que a mesma seja excluída, já que ela documenta as alterações realizadas ao longo do projeto.

O log de usuários irá registrar o usuário responsável pelas alterações na revisão de escopo atual, da mesma forma que registraria se fosse uma alteração normal.  
Além disso, como a Revisão de Reprogramação quando criada não leva para o projeto os Contratos e suas Medições, Riscos, Apontamentos, Mobilidade e Planos de Compras realizados no projeto pai, faz-se necessário que no momento da Aplicação, o TOTVS Obra e Projetos realize consistências, garantindo a integridade do projeto que está em execução. Para isso é necessário realizar a conferência e tratar as consistências dos seguintes módulos:

* Travamento de Períodos;
* Contrato;
* Plano de compras.

Para as consistências dos módulos de contrato e plano de compras o sistema irá levar em consideração o que foi parametrizado em Consistência da Revisão de Reprogramação e irá desprezar, somente avisar sobre as divergências encontradas ou barrar a aplicação da Revisão de Reprogramação, conforme parametrizado.  
Já no caso do travamento dos períodos do cronograma, como o sincronismo é um processo dependente do usuário, a rotina de aplicação de revisão de Revisão de Reprogramação irá analisar se existe compatibilidade entre o projeto aprovado e o projeto principal que se encontra em execução. Caso os projetos sejam incompatíveis o TOTVS Obras e Projetos irá abortar a rotina, informando ao usuário a necessidade de se executar o processo de sincronização de projetos.   
As consistências analisadas pelo TOTVS Obras e Projetos serão feitas pela dimensão de quantidade e irão garantir que a quantidade da tarefa no projeto de revisão esteja lançada no cronograma planejado respeitando os parâmetros do projeto definidos para o cronograma.  
Será garantido também que no processo de Aplicação da Revisão de Reprogramação, não se percam informações dos processos que envolvam integrações, tais como:

* Mobilidade: Apontamentos, Folhas, Associações de Bens, Funções, Equipes, Alocação de Mão de Obra, Custo Improdutivo e Produtivo;
* Apropriação;
* TimeSheet: Apontamento, Alocação;
* Pedido de Material;
* Contratos.

É importante que ao final do processo de aplicação de Revisão de Reprogramação o usuário realize uma conferência dos processos que envolvem integrações com o BackOffice como Integração com Orçamento e Fluxo de Caixa, pois como o planejamento pode ter sofrido alteração é importante que estes processos sejam atualizados pelos usuários.  
   
**Atenção:**  
   
Em caso de conflito de código, os Insumos | Composições | Grupos de Custo do projeto Origem passam a ser incluídos no projeto de Revisão de Reprogramação com um Código Padrão, como por exemplo: IALTESC0001 para Insumo | CALTESC0001 para Composição, ignorando máscara, auto incremento e parâmetros de projeto e o cliente deverá alterar o código default criado no formulário de insumo para realizar a aplicação.   
   
Para Aprovar ou Rejeitar a Aplicação de Revisão de Reprogramação é necessário que o Perfil do usuário tenha permissão para esta função.

---
