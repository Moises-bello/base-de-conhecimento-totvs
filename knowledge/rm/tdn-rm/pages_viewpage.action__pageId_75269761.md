---
content_hash: 4cb92698013f595cd7202f4d531d284dc7e66dc81bdd35abc2c98ff921bf372c
fetched_at: '2026-06-29T00:11:33.008170+00:00'
page_id: '75269761'
product: rm
source: tdn-rm
title: Criando uma Fórmula Visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=75269761
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.XX |
| **Processo** | **:** | Fórmula Visual |
| **Subprocesso** | **:** | Configuração de um Workflow para enviar e-mail para cada Usuário Novo cadastrado |
| **Data da publicação** | **:** | 18/09/2013 |

**Avisar** **ao** **usuário** **do** **Corpore** **seu** **login** **e senha** **por** **e-mail** **automaticamente**   
   
 **O** **Cadastro** **de** **Usuários** **é** **utilizado** **constantemente** **dentro** **dos** **sistemas** **da** **TOTVS** **para** **permitir** **que** **os** **colaboradores possam** **executar** **seu** **trabalho.**

**Através deste** **recurso, é** **possível** **enviar** **um** **e-mail** **automaticamente** **para cada** **usuário** **criado dentro** **de** **qualquer** **sistema** **Corpore.**

**A** **vantagem** **é** **que** **o** **usuário** **terá** **conhecimento** **do** **seu** **login** **e** **senha** **para** **acessar** **o** **sistema,** **não** **sendo** **necessário** **um contato** **do** **Administrador** **do** **sistema** **com** **cada** **usuário.**   
   
   
   
   
   
 **Figura** **1** **-** **Tela** **inicial** **do** **sistema** **utilizado** **na simulação**   
   
 **O** **primeiro** **passo** **é** **incluir um** **novo** **Worflow,** **que** **irá** **controlar** **toda** **a rotina. Acesse** **|** **Menu** **Utilitários** **|** **Workflow** **(Beta)** **|** **Workflows** **|** **Botão:** **Incluir** **|**   
   
   
   
   
 **Figura** **2** **-** **Acessando** **o** **recurso** **Workflow**   
   
 **O** **próximo** **passo** **é** **informar** **o** **nome** **do** **WorkFlow,** **sua** **categoria,** **e gravar** **o registro.**

***OBS:*** ***A*** ***Categoria informada irá determinar*** ***qual*** ***Perfil poderá dar*** ***manutenção neste Workflow.***   
   
   
   
 **Figura** **3** **-** **Dados básicos** **da criação** **do** **Workflow**

**Na** **Visão** **de** **Workflows** **clique** **duas** **vezes** **sobre** **o Workflow** **criado.**

***OBS:*** ***Se selecionar*** ***o*** ***Workflow e*** ***clicar*** ***no botão*** ***Editar*** ***o*** ***sistema abrirá*** ***apenas*** ***a janela de edição dos*** ***dados*** ***básicos.***   
   
   
   
   
   
 **Figura** **4** **-** **Edição** **Avançada do** **Workflow**   
   
   
 **Vá** **na** **Aba Atividades,** **selecione** **a Atividade** **'Se/Senão'** **e arraste** **para** **o** **quadro** **'Sequential** **Workflow'.**   
   
   
   
   
   
 **Figura** **5** **-** **Inclusão** **das** **Atividades** **do** **Workflow**

**Figura** **6** **-** **Propriedades** **da** **Atividade Se/Senão**   
   
   
   
 **No** **campo** **'ConditionName'** **clique** **no** **botão** **'...'.**

**Ao** **abrir** **a janela** **de** **Seleção** **de** **Condições** **pressione** **o** **botão** **'New'** **(Novo).**   
   
   
 **Figura** **7** **-** **Criando** **a** **condição** **de** **envio** **de e-mail**   
   
 **No** **campo** **'Condition'** **informe** **a seguinte** **sentença** **e** **confirme** **a inclusão:**   
 *this.Fields["SENHA"].IsModified*

***OBS:*** ***Esta janela de condições possui*** ***uma interação*** ***com funções do*** ***.NET.*** ***Desta forma você poderá informar*** ***uma propriedade e o*** ***.NET lhe fornecerá as opções disponíveis*** ***de argumentos, e*** ***demais*** ***relacionamentos.***  
 ***Use 'Ctrl*** ***+*** ***Espace' para*** ***exibir*** ***opções*** ***de propriedades disponíveis*** ***(semelhante à programação*** ***.NET)***   
   
   
   
 **Figura** **8** **-** **Elaboração** **da sentença** **que** **determinará** **a** **condição** **de envio** **de** **e-mail**   
   
   
 **Na** **Aba** **Atividades** **arraste** **as Atividades** **'Expressão'** **e** **'Envio** **de** **E-mail'** **para** **dentro** **da** **Atividade** **'Se/Senão'.**   
   
   
   
 **Figura** **9** **-** **Criando** **a** **condição** **de** **envio** **de e-mail**   
   
   
   
 **Selecione** **a** **Atividade** **Expressão** **dentro** **do** **quadro** **'Sequential** **Workflow',** **Selecione** **a Aba** **Propriedades,** **clique** **sobre** **o**  
 **botão** **'...'** **no** **campo** **'Expressões',** **e informe** **o texto** **que** **será** **enviado** **ao** **usuário.**   
 **Exemplo:**  
 'Prezado(a) [' + RMSWorkflow.NOME + '],' + Newline + NewLine + 'Seu cadastro como usuário no sistema TOTVS foi finalizado com sucesso!'  
 + Newline + Newline + 'Seu login de acesso é: ' + RMSWorkflow.CODUSUARIO + Newline + 'Sua senha inicial: 123456' + Newline + NewLine +  
 'Agora você está apto a realizar abertura de atendimentos.' + Newline + NewLine + 'Bom Trabalho!'   
 ***OBS:*** ***Esta janela permite que você utilize variáveis do*** ***sistema para*** ***envio*** ***de informações dinâmicas*** ***(conforme*** ***exemplo*** ***acima).***   
   
   
   
    
 **Figura** **10** **-** **Montando** **a** **mensagem** **que será enviada** **ao** **usuário**   
   
 **Após** **definir** **a mensagem** **devemos** **associá-la** **à Atividade** **Envio** **de** **E-mail.**  
 **Para** **tanto,** **nesta** **mesma** **Aba** **Propriedades** **clique** **duas** **vezes** **sobre** **o** **campo** **'Valor** **Calculado',**   
   
   
   
 **Figura 11** **-** **Associando** **a** **mensagem** **criada à** **Atividade** **'Envio** **de** **E-mail'**   
   
   
   
   
 **Selecione** **a Atividade** **Envio** **de** **E-mail** **dentro** **do** **quadro** **'Sequential** **Workflow',** **Selecione** **a Aba** **Propriedades,** **clique** **sobre o** **campo** **'Assunto',** **e informe** **o** **texto** **que** **será** **apresentado** **no** **Assunto** **do** **E-mail.**   
 **Exemplo:**  
 [E-mail automático] Login de acesso ao sistema TOTVS   
 **Informe** **também** **o campo** **'Texto** **do** **Email',** **pois** **o mesmo** **é obrigatório.** **Esta** **informação** **não** **será** **usada** **no** **envio** **do** **e** **- mail.**   
   
   
   
   
 **Figura 12** **-** **Edição** **da** **Atividade Envio** **do** **E-mail**   
   
 **Ainda** **na** **Atividade** **Envio** **de** **E-mail** **clique** **duas** **vezes** **sobre** **o campo** **'Destinatários',** **selecione** **o campo** **'Fields',** **pressione**  
 **F2,** **e dentro** **do** **colchete** **informe** **o texto** **"EMAIL"** **(conforme** **figura** **abaixo).**   
   
   
   
   
 **Figura 13** **-** **Associando** **o campo** **Destinatário ao** **e-mail do** **cadastro** **do Usuário**   
 **Ainda** **na** **Atividade** **Envio** **de** **E-mail** **selecione** **no** **campo** **'Remetente',** **a opção** **'Company',** **indicando** **que** **o** **remetente** **será**  
 **o** **contato** **de** **e-mail** **da** **Coligada** **utilizada.**   
 **Confirme** **a edição** **avançada** **do** **Workflow** **clicando** **em** **OK.**   
   
   
   
   
 **Figura 14** **-** **Indicando** **quem será o** **Remetente** **do** **E-mail** **ao Usuário**   
   
   
 **Na** **visão** **de** **Workflow** **selecione** **o Workflow** **e** **pressione** **o** **botão** **'Editar'.** **Vá** **à** **Aba** **'Gatilhos',** **selecione** **a opção** **'Antes** **da Atualização** **do** **Registro** **(Fim)'** **(este** **gatilho** **permite** **que** **comparemos** **o valor** **de** **um** **campo** **com** **seu** **valor** **anterior** **logo antes** **de** **salvar** **o registro).**   
   
   
   
 **Figura 15** **-** **Indicando** **qual** **será** **o** **disparador** **do** **Workflow**   
   
 **Após** **selecionar** **o gatilho** **'Antes** **da** **Atualização** **do** **Registro** **(Fim)'** **pressione** **o botão** **'Adicionar** **Objeto',** **e localize** **o**  
 **cadastro** **de** **Usuários,** **selecione,** **e confirme** **a alteração** **da** **Edição** **Básica** **do** **Workflow.**   
 **Após** **finalizar** **a configuração** **poderá** **realizar** **um** **teste** **de validação** **acessando** **o cadastro** **de** **usuários** **e alterando** **o campo**  
 **SENHA** **de** **algum** **usuário** **cadastrado,** **ou** **incluindo** **um** **novo** **Usuário** **no** **sistema.**   
   
   
   
 **Figura 16** **-** **Indicando** **qual** **será** **o** **disparador** **do** **Workflow**   
   
   
 *Observações*   
 **Para** **que** **este** **tipo** **de** **serviço** **funcione** **é** **necessário** **que** **o** **arquivo** **"RM.Host.Service.exe.config"**  
 **(C:\CorporeRM\RM.Net\RM.Host.Service.exe.config)** **esteja** **configurado.**  
 **Para** **tanto** **deve** **existir** **a** **linha** **"<add** **key="WorkflowEnabled" value="true"** **/>"** **no** **arquivo.**   
   
   
 <configuration>  
 <appSettings>  
 .  
 .  
 <add key="WorkflowEnabled" value="true" />  
 .  
 .  
 </appSettings>   
   
 **Figura 17** **-** **Alteração** **do** **arquivo** **'RM.Host.Service.exe.config'**

**Importante:**   
 ***O*** ***arquivo*** ***poderá*** ***ser*** ***editado*** ***utilizando*** ***um*** ***editor*** ***de*** ***texto*** ***(Exemplo:*** ***Bloco*** ***de*** ***Notas).***

***Para*** ***realizar*** ***esta*** ***alteração*** ***é*** ***necessário*** ***parar*** ***o serviço*** ***"RM.Host.Service",*** ***e reiniciar*** ***após*** ***o término*** ***do*** ***procedimento.***

Para maiores informações:

Consulte o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.LogAuditoria.aspx) TOTVS.

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)
