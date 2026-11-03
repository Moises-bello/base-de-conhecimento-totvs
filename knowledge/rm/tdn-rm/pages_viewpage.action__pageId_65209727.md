---
content_hash: 38d51fb5b20ef9aa75db8b79033bcbd9a217d6620e05e61b0f220ce4ebaacfc9
fetched_at: '2026-06-29T00:11:12.316170+00:00'
page_id: '65209727'
product: rm
source: tdn-rm
title: Instalação 3 Camadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=65209727
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                   **Versão:** 11.20 e superiores |
| **Processo** | **:** | Como realizar a instalação **3 camadas** |
| **Subprocesso** | **:** | Instalação 3 Camadas |
| **Data da publicação** | **:** | 08/07/2013 |

   
**Introdução**   
O objetivo deste documento é auxiliar os usuários da linha RM como configurar um ambiente em 3 camadas na versão 11.20 demonstrando seu funcionamento e suas vantagens.   
A arquitetura foi modificada estruturalmente para trazer benefícios e melhorar o processamento das tarefas e processos possibilitando ao usuário o agendamento de processos como relat órios, cubos entre outras vantagens.   
**Configuração** **Ambiente** **3** **Camadas**   
Nas versões anteriores era necessário a intervenção do usuário para configuração do ambiente 3 camadas. Já na versão 11.20 basta selecionar o tipo de instalação desejada durante a instalação da Biblioteca para que os arquivos sejam copiados e gerados os arquivos de configuração (config).  
A configuração de um ambiente em 3 camadas inicia - se com a instalação da biblioteca.   
Ao executar o instalador será apresentada a tela abaixo.   
  
Selecione a opção **Avançar** para prosseguir com a instalação.   
   
Serão apresentados os termos do contrato, selecione a opção de aceite e em seguida avançar.   
   
O próximo passo é inserir o nome do usuário e a organização. O preenchimento destes campos não é obrigatório.  
   
  
  
Nesta tela é apresentado o diretório em que será realizada a instalação do sistema RM. Caso deseje alterar este caminho acesse a opção alterar.   
  
  
   
Clique em instalar para prosseguir com a configuração.  
   
Nesta tela será configurado o ambiente 3 camadas.  
Selecione a opção **Server** se a instalação estiver sendo realizada no servidor de aplicação e a opção  
**Client** caso a instalação for feita na estação cliente.   
  
  
Ao selecionar Modo Server serão copiados para a pasta de instalação somente os arquivos necessários para o processamento de informações, ou seja, arquivos necessários para a execução do Host. Nesta opção, não será possível executar os sistemas.   
  
  
Ao selecionar o Modo Client serão copiados para a pasta de instalação somente os arquivos necessários para execução dos sistemas. O sistema será configurado para direcionar todo o processamento de dados para o Servidor de 3 Camadas, ou seja, o processamento de dados será realizado na máquina em que a Biblioteca for instalada selecionando a opção Modo Server.  
   
Se a opção marcada for **Client** será exibida a tela acima na qual deverá ser inserido o nome do servidor de aplicação e a porta padrão é a 8050.  
Caso contrário a instalação será finalizada.   
  
  
 *Caso* *ocorra* *um* *erro* *na* *conexão* *com* *o* *servidor de* *aplicação* *será* *exibida* *a* *mensagem abaixo:*   
  
*A* *instalação* *disponibiliza* *a* *opção* ***Salvar*** *que* *deverá* *ser marcada* *apenas se* *houver a* *certeza* *do nome* *do* *servidor e* *comunicação* *com* *o* *mesmo.* *Caso* *a* *conexão* *seja* *realizada* *incorretamente* *o sistema* *não* *irá* *funcionar no* *ambiente* *3* *camadas.*   
   
   
Caso o Servidor onde a biblioteca foi configurada,  já tenha sido instalada e/ou removida será verificada a existência do arquivo de configuração do aplicativo, como RMFluxus.exe.config e RMLabore.exe.config, que ficam localizados dentro da pasta dos aplicativos. Se neste arquivo contiver configurações específicas, como nome do servidor de aplicação, no momento da instalação serão exibidas as mensagens abaixo.   
   
  
  
  
.  
   
E por último será exibida a tela de conclusão da instalação.   
 

|  |  |
| --- | --- |
|  | **Para maiores informações:** Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
