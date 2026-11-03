---
article_id: 360055855973
category: TAF - eSocial - eSocial do Futuro
content_hash: a28bf9cc0443e88dd35069994f68f2b011172336d542d6815f3c9f5b09ff56dd
fetched_at: '2026-06-28T22:45:15.877431+00:00'
product: protheus
section_id: 1500001537001
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Erro ao abrir, acessar
  o Painel eSocial (com HTTP e REST configurado)
type: support-article
updated_at: '2026-06-25T12:28:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055855973-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Erro-ao-abrir-acessar-o-Painel-eSocial-com-HTTP-e-REST-configurado
---

**Dúvida**Ao entrar no TAF do Futuro, ocorrem erros ao entrar na rotina.

Neste caso, o cliente não possui configurado a Porta Multi Protocolo.

A configuração foi realizada via HTTP e REST.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Painel eSocial - Todas as versões.  
  
**Solução**

1 **-** Validar se o **HTTP** está no ar:

* Na pasta http-root que fica dentro do RootPath, crie um arquivo chamado **“teste.csv”**;
* Na url do servidor digitar: [http://SEUIP:PORTAHTTP/teste.csv](http://seuipportahttp/);
* Se o HTTP estiver configurado corretamente, vai ser feito o download do arquivo teste.csv.

2 **-** Validar se os artefatos do projeto estão dentro da pasta **app-root**, que fica dentro da pasta **http-root**:

​![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091031994)

3  - Validar o arquivo index.html da pasta **preindex** possui 91 linhas ou  mais:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091033714)

4 - Acesse o CONFIGURADOR do Protheus/TAF:  
[TAF - CONFIGURADOR - Como acessar o configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036108413)

5 - Acesse os parâmetros do sistema:

[TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233)

6 - Verifique o parâmetro MV\_BACKEND se está preenchido com a URL do serviço REST:  
![blobid0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094751373)  
**Obs.:** O IP, tem que ser o endereço do servidor da Aplicação do TAF. Para confirmar qual a porta da conexão REST, abre o arquivo appserver.ini e verifique a seção [HTTPREST] a porta configurada. **Exemplo:  
![blobid1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094751393)**

7 - Verifique outro parâmetro MV\_GCTPURL se está apontando para a URL do serviço HTTP:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006029162)  
**Obs.:** O IP, tem que ser o endereço do servidor da Aplicação do TAF. Para confirmar qual a porta da conexão HTTP, abre o arquivo appserver.ini e verifique a seção [HTTP] a porta configurada.

**Exemplo:**  
![blobid3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094751413)

8 - Verifique o parâmetro **MV\_TAFPO**\*.  
\***Obs**.: Preencher o parâmetro **MV\_TAFPO** com **.T.** se possui mais módulos de Protheus além do TAF ou possui mais de uma placa de rede no servidor onde está sendo executado o serviço HTTP e com **.F.** se possui apenas o TAF e apenas uma placa de rede:

![blobid4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092529534)

Se usar outros módulos Protheus preencha com .T.

![blobid5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092529554)

Se usar o TAF Segregado, usar o valor .F.

9 - Adicione no seu arquivo de configuração as chaves abaixo em cada seção apontada:

[TAF\_CFGJOB]  
**Instances=5,30,5,1**

**[HTTPURI]**  
**;PrepareIn=ALL(deixar essa linha comentada (;))**

[General]  
**MaxStringSize=10**

10 - Teste as URL´s dos serviços REST e HTTP:

**HTTP:**

Na pasta http-root que fica dentro do RootPath, crie um arquivo chamado “teste.csv”;

Pelo navegador de internet que utiliza, digitar o endereço HTTP (URL) que está no parâmetro MV\_GCTPURL, após a URL do parâmetro, insira /teste.csv

Se não existir bloqueios de *Firewall, antivírus, ou na VPN*, será iniciado o download do arquivo criado: teste.csv

**REST:**

Pelo navegador de internet que utiliza, digitar o endereço REST (URL) que está no parâmetro MV\_BACKEND;

Será aberta uma página com informações das API´s *(**Application-Programming Interface, ou Interface de Programação de Aplicação).*

11 - Caso a LIB não esteja atualizada, atualize de acordo com a documentação abaixo:  
[RH - Linha Protheus - TAF - eSocial - Atualização - Como atualizar a LIB no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10486499915159-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%A3o-Como-atualizar-a-LIB-no-TAF)

12 - Reinicie os serviços do Protheus e abra o eSocial do Futuro no sistema.
