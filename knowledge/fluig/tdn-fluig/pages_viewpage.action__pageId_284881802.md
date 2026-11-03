---
content_hash: 5fffa5862b093cf19113431b3f5ad826b6b84f20969b088be2c1a119e2539806
fetched_at: '2026-06-28T21:35:25.385126+00:00'
page_id: '284881802'
product: fluig
source: tdn-fluig
title: Monitoramento de serviços da plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284881802
version: 21
---

Atenção

Esta página é destinada para atualizações 1.6.2 e superiores do TOTVS Fluig Plataforma.

# Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é explicar como obter informações de monitoramento de serviços da plataforma. Estas APIs permitem que clientes monitorem e realizem consultas de diversos relatórios referente a serviços consumidos pela plataforma.

# Pré-requisitos

---

Para que se tenha uma compreensão completa destas informações, alguns conhecimentos são considerados pré-requisitos, entre eles:

* Visão geral sobre a plataforma TOTVS Fluig

Atenção

Para acessar as APIs de **Monitoramento de Serviços**, deve-se realizar autenticação com um usuário administrador ou com o usuário "wcmadmin".

# Funcionamento

---

O módulo de monitoramento permite a consulta de uma série de relatórios referente a serviços em uso pelo fluig. Estas informações são úteis para monitorar desenvolvimentos sobre a plataforma para evoluí-los. O acesso aos relatórios pode ser feito através de API REST (que retorna um JSON) e via JMX.

## Balanceamento de carga e alta disponibilidade - Cluster

---

Em um ambiente de alta disponibilidade com , a autenticação do wcmadmin deve ser realizada através do endereço: [protocolo]://[endereço\_ip]:[porta]/portal/home?dologin. Em seguida acessar a URL: http://[servidor\_fluig]:[porta]/monitoring/api/v1/**monitors**/report.

Em ambientes com balanceamento de carga, o monitoramento deverá ser realizado em cada nó. Isso significa que, não é possível consultar em um nó e obter o resultado dos demais no mesmo retorno.

# Serviços monitorados

---

Os monitores podem ser observados através de duas consultas REST diferentes. Você pode consultar diretamente o monitoramento que desejar incluindo o parâmetro na URL. Abaixo são apresentados as APIs com a relação de nomes e parâmetros de todos os monitores e seus serviços monitorados.

## API monitors

---

Para acompanhar os serviços listados abaixo, altere a URL da plataforma no navegador pela apresentada a seguir. Os resultados apresentam o status atual dos serviços.

bash]]>

|  |  |  |
| --- | --- | --- |
| **GRUPO** | **PARÂMETRO** | **DESCRIÇÃO** |
| Analytics | ANALYTICS\_AVAIABILITY | Indica a disponibilidade do fluig Analytics (<http://analytics.fluig.com/>). |
| Cache | CACHE\_AVAIABILITY | Indica a disponibilidade do servidor de *cache*. |
| **Misc** | LICENSE\_SERVER\_AVAILABILITY | Indica se o servidor de licenças está disponível. |
| MAIL\_SERVER\_AVAILABILITY | Envia um e-mail de teste para [test@fluig-monitor.com](mailto:para%C2%A0test@fluig-monitor.com), para indicar a disponibilidade do serviço de e-mails. |
| OPEN\_OFFICE\_AVAILABILITY | Indica se o servidor do OpenOffice está ativo. |
| SOLR\_SERVER\_AVAILABILITY | Indica se o servidor do Solr está ativo. |
| MS\_OFFICE\_AVAILABILITY | Indica se o Office está instalado e ativo no servidor. |
| VIEWER\_AVAILABILITY | Indica se o Viewer está configurado. |
| Realtime | REAL\_TIME\_AVAILABILITY | Retorna se o NodeJS encontra acessível. |

## API statistics

---

Para acompanhar os serviços listados abaixo, altere a URL da plataforma no navegador pela apresentada a seguir. É importante mencionar que os resultados não são monitorados em tempo real e sim checados a cada 5 minutos.

bash]]>

