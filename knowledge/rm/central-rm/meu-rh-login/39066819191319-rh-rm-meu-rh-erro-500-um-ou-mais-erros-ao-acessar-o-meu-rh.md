---
article_id: 39066819191319
category: Meu RH - Login
content_hash: a57eeebeecc12a5b27fccbfdebb04b397f0b2723a5c17e3f9c07008d9eea6659
fetched_at: '2026-06-28T22:47:27.210463+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Erro 500 Um ou mais erros, ao acessar o Meu RH
type: support-article
updated_at: '2026-03-16T13:44:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39066819191319-RH-RM-Meu-RH-Erro-500-Um-ou-mais-erros-ao-acessar-o-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39066819181463) Tempo aproximado para leitura: **00:04:30 min**  
  
**Ocorrência**  
Ao acessar o Meu RH, é apresentado a mensagem de erro: **"500 - One or more errors occurred"** ou **"500 -Um ou mais erros".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39067567615511)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Este erro ocorre devido a problemas de comunicação entre o servidor de Aplicação RM e Portal RM, que podem ser causados por configuração de IP ou Porta incorretas.  
  
**Solução**  
Para solucionar essa ocorrência, realize as seguintes validações:

**1.** Verifique se as Portas dos serviços Host utilizadas pelo Meu RH estão reservadas corretamente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39066819184151)

**Comandos Relacionados às Reservas de Portas:**

* **Reserva:**  
  `netsh http add urlacl url=http://+:Porta/ user=NetworkService`
* **Listar Todas as Portas Reservadas:**  
  `netsh http show urlacl`
* **Remover Reserva:**  
  `netsh http delete urlacl url=http://+:Porta/`

**Pontos de atenção:**

* **Reservar Portas WCF:** As portas do WCF devem ser reservadas apenas quando houver o uso de [**certificado no host**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6935374831127-Framework-Linha-RM-Frame-Habilitar-SSL-no-Host). Se o certificado estiver no **IIS**, execute o comando para listar as portas reservadas e remova as portas relacionadas à WCF.
* **Reservar Todas as Portas WebAPI:** Certifique-se de reservar todas as portas WebAPI utilizadas pelos Hosts dos "Servidores de Aplicação" e pelo "Servidor do Portal".
* **Reservar a Porta em HTTP ou HTTPS?**  
  Caso o certificado esteja vinculado ao IIS, a reserva de todas as portas deverá ser feita em **HTTP**. No entanto, se o certificado estiver vinculado diretamente ao Host, a reserva das portas deverá ser realizada em HTTPS.
* **Saúde do Ambiente:** Todas as portas WebAPI utilizadas pelo Meu RH, precisam retornar "Serviço Ok" nos testes healthcheck. Atualize o navegador diversas vezes para que a validação seja realizada em todas as portas. Utilize os seguintes links para validação:

  `http://IP_SERVIDOR_HOST_MEURH:PORTA_WEBAPI/api/rh/v1/services/healthcheck`  
  Exemplo: `http://10.173.16.246:8051/api/rh/v1/services/healthcheck`

  Para teste direto do servidor do portal:  
  `http://localhost/framehtml/rm/api/rest/new/services/healthcheck`  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39066819184919)  
     
  Caso as portas já estejam reservadas corretamente e ainda seja retornado o erro **“500 - Um ou mais erros”** em uma porta específica, siga os passos abaixo para verificar e corrigir a situação.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39066819185687)

**2.** Verifique no servidor se existem bloqueios de infraestrutura internos nesta porta específica. Uma forma rápida de realizar esse teste é utilizando o PowerShell, executando o seguinte comando:

**Test-NetConnection -ComputerName IP\_DO\_SERVIDOR -Port XXXX**

Se o resultado `TcpTestSucceeded` for `False`, isso indica que o problema está relacionado à rede ou à infraestrutura (por exemplo: bloqueio de firewall ou porta em uso por outra aplicação interna).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39066819186583)

**3.**Caso seja retornado `True` no resultado `TcpTestSucceeded`  e o erro persista na validação do healthcheck, o problema pode estar relacionado à comunicação entre o IP e o DNS do servidor.  
Para forçar a comunicação utilizando apenas o IP, realize os seguintes ajustes nos arquivos de configuração:  
  
**3.1. Alteração do arquivo Web.config**  
No diretório `C:\TOTVS\CorporeRM\FrameHTML`, edite o arquivo "Web.config". Dentro da tag `appSettings`, altere o valor da tag "Host" para o IP do servidor de aplicação do RM:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39066819187223)

**3.2.** **Alteração do arquivo RM.Host.Service**

No diretório `C:\TOTVS\CorporeRM\RM.Net`, edite os arquivos "RM.Host.exe.config" e "RM.Host.Service.exe". Dentro da tag `appSettings`, verifique se já existe a tag "Host" e altere o valor para o IP do servidor de aplicação. Caso não tenha esta tag, copie ela do arquivo Web.config para incluir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39066821614871)

**Observação**: Caso utilize a tag **"ServicesHostName"**nos arquivos Host**,**deverá alterar o valor dela também para o IP do servidor de aplicação do RM.

**Importante:** Sempre que realizar uma alteração de reserva de porta ou em arquivos configs, reinicie os **Hosts** e o **serviço IIS**.

**Saiba mais:**

[**RH - RM - Meu RH - Erro ao logar no APP Meu RH, Sistema indisponível no momento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4496031752343-RH-RM-Meu-RH-Erro-ao-logar-no-APP-Meu-RH-Sistema-indispon%C3%ADvel-no-momento)
