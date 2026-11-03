---
content_hash: 1fcb59272c902b498fab3e78142822d7e4b5221db7e4863e168999710bd83d07
fetched_at: '2026-06-29T00:09:13.639195+00:00'
page_id: '421385075'
product: rm
source: tdn-rm
title: Aprovação de Pedidos de Material Extra.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385075
version: 2
---

O Pedido de material extra tem a finalidade de controlar os gastos de material extra, ou seja, material além do planejado, onde são controladas todas as movimentações de pedidos, autorização do pedido, quantidade pedida para determinada tarefa e principalmente as pessoas envolvidas no processo.  
    
 O workflow de aprovação de pedidos de material extra via Fluig irá incorporar ao TOP (TOTVS Obras e Projetos) a opção de realizar a aprovação de pedidos de material extra através de um novo caminho, além do próprio TOP, o ambiente Fluig. Esse novo caminho para a aprovação irá seguir os mesmo passos da aprovação já existente, tentando ao máximo manter o elementos já presentes nela.  
    
 Através do pedido de material extra com aprovação via TOTVS Obras e Projetos, permite elaborar um pedido de material ao sistema de BackOffice, sendo que este deverá ser aprovado por algum gestor com permissões para exercer tal ação. Neste pedido o usuário irá incorporar itens que serão solicitados em quantidades de acordo com a necessidade descrita. Ao termino da elaboração do pedido o operador irá submeter esse pedido a aprovação, e neste momento o pedido será encaminhado a quem deverá analisa-lo e aprovar/reprovar o mesmo.  
 Após o envio do pedido para aprovação, o mesmo deverá ser aprovado/ reprovado. Neste ponto o usuário com permissões de aprovar o pedido e seus itens, irá manifestar seu consentimento ou não diante dos dados apresentados. Neste momento ele poderá: Aprovar completamente todo o pedido; Reprovar completamente todo o pedido; Aprovar item a item; Aprovar completamente o item; Aprovar parcialmente o item (informando a quantidade ou o percentual de aprovação); Reprovar o item. Este será o ponto o qual o workflow irá atuar fornecendo informações via Fluig para que o seja possível realizar a aprovação dentro da sua plataforma. O operador aprovador munido de um usuário com permissões para aprovar o workflow irá visualizar no Fluig as mesmas informações visualizadas no TOP, tanto do pedido quanto de seus itens.  
 **Parametrização:** Nos parâmetros gerais aba "Fluig" foi disponibilizado dois novos parâmetros. Esses parâmetros indicarão qual será o processo relativo ao workflow de aprovação de contratos e também quais serão os estados que indicarão que o workflow está "Aprovado" e "Reprovado". Nos parâmetros do Projeto, aba "Integração Fluig" foi adicionado os seguintes parâmetros, "Utilizar workflow de aprovação de pedido de material extra", que indica ao TOP que os pedidos de material extra serão avaliados no Fluig.   Aprovação total do pedido  
 O workflow de aprovação de pedido de material extra essa irá acontecer quando o usuário Fluig selecionar prosseguir o workflow para o estado final de "Aprovar", com todos os itens da listagem do formulário com suas quantidades aprovadas em 100% da quantidade pedida, essa avaliação será feita no momento que o workflow estiver mudando para o estado aprovado. Caso seja zerada a quantidade aprovada de todos os itens, ou seja, 0% da quantidade pedida, e o workflow prosseguir ao estado Aprovado, automaticamente o mesmo irá atribuir ao workflow o estado Reprovado, já que este é real estado refletido pelas quantidades aprovadas dos itens.   
 **Reprovação total do pedido** Atribuirá a todos os itens do pedido o percentual associado de 0% e o status de reprovado. No workflow de aprovação de pedido de material extra esse comportamento será representado pelo estado "Reprovar", atribuindo o percentual da quantidade associada de 0% da quantidade pedida.  
 **Aprovação parcial do pedido e Aprovação parcial dos itens** A aprovação parcial de um item o mesmo pode não ter sua quantidade aprovada integralmente (menos de 100% da quantidade solicitada). No workflow de aprovação de pedido de material extra esse comportamento será representado pelo estado "Aprovar, irá finalizar o pedido e irá encaminhar ao TOP os itens do pedido no estado que o aprovador os deixou. Ao visualizar o workflow de aprovação de pedido de material, o usuário acessa a aba que irá exibir os dados dos itens, e nesta aba será possível atribuir a quantidade aprovada a um item. Existirá também nesta a opção de aplicar um percentual de aprovação em sobre a quantidade pedida, bastando apenas informar esse percentual e selecionar quais itens deseja que seja aplicado o percentual.  
    
 **Comportamento na tela de Aprovação de pedido de material extra Fluig** Como o ambiente no qual o workflow está inserido existem particularidades, as telas de aprovação do workflow não serão espelhos das telas existentes no TOP. Alguns processos e campos serão eliminados, afim de tornar a visualização mais limpa e objetiva, deixando a vista somente dados relevantes da aprovação. Por tanto processos como os de aprovar, reprovar e aprovar parcialmente não existirão, e os seus comportamentos serão absorvidos por interações mais eficientes em um ambiente web e de workflow.   
 Continuando nesta linha de raciocínio a aprovação de um item será feita com a seleção do mesmo na caixa ao lado do seu nome. Visão Fluig dos itens do pedido, ao selecionar a caixa a quantidade aprovada será registrada em 100% da quantidade pedida. O mesmo ocorrerá ao desmarcar a caixa, porem, esse processo irá reprovar o item atribuindo ao mesmo na quantidade aprovada 0% da quantidade pedida. A qualquer momento o usuário poderá inserir na caixa de texto da quantidade aprovada um valor indo de 0,00...1 a 99,99...9% da quantidade pedida, esse comportamento irá atribuir ao item o status de aprovado parcialmente.  
 Nenhum outro campo a não ser a quantidade aprovada estará disponível para edição. A qualquer momento o usuário poderá salvar o formulário, usando-se do botão presente no workflow para tal ação.  
    
  Informações Complementares

