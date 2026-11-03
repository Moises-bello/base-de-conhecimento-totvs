---
article_id: 14208936050711
category: Financeiro - Viagens
content_hash: c12da76830e71853dd66df4e827e88185e4d127c2d8b4186d93adce3ff285e64
fetched_at: '2026-06-28T22:38:21.505890+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Validação REST para
  implantação APP minha prestação de contas
type: support-article
updated_at: '2023-04-28T23:46:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14208936050711-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Valida%C3%A7%C3%A3o-REST-para-implanta%C3%A7%C3%A3o-APP-minha-presta%C3%A7%C3%A3o-de-contas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **1****5:00:00min****Dúvida**  
Qual é a configuração Rest necessária para funcionamento do APP minha prestação de contas?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - A partir da versão 12.1.33  
  
**Solução**1 - Visão Geral

Para utilização dos Apps é necessário que o *REST* do Protheus esteja habilitado e configurado corretamente, com a autenticação habilitada. Nas seções abaixo temos alguns exemplos de configuração e validação.  
  
2 - Configuração do REST

Para fazer a configuração do *REST* é recomendado que seja criada uma cópia do **appserver** do Protheus para que rode em instâncias separadas conforme no exemplo abaixo:  
![](https://tdn.totvs.com/download/attachments/519719292/Screen%20Shot%202019-10-29%20at%2017.31.44.png?version=2&modificationDate=1572383396060&api=v2)

Os arquivos podem ser copiados da pasta **appserver**, sendo necessário alterar apenas o arquivo **appserver.ini** da pasta onde ficará o *REST*.

**Importante**

Caso você utiliza mais de um tipo de *webservice*, para correto funcionamento das integrações, o **appserver** *REST* e *SOAP* não devem rodar na mesma instância do serviço, nem estar expostos na mesma porta.  
  
3 - Configuração do appserver.ini  
O arquivo **appserver.ini** deve conter as chaves abaixo:

**Configuração REST sem os comentários**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27 | `[General]`  `MAXSTRINGSIZE=``10`    `[HTTPV11]`  `Enable=``1`  `Sockets=HTTPREST`    `[HTTPREST]`  `Port=``8080`  `IPsBind=`  `URIs=HTTPURI`  `Security=``1`    `[HTTPURI]`  `URL=/rest`  `PrepareIn=ALL`  `Instances=``2``,``5``,``1``,``1`  `CORSEnable=``1`  `AllowOrigin=*`    `[HTTPJOB]`  `MAIN=HTTP_START`  `ENVIRONMENT=environment`    `[ONSTART]`  `jobs=HTTPJOB`  `RefreshRate=``30` |

O exemplo abaixo contém  valores obrigatórios referente ao *REST* com comentários.

**Configuração REST com comentários**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40 | `[General]`  `MAXSTRINGSIZE=``10`  `;``//MAXSTRINGSIZE: Essa chave é obrigatória com o valor mínimo de 10.`    `[HTTPV11]`  `Enable=``1`  `Sockets=HTTPREST`    `[HTTPREST]`  `Port=``8080`  `;``//Port: Porta que o REST irá utilizar para subir o serviço, pode ser alterada para qualquer outra porta.`  `IPsBind=`  `URIs=HTTPURI`  `Security=``1`  `;``//Security: O valor 1 é obrigatório.`    `[HTTPURI]`  `;``//HTTPURI: Mesmo valor da chave URIs, definido na linha 13.`  `URL=/rest`  `;``//URL: Path onde o rest irá subir, pode ser alterado.`  `PrepareIn=ALL`  `;``//PrepareIn: Chave que indica qual environment será preparado para o rest. ALL significa que deve ser preparado para atender todas as empresas. Caso você queira utilizar o REST com empresa 1 filial 01, por exemplo, inserir na chave 1,01.`  `Instances=``2``,``5``,``1``,``1`  `;``//Instances: Chave obrigatória, mais informações sobre configuração em http://tdn.totvs.com/display/tec/Instances . A configuração desta chave impacta diretamente no total de licenças consumidas pelo REST.`  `CORSEnable=``1`  `;``//CORSEnable: Essa chave é obrigatória e com o valor 1, caso contrário, o REST não aceitara as requisições dos apps.`  `AllowOrigin=*`  `;``//AllowOrigin: Essa chave limita os IP's que o REST do Protheus pode responder, deve conter o valor * (responder para qualquer ip) ou os ip's específicos onde a integração será realizada.`    `[HTTPJOB]`  `MAIN=HTTP_START`  `;``//MAIN: Cria um JOB que inicializa o servidor HTTP na inicialização do serviço.`  `ENVIRONMENT=environment`  `;``//ENVIRONMENT: Diz em qual environment(ambiente) o JOB será configurado.`    `[ONSTART]`  `jobs=HTTPJOB`  `;``//Jobs: Indica que o HTTPJOB será iniciado quando o serviço for iniciado.`  `RefreshRate=``30`  `;``//RefreshRate: Indica qual a taxa de atualização para reiniciar o JOB em caso de falha.` |

Configuração específica Meu **Coletor de Dados**

Exclusivamente para o aplicativo **Meu Coletor de Dados**, é necessário incluir a chave *MODULE* na seção *HTTPURI*:

|  |
| --- |
| `[HTTPURI]`  `Module=46` |

A configuração do *REST* do **Meu Coletor de Dados**não pode ser compartilhada com os demais aplicativos.

Após configurado, você pode iniciar o executável do **appserver** do *REST* em modo console e verificar se subiu corretamente através da mensagem no console:

*![](https://tdn.totvs.com/download/attachments/519719292/image2019-11-2_12-31-48.png?version=1&modificationDate=1572708708310&api=v2)*4 - Problemas mais comuns:

A falta de quaisquer uma das chaves no exemplo acima faz com que o *REST* não funcione como esperado. Abaixo listamos algumas:

* **SECURITY=0**

A chave **SECURITY** indica se o *REST* irá validar o usuário que está fazendo a chamada ou não, quando o valor está como 0, é desconsiderado o usuário enviado e o Protheus executa a chamada com o usuário administrador. Essa configuração traz grandes problemas de segurança para o Protheus e deve ser usado apenas em modo de desenvolvimento.  
             Os aplicativos também não funcionam corretamente, pois independente do usuário que fez o login, os dados e configurações de usuário exibidos dentro do aplicativo, são do usuário administrador.  
             Caso não haja a chave **SECURITY**, o valor dela é 1, o que esta correto também.

* **PrepareIn**

A chave prepareIn indica para quais empresas/filiais o *REST* irá subir uma thread. O Valor *ALL* usado no exemplo acima sobe uma *thread* para cada empresa e filial. Porém é consumida uma licença (TOTVS i) para cada thread. Caso o cliente não for utilizar todas as empresas, é possível subir apenas para as que ele deseja. Exemplo:  
PrepareIn=T1, D MG 01

* **CORSEnable**

           A chave **CORSEnable** indica se o *REST* do Protheus pode receber requisições fora do próprio servidor. Para utilização dos Apps, essa chave é obrigatória com o valor 1. Pois seu valor padrão é 0.

* **AllowOrigin**

          A chave AllowOrigin indica de quais ip's o *REST* pode responder. Quando o valor é **\*** (asterisco), indica que o Protheus pode responder para qualquer ip. Para utilização dos Apps, é possível limitar o acesso apenas para os ranges de ip's do Mingle listados abaixo:

* 138.219.88.0/24
* 189.125.78.128/25
* 187.94.48.0/20
* 189.89.32.0/20
* 181.41.160.0/19
* 3.14.95.150
* 3.14.95.34

3.14.95.255  
  
Essa configuração também deve ser feita no firewall da rede do cliente.  
  
5 - Validações   
Existem diferentes maneiras para verificar se o *REST* esta com a configuração correta.

5.1. Acesso pelo navegador

Acessa-lo pelo navegador, verificando esse acesso é possível saber se o *REST* está confirmado. Caso não seja possível acessá-lo, os aplicativos não irão funcionar.

Como testar:  
  
5.1.1 - Ambiente Local

Caso esteja fazendo o teste em ambiente local, siga os passos abaixo:

1. Descobrir o ip local:  
   é possível verificar rodando o comando ipconfig no command do windows:  
   ![](https://tdn.totvs.com/download/attachments/519719292/ipconfig.png?version=2&modificationDate=1572543024600&api=v2)
2. Verificar qual porta foi configurado o *rest*:  
   é a chave Port dentro da tag HTTPREST do arquivo appserver.ini.  ( linha 9 do exemplo na sessão 3)
3. Verificar qual a chave do rest:  
   é a chave URL dentro da tag HTTPURI do arquivo appserver.ini.  ( linha 15 do exemplo na sessão 3)

Em nosso exemplo, ficaria

<http://10.172.145.178:8080/rest>

Acessar o endereço pelo navegador.   
  
5.1. 2 - Ambiente do cliente

Caso o teste seja feito em um ambiente do cliente, será necessário orientá-lo a seguir os passos acima.

Após ter o endereço do *REST* em mãos, é recomendado testar de um outro aparelho que não seja o próprio servidor. Pode ser qualquer computador ou celular que esteja na mesma rede (do cliente).

Em ambos os casos, deverá ser aberta uma página semelhante a abaixo:

![](https://tdn.totvs.com/download/attachments/519719292/Screen%20Shot%202019-10-30%20at%2014.01.46.png?version=1&modificationDate=1572544306760&api=v2)  
  
6 - Exposição do endereço externo

Após ter seu *REST* configurado e funcional no ambiente, para alguns aplicativos, pode ser necessário expo-lo em IP fixo externo (para configuração do *ALIAS do Mingle*).

Esta configuração deve ser feita na infraestrutura de rede de sua empresa, e os IPs de origem do *Mingle* devem ser liberados para realizar conexões de entrada e saída.

**Importante:** Não é recomendável liberar o acesso à todas as requisições no firewall, pois pode gerar um problema de segurança.

**Exemplo de Utilização**

HTTP do Protheus, na versão 1.1, utilizando a seção HTTPV11.

Nesta seção, será indicado também qual seção será responsável por identificar os sockets que irão responder as requisições de entrada.

[HTTPV11] 

Enable=1 

Sockets=HTTPREST

Abaixo um exemplo de todas as seções configuradas:

[HTTPV11] 

Enable=1 

Sockets=HTTPREST

[HTTPREST] 

Port=8084

URIs=URIHTML

SECURITY=1

[URIHTML]

URL=/rest

PrepareIn=All

Instances=2,2

CORSEnable=1

AllowOrigin=\*

[ONSTART]

jobs=HTTPJOB

RefreshRate=30

[HTTPJOB]

MAIN=HTTP\_START

ENVIRONMENT=environment

 

Após executar todas as configurações, ao iniciar o appserver em modo console, deve ser possível visualizar a marcação do *REST*:

![](https://tdn.totvs.com/download/attachments/435098014/image2018-11-8_14-9-38.png?version=1&modificationDate=1541696951427&api=v2)

**Saiba Mais**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=185747842>
