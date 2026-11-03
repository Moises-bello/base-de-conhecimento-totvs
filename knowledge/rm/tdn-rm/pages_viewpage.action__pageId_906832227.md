---
content_hash: ca9a73230edaab47abc066c7ae21b1a86306114326ac51d8183955407f08b554
fetched_at: '2026-06-29T00:12:03.318779+00:00'
page_id: '906832227'
product: rm
source: tdn-rm
title: Integração Imagem Pixeon
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=906832227
version: 21
---

PrincipalIdConfiguracaoIdConfiguração

**CONFIGURAÇÃO**

Para configurar a integração pixeon para resultados de imagem é necessário seguir os passos abaixo:

1) Configure a unidade de atendimento que irá utilizar a integração em: Cadastros > Unidades de Atendimento > Aba Integrações > Opções: Diagnóstico por Imagem e Setores.

2) Será necessário habilitar a utilização da integração Pixeon em diretorio e configurar a visualização de imagem. Para isso vá em: Ambiente > Parâmetros > Gestão Hospitalar > Unidades Diagnóstico > Integrações > Diagnóstico por Imagem > Pixeon.

2.1) Parâmetros > Gestão Hospitalar:

2.1) Diagnóstico por Imagem > Pixeon:

PixeonIdExecução e Pasta

**EXECUTAR INTEGRAÇÃO:**

Essa integração utiliza arquivos em diretório, se faz necessário a execução do processamento do arquivo que pode ser feito de 2 formas:

1) De forma manual em: Utilitário > Processamento Manual de Arquivos de Integração.

2) De forma automática atravéz de jobs utilizando o processamento manual de arquivos de integração. Lei mais: ;

**ESTRUTURA DE PASTAS:**

* A pasta principal esta definida na configuração do host: ;
* A partir da pasta principal, é criado uma subpasta padrão, seguindo as regras por coligada: . Observação: Como o controle de arquivo da integração é única para todas as unidades de atendimento, é criado uma pasta única de filial com o código 0, Exemplo: **...\Saude\Coligada\_X\Filial\_0\Pixeon, onde X é o código da coligada**
* Após a pasta padrão, é criado outras subpasta, exemplos:
  + **...\Saude\Coligada\_X\Filial\_0\Pixeon\Requisicao\Resposta\Processado**
  + **...\Saude\Coligada\_X\Filial\_0\Pixeon\Relatorio\Resposta\Processado**

ArquivoIdArquivo

**ARQUIVOS:**

1) Envio (Totvs) de pedido de exame:

* + O Arquivo é gerado na subpasta **...\Saude\Coligada\_X\Filial\_0\Pixeon\Requisicao;**
  + Nome do arquivo segue o seguinte padrão:
    - código da coligada + número do pedido de exame + Sequencia exame + ".xml"
    - Exemplo: 11490061.xml
  + Conteúdo:

| *<?xml version="1.0" encoding="ISO-8859-1"?>* *<MWL\_ITEM>* *<WS\_UID>11490071</WS\_UID>* *<SITE>3ºA</SITE>* *<PATIENT\_ID>46594</PATIENT\_ID>* *<PATIENT\_NAME>JOSE BETSAIDA</PATIENT\_NAME>* *<PATIENT\_BIRTHDATE>19470611</PATIENT\_BIRTHDATE>* *<PATIENT\_SEX>M</PATIENT\_SEX>* *<PATIENT\_EMAIL\_CONSENT>Y</PATIENT\_EMAIL\_CONSENT>* *<PATIENT\_EMAIL>josebetsaida@[gmail.com](http://gmail.com)</PATIENT\_EMAIL>* *<PATIENT\_LOCATION>Andar: 3 - 308       </PATIENT\_LOCATION>* *<ACCESSION\_NUMBER>11490071</ACCESSION\_NUMBER>* *<REFERRING\_PHYSICIAN>MARIA JERUSALEM</REFERRING\_PHYSICIAN>* *<REFERRING\_PHYSICIAN\_IDENTIFICATION>55507</REFERRING\_PHYSICIAN\_IDENTIFICATION>* *<REQUESTING\_DEPARTMENT>3ºA</REQUESTING\_DEPARTMENT>* *<MODALITY>DX</MODALITY>* *<REQUESTED\_PROCEDURE\_DESCRIPTION>RX- ANTEBRACO D (AP - LATERAL) - 40803104</REQUESTED\_PROCEDURE\_DESCRIPTION>* *<SCHEDULED\_PERFORMING\_PHYSICIAN>* *</SCHEDULED\_PERFORMING\_PHYSICIAN>* *<SCHEDULED\_STATION\_AE\_TITLE>* *</SCHEDULED\_STATION\_AE\_TITLE>* *<SCHEDULED\_PROCEDURE\_STEP\_ID>2</SCHEDULED\_PROCEDURE\_STEP\_ID>* *<DATE>20250115</DATE>* *<TIME>102149</TIME>* *<REQUESTED\_PROCEDURE\_ID>30007</REQUESTED\_PROCEDURE\_ID>* *</MWL\_ITEM>* |
| --- |

2) Envio (Totvs) de cancelamento de pedido de exame:

