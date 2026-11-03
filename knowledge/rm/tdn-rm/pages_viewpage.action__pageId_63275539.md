---
content_hash: 4b1e2e7f224b6e1ea01dcc918386549d9929e77db6c5e1e9a32da6cbaca8fbad
fetched_at: '2026-06-29T00:11:06.100745+00:00'
page_id: '63275539'
product: rm
source: tdn-rm
title: Relatório Agendado - Jobserver
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63275539
version: 11
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.50 |
| **Processo** | **:** | Relatório - Execução |
| **Subprocesso** | **:** | Relatório Jobserver no Portal RM |
| **Data da publicação** | **:** | 21/10/2013 |

**Executar um relatório pelo via Jobserver:**

**1º - Será necessário editar o relatório e habilitar a opção de "Executa em Jobserver". Para habilitar o seu relatório em Jobserver você deve acessar sistema (Executável), ir ao menu "Relatórios | Gerador de Relatórios", selecione o relatório que você deseja gerar e clique no terceiro ícone da esquerda para direita "Editar". O sistema irá abrir o formulário abaixo, basta marcar a opção "Executa em JobServer".**

**2º** **-** **Acesse** **o diretório** **"****C:\totvs\CorporeRM\RM.Net****"** **da** **máquina** **onde está** **instalado** **o RM** **Portal** **e edite** **o arquivo** **"****RM.Host.Service.exe.config****" utilizando** **o Bloco** **de** **Notas.** **Neste** **Arquivo,** **será** **necessário** **criar** **(caso ainda** **não** **tenha** **feito)** **a** **seguinte** **tag** **em destaque:**

**<appSettings>**  
 **<add** **key="CommunicationStyle"** **value="WCF"** **/>**  
 **<add** **key="JobServer3Camadas" value="true"** **/>**  
 **<add** **key="Port"** **value="8050"** **/>**  
 **<add** **key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bi****n"** **/>**  
 **</appSettings>**

**3º** **-** **Acesse** **o diretório** **"****C:\totvs\CorporeRM\Corpore.Net****"** **e edite** **o arquivo** **"****Web.Config****"** **utilizando** **o Bloco** **de** **Notas.** **Neste** **Arquivo,** **será necessário** **criar** **(caso** **ainda** **não** **tenha** **feito)** **a** **seguinte** **tag** **em** **destaque:**   
   
 **<!-- Configurações** **de Remoting ->**  
 **<add** **key="RemoteLoad"** **value="false"** **/>**  
 **<add** **key="SelfHosted"** **value="false"** **/>**  
 **<add** **key="ServerHost"** **value="localhost"** **/>**  
 **<add** **key="ServerPort"** **value="8050"** **/>**  
 **<add** **key="JobServer3Camadas" value="true"** **/>**  
 **<add** **key="Protocol"** **value="tcp"** **/>**  
 **<add** **key="ServerUrl"** **value="**[**http://localhost/RM.net/"**](http://localhost/RM.net/) **/>**

**4º** **-** **Volte** **ao** **diretório** **"****C:\totvs\CorporeRM\RM.Net****"** **e** **acesse** **o executável** **"****RM.AliasManager.exe****".** **Neste** **aplicativo,** **na** **"****Aba** **Serviços****", será** **necessário** **habilitar** **a** **opção** **de** **Processamento** **de** **Job** **e** **definir** **um valor** **de** **execuções** **simultâneas.**

**Muito** **cuidado** **ao** **definir** **esse** **valor.** **Se** **for inserido** **um** **valor** **muito auto,** **poderá** **sobrecarregar** **o servidor.**

**Para** **poder** **dividir** **esse** **processamento,** **poderá** **ser** **feita** **a** **mesma configuração** **em** **outras** **máquinas** **porem** **com** **a** **opção** **de** **"****Executar** **apenas Jobs** **Locais****",** **desmarcada.** **A** **vantagem** **é que** **essas** **máquinas** **não** **serão** **de uso** **exclusivo** **para** **execução** **de** **processos** **e** **o usuário** **poderá** **trabalhar normalmente.**

**5º** **-** **Ainda** **no** **diretório** **"****C:\totvs\CorporeRM\RM.Net****",** **execute** **o** **aplicativo** **"****RM.Host.ServiceManager.exe****"** **e siga** **os** **seguintes** **passos:**

**a)** **Clicar** **no** **botão** **Desinstalar**  
 **b)** **Apagar** **o arquivo** **\_Broker.dat** **da** **pasta** **RM.Net**  
 **c)** **Clicar** **em** **instalar** **e esperar** **que** **o serviço** **esteja** **iniciado.**

**Agendando um relatório**

**1 – Selecione o Relatório deseja e edite o mesmo:**

**2 – Marque a opção Executa em JobServer e Salve a Alteração**

**3 – Selecione opção em vermelho: Agendar a execução do relatório.**

**4 - Será exibida a seguinte tela Escola um nome para o Processo e Clique Avançar:**

**6 – Caso o Relatório tenha filtros configure e clique em Avançar de novo.**

**7 - Marcar a opção Enviar o relatório gerado por E-Mail e digitar o email desejado.**

**8 - Digite o assunto que será recebido no email.**

**9 - Definir as configurações de envio desejadas, neste caso, por exemplo, irá se repetir todos os dias, menos sexta, sábado e domingo.**

**10 – Finalize o Processo.**

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
