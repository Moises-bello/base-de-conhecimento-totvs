---
article_id: 360004837051
category: Folha Mensal
content_hash: 2c0c1a98d3e6f52dacf877a16afc5f2e8730db08110b910da9fd3b5f8950c435
fetched_at: '2026-06-28T22:47:00.327847+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Repetição de eventos na Folha Analítica '
type: support-article
updated_at: '2025-02-27T18:47:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004837051-RH-RM-FOP-Repeti%C3%A7%C3%A3o-de-eventos-na-Folha-Anal%C3%ADtica
---

**Ocorrência**

Ao gerar o relatório da Folha analítica na nova MDI de versão 12.1.20, está saindo no relatório várias vezes os Proventos, Descontos e Total Líquido.

Exemplo:

 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360006131951/image.png) 

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento  -  A partir da versão 12.1.20

**Causa**A provável causa seria um lixo no direcionamento das dlls  
  
**Solução**Realize a exclusão do relatório de Folha Analítica acessando: Gestão > RM Reports > utilize um filtro para exibir todos os relatórios da Folha de Pagamento > selecione o relatório da folha analítica e exclua-o. Logo em seguida, importe-o novamente;

Verifique se o relatório que está importando é o padrão

**O relatório padrão do sistema é o FOPREL0009 - Folha Analítica.TotvsReport.**

* Se persistir a inconsistência, realize os passos abaixo:

1. Acesse o aplicativo RM.HOST.SERVICEMANAGER.EXE no diretório C:\totvs\CorporeRM\RM.Net desinstale o serviço, e feche o aplicativo.

 

2.Acesse o diretório C:\totvs\CorporeRM\RM.Net e apague o arquivo \_BROKER.DAT, responsável pelo direcionamento das dlls.

 

3.Acesse o diretório C:\totvs\CorporeRM\RM.Net, localize o arquivo RM.HOST.EXE e clique duas vezes sobre o mesmo.

Ao iniciar espere um tempo até que o ícone na parte inferior direita da tela do Windows fique verde, de forma que o serviço seja reiniciado e o arquivo \_BROKER.DAT seja criado novamente e o serviço RM.HOST.SERVICE reiniciado.

4.Verificar na pasta C:\totvs\CorporeRM\RM.Net se o arquivo \_BROKER.DAT foi criado.

 

5.Verificar no painel de serviços do Windows (Iniciar > Executar > services.msc) se o serviço RM.HOST.SERVICE está iniciado, caso não, acessar o caminho C:\totvs\CorporeRM\RM.Net o RM.HOST.SERVICEMANAGER.EXE novamente e clicar em Instalar e depois Iniciar o serviço.
