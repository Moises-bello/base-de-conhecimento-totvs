---
content_hash: 68feaef18408cdc9ad4330b8efa9eefbdcb9a61db15bc3ad9b1458f58e6a246f
fetched_at: '2026-06-29T00:12:01.330296+00:00'
page_id: '893424097'
product: rm
source: tdn-rm
title: Informações úteis (Contech)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=893424097
version: 42
---

## **01. CODE REVIEW**

Quando o analista finaliza a codificação de uma tarefa deve ser realizado o Code Review, que se trata de uma análise do código por outro membro da equipe, caso haja alguma melhoria ou correção a ser efetuada no código deve ser efetuado antes de avançar a tarefa para a etapa de teste. Ao se realizar o code review de uma tarefa é importante seguir o CheckList do link abaixo:

criar documento

## **02. CASO DE TESTE**

Ao realizar uma codificação é aconselhável adicionar um comentário na tarefa correspondente, com as orientações de como deve ser realizado o teste.

É importante que esse caso de teste contenha:

* O problema
* A solução efetuada
* As pré-condições (o que deve ser parametrizado no sistema antes de efetuar o teste) e o passo a passo de execução
* Sempre que possível detalhar o máximo o caso incluindo até mesmo orientações de onde cada menu encontra-se no sistema, facilitando assim a execução do teste
* Orientar se será necessário testar em mais versões. Atualmente o teste é realizado apenas na atual e na versão do cliente, porém se o código de outra versão estiver muito diferente deve ser testado nesta versão também
* Orientar se deve efetuar o teste em Oracle
* Orientar se é necessário testar com e sem token

Estas orientações também podem ser repassadas/complementadas para o Tester através do chat, ligação, entre outros.

## **03. TDN**

 O TDN é uma rede de documentação da TOTVS. O que for criado no TDN deve ser revisado por um membro da equipe antes de efetuar a publicação.

RM Gestão Contábil -  [TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=189305605)  |  [TDN - Gestão Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=198948832)

