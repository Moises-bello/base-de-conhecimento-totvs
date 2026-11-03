---
article_id: 30707981726103
category: Meu RH - Login
content_hash: 5be5c0dc7bc7c1c152e4647e7f4dbf846f41285bd38cf03c8700f946e1a62c0e
fetched_at: '2026-06-28T22:47:27.244778+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: 'RH - RM - Meu RH - Erro ao logar no Meu RH: Usuário não está autenticado'
type: support-article
updated_at: '2026-01-16T15:25:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30707981726103-RH-RM-Meu-RH-Erro-ao-logar-no-Meu-RH-Usu%C3%A1rio-n%C3%A3o-est%C3%A1-autenticado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30707994719383) Tempo aproximado para leitura: **00:03:30 min**  
  
**Ocorrência**  
Ao acessar o Meu RH e tentar efetuar o login é apresentado a mensagem de erro: **Usuário não está autenticado.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois o Meu RH não está conseguindo identificar a base de dados para realizar a conexão.  
  
**Solução**  
O Meu RH verifica qual Base de Dados será acessada por meio dos arquivos *RM.Host.exe.config*, *RM.Host.Service.exe* e *Web.config*. Portanto, é essencial conferir o "ALIAS" especificado nesses arquivos de configuração. Abaixo, seguem os caminhos para a conferência de cada um deles:  
  
Para visualizar a configuração realizada no ambiente, acesse a pasta **C:\TOTVS\CorporeRM\RM.Net** e localize os arquivos de configuração de seu Host.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30707981675927)

Edite o arquivo de configuração do host e verifique qual é o nome do Alias informado na tag **DefaultDB**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30707981678231)

Acesse a agora a pasta **C:\TOTVS\CorporeRM\FrameHTML** e localize o arquivo **Web.config.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30707994728471)

Edite o arquivo **Web.config** e informe o mesmo nome do Alias que está informado na tag **DefaultDB**do arquivo de host que foi identificado anteriormente.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30707994730263)

**Observação:** O nome do ALIAS informado nos arquivos mencionados deve corresponder exatamente ao registrado no aplicativo RM.AliasManager.exe, localizado na pasta C:\TOTVS\CorporeRM\RM.Net.  
  
Após o procedimento, reinicie **todos** os serviços RM.Host.Service.exe, RM.Host.Service1.exe, etc de seu ambiente e após iniciados, reinicie também o IIS (poderá utilizar o comando IISRESET pelo CMD em modo administrador)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30707994731159)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30707994732311)

Após o procedimento, poderá realizar o teste novamente de login.

**Importante**  
Se o erro persistir, acesse a pasta **C:\TOTVS\CorporeRM\**[**RM.Net**](http://RM.Net)e exclua o arquivo **ALIAS.DAT**. Em seguida, abra o aplicativo **RM.AliasManager.exe** na mesma pasta, preencha os dados da base de dados com atenção para não inserir espaços indevidos e salve. O sistema gerará automaticamente um novo arquivo **Alias.dat**. Por fim, reinicie novamente e teste o acesso ao Meu RH.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30707994734359)
