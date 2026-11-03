---
article_id: 4410703652375
category: Atualização
content_hash: 66f6da7f79effa9d7ebdcf109970bcb6eb36dda647e644183089123341893ffe
fetched_at: '2026-06-28T22:42:21.163341+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus - Atualização de Artefatos para Binário Harpia (Release
  33)
type: support-article
updated_at: '2024-03-26T12:24:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410703652375-Framework-Linha-Protheus-Atualiza%C3%A7%C3%A3o-de-Artefatos-para-Bin%C3%A1rio-Harpia-Release-33
---

**Dúvida**  
Quais Artefatos devo atualizar para utilizar a Release 33 do Protheus?  
  
**Ambiente**  
Protheus - AppServer - A partir da versão 12  
  
**Solução**Seguem abaixo passos e caminhos para o download e aplicação dos artefatos do Protheus para o binário Harpia (necessário para Release 33 e posteriores).  
  
DOWNLOAD Binário Harpia (AppServer 64 bits e SmartClient)  
- Acesse o portal : [https://suporte.totvs.com/](https://suporte.totvs.com/portal/p/10098/download)  
- Clique em Downloads;  
- Na Lista de Produtos selecione Protheus;  
- Seleciona na lista ao lado TOTVSTEC-FRAMEWORK;  
- Selecione Appserver;  
- No canto superior direito da página, na opção Filtro de pacotes, clique em Todos pacotes disponíveis  
- Baixe o Appserver APPSERVER HARPIA VERSAO 12 de acordo com seu Sistema Operacional;  
- Volte um nível e selecione Smartclient;  
- Baixe o Smartclient SMARTCLIENT HARPIA VERSAO 12 de acordo com seu Sistema Operacional.  
  
ATUALIZAÇÃO:  
Importante: o binário Harpia possui uma arquitetura exclusiva. Portanto, não sobrescreva os arquivos do Harpia na pasta do antigo Lobo Guará. Faça uma pasta nova de binário (renomeie as antigas appserver e smartclient e crie novas), descompacte o novo binário nelas, e copie da original apenas os arquivos appserver.ini e smartclient.ini.  
  
- Na pasta /bin/, renomeie as pastas appserver e smartclient;  
- Crie novas pastas appserver e smartclient;  
- Descompacte os arquivos baixados, para suas respectivas pastas (appserver e smartclient);  
- Das antigas pastas renomeadas, copie apenas os arquivos appserver.ini para a nova pasta appserver e smartclient.ini para a nova pasta smartclient.  
  
  
DOWNLOAD DBAccess:  
- Acesse o portal : [https://suporte.totvs.com/](https://suporte.totvs.com/portal/p/10098/download)  
- Clique em Downloads;  
- Na Lista de Produtos selecione Protheus;  
- Nas opções ao lado selecione TOTVSTEC-FRAMEWORK;  
- Selecione DBACCESS;  
- No canto superior direito da página, na opção Filtro de pacotes, clique em Todos pacotes disponíveis;  
- Baixe o DBAccess TOTVS DBACCESS X64 - BUILD 21.1.1.0 referente ao seu sistema operacional.  
  
ATUALIZAÇÃO:  
- Faça um backup da pasta do DBAccess;  
- Descompacte o arquivo baixado dentro da pasta do DBAccess, sobrescrevendo os arquivos.  
  
  
DOWNLOAD RPO (Repositório de Objetos Harpia):  
- Acesse o portal : [https://suporte.totvs.com/](https://suporte.totvs.com/portal/p/10098/download)  
- Clique em Downloads;  
- Na Lista de Produtos selecione Protheus;  
- Nas opções ao lado selecione MICROSIGA PROTHEUS VERSÃO 12.1.33;  
- Selecione REPOSITÓRIOS;  
- No canto superior direito da página, na opção Filtro de pacotes, clique em Todos pacotes disponíveis;  
- Baixe o REPOSITORIO DE OBJETOS 12.1.33 - MULTI IDIOMA.  
  
Importante: ao utilizar o RPO para Harpia (Release 33 e posteriores), deve-se alterar, no arquivo appserver.ini, na seção do Ambiente, a linha RPOLANGUAGE para =multi.  
Ex.:  
[P12.1.33]  
SourcePath=  
...  
RPOLANGUAGE=multi  
  
ATUALIZAÇÃO:  
- Renomeie o arquivo baixado para tttm120.rpo  
- Copie-o para a pasta apo
