---
content_hash: 42b10a62f976afb10a4bb2f8a5b968d9c258d3d0350b962566792068baa0e272
fetched_at: '2026-06-28T21:35:28.931286+00:00'
page_id: '73075448'
product: fluig
source: tdn-fluig
title: Matriz de Portabilidade
type: documentation
url: https://tdn.totvs.com/display/fluig/Matriz+de+Portabilidade
version: 275
---

trueIdioma

---

2.\*ndice

---

Na matriz de portabilidade você encontra os requisitos necessários para a execução do TOTVS Fluig, como por exemplo, sistema operacional e navegadores.

A matriz é atualizada constantemente na tabela abaixo. Os ***status*** correspondem a  **HOMOLOGADO**,  **EM ANÁLISE** e  **NÃO HOMOLOGADO**.  para saber mais.

| TOTVS Fluig | | | | |
| --- | --- | --- | --- | --- |
| Servidor | | | | |
| Categoria | Produto | Versão | *Status* | Observações |
| **SGBD** | SQL Server | 2008 |  | Não homologado a partir da atualização 1.5.10 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-sql-server-2008) para saber mais. |
| 2012 |  | Não homologado a partir da atualização 2.0 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-mysql-sqlserver-oracle) para saber mais. |
| 2014 |  | Não homologado a partir da atualização 2.0 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-mysql-sqlserver-oracle) para saber mais. |
| 2016 |  | Homologado a partir da atualização 1.6.5 da plataforma. |
| 2017 |  | Homologado a partir da atualização 1.6.5 da plataforma. |
| 2019 |  | Homologado a partir da atualização 1.8.0-221004 da plataforma. |
| 2022 |  | Homologado a partir da atualização 2.0 da plataforma. |
| MySQL | 5.5 |  | Não homologado a partir da atualização 1.7 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-mysql-55) para saber mais. |
| 5.6 |  | Não homologado a partir da atualização 2.0 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-mysql-sqlserver-oracle) para saber mais. |
| 5.7 |  | Não homologado a partir da atualização 2.0 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-mysql-sqlserver-oracle) para saber mais. |
| 8.0 (a partir da 8.0.27) |  | Homologado a partir da atualização 1.8.1 da plataforma. |
| Oracle | 10G R2 |  | Não homologado a partir da atualização 1.8 da plataforma. |
| 11G |  | Não homologado a partir da atualização 1.8 da plataforma. |
| 12C |  | Não homologado a partir da atualização 1.5.10 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-mysql-sqlserver-oracle) para saber mais. |
| 18C |  | Não homologado a partir da atualização 1.5.10 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-mysql-sqlserver-oracle) para saber mais. |
| 19C |  | Homologado a partir da atualização 1.8 da plataforma. |
|  | | | | |
| **MIDDLEWARE** | Sistemas operacionais**1** | Windows Server 2012 |  | Não homologado a partir da atualização 2.0 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-windows-server-2012) para saber mais. |
| Windows Server 2012 R2 |  | Não homologado a partir da atualização 2.0 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-windows-server-2012) para saber mais. |
| Windows Server 2016 |  |  |
| Windows Server 2019 |  |  |
| Windows Server 2022 |  | Homologado a partir da atualização 2.0 da plataforma. |
| Windows Server 2025 |  |  |
| Red Hat Enterprise Linux 6.4 a 8.7 |  |  |
| Red Hat Enterprise Linux 9.5 |  | Homologado a partir da atualização 2.0 da plataforma. |
| CentOS 6.4 a 7.5 |  |  |
| Oracle Linux 6.4 a 8.7 |  |  |
| Oracle Linux 9.5 |  | Homologado a partir da atualização 2.0 da plataforma. |
| Ubuntu Server 16.04 a 22.04 |  | **Observação destinada somente para clientes que usam o MySQL no mesmo servidor do Fluig**: para usar o Ubuntu 20.04 ou 22.04, é necessário que o Fluig esteja na atualização 1.8.1 ou superior, pois ao atualizar para essas versões do Ubuntu, o MySQL é atualizado automaticamente para a versão 8, que é homologada apenas a partir da 1.8.1.  Para quem usa outros bancos de dados não há impacto. |
| Ubuntu Server 24.04 |  | Homologado a partir da atualização 2.0 da plataforma. |
| **1** → Os sistemas operacionais descritos em **Servidor** na matriz de portabilidade também estão homologados para o servidor do ESB. | | | | |
|  | | | | |
| **LOAD BALANCER / PROXY REVERSO** | Apache | 2.4.12 |  | Salientando que a melhor performance do Apache é em servidores Linux. Não recomendamos sua utilização em sistemas operacionais Windows, pois pode comprometer o desempenho. |
| Big IP | Firmware versão 10 |  |  |
| Appliance LTM 1300 |  |  |
| Nginx | 1.22.0 |  |  |
| 1.24 |  | Essa versão não é compatível com o módulo *nginx-stick-module-ng* que é utilizado para o balanceamento de carga na versão *open-source*. |
| 1.26 |  | Essa versão não é compatível com o módulo *nginx-stick-module-ng* que é utilizado para o balanceamento de carga na versão *open-source*. |
| 1.28 |  | Essa versão não é compatível com o módulo *nginx-stick-module-ng* que é utilizado para o balanceamento de carga na versão *open-source*. |
| Microsoft NLB | Embarcado no Windows Server 2016 |  |  |
| WAF | Web Application Firewall |  | Foram realizados testes internos que apresentaram problemas. |
|  | | | | |
| **VIRTUALIZAÇÃO** | VMWare | VMware vSphere 5.0 a 6.5 |  |  |
| Hyper-V | Hyper-V em Microsoft Windows Server 2012 R2 |  |  |
|  | | | | |
| Cliente Desktop | | | | |
| **Categoria** | **Produto** | **Versão** | ***Status*** | **Observações** |
| **BROWSER/ NAVEGADOR** | Google Chrome | 97.0.X ou superior |  |  |
| Firefox | 97.0.X ou superior |  | Não homologado a partir da atualização 2.0 da plataforma. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-firefox) para saber mais. |
| Safari | - |  |  |
| Internet Explorer | IE 11 |  | O suporte à plataforma com o navegador Internet Explorer foi encerrado em 01/03/2021. [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055344913) para saber mais. |
| Microsoft Edge | 97.0.X ou superior |  | Homologado a partir da atualização 1.8.0-221004 da plataforma. |
| Resolução | Mínimo: 1024x768 |  | Até a atualização 1.8.2 da plataforma, a resolução mínima é 1024x768.  Nas releases posteriores, a resolução mínima será 1366x768. |
| Método de entrada | *Mouse* e Teclado |  |  |
|  | | | | |
| **RUNTIME** | Oracle Java | *Version* 7 *Update* 60 ou superior |  | Homologado até a atualização 1.5.13 da plataforma. Utilizado apenas para edição de documentos (WebDAV). |
| *Version* 8 *Update* 121 ou superior |  | Homologado a partir da atualização 1.6.0 da plataforma. Utilizado apenas para edição de documentos (WebDAV). |
| PDF | 1.7 ou inferior |  |  |
| MS Office | 2010 - 2013 |  |  |
| 2016 |  |  |
| 2019 |  | Homologado a partir da atualização 1.7.1 da plataforma. O visualizador interno utiliza o motor do Office 2016, por isso pode haver incompatibilidade com alguns recursos mais novos. |
| Microsoft Office 365 Business |  | Homologado a partir da atualização 1.8.2 da plataforma. |
|  | | | | |
| Cliente Mobile | | | | |
| **Categoria** | **Produto** | **Versão** | ***Status*** | **Observações** |
| **BROWSER/ NAVEGADOR** | iOS - Safari | iOS 6 ou superior |  |  |
| Android - (Chrome e webkit) | Android 5 ou superior |  |  |
| Windows Phone - IE | Windows Phone 8.0 ou 8.1 |  |  |
| Windows Mobile - EDGE | Windows 10 Mobile |  |  |
|  | | | | |
| **APP NATIVO2** | iOS | iOS 15 ou superior |  | Recomendamos manter o dispositivo na última versão disponível do iOS, dessa forma ele contará com todas as correções disponibilizadas pela fabricante. |
| Android | Android 11 ou superior |  | Consulte a regra de versionamento para Android com suporte garantido [clicando aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=871502812#NOT%C3%8DCIAS-android).  Recomendamos manter o dispositivo na última versão disponível do Android dessa forma ele contará com todas as correções disponibilizadas pela fabricante. |
| Windows Phone | Windows Phone |  | Conforme notícia publicada em 13/12/2016 e 23/03/2017 removemos o aplicativo Windows Phone da loja e finalizamos o suporte a ele. [Clique aqui](https://tdn.totvs.com/x/3BPyMw#NOT%C3%8DCIAS-windows-phone) para saber mais. |
| **2** →  O aplicativo do Fluig para cada plataforma móvel (iOS, Android) pode ter recursos diferentes, visto que uma pode ser uma evolução diferente da outra. Na documentação de Recursos do My Fluig estão os recursos disponíveis nos aplicativos para cada plataforma. [Clique aqui](http://tdn.totvs.com/x/fIYtCw) para saber mais. | | | | |
|  | | | | |
| Tradução | | | | |
| **País** | | **Idioma** | | ***Status*** |
| Estados Unidos | | Inglês | |  |
| Brasil | | Português | |  |
| Estándar | | Espanhol | |  |

Importante!

O *plug-in* Fluig Studio está homologado apenas para os sistemas operacionais Windows e Linux. 

| LEGENDA legenda | | |
| --- | --- | --- |
| **HOMOLOGADO**   ---   Passou por nossos testes e suportamos essa configuração em nosso atendimento. | **EM ANÁLISE**   ---   A homologação deste item está em *roadmap* e está condicionada a análise, portanto não há uma previsão de homologação para os itens nesta situação. | **NÃO HOMOLOGADO**   ---   O item foi avaliado e não é homologado para a plataforma. |

# Matriz de portabilidade Identity

---

Acesse a matriz de portabilidade do Identity .

# Matriz de portabilidade para documentos via Webdav

---

Acesse a matriz de portabilidade do Webdav para edição de documentos [aqui](http://tdn.totvs.com/x/E5MbCQ).

Ficou com alguma dúvida?

Entre em contato com a equipe de **Atendimento TOTVS Fluig** agora mesmo: **(11) 4003-0015**, opção **2** - **2** - **8** - **6**.

.confluenceTable .confluenceTd {
vertical-align: middle !important;
}
]]>
