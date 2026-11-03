---
article_id: 4406757164311
category: TAF - REINF
content_hash: 5d01ec74cf47b2f1c50a4f51c17ecc5611eaa8f1c8b59eb05ada2b04223c0de5
fetched_at: '2026-06-28T22:41:33.625464+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como aplicar a atualização
  do TAF utilizando o Visual Studio Code?
type: support-article
updated_at: '2023-10-11T20:36:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406757164311-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-aplicar-a-atualiza%C3%A7%C3%A3o-do-TAF-utilizando-o-Visual-Studio-Code
---

**Dúvida**A aplicação de pacotes no TAF é feita através da ferramenta VSCode (Visual Studio Code).  
Como aplicar pacote de correção via *VSCode*?

**Ambiente**TAF - REINF - A partir da 12.1.27

**Solução**

1 - Caso seja utilizado TAF Segregado: é necessário parar o serviço TAF-WS antes de executar os passos seguintes.

Caso seja utilizado TAF como módulo do Protheus: verifique se o appserver.ini possui algum job na seção ONSTART, se possuir, será necessário comentar essa linha conforme exemplo abaixo:

![sc1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406753979543/sc1.png)

2 - Realize o download do VSCode através do link abaixo:

<https://code.visualstudio.com/download>

Observação: Não é necessário realizar nenhuma alteração durante o processo de instalação. Avance até o final.

3 - Com o *VSCode* instalado, acesse a opção *Extension* e instale o *Plugin* "***TOTVS Developer Studio for VSCode"***, conforme imagem:

![sc2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406754035735/sc2.png)

3 - Acesse o diretório C: do servidor no qual o processo de instalação está sendo executado e crie uma nova pasta de nome VSCode:

![sc3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406754061335/sc3.png)

5- Clique no menu ***File******> Open Folder*** e selecione a pasta criada anteriormente no diretório C: do seu servidor:

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001860322/mceclip2.png)**

6 - Com o serviço do TAF iniciado, clique no plugin da Totvs instalado anteriormente e clique em adicionar server:

![sc5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406754147095/sc5.png)

Observação: A instalação do plugin demora alguns minutos. É necessário aguardar a finalização da instalação para que o ícone da Totvs seja exibido no canto esquerdo da tela.

7 - O ***Server Name*** será de acordo com o nome do seu ambiente. O nome e a porta serão aqueles que estão parametrizados no arquivo appserver.ini do TAF. Para ambiente TAF Segregado, por padrão o ambiente é TAF. Clientes com TAF módulo do Protheus pode possuir outro nome de ambiente.

![sc6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406748378903/sc6.png)

Observação: Para configuração e aplicação de patch os includes não é necessário, podendo deixar em branco.

8 - Após a inclusão do servidor, clique com o botão direito e realize a conexão. (print abaixo com outro nome de ambiente como exemplo)

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001906281/mceclip6.png)**

9 - Serão pedidos as informações de ambiente, usuário e senha para que a conexão seja realizada. Para ambiente informe o nome do ambiente. O usuário será admin com a senha utilizada para acesso ao TAF. Clique em OK para avançar.

10 - Após a conexão ser realizada com sucesso, clique com botão direito no servidor e ***Patch Apply***:

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001860582/mceclip7.png)**

11 - Selecione o arquivo .PTM para aplicação do patch e posteriormente clique em ***Apply/Close***:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102963113/mceclip0.png)**

Concluído! No console do TAF será apresentado o processamento de aplicação do patch e o arquivo .apo será atualizado com o pacote de correção escolhido. 

Importante: Para eliminar sujeira do arquivo .apo é necessário executar a opção ***Desfrag RPO*** dentro do VSCode. O tamanho do arquivo será reduzido.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001954521/mceclip1.png)
