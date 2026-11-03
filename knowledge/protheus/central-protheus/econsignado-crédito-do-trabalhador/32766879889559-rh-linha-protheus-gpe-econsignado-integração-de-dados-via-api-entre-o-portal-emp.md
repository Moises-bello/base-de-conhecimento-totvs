---
article_id: 32766879889559
category: eConsignado (Crédito do Trabalhador)
content_hash: d37a783309de27c86bfa2e16d929d89a5b1bc46ab09c2a6b49ed3f3d5f300297
fetched_at: '2026-06-28T22:43:07.290239+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - eConsignado - Integração de dados via API entre
  o Portal Emprega Brasil e Protheus
type: support-article
updated_at: '2026-06-10T19:49:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32766879889559-RH-Linha-Protheus-GPE-eConsignado-Integra%C3%A7%C3%A3o-de-dados-via-API-entre-o-Portal-Emprega-Brasil-e-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32766893059863) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Funcionalidade para importação de dados do eConsignado via API/ WebService direto do Portal Emprega Brasil?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) GPE - Gestão de Pessoal - A partir da versão 12.1.2310  
  
**Solução**  
  
Os empréstimos serão buscados diretamente no **webservice** do **governo**, eliminando a necessidade de *download* dos arquivos.

**Pré-Requisitos**

Ambiente\*\* atualizado

* **SIGAGPE**: Fonte **GPEM815.APP**, no repositório, deve ter data igual ou superior a 07/10/2025.
  + <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO_CONTINUA.ZIP>
* **SIGATAF**atualizado e configurado para o eSocial
  + Fonte **WSTAFCONSIGNADO.PRW** deve possuir data igual ou superior a 16/09/2025.
    - <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/TAF_EXPEDICAO_CONTINUA.ZIP>
  + **RH.TAF.WS.WSTAFCREDTRAB.TLPP** com data igual ou superior a 11/03/2026
    - 12.1.2310:<https://r.totvs.io/p/1243307> ; **SOMENTE PARA CLIENTES COM GARANTIA ESTENDIDA**  
      12.1.2410:<https://r.totvs.io/p/1243305> ;   
      12.1.2510:<https://r.totvs.io/p/1243306> ;
* **SIGATSS** atualizado, fonte **TSSWSCONSIGNADO.PRW** deve possuir data igual ou superior a 30/10/2025.
  + <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/TSS_EXPEDICAO_CONTINUA.ZIP>

\*\*Caso utilize **mais de um RPO** (dedicados separadamente para RH, TAF, TSS etc.), as atualizações devem ser feitas em **todos eles**.

Configurações

* [**Web Service REST** - Consulta Crédito do Trabalhador c](https://tdn.totvs.com/pages/viewpage.action?pageId=983803616)onfigurado
* Job **TAF\_CFGJOB** habilitado no appserver.ini no serviço de todas as aplicações/ *slaves* (para ambientes que **não** utilizam o SIGAGPE - MV\_RHTAF = .F.).
  + Caso utilizem o SIGAGPE e o **MV\_RHTAF = .T.**, **não é necessário** cadastrar a chave **T**AF\_CFGJOB no appserver.ini no serviço das aplicações

**Exemplo**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | `[TAF_CFGJOB]`  `MAIN=TAF_CFGJOB`  `Instances=5,30,5,1`  `PrepareIn=T1`  `Environment=P27D-1`  `RefreshRate=120`    `[OnStart]`  `JOBS=TAF_CFGJOB`  `RefreshRate=120` |

|  |
| --- |
| **Atenção!**  Chave `PrepareIn=` deve conter o código do grupo de empresa que consta na SYS\_COMPANY, campo  M0\_CODIGO. Chave `Environment=` deve constar o nome do ambiente. |

**Configurações Gerais**

As verbas utilizadas para **importação** devem ser previamente cadastradas como segue abaixo:

**Tipo (RV\_TIPOCOD)** = 2 (Desconto);  
**Natureza (RV\_NATUREZ)** = 9253 (Empréstimo eConsignado - Desconto);  
**Código de Incidência do FGTS** (RV\_INCFGTS) = 31 (Desconto eConsignado).  
[RH - Linha Protheus - GPE - Como cadastrar as verbas de desconto do eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31149947210519-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-desconto-do-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador)

Para o eSocial, se faz necessário utilizar **uma verba para cada empréstimo** ativo. Por isso, foi disponibilizada, em **Manutenção de Tabelas**, a tabela **S154**, onde devem ser informadas as verbas com a configuração do eConsignado.  
  
![](https://tdn.totvs.com/download/attachments/944703898/image-2025-6-20_18-30-37.png?version=1&modificationDate=1750455037830&api=v2)  
  
Ter a rotina **Painel de Importação** (GPEM815A) incluída no menu do **SiGAGPE**.  
[RH - Linha Protheus - GPE - Como incluir a rotina Painel de Importação do arquivo eConsignado GPEM815A no menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34817817809943-RH-Linha-Protheus-GPE-Como-incluir-a-rotina-Painel-de-Importa%C3%A7%C3%A3o-do-arquivo-eConsignado-GPEM815A-no-menu)

**Passo a passo:**

1. Selecione a opção **Sincronização via webservice**;
2. Preencha os parâmetros **Empregador**, **Competência** e **Forçar nova consulta no Governo**;
3. Clique no botão **Buscar Empréstimos**;
4. Aguarde os empréstimos serem carregados, em seguida clique em **Confirmar Importação**;

![image-2025-10-14_10-16-24.png](https://tdn.totvs.com/download/attachments/944703898/image-2025-10-14_10-16-24.png?version=1&modificationDate=1760447785570&api=v2)

O resultado do processamento será apresentado:

![image-2025-10-14_10-30-3.png](https://tdn.totvs.com/download/attachments/944703898/image-2025-10-14_10-30-3.png?version=1&modificationDate=1760448604337&api=v2)  
  
**Importante**  
Com o eSocial configurado como **homologação**, a API do governo **não retornará empréstimos reais**, apenas dados **fictícios**.  
  
Na rotina só irá demonstrar as filiais definidas como **Matriz** no TAF  (isso pode ser identificado na tabela **C1E** - campo **C1E\_MATRIZ = .T.**).   
Mas os funcionários das outras filiais devem aparecer ao selecionar todas as filiais disponíveis na rotina.    
   
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Como consultar o Historico de Importação RUO Econsignado (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32579319541271-RH-Linha-Protheus-GPE-Como-consultar-o-Historico-de-Importa%C3%A7%C3%A3o-RUO-Econsignado-MP1-292-2025)  
[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)

<https://tdn.totvs.com/pages/viewpage.action?pageId=1050287701>   
Manual [Crédito do Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=944703898)
