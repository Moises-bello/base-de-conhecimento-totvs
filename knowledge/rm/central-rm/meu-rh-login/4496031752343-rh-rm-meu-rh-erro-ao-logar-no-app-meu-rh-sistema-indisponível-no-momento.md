---
article_id: 4496031752343
category: Meu RH - Login
content_hash: cb8a2be1383a3b800d36517bd51bad96465ef8ea1d91ed6b40d3170b47135a95
fetched_at: '2026-06-28T22:47:27.294668+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: RH - RM - Meu RH - Erro ao logar no APP Meu RH, Sistema indisponível no momento
type: support-article
updated_at: '2026-03-06T20:46:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4496031752343-RH-RM-Meu-RH-Erro-ao-logar-no-APP-Meu-RH-Sistema-indispon%C3%ADvel-no-momento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22824712121239) Tempo aproximado para leitura: **00:05:45 min**  
  
**Ocorrência**  
Ao tentar acessar o APP Meu RH é apresentada a mensagem: **Sistema indisponível no momento**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32156074358039)  
  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.34  
  
**Causa**  
Esse erro ocorre devido a uma falha de comunicação entre o aplicativo e o servidor.  
  
**Solução**  
Este documento apresenta as possíveis causas do erro. É essencial a leitura completa para garantir a solução adequada.  
  
A **principal causa** do erro está relacionada às **portas da WebAPI**. Assista ao vídeo "How To" que orienta como **reservar as portas** corretamente, verificar a **saúde do ambiente** e garantir que seu **certificado seja válido** para o Meu RH.  
  
**Importante:** Embora o vídeo mencione o erro "Ops! Algo deu errado", houve uma atualização na mensagem, que agora aparece como "**Sistema indisponível no momento**". No entanto, **as causas do erro permanecem as mesmas.**

 

**Comandos Relacionados às Reservas de Portas:**

* **Reserva:**  
  `netsh http add urlacl url=http://+:Porta/ user=NetworkService`
* **Listar Todas as Portas Reservadas:**  
  `netsh http show urlacl`
* **Remover Reserva:**  
  `netsh http delete urlacl url=http://+:Porta/`

**Verificação da Saúde do Ambiente:**  
Verifique se cada porta retorna "OK" usando os seguintes links:

* `http://IP_SERVIDOR_HOST_MEURH:PORTA_WEBAPI/api/rh/v1/services/healthcheck`  
  Exemplo: `http://10.173.16.246:8051/api/rh/v1/services/healthcheck`
* Para teste direto do servidor do portal:  
  `http://localhost/framehtml/rm/api/rest/new/services/healthcheck`

**Pontos de atenção:**

* **Reservar Portas WCF:** As portas do WCF devem ser reservadas apenas quando houver o uso de [**certificado no host**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6935374831127-Framework-Linha-RM-Frame-Habilitar-SSL-no-Host). Se o certificado estiver no **IIS**, execute o comando para listar as portas reservadas e remova as portas relacionadas à WCF.
* **Reservar Todas as Portas WebAPI:** Certifique-se de reservar todas as portas WebAPI utilizadas pelos Hosts dos "Servidores de Aplicação" e pelo "Servidor do Portal".
* **Reservar a Porta em HTTP ou HTTPS?**  
  Caso o certificado esteja vinculado ao IIS, a reserva de todas as portas deverá ser feita em HTTP, conforme mostrado no vídeo acima. No entanto, se o certificado estiver vinculado diretamente ao Host, a reserva das portas deverá ser realizada em HTTPS.
