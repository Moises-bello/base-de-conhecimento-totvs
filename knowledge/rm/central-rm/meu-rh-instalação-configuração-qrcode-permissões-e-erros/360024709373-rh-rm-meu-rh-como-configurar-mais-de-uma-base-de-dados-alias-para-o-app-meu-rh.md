---
article_id: 360024709373
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 460bee7c3f260123067b07b555e176ee00ed510f552ed3591ab4d674bc8abcc9
fetched_at: '2026-06-28T22:47:29.591188+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Como configurar mais de uma base de dados Alias para o app
  Meu RH
type: support-article
updated_at: '2026-03-30T16:37:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024709373-RH-RM-Meu-RH-Como-configurar-mais-de-uma-base-de-dados-Alias-para-o-app-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24083966224407) Tempo aproximado para leitura: 00:02:45 min**

**Dúvida**  
Como configurar mais de uma base de dados/Alias para o *app* Meu RH?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.27  
  
**Solução**

A definição do alias da base de dados utilizada pelo Meu RH é realizada no arquivo W**eb.config**, localizado na pasta de instalação do portal, por meio da tag `ServiceAlias`.

> **Importante:** Não é possível alterar o alias diretamente na tela de login do aplicativo como é feito no RM ou Portal RH (corpore.net).

Para acessar outra base de dados, é necessário alterar o valor do "Alias" através da tag `ServiceAlias` no arquivo **Web.config** localizado na pasta **FrameHTML,** ou modificar o apontamento da base vinculada ao alias utilizando o **RM.AliasManager.exe**, localizado na pasta **RM.Net**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39392814764183)

Caso seja necessário manter acesso a mais de uma base de dados ao mesmo tempo, é necessário criar ambientes distintos. Para isso, siga os passos abaixo para criação de um novo ambiente:

**1.** Realize uma cópia da pasta **FrameHTML** no mesmo diretório padrão. Atualize o nome da pasta copiada para a descrição desejada, exemplo "**FrameHTML 2**".  
![](https://totvssuporte.zendesk.com/attachments/token/Ryz2xz3CbQz87cnheECHywfMo/?name=image.png)  
   
**2.** No arquivo **Web.config** de **ambas as pastas (original e cópia)**, adicione no bloco `<appSetings>` a  tag :

`<add key="ConsiderServiceAliasMyHr" value="true" />`   
   
![](https://totvssuporte.zendesk.com/attachments/token/Ayn1H0KGYuBl1vpVQKhVwm9Rl/?name=image.png)  
   
3- Na pasta réplica, edite o arquivo **W****eb.config** e atualize o valor da tag `ServiceAlias` para o alias da nova base desejada. Exemplo: "CorporeRM\_Teste"

`<add key="ServiceAlias" value="CorporeRM_Teste" />`  
![](https://totvssuporte.zendesk.com/attachments/token/QhwVs8niJHmBSk22WjsIFY3FB/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/A9oZ7fZYbIT8pYBvY55jvSlf4/?name=image.png)  
   
4- Acesse o **IIS Manager** > **Default Web site** > **Adicionar aplicativo.**  
![](https://totvssuporte.zendesk.com/attachments/token/azpaQujnevwQGClFlNfxvl4hK/?name=image.png)  
 

No campo **Alias**, informe o nome da pasta replicada (ex.: *FrameHTML2*). Em **Pool de Aplicativos**, selecione a opção ***FrameHTML***. Já no campo **Caminho físico**, informe o diretório correspondente à pasta replicada (ex.: *C:\TOTVS\CorporeRM\FrameHTML2*).  
![](https://totvssuporte.zendesk.com/attachments/token/7o5ZmUQPauMrwbFbiXEGgvmuX/?name=image.png)  
   
Após concluir as configurações, será criado um novo site de acesso "**FrameHTML2**" apontando para outra base (Alias). É necessário reiniciar os serviços **Host** e o **IIS** para validação.  
![](https://totvssuporte.zendesk.com/attachments/token/12ngkjOFfIPHPmsCA2w3a4GNs/?name=image.png)

**Importante**: Para o acesso através do aplicativo mobile, configure um novo QR Code utilizando a URL do novo site de acesso que foi criado. Para informações sobre como gerar o QR Code, acesse: [RH - RM - Meu RH - O que é e como gerar um QR Code de acesso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024702953-RH-RM-Meu-RH-O-que-%C3%A9-e-como-gerar-um-QR-Code-de-acesso)