RM Gestão Patrimonial -  [TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=189305605)  |  [TDN - Gestão Patrimonial](https://tdn.totvs.com/pages/viewpage.action?pageId=198948882)

APP - [TDN - Meu Patrimônio](https://tdn.totvs.com/pages/releaseview.action?pageId=848820962)

## **04. INTEGRAÇÃO CONTÍNUA**

É possível verificar o status de build das versões através do link abaixo:

[Integração contínua](http://engenhariabh/ic/versions/latest)

## **05. CHECKIN BACK-END**

Sempre realizar Checkin na versão atual, somente após os testes realizar o Checkin nas versões de mercado. Deve abrir uma sub-tarefa de codificação na issue para realizar os merges nas versões de mercado.

Para o front realizar o Checkin da atual apenas no Azure na development e nas versões de mercado utilizar as branch de cada release.

As versões de mercado incluem as 3 versões anteriores a versão atual (para realizar Checkin em versões que já estejam expiradas é necessário alinhar com PO).

Checkins realizados até 8h do dia da expedição já saem na versão (esse horário pode variar de acordo com solicitações dos times). O patch é expedido ao 12h caso não haja nenhum atraso.

## **06. CHECKIN FRONT-END**

Para checkins no front-end há algumas regras de boas práticas de programação que devem ser observadas. Segue link:  
[Guia de boas práticas](https://dev.azure.com/totvstfs/AppMeuRH/_git/Portais?path=%2FPortalMeuRH%2FSTYLEGUIDE.MD&_a=preview)

Orientações para o checkin

* Criar o PR como de costume na branch development;
* Realizar merge da branch development para a branch main;
* Criar um PR na branch main com os mesmos ajustes do PR do criado na branch development;
* Apenas quando os PRs criados executarem com sucesso, avançar a issue pra code review;
* Durante o code review ambos os PRs devem ser aprovados, o PR da branch main irá completar e sairá no restore;
* A pessoa responsável pela execução dos testes irá executar o restore e efetuar os testes a partir dele;
* Após a finalização dos testes um QA deve aprovar o PR da development para que ele complete (caso seja um dev o responsável pelo teste, deve solicitar a um QA a aprovação);
* Caso tenha algum defeito:

+ Realizar a criação de um PR na branch main com o ajuste, utilizando a sub-tarefa de defeito;
+ Replicar a correção do defeito para o PR da development que está em aberto. Este item precisa ser realizado com cautela para garantir que nada ficará fora do ajuste;
+ Durante o code review do defeito realizar a aprovação do PR da main, para que ele seja completado e esteja no restore para a realização dos testes.

Observações: As validações do sonnar, executam diariamente no build full que acontece todos os dias às 21:00h, desta forma, sempre verificar no dia seguinte das alterações, se algo foi quebrado no sonnar e já realizar o ajuste.

## **07. MERGE**

Manutenção: Conforme acordado com o time em reunião de retrospectiva, fica acordado que o merge de correção das issues de manutenção ocorrerá para todas as versões de mercado. Quando a correção for extremamente complexa, em último dos casos, verificar antes com o PO.  
Story (Inovação): Conforme acordado com o PO.

## **08. MERGE FRONT-END**

Com a migração das soluções do TFS para o Azure, a partir de agora o processo de merge para as versões de mercado deverá ser realizado, conforme documentação abaixo:  
[Processo de Merge - Frontend Legado](https://tdn.totvs.com/display/NPR/Processo+de+Merge+-+Frontend+Legado)

## **09. TESTES**

Sempre realizar teste na versão atual e na versão do cliente, exceto se o desenvolvedor orientar que o teste deve ser realizado em alguma outra versão.

Para a realização dos testes na versão do cliente, quando alterado o frontend é orientado como boa prática, sempre retestá-la pelo restore e jamais por dist. Isso porque nesses testes é possível pegar problemas na liberação da correção para o cliente.

Issues com status ‘Teste de aceitação concluído’ até as 12:00 do dia da expedição tem a notificação do cliente realizada de forma automática, desde que a release para notificação esteja preenchida.

## **10. AUTOMAÇÃO DE TESTES**

É importante sempre que possível realizar automações nas Issues de inovações. Seguem alguns documentos importantes para orientar na execução  destes testes:

[Teste Flow](http://bh-testflow/testflow/projectStatus)

## **11. GATED CHECK-IN**

Ao se realizar um check-in é realizado uma verificação para prevenir a quebra de build, caso seja localizado algum problema este é interrompido. É possível verificar o status dos check-ins no link abaixo: É importante também efetuar Get e realizar o build antes de cada Checkin e/ou Merge.

[Gated Checkin](http://tfs2015.totvs.com.br:8080/tfs/CD-BH/RM/_build?_a=queued&definitionId=159)

## **12. PORTAL DA ENGENHARIA**

É possível verificar a data de expedição dos Patchs e Releases:

Engenharia BH: <http://engenhariabh/DashboardExpedicao> ou <http://bh-eng-websrv.sp01.local/DashboardExpedicao> (Conectado a VPN)  
Para mais dúvidas consultar [FAQ: Expedição de Patches](https://tdn.totvs.com/pages/releaseview.action?pageId=187534511)

Observações:

* A antepenúltima release de mercado é expedida somente as sextas;
* As outras releases de mercado são expedidos toda quarta e sexta;
* Patchs expirados ou que precisem ser expedidos com urgência devem ser solicitados através de uma versão emergencial;
* Checkins realizados até 8h do dia da expedição já saem na versão (esse horário pode variar de acordo com solicitações dos times);
* Issues com status ‘Teste de aceitação concluído’ até as 12:00 do dia da expedição tem a notificação do cliente realizada de forma automática, desde que a release para notificação esteja preenchida.

## **13. SONNARQUBE**

É uma ferramenta que demonstra algumas melhorias que devem ser efetuadas no código com base em regras pré-definidas pelas equipes. No link abaixo é possível verificar quais são estes itens:

Geral **-**[Sonar](http://bh-eng-sonar.sp01.local:9900/about)

## **14. SOLICITAÇÃO DE SCRIPT**

É efetuada a solicitação de script através da ferramenta 'AutoScript', onde a solicitação é encaminhada para a aprovação da equipe de banco de dados. Segue link abaixo:

Auto Script: <http://engenhariabh/AutoScript>

## **15. Feedz e Tolecas**

É utilizado para reconhecer atitudes positivas dos participantes. Ao final de cada dois meses é realizada uma reunião para realizar a leitura de alguns destes reconhecimentos.

Performance e Metas: [Feedz](https://app.feedz.com.br/inicio)

Reconhece: [Reconhece](https://engenhariabh.totvs.com.br/TOTVSReconhece/#/TOTVSReconhece/)

## **16. MANUTENÇÕES INTERNAS**

Para defeitos internos encontrados deve ser alinhado PO para realizar a abertura de defeitos internos.

## **17. DOWNLOADS E ATUALIZAÇÕES**

Portal do cliente, onde são realizados os downloads das versões pelos clientes.

[Portal do Cliente](https://suporte.totvs.com/portal/p/10098/download#000023/12.1/CORPORE%20RM/)

## **18. SERVIDORES**

* \\bhengfiles\Publicado: Os Patchs ficam disponíveis neste diretório.
* \\bhengfiles\VersoesHomologacao: As bases de dados exemplo e vazias ficam neste diretório.
* \\bhengfiles\rmflex$\Outros\Ferramentas: Algumas ferramentas como o Restore e RM-Específica ficam disponíveis neste diretório.
* \\Bh-autbdback\basesautomacao Bases Automação

## **19. DRIVE COMPARTILHADO**

Drive compartilhado da equipe: [Drive Contech](https://drive.google.com/drive/folders/0AFjGpxhEeOU0Uk9PVA)

## **20. VPN**

Configuração da VPN: [Configuração VPN](https://drive.google.com/drive/folders/1AxygoTknIwJhaQlRbFibKRpqXr9i_CUo)

## **21. RESTORE**

Utilizado para montar os ambientes do RM.

Documentação: <https://tdn.totvs.com/pages/releaseview.action?pageId=607585039>

Restore: <https://totvsrestore.z15.web.core.windows.net/#/user-environments>. 

## **22. JIRA**

**Jira:**Utilizado movimentar as issue, algumas definições importantes:

* Sempre que assumir uma issue preencher os campos;
* Release para notificação: Sempre com a versão do cliente e sempre antes do Checkin (para notificar corretamente o cliente);
* Fix Version/S: Preencher com a versão atual;
* Se a issue for critica deverá preencher a 'Causa ocorrência ' que gerou o problema;
* Para issues do tipo 'Defeito' necessário especificar o erro e também o que foi a correção.

## **23. INTEGRAÇÕES**

## **24. DEBUG TCLOUD**

Verificar o TDN com as [Orientações para debug](https://atendimento.totvs.com/hc/pt-br/articles/4413668257559);

Verificar se possui acesso ao [TCLOUD](https://tcloud.totvs.com.br/login), caso não possua acionar o PL para solicitar acesso;

Para debug remoto siga os passos abaixo:

Acesse informações do ambiênte:

Escolha o endereço conforme versão do Visual studio.  
  
  
Após isso vá em credenciais Debug Remoto  
  
  
Copie as informações:

Com as informações em mãos, faça o attach no Visual Studio com as seguintes configurações:

## **25. DEBUG DNSPY**

Seguir as [Orientações DnSpy](https://tdn.totvs.com/pages/viewpage.action?pageId=606663183)

LogMeIn

## **26. PLANILHA DE AUSÊNCIAS**

As ausências relacionadas a férias devem ser inseridas na planilha abaixo para controle além de inseridas na agenda do time.

[Planilha de Ausências](https://docs.google.com/spreadsheets/d/1-BMVnlUtq9ORfiKok_Tjorc_rdiUFSLt/edit?rtpof=true&sd=true&gid=1245649301#gid=1245649301)

## **27. ACESSOS**

* JIRA
* TFS
* Azure
* Universidade TOTVS
* RM Específica (Solicitado pelo colaborador via e-mail)

           Instruções: *Enviar e-mail para:**[gcad.bh.expedicao@totvs.com.br](mailto:gcad.bh.expedicao@totvs.com.br)**solicitando o cadastro no RM específica  
           Assunto: Acesso ao RM Especifica  
          Texto deve conter:  
          CPF:  
          Nome completo:  
         Módulos que atua: RM Labore, Chronus, Vitae e SMT  
         E-mail:*

* VPN
* TDN (Solicitado pelo colaborador ou gestor pelo link abaixo)  
  <https://atendimento-totvs.atlassian.net/servicedesk/customer/portal/7/group/219>
* Alura
* Apicurio (Solicitar ao AM)
* Drive compartilhado
* Chat/Discord
* Planilhas de automação
* Planilha de ausências
* Para realizar desenvolvimento mobile: [Orientações para Desenvolvimento Mobile](https://tdn.totvs.com/pages/viewpage.action?pageId=751506621)

## **28. FERRAMENTAS**

* Visual Studio: [Visual Studio](https://visualstudio.microsoft.com/pt-br/thank-you-downloading-visual-studio/?sku=Professional&rel=16)
* Build Tools for Visual Studio (Necessário a instalação caso os testes unitários de backend não sejam executados e não seja exibido erro na execução): [Build Tools For Visual Studio](https://my.visualstudio.com/Downloads?q=build%20tools%20for%20visual%20studio);
* Restore: \\bhengfiles\rmflex$\Outros\Ferramentas\RM Restore (Novo)
* RM-Especifica: \\bhengfiles\rmflex$\Outros\Ferramentas\RM Especifica
* Banco de dados: [SQL](https://docs.microsoft.com/pt-br/sql/ssms/download-sql-server-management-studio-ssms?redirectedfrom=MSDN&view=sql-server-ver15)
* Visual Studio Code (Sugestão): [Visual Studio Code](https://code.visualstudio.com/)
* Git Hub Desktop (Sugestão): [Git Hub](https://desktop.github.com/)
* Check In Policies e Eng.Pack: [Checkin Policies](https://tdn.totvs.com/display/public/EN/Check+In+Policies) e [Eng.VSPack](https://tdn.totvs.com/display/public/EN/Extension+RM.Eng.VSPack)

## **29. CAPACITAÇÕES**

* [LIB](https://universidadetotvs.com.br/skin/atena/training/trail/2005)
* Repositório Contábil com vídeos de treinamentos: [Guilda Técnica - Contech](https://drive.google.com/drive/folders/1DvzZ3AJNoh2uat5IEbMuvRNWFHZTxT2E)
* [Jira](https://universidadetotvs.com.br/skin/atena/training/trail/565)

## **30. BASES ORACLE**

Caminho das bases Oracle que utilizamos:

Caminho para verificar as bases: <http://bh-eng-websrv.sp01.local/DashboardAmbientes/database>

Observações:

* Ao utilizar a base crie um usuário novo, não utilize o usuário mestre para testes que envolvam permissionamento.
* Manter os registros atualizados sempre que possível (período de ponto, competência, entre outros);
* Ao converter a base de dados ou realizar alguma alteração de estrutura sempre verificar com o time se alguém está utilizando a base.

## **31. TESTE UNITARIOS BACK-END**

Execução de Testes Unitários de Backend no Visual Studio

Caso tenha sido instalado o Visual Studio corretamente e o componente de Ferramentas de Build (Build Tools for Visual Studio), citado no tópico de Ferramentas para instalar, porém os testes ainda não tenham sido executados e os testes sejam nas soluções Fop-Folha (Folha e Folha.WebForms), remover os arquivos abaixo localmente:

## **32. Desenvolvimento APP Meu Patrimônio**

[Google Play Console](https://play.google.com/console/u/0/developers/7961332248836275081/app-list): Gerenciar Versões de teste e produção  
[Código do APP](https://totvstfs.visualstudio.com/Backoffice-RM/_git/app-meu-patrimonio)  
[PipeLine App](https://totvstfs.visualstudio.com/Backoffice-RM/_build): Nesse pipeline o app é enviado diretamente para a loja do google no modo teste interno.

Servidor de teste: <http://138.219.88.124:8051>

Acompanhamento do app:

[Gerador de Código de barras:](https://www.invertexto.com/codigo-barras) Nesse site podemos gerar Códigos de barras em todos os formatos aceitos pelo APP.

[FireBase Console:](https://console.firebase.google.com/project/app-meu-patrimonio/overview) Verificar erros e logs de alertas gerados pelo APP

Para Execução de Teste

Atenção! a versão atual do SDK é a 35 com net9.0.  
  
Para executar o projeto de teste, precisa ser adicionado o seguinte código no projeto **PatMobile**:

Porem este recurso impacta no momento de gerar o build, neste caso, e preciso dar **Unload** no projeto de teste:

Em seguida alterar o projeto principal para:

Para executar os testes, altere o TargetFrameworks para net9.0 nova versão.

## **33. Logs Customizados por cor**

/// Gera o log com o ícone responsável por representar erro de execução
///
/// Nome do log
/// Código da coligada
/// Informa se o processo está parametrizado para trabalhar com fracionamento
/// Nome do log
private string GerarLogErro(string nomeLog, int codColigada, bool isSliced)
{
this.ServerLog.Close(nomeLog);
string conteudoLog = this.ServerLog.GetLog(nomeLog);
this.ServerLog.Delete(nomeLog);
nomeLog = GetNomeLog(codColigada, isSliced, RMSJobStatus.Error);
this.ServerLog.Open(nomeLog);
this.ServerLog.Write(nomeLog, conteudoLog);
return nomeLog;
}
private void SetStatusExecucaoProcesso(List listaColigadasExecutadasComSucesso, List listaColigadasExecutadasComErro)
{
if (listaColigadasExecutadasComSucesso.Any() && listaColigadasExecutadasComErro.Any())
this.Status = RMSProcessStatus.Warning;
else if (listaColigadasExecutadasComErro.Any())
this.Status = RMSProcessStatus.Error;
}]]>

## **34. Remoção do Botão "Executar novamente" de Processos**

Diferente dos demais botões do RMSFormParamsProc, o executar novamente é criado em Run Time, não sendo possível acessá-lo diretamente.

É necessário usar uma sobrescrita para isso, sendo ela a seguinte:

## **35. Integração EAI - Compartilhamento não funcionando**

Passo 1: Verificar se o retorno na mensagem está como CCC. <https://tdn.totvs.com.br/pages/releaseview.action?pageId=463820885>  
Passo 2: No cadastro de coligada do RM deve ser configurado o campo Código Externo com o mesmo código do Grupo de Empresa do Protheus.

Veja imagem

## **36.** **Realizar Expedição Manual para clientes**

Passo 1: Verificar se o changset foi expedido em: <http://engenhariabh/DashboardExpedicao/Patch/ChangesetPatch>  
Passo 2: Verificar o link de download da versão em: <http://engenhariabh/DashboardExpedicao/Publicador/PublicadorHistorico>

Passo 3: Clicar em Expedir na issue e colocar o texto padrão abaixo, alterando o link de download.  
  
Texto Padrão:  
  
Olá Cliente,  
A Release Oficial foi expedida e publicada na Central de Downloads.  
O pacote pode ser acessado no endereço: <https://suporte.totvs.com/portal/p/10098/download?e=1195666>  
Não esqueça de responder a nossa Pesquisa de Satisfação para melhor atendê-lo.  
Atenciosamente,  
Equipe TOTVS.

## **37.** **Retirar aba de "Bem Vindo" dos formulários de processo.**

Dentro do construtor do formulário, após o InicializeComponent deve ser colocado o código abaixo:  
 if (!this.DesignMode) this.tbcWizard.Controls.Remove(this.tabStep0);

## **38.** **Corrigir problema de FORM perdendo a formatação da lib.**

**Para os componentes visuais, as DLLs de .design encontram-se em:**

* $/RM/Terceiros/DevX/21.1/21.1.5/Bin.Design...
* obs: Sempre copie a versão mais atual da Bin.Design

**E devem ser copiadas para:**

* C:\Program Files (x86)\Microsoft Visual Studio\<Versao>\<**Professional** ou **Enterprise**>\Common7\IDE;

**Depois disso, mude a resolução da tela para 100%.**

Se mesmo assim após qualquer modificação no form, a formatação for perdida, volte o código para a versão original (formatação correta) e antes de modificar qualquer coisa no formulário, faça a configuração abaixo:

Selecione toda a barra que contem os botões e bloqueie os controles.Se

## **39.** **ToolBox: Como adicionar a biblioteca de componentes winForms da lib**

Existem duas formas:  
1) Em modo administrador do VS, crie uma nova tab dentro da toolbox e carregue a dll RM.Lib.WinForms conforme indicado na imagem abaixo.2) Não é necessário abrir o vs como admin, basta arrastar a dll para dentro da tab nova criada (em alguns casos não funciona, use a opção 1).  
  
Depois de vinculado a dll da lib, todos os componentes serão disponibilizados. Assim, é mais simples criar ou alterar uma tela, sem a necessidade de copiar um componente já existente de outro form.

## **40.** **Acessar informações do ZENDESK**

Nós do desenvolvimento não possuímos acesso ao ZENDESK, para verificar Tickets e status. Porém, por esse link, é possível realizar a verificação: <https://suporte.totvs.com/portal/p/10098/consulta-tickets>

## **41.** **Snowden - Verificação de relatórios para bases Cloud**

Acesso: <https://snowden.smart-view.totvs.app/login>  
  
Usuário: snowden  
Senha: snowden2023  
  
Sugestões:

## **42.** **Responsabilidades do responsável Triagem**

1º - Verificar Manutenções Entrantes:

* Colocar no rótulo da manutenção a tag "analisada", para que o grupo de alertas pare de enviar notificação sobre essa nova entrada;
* Edite a manutenção e preencha o story point com valor 1 e coloque o epico vinculado (normalmente é "Manutenções 12.1.xxxx" da release atual)
* Ainda na edição da manutenção preencha os campos obrigatórios possíveis para que não fique com a indicação na cor roxa no board:  
  Versões Afetadas / Versões Corrigidas / Release para Notificação / Causa Raiz (este é preenchido pelo desenvolvedor)  
    
    
   Registrar a causa raiz no campo **Causa Ocorrência**, segundo a lista:
  + Descuido - Inovação
  + Descuido - Legado
  + Análise de impacto incompleta
  + Falta de conhecimento na linguagem (app)
  + Legado de outras equipes (EAI)
  + Falta de conhecimento na regra de negócio
  + Falta de testes automatizados
  + Causa raiz não identificada devido à falta de informações
  + Inconsistência na Base de Dados
  + Gap de Legislação.
  + Implementação
  + Efeito Colateral de Sonar\Code Smell
* **TAG'S Manutenção**

  **(Usaremos apenas em casos de muito volume de manutenção para agilizar o entendimento e priorizar corretamente)**

  **-**CLOUD  
  -VPN  
  -SLA VENCIDO  
  -SEM URGÊNCIA  
  -URGENTE  
  -SEM SOLUCAO CONTORNO  
  -POSSUI SOLUCAO CONTORNO  
  -SEM AMBIENTE SIMULACAO
* Analisar prioridade da manutenção. As seguintes manutenções devem ser priorizadas:
  + Manutenções Prime Faixa 3
  + Manutenções com associadas. Impacto crescente em outros clientes.
  + Manutenção em módulos de muito uso, sendo possível impacto de alteração recente.
* Analisar se a manutenção possui os requisitos mínimos para ser atendida.
  + Verificar DOR de manutenção.
* Analisar se o problema encontrado possui solução de contorno e aponta-lo ao cliente.

2º - Verificar automações:

* Necessário avaliar se as automações no teste flow estão sendo executadas corretamente pela CT.

3º - Verificar quebras no Sonar:

* New Bugs ou Code Smells devem ser avaliados e reportados a equipe, além da diminuição das métricas de TU.

4º - Verificar tempo de expiração de manutenções com base em cloud no link <https://lookerstudio.google.com/s/o-ktEgDp9CA>

* Avaliar se algum prazo está vencendo e pedir renovação.
* Colocar na agenda do time, caso não exista, a data de expiração da base, sempre considerando um lembrete de pelo menos 2 dias antes do vencimento

obs: Os apontamentos de tempo utilizados nessas ações podem ser feitos por aqui: JIRA0c783de1-186e-383b-975c-a1acd7d76cb5CONTROLADORIA01-4541

## **43.** **Métodos utilitários para Oracle - Quebra em listas menores**

Classe CtbUtils - RM.Ctb.Utils.Intf

## **44.** **Configurações de host da migraçã para WCF**

Em casos de erro de referencia de dll em TU inserir as tag citadas  no arquivo .csproj do projeto de teste. 

## **45.** **Prompts Gemini**

O Gemini é integrado ao TDN, permitindo a realização de prompts sobre o RM. É através das GEMS que se torna possível criar prompts específicos para cada assunto. Para isso, utilize o link abaixo:

<https://script.google.com/a/macros/totvs.com.br/s/AKfycbyeHhiHURmCo7JuSIaSoLF2IRjQNtm5YG1u5vzRvdjPxjkBAw3kn8PlfK0UVMY0ogRk/exec>

c#Prompt Teste Integrado \*\*🔍 Fonte da Verdade:\*\*
> \* \*\*Documento/Tópico:\*\* [Título ou resumo da demanda base]
> \* \*\*Link:\*\* [Links fornecidos na issue, se houver]
---
\*\*DADOS DA DEMANDA A SER ANALISADA:\*\*
[Tipo da ISSUE]
[TItulo da issue /Key da issue
/
Descrição da issue
]]]>

## **46. Publicação de objetos gerenciais - TOTVS Compartilhamento**

1)Exportar o objeto gerencial (layout, conceito, relatórios e etc) :

2) Atualização e inclusão no azure:

Dica extra: Caso tenha que alterar algo na dll no layout para o Gerenciador de Saídas (como por exemplo, mudar a nomeclatura ou namespace de alguma classe), é necessário referenciar a dll novamente editando o layout, assim será feita a atualização com a dll modificada:
