---
article_id: 23472097356439
category: TAF - eSocial - Configuração
content_hash: bf05e85a34b9b2fb2c68ab3290656e1a131562ada5f916d6f5dee59568e9cbf9
fetched_at: '2026-06-28T22:45:14.331451+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como configurar o TAF
  para transmitir eventos automaticamente (Schedule) para o eSocial
type: support-article
updated_at: '2026-06-16T12:45:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23472097356439-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-configurar-o-TAF-para-transmitir-eventos-automaticamente-Schedule-para-o-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23472097289879) Tempo aproximado para leitura: **HH:30:00 min**

**Dúvida**  
Como configurar o TAF para realizar transmissões automáticas para o e-Socia (Schedule)l?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configurações - Schedule - Todas as versões

**Pré-requisito:**

1. Para o Schedule realizar a transmissão automática, é necessário que serviço do TSS esteja ativo.

2. Validar o parâmetro **MV\_TAFSTRS,** deixar o mesmo com conteúdo: **" ", "0","1**"

3. Para ser apresentada a nova janela Schedule (demonstrada neste documento), é necessário atualizar a LIB.

Para atualizar a LIB siga a documentação abaixo, que já contempla os links para download:

[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239)

**Solução**

1 - Acesse o **Configurador (SIGACFG),** em seguida, as opções do menu **Ambiente > Schedule > Schedule:**

![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23472035249815)

***2 - Configurando o "Agente"***

No menu lateral, selecione a opção ***"Agentes"**,*em seguida, selecione ***"Novo":***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23633598428311)              ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23633646932503)              ![](https://centraldeatendimento.totvs.com/hc/article_attachments/23633646941335)

*2.1 Preencha os campos e salve.*

**Descrição:** Insira um nome para o Schedule

**Status:** Defina se o Schedule deve ficar habilitado ou desabilitado (essa opção pode ser alterada posteriormente)

**IP:** O cliente pode optar por colocar:

Localhost

IP local sem rede, exemplo: 127.0.0.1

IP do servidor, onde está localizado o appserver.ini do Protheus;

***\*\***Recomendamos deixar o IP local sem rede, 127.0.0.1, pois, se houver manutenção no IP de rede, o Schedule não perderá as configurações.*

**Porta:** Utilize a porta TCP do appserver.ini do Protheus.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23634239829399)

**Número de Threads:** Definida pelo administrador (usuário) conforme disponibilidade.

**Ambiente:** Será preenchido automaticamente, no ambiente que está logado.

**Empresa:** Selecione as empresas que utilizaram o Schedule.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23668894336663)

2.2. Após salvar, observe que será apresentado um registro em **"Agentes"**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23639738591255)**

3 - ***Configurando os "Agendamentos"***

***IMFORMAÇÕES IMPORTANTES:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23663568240279) Clientes segregados, que utilizam **RM, Datasul,** para integração com o TAF**,** é necessário configurar os processos **TAFSCHED2,** **TAFSCHED4 e TAFSCHED5**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23663568240279) Clientes que utilizam somente módulos do **Protheus** , é necessário configurar somente os processos **TAFSCHED4 e TAFSCHED5**

3.1 - No menu lateral, selecione a opção ***"Agendamentos"**,*em seguida, selecione ***"Novo":***

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/23639768947223)![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23633646932503)![](https://centraldeatendimento.totvs.com/hc/article_attachments/23641846184087)***

3.2. Configurando o **TAFSCHED2 - Processamento ERP x TAF**

**Este processo é responsável pelo processamento de eventos integrados de ERP terceiros com o TAF.**

Após selecionar "Novo", será apresentada a tela abaixo, insira o nome do nome do processo: **TAFSCHED2**e selecione **"Avançar"**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23641875386647)

Defina a data e horário da primeira execução do processo, assim como a periodicidade, após preencher, selecione **"Avançar":**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23641875395607)**

 

Na próxima tela configure as filiais/ empresas onde o processo (Schedule) deve ser executado:

**Importante:** No campo **"Módulo"** escolha s opção **84 - TOTVS Automação Fiscal**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23641875402903)

Após preencher os campos, selecione **"Avançar",**a tela abaixo será apresentada, com o resumo da configuração do processo, selecione **"Concluir"**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23641846238999)

Após concluir, será listado, apresentado o registro **TAFSCHED2 ,** dentro de **"Agendamentos":**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23641875439127)**

3.3 Configurando o ***TAFSCHED4 - Transmissão TAF x TSS***

***Este processo é responsável pela transmissão do TAF com o TSS.***

Selecione menu lateral ***"Agendamentos"**, em seguida* selecione ***"Novo":***