* + O Arquivo é gerado na subpasta **...\Saude\Coligada\_X\Filial\_0\Pixeon\Requisicao;**
  + Nome do arquivo segue o seguinte padrão:
    - del + código da coligada + número do pedido de exame + Sequencia exame + ".xml"
    - Exemplo: del11490061.xml

* + Conteúdo:

| *<?xml version="1.0" encoding="ISO-8859-1"?>* *<MWL\_ITEM>* *<ACTION>DELETE</ACTION>* *<WS\_UID>11490061</WS\_UID>* *</MWL\_ITEM>* |
| --- |

3) Resposta (Pixeon) em XML de pedido de exame:

* + O Arquivo é gerado na subpasta **...\Saude\Coligada\_X\Filial\_0\Pixeon\Requisicao\Resposta;**
  + Nome do arquivo segue o seguinte padrão:
    - código da coligada + número do pedido de exame + Sequencia exame + "." + código do laudo + ".xml"
    - Exemplo: 11490061.40006.xml
  + Ao importar o arquivo xml, o sistema realiza o seguinte processo:
    - Atualiza o pedido de exame indicando o médico responsável;
    - Copia o arquivo para pasta **...\Saude\Coligada\_X\Filial\_0\Pixeon\Requisicao\Resposta\Processado;**
  + Conteúdo:

| <?xml version="1.0" encoding="ISO-8859-1"?> <report> <report\_id>40081</report\_id> <acession\_number>11490181</acession\_number> <patient\_id>46594</patient\_id> <patient\_name>*JOSE BETSAIDA*</patient\_name> <study\_date>20220714150000</study\_date> <study\_description>[object Object]</study\_description> <study\_modal>undefined</study\_modal> <referring\_physician/> <release\_date>20220714 160000</release\_date> <release\_doctor>MEDICO TOTVS</release\_doctor> <crm\_doctor>20</crm\_doctor> <uf\_doctor>MG</uf\_doctor> <report\_file\_path>C:\TOTVS\report\11490182.40081.pdf</report\_file\_path> <integration\_datetime>20220714170000</integration\_datetime> <final>true</final> </report>Conteúdo: |
| --- |

4) Resposta (Pixeon) em PDF (Laudo) de pedido de exame:

* + O Arquivo é gerado na subpasta **...\Saude\Coligada\_X\Filial\_0\Pixeon\Relatorio\Resposta;**
  + Nome do arquivo segue o seguinte padrão:
    - código da coligada + número do pedido de exame + Sequencia exame + "." + código do laudo + ".pdf"
    - Exemplo: 11490061.40006.pdf
  + Ao importar o arquivo de laudo, o sistema realiza o seguinte processo:
    - Salva o arquivo na tabela SZARQUIVO;
    - Copia o arquivo para pasta **...\Saude\Coligada\_X\Filial\_0\Pixeon\Relatorio\Resposta\Processado;**
    - Exclui o arquivo da pasta **...\Saude\Coligada\_X\Filial\_0\Pixeon\Relatorio\Resposta;**
    - Criar um arquivo XML de Resposta (**Item 5.**).

5) Resposta (Totvs) que o arquivo em PDF (laudo) foi importado:

* + O Arquivo é gerado na subpasta **...\Saude\Coligada\_X\Filial\_0\Pixeon\Relatorio;**
  + Nome do arquivo segue o seguinte padrão:
    - nome arquivo em PDF sem extenção PDF  + ".xml"
    - Exemplo: 11490061.40006.xml

* + Conteúdo:

| *<?xml version="1.0" encoding="ISO-8859-1"?> <REPORT>   <REPORT\_ID>40006</REPORT\_ID>   <ACCESSION\_NUMBER>11490061</ACCESSION\_NUMBER>   <INTEGRATION\_DATETIME>20250117 081412</INTEGRATION\_DATETIME>   <RESPONSE>SUCCESS</RESPONSE>   <MESSAGE>   </MESSAGE> </REPORT>* |
| --- |
