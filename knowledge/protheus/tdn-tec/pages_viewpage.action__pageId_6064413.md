---
content_hash: ca7e42054623eace9b69a787bccb199d5cfcc8d52c6e9fe7ef7dd301088062ef
fetched_at: '2026-07-02T19:24:26.713820+00:00'
page_id: '6064413'
product: protheus
source: tdn-tec
title: Como fazer para realizar a atualização para ACE 6.11
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6064413
version: 3
---

BLOCK

Como fazer para realizar a atualização para ACE 6.11

## Como fazer para realizar a atualização para ACE 6.11

O ACE - *Advantage Client Engine* é utilizado para abertura de arquivos locais ISAM padrão DBF.

Desta forma, aconselhamos a atualização do ACE (ADS local) para 6.11 ou superior em todas a versões do ERP.

As principais vantagens são:

* Melhor performance
* Melhora das mensagens de erro
* Suporte para índices formados por chaves longas
* Sem limite de 255 tabelas por conexão
* Aumento do limite de *threads* por servidor para evitar o erro *TLS Initialization failed* que pode travar ou derrubar a servidor do sistema ERP.  
   A janela com a mensagem *TLS Initialization failed* só é visualizada em modo console. Caso contrário (serviço), o servidor fica travado.

| Importante |
| --- |
| Essa atualização só pode ser realizada se o banco de dados for ADS - *Advantage Database Server* e a versão igual ou superior a 6.11, embora o erro *TLS Initialization failed* não exista quando LocalFiles=ADSServer não depende da versão do mesmo. |

### Como fazer para atualizar

1. Descompacte o arquivo ACE\_6.11.zip e copie todos os arquivos para o diretório de instalação do TOTVS | Application Server.  
    Exemplo: C:\SistemaERP\bin\appserver

   | Observação |
   | --- |
   | Há uma alteração, no arquivo ads.ini, para suporte com mais de 50 conexões para a versão 6.11. Portanto, não esqueça de copiar esse arquivo. |

   Realizada a descompactação, não é necessário configurar o arquivo .ini do TOTVS | Application Server. Caso exista alguma configuração, a mesma será ignorada, pois o que define a versão utilizada são os arquivos que estão no diretório do TOTVS | Application Server.  
      
    Se o TOTVS | Application Server for executado em modo console, a mensagem **Using ACE32.dll - Versão 6.11** será apresentada.