**ATENÇÂO**: É pelo processo **TAFSCHED4**que o **Grupo de Eventos** (**TAFA441)** deve ser inserido.

\*\*Se necessário, crie o **Grupo de Eventos**, antes de configurar o **TAFSCHED4,** a documentação abaixo explica como criar o Grupo de Eventos, o grupo contém os eventos que devem ser transmitidos automaticamente pelo Schedule (não é uma configuração obrigatória, deve ser configurado se o cliente deseja transmitir de forma automática, apenas alguns eventos, caso contrário, será transmitido todos os eventos)

[RH - Linha Protheus - TAF - eSocial - Configuração - TAFA441 - Como criar o Grupo de Eventos no TAF, para transmissão automática eSocial (Schedule)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23670096128791)

Na tela apresentada abaixo, se possuir **Grupo de Eventos** **(TAFA441)** **,** atente-se para configurar correto o nome do processo:

**TAFSCHED4("****número do empresa****", "número do código criado no TAFA441")**

*Exemplo:*

Quando o grupo de eventos foi criado.

Abra a rotina TAFA441 no TAF, e verifique o número do código:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23643032720407)

As informações que estão entre parênteses são: o número do grupo de empresa **"02"** e em seguida o código do grupo criado na rotina TAFA441 **"01"**

Neste exemplo, o nome configurado foi: **TAFSCHED4("02","01")**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23642365887255)

Caso não configure o Grupo de Eventos, preencha com somente **TAFSCHED4:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23642365897495)

Defina a data e horário da primeira execução do processo, assim como a periodicidade, após preencher, selecione **"Avançar":**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23643004010007)**

Na próxima tela configure as filiais/ empresas onde o processo (Schedule) deve ser executado:

**Importante:** No campo **"Módulo"** escolha s opção **84 - TOTVS Automação Fiscal**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23643032734615)

Após preencher os campos, selecione **"Avançar",**a tela abaixo será apresentada, com o resumo da configuração do processo, selecione **"Concluir"**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23643032750103)

Após concluir, será listado, apresentado o registro **TAFSCHED4 ,** dentro de **"Agendamentos":**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23643032761111)

3.4 Configurando o **TAFSCHED5 - Consulta de retorno**

**Este processo é responsável pela Consulta do TAF no TSS.**

Selecione menu lateral ***"Agendamentos"**, em seguida* selecione ***"Novo":***

Após selecionar "Novo", será apresentada a tela abaixo, insira o nome do nome do processo: **TAFSCHED5** e selecione **"Avançar"**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23645608647703)

Defina a data e horário da primeira execução do processo, assim como a periodicidade, após preencher, selecione **"Avançar":**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23645608656919)

Na próxima tela configure as filiais/ empresas onde o processo (Schedule) deve ser executado:

**Importante:** No campo **"Módulo"** escolha s opção **84 - TOTVS Automação Fiscal**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23645608668823)**

Após preencher os campo, selecione **"Avançar",**a tela abaixo será apresentada, com o resumo da configuração, selecione **"Concluir"**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23645581301143)

Após concluir, será listado, apresentado o registro **TAFSCHED5 ,** dentro de **"Agendamentos":**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23645581314455)

**4. Habilitar o Agente e os Agendamentos**

Após configurar os "Agentes" e "Agendamentos", verifique se os mesmo estão habilitados:

**Agente:**

Selecione os "três pontinhos" localizados na frente do Agente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23645581322263)

Agendamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23645608715287)

**5. Validar o funcionamento do Schedule:**

Ative a chave **TafConOut** no appserver.ini do Protheus, no grupo **[environment]**

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23669699144087)

Com o Schedule Habilitado, consulte o arquivo **console.log** do Protheus.

No sumario é informado a quantidade de vezes que a API do schedule chamou as rotinas agendas e qual processo a thread em questão executou.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23669699156247)

Quando um processo encontra um registro elegível para execução a filial, tabela, status os recno são informados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23669699183255)

**Documentações Relacionadas:**

[Configure o Processamento automático dinâmico (Opcional)](https://tdn.totvs.com/pages/releaseview.action?pageId=498457633)

**Outras documentações que podem interessar:**

Dúvidas, entrar em contato com a área responsável pela documentação:

[RH - Linha Protheus - GPE - eSocial - S-2206 - Como gerar eventos de alteração salarial do SIGAGPE para o TAF com Job/Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007038211)

[RH - Linha Protheus - MDT - eSocial - S-2240 - Como utilizar a rotina Schedule (JOB) de Tarefas para envio do S-2240 para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033184593)

[RH - Linha Protheus - GPE - eSocial - S-2206/S-2230 - Como funciona o Job/Schedule na prática referente a integração das Alterações Salariais e Fim de Afastamento com o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035063413)
