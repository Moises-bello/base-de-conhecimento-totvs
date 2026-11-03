---
article_id: 11571907280663
category: eSocial
content_hash: 9b7e959875c53aded589a9afe9269376ad1c15f36e2d47d467e9e263dc7f29ea
fetched_at: '2026-06-28T22:47:15.444903+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: RH - RM - RHU - Erros de conexão ao acessar o menu de Processos Trabalhistas
  (TAF e Smart)
type: support-article
updated_at: '2025-08-22T20:20:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11571907280663-RH-RM-RHU-Erros-de-conex%C3%A3o-ao-acessar-o-menu-de-Processos-Trabalhistas-TAF-e-Smart
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15864031312919) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao acessar o menu de Processos Trabalhistas, aparece mensagem(s) de erro de conexão, o que fazer?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas -**12.1.34.263**, **12.1.2205.211**, **12.1.2209.155** e superiores.

**Solução**

Para o correto acesso a tela de Processos Trabalhistas deverão informar no Parametrizador da Folha de Pagamento o IP de Servidor ou Nome de uma máquina cuja qual possua o RM instalado. Este servidor será utilizado para acesso a tela em questão. Dessa forma, informe IP de um servidor correspondente a sua instalação de Produção caso seja ambiente oficial ou servidor de homologação caso seja teste.

Para isso, devem acessar o módulo Folha de Pagamento, o menu **Configurações** | **Parametrizador** e selecionar o item **eSocial** | **Configurações Gerais**, clique em avançar.  Avance até a etapa **Integração com o TAF** | **Outros Parâmetros.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34382053453591)

As portas informadas deverão estar disponíveis para acesso web. Por padrão quando o RM é instalado as portas utilizadas são a 8051. Contudo, caso utilizem outra porta nos arquivos de configuração do RM, as portas informadas no sistema deverão ser as mesmas dos arquivos .config >>> RM.Host.exe e RM.Host.Service.exe da pasta de instalação do produto (C:\TOTVS\CorporeRM\RM.Net)

1. Acesse no local (em caso de ambiente três camadas, servidor principal) onde está instalado o **RM**, o caminho: C:\totvs\CorporeRM\RM.Net e edite os arquivos **RM.Host.exe.config** e **RM.Host.exe.config** e confira se nas tags **APIPORT** e **HTTPPORT** estão apontadas para a porta **8051** (por padrão, esta é a porta utilizada).  
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11653997894167)  
   Caso esteja apontada alguma outra porta como por exemplo a 8052, validem se a porta é realmente utilizada e se ela esta acessível através do TOTVS TBC. Basta acessar a máquina em que possui o RM instalado localmente e valide se a URL é carregada quando acessada através do link: http://NOMEouIPSERVIDOR:PORTA/wsPageIndex/ em uma navegador instalado nesta mesma máquina.

Para avaliar as configurações de **HttpPort** e **ApiPort** via Host, acesse o link a seguir: **[O que é e como configurar a HttpPort e ApiPort](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-O-que-%C3%A9-e-como-configurar-a-HttpPort-e-ApiPort-?source=search)**

**Caso tenha sido necessário a troca da porta nos aquivos de .config, pare e reinicie o serviço do host do RM. No link abaixo, segue as orientações de como reinicia**r: **[Reiniciar Host.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000095827-Framework-Linha-RM-Frame-Reiniciar-Host)**

Para fazer o envio das informações deve ter a configuração da integração do webservice do RM. Para configurá-lo, acesse o link a seguir: **[Como Habilitar Webservice via RM Host](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003035312)**.

Caso a integração já esteja habilitada, avalie se a tag **DefaultDB** nos arquivos **RM.Host.Service.exe.config** e **RM.Host.exe.config** estão com o nome (Alias) da base de dados em que irá cadastrar as informações do Processo Trabalhista. Exemplo: Nome do Alias = CorporeRM

*Tag: <add key ="DefaultDB" value="CorporeRM" />*

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11572238814487)

**Importante**

Por se tratar de uma parametrização de uso geral (por coligada), sugiro que faça uma instalação do RM em um servidor no qual ficará com o host iniciado e aponte no parâmetro o IP deste servidor.

**Saiba mais:**

Para maiores informações, acesse: 

- [RH - RM - RHU - Como habilitar a funcionalidade de cadastro dos Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11452008640663-TOTVS-RH-Linha-RM-RHU-Como-habilitar-a-funcionalidade-de-cadastro-dos-Processos-Trabalhistas?source=search)

- [RH - RM - RHU - Erros de conexão ao acessar o menu de Processos Trabalhistas - Middleware](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11700201570583)

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
