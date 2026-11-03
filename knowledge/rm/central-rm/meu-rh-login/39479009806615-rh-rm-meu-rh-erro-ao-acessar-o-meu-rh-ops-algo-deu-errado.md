---
article_id: 39479009806615
category: Meu RH - Login
content_hash: 60d755303a07fd12c50c1fd1c306e2f0ddf97a6c467e8096cbabb5daa76c8b41
fetched_at: '2026-06-28T22:47:27.190208+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Erro ao acessar o Meu RH, "Ops! Algo deu errado"
type: support-article
updated_at: '2026-04-06T11:03:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39479009806615-RH-RM-Meu-RH-Erro-ao-acessar-o-Meu-RH-Ops-Algo-deu-errado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39479009788951) Tempo aproximado para leitura: **00:01:00min**  
  
**Ocorrência**  
Ao tentar realizar o acesso ao aplicativo Meu RH, é apresentada a mensagem de erro: *"Ops! algo deu errado".*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39479251825687)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas Versões  
  
**Causa**  
Este erro ocorre, quando o Meu RH não consegue localizar o Alias (Base de dados) para autenticar o login.  
  
**Solução**  
Para solucionar essa ocorrência, acesse o diretório `C:\TOTVS\CorporeRM\RM.Net`,  edite os arquivos "*RM.Host.exe.config*" e "*RM.Host.Service.exe*", "*RM.Host.Service1.exe...*". Dentro da tag `appSettings`, inclua a tag:  
  
`<add key="DefaultDB" value="CorporeRM" />`  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/39478994727447)**

Caso já tenha esta tag nos arquivos, valide se o valor definido está com a descrição correta conforme o [Alias Manager](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016257412-Framework-Linha-RM-Frame-Como-incluir-um-Alias).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39478994728471)

Após alteração, reinicie todos os serviços **Host** e o **IIS Manager** para nova validação.

**Saiba mais:**

[**RH - RM - Meu RH - Erro ao logar no APP Meu RH, Sistema indisponível no momento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4496031752343-RH-RM-Meu-RH-Erro-ao-logar-no-APP-Meu-RH-Sistema-indispon%C3%ADvel-no-momento)
