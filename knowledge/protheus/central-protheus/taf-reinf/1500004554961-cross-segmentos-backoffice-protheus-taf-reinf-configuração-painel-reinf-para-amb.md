---
article_id: 1500004554961
category: TAF - REINF
content_hash: 0c539418aa14bfd007428b710a93dec234d5cbbc4e86ee6c95d4364021edc7df
fetched_at: '2026-06-28T22:41:34.600263+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Configuração Painel REINF
  para ambiente que Utiliza MEU RH com chave de baixo consumo de licença Habilitada.
type: support-article
updated_at: '2023-03-31T16:28:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004554961-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-REINF-para-ambiente-que-Utiliza-MEU-RH-com-chave-de-baixo-consumo-de-licen%C3%A7a-Habilitada
---

**Dúvida**

Como configurar o Painel REINF, tendo o meu RH.

**Ambiente**

TAF - A partir de 12.1.23

**Solução**

     Para MEU RH e Painel Reinf e a chave Stateless=1 irá gera conflito e erro no Painel REINF, esta chave estando desabilitada gera alto consumo de licença no meu RH.

   Neste cenário é alterada a configuração do Appserver.ini deixando o /REST para uso do meu RH e /APP para uso do Painel REINF.

Exemplo configuração do INI correta:

[ONSTART]  
JOBS=HTTPJOB,TAF\_CFGJOB  
REFRESHRATE=120  
  
[HTTPJOB]  
MAIN=HTTP\_START  
ENVIRONMENT=TAF25  
  
[TAF\_CFGJOB]  
MAIN=TAF\_CFGJOB  
Instances=5,30,1  
PrepareIn=ALL  
Environment=TAF25  
RefreshRate=120  
  
[HTTPV11]  
Enable=1  
Sockets=HTTPREST

[HTTPREST]  
Port=3000  
IPsBind=  
URIs=HTTPURI,MEURH  
    ;//Na chave HTTPREST informamos as duas URI's que serão utilizadas.  
Security=1  
  
[HTTPURI]  
URL=/app  
    ;//Atualizar o parâmetro MV\_BACKEND com o novo caminho utilizando o /app para que não ocorra conflito com a configuração do Meu RH.  
PrepareIn=ALL  
CORSEnable=1  
Instances=2,2  
AllowOrigin=\*  
  
[MEURH]  
URL=/rest  
PrepareIn=88  
Instances=1,1,1,1  
CORSEnable=1  
AllowOrigin=\*  
Stateless=1  
Public=fwjwt/refresh\_token,auth  
EnableKeepAlive=0

[HTTP]  
Enable=1  
Port=8090  
Path=C:\TOTVS12\Protheus\protheus\_data\http-root  -> Caso não tenha a pasta http-root cria-la dentro da protheus\_data.

Inserir também a chave MAXSTRINGSIZE=10 na seção GENERAL

## Parâmetros

É necessário configurar os seguintes parâmetros para a instalação:

* Criar o parâmetro MV\_GCTPURL do tipo caractere, com o conteúdo http://{hostname-do-servidor}:{porta-http}
* Criar o parâmetro MV\_BACKEND do tipo caractere, com o conteúdo http://{hostname-do-servidor}:{porta-rest}/rest
* Criar o parâmetro MV\_TAFPO do tipo lógico, com .T. se possui mais módulos de Protheus além do TAF ou possui mais de uma placa de rede no servidor onde está sendo executado o serviço HTTP e com .F. se possui apenas o TAF e apenas uma placa de rede;

Exemplo configuração Parâmetro MV\_BACKEND:

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018573881/Screenshot_2.png)

O parâmetro **MV\_TAFVLRE**precisa estar com o conteúdo**1\_05\_01** 

[TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233-TAF-CONFIGURADOR-Como-acessar-os-par%C3%A2metros-do-sistema-?source=search)

Para o correto funcionamento o ambiente precisa está atualizado.

[MP - TAF - REINF - Atualização Completa REINF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-MP-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-REINF?source=search)
