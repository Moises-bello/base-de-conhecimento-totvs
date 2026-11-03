---
content_hash: ee16af2f4a374cd725ad83711192593cc9cc7e9823bf57999bb38a5b85799254
fetched_at: '2026-06-29T00:11:11.328123+00:00'
page_id: '64652057'
product: rm
source: tdn-rm
title: Arquitetura 3 Camadas - Versão 11.50
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=64652057
version: 9
---

# **Arquitetura 3 Camadas -****Versão 11.50.0**

# 

**Conteúdo**

 

# \_Toc302141797 **Introdução**

O objetivo deste documento é trazer uma visão do que é e como funciona a Arquitetura 3 Camadas .Net, bem como configurar o ambiente em suas estações para correto funcionamento das aplicações neste cenário.

# \_Toc302141798**O que é a Arquitetura 3 camadas?**

Anteriormente, na Arquitetura Cliente-Servidor, a camada cliente acessava diretamente a camada de Banco de Dados, além de todos os processos serem executados no cliente, tais como: abertura de formulários, acesso a dados, regras de validação, cálculos e relatórios.   
 A figura abaixo mostra como é a arquitetura Cliente-Servidor:   
   
   
    
   
   
   
 Na Arquitetura 3 camadas, apesar da complexidade do ambiente a divisão das tarefas em camadas possibilita maior distribuição do processamento do sistema. Na camada cliente temos apenas os formulários que serão abertos na execução do programa.   
 A camada Servidor de Aplicação fica por conta da execução da Regra de Negócio, Cálculos, processos, Relatórios além de fazer a comunicação com a Camada de Banco de Dados.   
   
   
   
   
 As figuras abaixo exemplificam esta Arquitetura:   
   
   
    
   
    
   
 Como mostrado nas figuras, a Camada Servidor de Aplicação pode ser distribuída em processos específicos. Você pode distribuir cada serviço em um servidor de aplicação.   
 **Por** **exemplo:** um servidor de aplicação executa todas as rotinas de cálculos e outro servidor, todas as execuções de relatórios.

# \_Toc302141799**Quais são as vantagens da Arquitetura 3 camadas?**

Confira as vantagens da execução da Linha RM em Arquitetura 3 Camadas:

* Permite maior escalabilidade;
* Permite reaproveitamento de regras de negócio e cálculo;
* Permite utilização mais racional de hardware;
* Permite balanceamento de carga;
* Permite montagem de ambientes com reforço de contingência;
* Diminuição da sobrecarga na camada cliente.

# \_Toc302141800**Como configurar um ambiente 3 camadas na Linha RM?**

A TOTVS distribui um instalador que permite selecionar o tipo da instalação, se local ou ambiente 3 Camadas, extremamente simples configurar.   
 Os arquivos de configuração, tanto do cliente como do Servidor de Aplicação, devem trabalhar na mesma porta TCP para a mesma versão, e portanto devem estar configurados na mesma porta de comunicação.   
 Veja os exemplos desses arquivos de configurações do cliente e do Servidor de Aplicação, respectivamente:

|  |
| --- |
| **RM.exe.config**     <?xml version="1.0"?>   <configuration>   <appSettings>   <add key="CommunicationStyle" value="WCF" />   <add key="JobServer3Camadas" value="true" />   <add key="Port" value="8050"/>   <add key="ActionsPath" value="c:\totvs\CorporeRM;c:\totvs\Corpore.net\bin"/>   </appSettings>   <runtime>   <NetFx40\_LegacySecurityPolicy enabled="true"/>   </runtime>   <startup>   <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/>   </startup>   </configuration> |
| **RM.Host.Service.exe.config**     <?xml version="1.0"?>   <configuration>   <appSettings>   <add key="CommunicationStyle" value="WCF" />   <add key="JobServer3Camadas" value="true" />   <add key="Port" value="8050" />   <add key="Host" value="localhost" />   </appSettings>   <runtime>   <NetFx40\_LegacySecurityPolicy enabled="true"/>   </runtime>   <startup>   <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/>   </startup>   </configuration> |

Para configurar a Arquitetura 3 Camadas da Linha RM, é necessário realizar os seguintes passos:

* Instalar a BibliotecaRM no Servidor de Aplicação (no momento de instalação, selecionar ambiente 3 camadas e Server)

* Instalar a BibliotecaRM em cada Cliente (no momento de instalação, selecionar ambiente 3 camadas e Client. Após isso, informar o servidor (acima) e porta utilizada (padrão 8050))

* Instalar os Produtos da RM em cada Cliente (Os produtos são possíveis instalar apenas em ambiente Client, quando for 3 camadas)

Durante a instalação da BibliotecaRM, você poderá escolher se deseja instalar em ambiente local ou em ambiente 3 camadas.

|  |
| --- |
| **Outras observações importantes**     * Deve-se adicionar a Porta que será usada no ambiente 3 camadas nas Exceções do Firewall utilizado no seu ambiente.      * Na arquitetura 3 camadas, a parte cliente não possui o Host e o arquivo “\_Broker.dat”. Estes itens devem estar apenas no Servidor de Aplicação. Outro detalhe importante é que não se deve apagar o “\_Broker.dat” no Servidor de Aplicação. |

**Para mais informações entre em contato com o Help Desk TOTVS 4003-0015.**

 

**OBS.: Os clientes que estejam utilizando a linha de produto RM a partir da versão 10.76 já podem utilizar o License Server. A nova versão (11.50.0) da linha de produto RM, funcionará apenas com o License Server.**

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
