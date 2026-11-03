---
article_id: 41454099581591
category: Usabilidade
content_hash: 7ba3cf71d43e1c23852eb92f35cee459db1428d32d8254d6b1f765054ff04b23
fetched_at: '2026-06-28T22:42:17.290879+00:00'
product: protheus
section_id: 360000076807
source: central-protheus
title: 'Framework – Protheus – Erros UnZipApp: Não foi possível extrair o arquivo
  / RemDirApp: Falha ao excluir os arquivos do diretório'
type: support-article
updated_at: '2026-06-24T13:51:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41454099581591-Framework-Protheus-Erros-UnZipApp-N%C3%A3o-foi-poss%C3%ADvel-extrair-o-arquivo-RemDirApp-Falha-ao-excluir-os-arquivos-do-diret%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41454087819159) Tempo aproximado para leitura: **00:02:10 min**  
  
**Dúvida**  
Como corrigir os erros UnZipApp e RemDirApp?  
  
**Ambiente**  
Framework - Protheus - Todas as versões  
  
**Solução**  
É necessário ajustar as chaves App\_Environment e App\_Environment\_Extra nos appserver.ini dos ambientes e refazer a pasta http-root.

Estes erros ocorrem quando a pasta http-root, localizada na protheus\_data, sofre corrompimento dos arquivos. Isso faz com que na utilização dos ambientes gere o erro UnZipApp ou RemDirApp. O corrompimento ocorre quando as chaves App\_Environment e App\_Environment\_Extra não estão configuradas corretamente nos appserver.ini.

Para solucionar, realize o seguinte procedimento:

* Pare todos os serviços
* Nos appserver.ini dos ambientes, ajuste as chaves App\_Environment e App\_Environment\_Extra
* Na App\_Environment informe o nome de um dos ambientes existentes no appserver.ini
* Na App\_Environment\_Extra repita o nome do ambiente configurado na App\_Environment seguido de todos os outros declarados separados por vírgula. Segue exemplo:

```
[GENERAL]
…
App_Environment=Producao
App_Environment_Extra=Producao,Ambiente2,Ambiente3,Ambiente4
```

* Caso tenha apenas um ambiente declarado no appserver.ini, configure a App\_Environment\_Extra com o mesmo ambiente duas vezes. Segue exemplo:

```
[GENERAL]
…
App_Environment=Producao
App_Environment_Extra=Producao,Producao
```

* Na protheus\_data, renomeie a pasta http-root
* Suba um serviço e após iniciar, acesse o Protheus e abra cada ambiente da porta iniciada até a tela de login. Não precisa fazer login. Repita o procedimento para os outros serviços, sempre iniciando um e acessando os ambientes, até que todos estejam no ar
* Após realizar estes ajustes, o problema não deve mais ocorrer. No dia a dia, quando necessário, poderá parar todos os serviços e iniciar novamente de uma única vez

**Obs.:** Após ajustar os appserver.ini não inicie todos os serviços ao mesmo tempo, isso faz com que haja concorrência de gravação na pasta \http-root\app-root e não dá tempo de gravar as informações de todos os ambientes de uma única vez, fazendo com que os erros continuem ocorrendo.
