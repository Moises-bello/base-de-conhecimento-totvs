---
content_hash: f11c522eaf2c4253c322142ebd5cedd7de236bb495f16259e282ff9302cb0967
fetched_at: '2026-06-29T00:09:32.441035+00:00'
page_id: '425458849'
product: rm
source: tdn-rm
title: Execução de provas e pesquisas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458849
version: 6
---

No TOTVS Avaliação e Pesquisa o usuário tem a possibilidade de responder suas provas/pesquisas de duas formas:

* Executor Web;
* RM Executor.

Para utilizar o **Executor Web** é preciso acessar um link disponibilizado pela instituição do portal Web e informar o número da inscrição do candidato na prova e executar a mesma.  
   
Já o **RM Executor**, que é um aplicativo desktop, ao inicia-lo será solicitado ao candidato o número da inscrição e o tipo de acesso definido para a execução da prova.  
   
No tipo de acesso poderá ser definido como:  
   
**Execução local (offline)** - Neste modo a avaliação será executada de forma desconectada e isolada do TOTVS Avaliação e Pesquisa. A comunicação entre o RM Executor se dará por arquivos gerados através do processo "Gerar prova (off-line)" do TOTVS Avaliação e Pesquisa. Esses arquivos serão requeridos durante a execução da prova. Após a finalização, as respostas dos candidatos serão salvas nesse mesmo arquivo que posteriormente será importado no TOTVS Avaliação e Pesquisa através do processo "Recuperar prova local (off-line)".   
Para executar provas locais, é preciso seguir os seguintes procedimentos:  
1 - Inscrever um candidato em uma prova, através do menu **Cadastros > Provas > Anexos > Candidatos**.  
2 - Gerar a prova local para o candidato através do processo Gerar prova local (offline).  
3 - Acessar o **RM Executor** e informar a inscrição do candidato gerado no **passo 1**.  
4 - Selecionar o tipo de acesso **Local (Offline)** e informar o local onde se encontra o arquivo gerado no **passo 2**.  
5 - Clicar no botão **OK** e executar a prova.  
Para realizar a correção das provas executadas dessa forma, é preciso:  
1 - Acessar a prova executada.  
2 - Recuperar a prova local através do processo Recuperar prova local (off-line).  
3 - Visualizar o desempenho do candidato no ranking.  
**Execução via WebService (online) -** Para este tipo de execução é preciso que seja criado o WebService, para maiores detalhes consulte a página Configurar Webservice.Neste modo é utilizado o WebService para realizar a comunicação do RM Executor com o TOTVS Avaliação e Pesquisa. Assim quando é informado a inscrição e a URL do WebService, a prova é disponibilizada para execução e quando a mesma é concluída, as informações referente ao desempenho do candidato é atualizada no Ranking.   
   
Para executar provas através de um webservice, é preciso realizar os seguintes procedimentos:  
1 - Inscrever um candidato em uma prova, através do menu **Cadastros > Provas > Anexos >** **Candidatos**.  
2 - Acessar o **Executor de Avaliações e Pesquisas** e informar a inscrição do candidato gerado no **passo 1**.  
3 - Selecionar o tipo de acesso **WebService (Online)** e informar o endereço do webservice a ser utilizado.  
4 - Clicar no botão **OK** e executar a prova.  
   
Quando executada as provas de avaliação de conhecimento que possuem questões abertas as mesmas precisam ser corrigidas. Para isto é preciso acessar o Ranking do candidato.  
   
**Atenção** Ao executar uma prova  através do RM Executor que esteja parametrizado para não permitir a mudança de tela, além de outros travamentos, o sistema irá tentar travar também o acesso ao Gerenciador de Tarefas do Windows através do atalho CTRL + ALT + DEL. Por motivos diversos e, principalmente por questões de políticas de segurança e restrições do ambiente, o aplicativo poderá fracassar ao tentar realizar essa alteração. Nesse caso, pode ocorrer de exibir mensagem atrás da prova, sem que o usuário tenha conhecimento da mesma e o impedir de realizar a prova enquanto a mensagem não for fechada. Para que isso não ocorra o acesso ao **Executor de Avaliações e Pesquisas** deverá ser realizado no modo administrador.  
   
**Importante**  
Quando é definido a periodicidade para gravação da prova em parâmetros do sistema, ao responder a prova/pesquisa e alcançar o tempo definido para gravação da prova, as respostas e a qual questão o candidato se encontra são salvas. E assim caso haja uma interrupção da execução da prova será permitido reabrir a prova mesmo que não esteja parametrizado para isto na ultima questão respondida pelo candidato.  
Quando o candidato for executar uma prova multi-idiomas e que não possuir um idioma definido, será exibido um lista para o candidato selecionar o idioma que o mesmo irá responder a prova.

 Como fazer

---