|  |  |  |
| --- | --- | --- |
| **GRUPO** | **PARÂMETRO** | **DESCRIÇÃO** |
| Database | DATA\_SOURCE\_FLUIGDS | Retorna o tamanho do *pool* de conexões para o *datasource* transacionado. |
| DATA\_SOURCE\_FLUIGDSRO | Retorna o tamanho do *pool* de conexões para o *datasource* somente de leitura sem transação. |
| DATABASE\_SIZE | Indica o tamanho total da base de dados utilizada pela plataforma. |
| DATABASE\_TRAFFIC | Indica o tráfego de envio e de recebimento da base de dados utilizada pela plataforma. Só para MySQL. |
| DATABASE\_INFO | Retorna dados sobre o nome e versão do banco de dados e do driver de conexão e versão do drive. |
| Filesystem | ARTIFACTS\_APPS\_DIR | Retorna a relação de arquivos implantados no [diretório\_instalação]/appserver/apps com suas respectivas Hash MD5. |
| LOG\_DIR\_SIZE\_MONITOR | Indica o tamanho do diretório de logs do servidor. |
| ROOT\_FILE\_SYSTEMS | Retorna as raízes de montagem do *filesystem* com seus respectivos tamanhos em bytes. |
| TEMPLATE\_DIR\_SIZE | Indica o tamanho do diretório de templates. |
| VOLUME\_DIR\_SIZE | Indica o tamanho do diretório de volume. |
| TEMPORARY\_DIR\_SIZE | Indica o tamanho do diretório temporário do servidor. |
| Atenção Os parâmetros LOG\_DIR\_SIZE\_MONITOR,TEMPLATE\_DIR\_SIZE, VOLUME\_DIR\_SIZE e TEMPORARY\_DIR\_SIZE foram depreciados na **atualização 1.6.4**. | |
| JVM | RUNTIME | Retorna a hora de início e o tempo que está em execução. |
| THREADING | Retorna o número de threads em execução, pico e quantidade iniciadas. |
| Memory | DETAILED\_MEMORY | Retorna a relação de memórias da JVM, com tipo, total alocado, total comprometido e máximo. |
| MEMORY | Retorna o total de memória *heap* e *non-heap* alocados. |
| **Cache** | CACHE\_CONFIGURATION | Indica se a configuração do endereço do servidor de cache está definida para algo diferente de "LOCAL\_MAP". |
| Misc | EXTERNAL\_CONVERTER | Indica se conversor interno de documentos está ativo. |
| Users | CONNECTED\_USERS | Indica o número de **sessões** de usuários ativas no portal. Este número **não** corresponde necessariamente ao número de usuários autenticados na plataforma. |

Atenção

Sempre que um monitor retornar ***FAILURE*** é possível acessar o arquivo server.log, armazenado em [diretório\_instalação]\appserver\standalone\log (a partir da **2.0**) ou [diretório\_instalação]\appserver\domain\servers\fluig1\log (**1.6 até 1.8.2**)*,* para obter informações detalhadas do erro ocorrido.

# Acesso REST

---

Para acessar os serviços via interface REST existem duas formas:

| Método | URL | Explicação |
| --- | --- | --- |
| GET | http://<host>/monitoring/api/v1/**monitors**/report | Retorna o relatório consolidado de todos os monitores citado acima, sem uso de parâmetros. |
| http://<host>/monitoring/api/v1/**statistics**/report |
| GET | http://<host>/monitoring/api/v1/**monitors**/report/[PARÂMETRO] | Retorna o relatório para um recurso em específico. O parâmetro deve ser escrito em maiúsculo. |
| http://<host>/monitoring/api/v1/**statistics**/report/[PARÂMETRO] |

Onde:

* [PARÂMETRO] = Nome do monitoramento.
* Os retornos sempre são *Strings*.

Acesso RESTExemplo de consulta consolidada

**Figura 1 - Exemplo de consulta consolidada**

Onde:

* **FAILURE**: Falha na resposta do serviço;
* **NONE**: Não foi utilizado até o momento;
* **OK**: Em funcionamento e/ou ativado.

Exemplo de consulta parametrizada

**Figura 2 - Exemplo de consulta parametrizada**
