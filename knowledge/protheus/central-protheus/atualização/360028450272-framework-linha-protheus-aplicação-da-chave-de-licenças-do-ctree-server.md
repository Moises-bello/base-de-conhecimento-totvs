---
article_id: 360028450272
category: Atualização
content_hash: d7b5c983ae27b7b42ae66f9e696e734da2c427e1bad18b79266736607a9a8612
fetched_at: '2026-06-28T22:42:21.187327+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Aplicação da chave de licenças do Ctree Server
type: support-article
updated_at: '2024-03-26T13:13:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028450272-Framework-Linha-Protheus-Aplica%C3%A7%C3%A3o-da-chave-de-licen%C3%A7as-do-Ctree-Server
---

**Dúvida**Como efetuar a aplicação da chave de licenças do Ctree?  
  
**Ambiente**Protheus - Ctree Server - Todas as versões  
  
**Solução**Seguem abaixo os procedimentos de aplicação de chave do Ctree, em ambientes Windows e Linux.  
  
**Windows:**  
- Pare o serviço do Ctree Server  
- Execute o Programa Activate.exe (pasta padrão: C:\FairCom\V9.5.2\winX64\bin\ace\isam)  
- Preencha os dados enviados pelo Suporte Framework ou Executivo de Contas (Serial Number e Activation Key)  
![2019-05-23_1040.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029255231)  
  
- Clique em Activate  
- É necessário também inserir no arquivo de configuração do CtreeServer (ctsrvr.cfg) a configuração USERS , informando o número de licenças que será utilizado. Por exemplo, ao instalar uma licença para 150 usuários, insira no arquivo ctsrvr.cfg a linha abaixo:   
USERS 150  
- Reinicie o CtreeServer  
  
**Linux:**  
- Pare o serviço do Ctree Server  
- Localize o arquivo fcactvat e execute-o  
- Serão solicitadas informações, preencha com os dados enviados pelo Suporte Framework ou Executivo de Contas  
![2019-05-23_1041.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029253612)  
  
- Insira a Activation Key  
- Insira os últimos 6 dígitos do Número de Série  
- É necessário também inserir no arquivo de configuração do CtreeServer (ctsrvr.cfg) a configuração USERS , informando o número de licenças que será utilizado. Por exemplo, ao instalar uma licença para 150 usuários, insira no arquivo ctsrvr.cfg a linha abaixo:   
USERS 150  
- Reinicie o CtreeServer  
  
**Para verificar quantos usuários estão liberados (tanto Windows quanto Linux):**  
- Entrar na pasta ctreeTools\ctreeAdmin\Client ou \tools\cmdline\admin\client  
- Executar o programa ctadmn  
- Usuário do Administrador (Default: ADMIN)  
- Senha do Administrador (Default: ADMIN)  
- Tecle [Enter]  
- Tecle [Enter]  
- Opção 6 - Server Configuration  
- Verificar a quantidade de usuários nos campos:  
Maximum number of logons  
Limit for the maximum number of logons