* **Reinicie após Alterações:** Sempre que realizar uma alteração de porta ou em configs, reinicie os Hosts e o serviço IIS.
* **Certificado Válido:** O certificado deve ser válido e não pode ser auto-assinado. [Consulte a documentação para testar seu certificado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035159453-RH-RM-Meu-RH-Testando-se-o-certificado-HTTPS-SSL-%C3%A9-v%C3%A1lido)
* **Saúde do Ambiente:** Todas as portas WebAPI utilizadas pelo Meu RH, precisam retornar serviço Ok nos testes do healthcheck. Atualize o navegador diversas vezes para que a validação seja realizada em todas as portas.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38863800626071)  
     
  Caso as portas já estejam reservadas corretamente e ainda seja retornado o erro **“500 - Um ou mais erros”** em uma porta específica, siga os passos abaixo para verificar e corrigir a situação.

  **Clique aqui para expandir as instruções.**

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38863792057495)

  **1.** Verifique no servidor se existem bloqueios de infraestrutura internos nesta porta específica. Uma forma rápida de realizar esse teste é utilizando o PowerShell, executando o seguinte comando:

  **Test-NetConnection -ComputerName IP\_DO\_SERVIDOR -Port XXXX**

  Se o resultado `TcpTestSucceeded` for `False`, isso indica que o problema está relacionado à rede ou à infraestrutura (por exemplo: bloqueio de firewall ou porta em uso por outra aplicação interna).

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38863792069527)

  **2.** Caso seja retornado `True` no resultado `TcpTestSucceeded`  e o erro persista na validação do healthcheck, o problema pode estar relacionado à comunicação entre o IP e o DNS do servidor.  
  Para forçar a comunicação utilizando apenas o IP, realize os seguintes ajustes nos arquivos de configuração:  
    
  **2.1. Alteração do arquivo Web.config**  
  No diretório `C:\TOTVS\CorporeRM\FrameHTML`, edite o arquivo "Web.config". Dentro da tag `appSettings`, altere o valor da tag "Host" para o IP do servidor de aplicação do RM:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38863792070679)

  **2.2.** **Alteração do arquivo RM.Host.Service**

  No diretório `C:\TOTVS\CorporeRM\RM.Net`, edite os arquivos "RM.Host.exe.config" e "RM.Host.Service.exe". Dentro da tag `appSettings`, verifique se já existe a tag "Host" e altere o valor para o IP do servidor de aplicação. Caso não tenha esta tag, copie ela do arquivo Web.config para incluir:  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38863792073111)

  **Observação**: Caso utilize a tag **"ServicesHostName"** nos arquivos Host**,** deverá alterar o valor dela também para o IP do servidor de aplicação do RM.

### Caso o Erro Persista

Verifique os itens abaixo que também podem causar o erro **"Sistema indisponível no momento"**:

**1. Configuração do Alias no RM.Host.Service:**  
No diretório `C:\TOTVS\CorporeRM\RM.Net`, edite os arquivos "RM.Host.exe.config" e "RM.Host.Service.exe". Dentro da tag `appSettings`, verifique se já existe a tag:  
  
**<****add****key****=****"DefaultDB"****value****=****"CorporeRM"** **/>**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26596290246039)**  
  
**2. Habilitar o Token no Meu RH:**  
[Consulte a documentação para habilitar o token.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5693723606167-RH-RM-Meu-RH-Utilizar-token-para-o-Meu-RH)  
  
**3.** **Verificar se a Biblioteca e Portal encontram-se no mesmo Patch**  
O Meu RH deve estar no mesmo patch da Biblioteca RM. Em ambientes de múltiplas camadas, verifique se todos os servidores estão no mesmo Patch do Portal e Biblioteca.  
[Consulte a documentação para conferência.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402311146263-RH-RM-Meu-RH-Como-verificar-Vers%C3%A3o-e-Patch-da-Biblioteca-RM-e-Meu-RH)  
  
**4. Diagnóstico do Problema com o Postman**  
Utilize o Postman para executar scripts desenvolvidos que validam os serviços do Meu RH.  
[Consulte a documentação para obter o script e utilizar-lo no Postman.](https://tdn.totvs.com/pages/viewpage.action?pageId=844981132)