---

**Procedimento para Implantação:**  
 Deverá ser exportado para o servidor Fluig o Workflow RM.Prj.AprovacaoPedidoMaterialExtra que se encontra no diretório de Objetos Gerenciais da instalação do produto.  
 Deverá ser exportado também duas Consultas SQL que se encontram no diretórios ConsultaSQL dentro do diretório do Workflow. O nome do arquivo é PedidoExtra-WfFluig.TotvsSQL e o nome das consultas são: MPEDIDOMATEXTRA e MITMPEDMATEXTRA  
 Para exportar o workflow utilize você deverá ter instalado o TDS (TOTVS Developer Studio) e o plugin do Fluig. Visite o TDN para informações de instalação dos mesmos: Guia de instalação fluig Studio.  
 Uma vez instalado agora é hora de importar o Workflow para o TDS para manipularmos e posteriormente importá-lo para o servidor Fluig do cliente. Para importar o Workflow siga os passos explicados no TDN na página: Importação e exportação de projeto no Fluig Studio#ExpediçãodeprocessodeworkflowpelopluginFluignoTDS.  
 Caso deseje criar um novo Workflow a página seguinte detalha a criação e importação para o servidor Fluig do novo Workflow: Guia Rápido Fluig#Workflow.  
 É importante que se modifique o nome do Serviço utilizado para acessar os métodos do Serviço de Consulta SQL contidos nos datasets do workflow.  
    
    
   Como Fazer

---

