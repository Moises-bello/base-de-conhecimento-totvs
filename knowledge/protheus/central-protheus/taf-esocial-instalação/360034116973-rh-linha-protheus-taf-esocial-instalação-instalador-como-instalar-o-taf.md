---
article_id: 360034116973
category: TAF - eSocial - Instalação
content_hash: 6a79d9681c438734a064ed624755d8c7da069a238abaf8489cea6ebd8983e128
fetched_at: '2026-06-28T22:45:11.001987+00:00'
product: protheus
section_id: 1500001536881
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Instalação - INSTALADOR - Como instalar
  o TAF
type: support-article
updated_at: '2024-05-29T14:37:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034116973-RH-Linha-Protheus-TAF-eSocial-Instala%C3%A7%C3%A3o-INSTALADOR-Como-instalar-o-TAF
---

**Dúvida**

**ATENÇÃO:** *Clientes que de alguma forma perderam a instalação do TAF porém tem seus dados armazenados no banco de dados em backup é recomendável que este processo seja executado por um consultor in loco **qualificado** para executar a instalação.*

Como instalar o TAF e o TSS via instalador?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Instalação - Instalador – À partir da versão 12.1.27  
  
**Solução**

1 - Para seguir com o procedimento abaixo, veja os requisitos necessários para instalação do sistema em seu ambiente:  
[Pré Requisitos para instalação do TAF e do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034038393)

**\* Obs.:** É necessário estar com a versão do License Server igual ou acima da 3.2.0:  
[RM - Frame - Identificar versão do License Server Virtual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016111748-RM-Frame-Identificar-vers%C3%A3o-do-License-Server-Virtual)

2 - Caso não tenha realizado o download do instalador, possuímos a documentação como realizar o download do instalador:  
[Como realizar o download do instalador do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033541434)

3 - Após o download e descompactá-lo, acesse o diretório "baixado" e acesse o **Aplicativo TOTVS.PackManager** para executar o processo de instalação:

![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043209034)

4 - Ao realizar o download, sera exibido a tela abaixo e selecione "Realizar nova instalação". Clique em **Próximo**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056734133)

5 - Serão apresentados os módulos a serem instalados. Clique em **Próximo:**

![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044042513)  
  
6 - Selecione o diretório onde deseja instalar o sistema. Se quiser deixar no caminho padrão: (C:\totvs\TAF). Clique em **Próximo**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055862874)  
  
7 - Informe o endereço do License Server e a porta do servidor para prosseguir com a instalação:

![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044042533)

8 - Para o TAF e o TSS, devemos configurar a conexão com o banco de dados. Nesse caso iremos configurar o DBAccess. Para conectar com o banco, deve-se clicar em **Parâmetros de Instalação** para iniciar o processo de configuração:

![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043209074)

9 - Selecione o tipo de Banco, o Nome ou IP de conexão com o servidor do Banco, coloque o nome do banco, usuário e senha:  
**Obs.:** Se seu banco de dados for **SQL Server**, selecione o driver SQL Native Client.  
Se seu banco for **Oracle**, o Driver deve estar configurado em **64 Bits.**

TAF:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072722654)

TSS:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081672473)

10 - Clique em **Testar** e veja se a conexão foi testada com sucesso:

![7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043209094)

11 - Repare que a etiqueta que estava em vermelho ficou da cor verde, ou seja, os teste de conexão com o banco de dados foram validados com sucesso.  Clique em **Próximo** para prosseguirmos com a instalação:

![8.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043209114)

12 - Próximo passo é configurarmos as portas de comunicação da WebService do TAF e do TSS.  
***OBS.:*** As portas de comunicação por padrão: 8080 e 8081, recomendamos alterar os valores. Clique em **Próximo:**

![9.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044042573)

13 - Informe a Porta HTTP utilizada para abertura das interfaces do TAF do Futuro. Clique em **Próximo**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056734493)

```
Importante!  
  
TAF do Futuro:  
  
O Projeto TAF do futuro tem como objetivo evoluir o produto gerando visões   
gerenciais para entrega de suas obrigações acessórias com uma melhor experiência   
do usuário, iniciamos pelo eSocial e REINF mas iremos replicar todo esse novo   
modelo de usabilidade para todas as obrigações contempladas pelo produto.   
Estamos utilizando o PORTINARI para essa reformulação   
( Saiba mais sobre o Portinari ), isso nos permite evoluir muito principalmente   
a questão de usabilidade.
```

14 - Confirme o início da Instalação e será iniciado o Processo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056734513)

15 - Nesse momento o sistema estará extraindo os arquivos para o Diretório que foi informado no começo da instalação:

![10.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044042593)

16 - Em seguida vai aparecerá a tela abaixo, onde informa os status de instalação do TAF e TSS. Aguarde o processo finalizar;

![11.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043209134)

17 - Quando o processo de instalação terminar, os status deverão ficar verdes e em seguida clique em **Finalizar**;

![12.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360043209154)

18 - Após finalizar a instalação o TAF e o TSS o próximo passo é atualizar o sistema, o próximo passo é seguir com a atualização do TAF e TSS, clique na documentação à seguir:  
[TAF - ATUALIZAÇÃO - Como atualizar o TAF e o TSS via atualizador? (SEGREGADO)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020127812)

19 - Finalizando a atualização, acesse a documentação à seguir para continuar com a configuração do TAF e TSS:  
[Configurando o TAF no primeiro acesso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034360513)

**REFERÊNCIA:**  
https://tdn.totvs.com/display/public/TAF/Instalador+do+TAF+-+Processo+Completo