**Procedimento para Configuração**  
 **CONFIGURAÇÃO DE PARÂMETROS**  
  São três tipos de configurações de parâmetros que devem ser feitas no TOTVS Obras e Projetos para se trabalhar com o Workflow Fluig.  
 Na **Configuração Global**, acesse Construção e Projetos | Projeto | Globais | Agrupador Integração Fluig. Configure os dados do endereço do servidor Fluig, usuário, senha e identificador da empresa.  
    
 Nas **Configurações Gerais do TOP**, acesse Construção e Projetos | Projeto | Construção e Projetos| Gerais | Agrupador Fluig | Agrupador Pedido Extra. Escolha qual Workflow será utilizado para a aprovação de pedido de material extra e quais serão os Estados de aprovação e de reprovação.  
    
 Nos **Parâmetros de Projetos do TOP**, acesse Construção e Projetos | Projeto | Construção e Projetos | Projetos | Agrupador Integração | Agrupador Integração Fluig. Marque a opção "Integração Fluig" e "Utilizar Workflow de Pedido de Material Extra".  
    
 Nos **Parâmetros de Projetos do TOP**, acesse Construção e Projetos | Projeto| Construção e Projetos| Projetos| Agrupador Integração |Agrupador Integração Suprimento e Faturamento | Pedido de Material Extra| Utilizar fluxo de aprovação para pedido extra | Geração do movimento após aprovação. Podendo marcar a opção "Manual", "Automática Movimento Único", "Automática Movimento por data de entrega" .  
    
 **Procedimento para Utilização** **Utilizando o Workflow no TOTVS Obras e Projetos**  
 Após configurar e escolher um projeto no TOP, acesse Construção e Projetos | Planejamento | Geração de Pedido Extra. Crie um novo Pedido de Material Extra e insira os itens para o pedido.  
 Na visão de Pedidos de Material Extra escolha o Processo "Enviar Pedido Extra para Aprovação". Ao final do processo uma mensagem será exibida informando da criação de um Workflow Fluig para aprovação do Pedido.  
    
 **Visualização e aprovação/reprovação do Workflow no Fluig**  
 Faça login no Fluig e clique no link Tarefas a concluir.  
    
 A página seguinte irá mostrar todas as suas tarefas à concluir. Encontre na tabela de tarefas o Workflow "Aprovação de Pedido de Material Extra" e dê um clique sobre ele.  
    
 Será aberto o Workflow com os dados do Pedido de Material Extra e os dados dos Itens do Pedido, além das opções de "Solicitar Justificativa", "Aprovar" e "Reprovar" o Workflow.  
 Caso queira solicitar uma justificativa para aprovar o Workflow, no campo "Enviar para a atividade" escolha Solicitar Justificativa e insira alguma informação (opcional) no campo Justificativa e escolha para qual usuário você estará pedindo a Justificativa e em seguida clique no botão Salvar e logo depois em Enviar, conforme figura abaixo. Após enviar o Workflow o mesmo irá aparecer para o usuário escolhido informar a justificativa.  
    
 Para Aprovar ou Reprovar o Workflow escolha no campo "Enviar para a atividade" sua opção e depois clique no botão Enviar.  
 Para aprovação parcial dos itens defina a quantidade aprovada no campo "Quant. Aprovada" de cada item e depois no campo "Enviar para a atividade" escolha Aprovar. Você tem a opção de inserir um percentual de aprovação por item.   
 Após Aprovar o Workflow o Pedido de Material Extra já pode ser Gerado o movimento.   
 Ao aprovar um workflow no Fluig para geração de um pedido extra , quando ocorrer algum erro na integração e o parâmetro "utilizar fluxo de aprovação para pedido extra" estiver habilitado será disparado automaticamente um e-mail para o responsável cadastrado reportando o erro ocorrido.(Não foi integrado com o BackOffice, com as informações detalhadas).  
 Casa não tenha nenhum responsável cadastrado para ser reportado o erro , será enviado um e-mail para o responsável que gerou o pedido de material extra informando o problema ocorrido.  
 E por fim caso nenhuma das ações acima sejam atendidas será enviado um e-mail reportando o erro detalhado ao usuário do processo.
