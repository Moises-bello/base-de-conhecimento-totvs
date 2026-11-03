---
article_id: 360028365571
category: Materiais - Compras (SIGACOM)
content_hash: 1898cda85bc9a802fdbf6df1511d8ab209ab2ab5e026f0047267d5303f3a1b63
fetched_at: '2026-06-28T22:41:17.329112+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - DOCUMENTAÇÃO TOTVS
  COLABORAÇÃO 2.0
type: support-article
updated_at: '2022-05-16T21:40:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028365571-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-DOCUMENTA%C3%87%C3%83O-TOTVS-COLABORA%C3%87%C3%83O-2-0
---

Atualmente, o TOTVS Colaboração utiliza o TSS (TOTVS® Service SOA) para realização do tráfego dos documentos entre o ERP Microsiga Protheus® e a plataforma NeoGrid por meio do emprego da tecnologia Web Service. Nesta versão do TOTVS Colaboração, denominada 2.0, foi empregado o uso do **Client** **NeoGrid**- que será o responsável pelo tráfego dos arquivos gerados pelo Microsiga Protheus® - e dos sistemas da NeoGrid em substituição a utilização do TSS.

A proposta do Client NeoGrid é facilitar e agilizar o processo de transmissão dos documentos fiscais, pois trabalha completamente integrado aos serviços disponíveis no TOTVS Colaboração no que se refere à plataforma NeoGrid. Basicamente, trata-se de um software que deve ser instalado no servidor de aplicação ERP, capaz de monitorar um diretório de saída de documentos alimentado pelo ERP Microsiga Protheus® e de realizar a transmissão para os serviços disponíveis do TOTVS Colaboração sob plataforma NeoGrid. Este software também tem como finalidade verificar junto a plataforma NeoGrid a existência de documentos pendentes de retorno, e em caso afirmativo, atualizar um diretório de entrada para leitura do ERP Microsiga Protheus.

Para melhor entendimento, seguem abaixo as etapas do processo padrão de envio de arquivos via TOTVS Colaboração 2.0:

**Envio**

1. O Protheus® gera o arquivo com extensão \*.xml no diretório de saída do Client NeoGrid.
2. O Client NeoGrid faz uma busca no diretório de saída e envia o arquivo para os serviços web do TOTVS Colaboração na NeoGrid.
3. Após concluir o envio, o arquivo do diretório de saída é movido para o diretório de documentos enviados.

**Recebimento**

1. O Client NeoGrid analisa, em um determinado intervalo de tempo, a existência de documentos disponíveis para recebimento. Em caso afirmativo, será gravado no diretório de entrada o arquivo .xml correspondente ao documento de entrada.
2. Após esta gravação, o ERP Microsiga Protheus® executa, via Schedule de importação, a leitura do arquivo e a sua importação para o sistema.
3. O ERP Microsiga Protheus® executa também, via Schedule de importação, a movimentação do arquivo lido (que está no diretório de entrada) para o diretório de arquivos lidos/processados.

Lista de documentos

Abaixo está a lista de documentos disponíveis no produto TOTVS Colaboração 2.0, referente a linha Microsiga Protheus®.

|  |  |  |
| --- | --- | --- |
| **Documento** | **Tipo Requisição** | **Descrição** |
| **NF-e** | Emissão | Emissão, Cancelamento e Inutilização. |
| **NF-e – CC-e** | Emissão | Envio do evento do CC-e |
| **MD-e** | Emissão | Envio da Manifestação do destinatário |
| **NFS-e** | Emissão | Emissão e Cancelamento. |
| **MDF-e** | Emissão | Emissão, Cancelamento e Encerramento. |
| **CT-e** | Emissão | Emissão, Cancelamento e Inutilização. |
| **EDI - Pedido** | Recebimento | Recebimento de Pedido de compra, para geração do pedido de venda e programação de entrega. |

## Procedimento para Implementação

* Tabela CKP – Parâmetros TOTVS Colaboração

|  |  |
| --- | --- |
| **Arquivo** | CKP |
| **Nome** | Parâmetros TOTVS Colaboração |
| **Mod. Ac. Filial** | Exclusivo |
| **Mod. Ac. Unidade** | Exclusivo |
| **Mod. Ac. Empresa** | Exclusivo |
| **Chave Única** | CKP\_FILIAL+CKP\_PARAM |

* Tabela CKQ – Monitor de documentos TOTVS Colaboração

|  |  |
| --- | --- |
| **Arquivo** | CKQ |
| **Nome** | Controle de Arq. TOTVS Colab. |
| **Mod. Ac. Filial** | Exclusivo |
| **Mod. Ac. Unidade** | Exclusivo |
| **Mod. Ac. Empresa** | Exclusivo |
| **Chave Única** | CKQ\_FILIAL+CKQ\_MODELO+CKQ\_TP\_MOV+CKQ\_IDERP |

* Tabela CKO – Controle de arquivos TOTVS Colaboração

|  |  |
| --- | --- |
| **Arquivo** | CKO |
| **Nome Arq.(X2\_NOME)\*** | CKOCOL |
| **Nome** | Controle de Arq. TOTVS Colab. |
| **Mod. Ac. Filial** | Exclusivo |
| **Mod. Ac. Unidade** | Exclusivo |
| **Mod. Ac. Empresa** | Exclusivo |
| **Chave Única** | CKQ\_FILIAL+CKQ\_MODELO+CKQ\_TP\_MOV+CKQ\_IDERP |

**Importante**

A tabela CKO deve ser única para todas as empresas do sistema, desta forma o campo **X2\_ARQUIVO** deve estar preenchido **obrigatoriamente** com o conteúdo **CKOCOL**, para que a importação de arquivos funcione corretamente.

![](http://tdn.totvs.com/download/attachments/187534008/image2015-7-1%2015%3A47%3A5.png?version=1&modificationDate=1435776438000&api=v2)

1. Criação de **Campos** no arquivo**SX3 – Campos****:**

* Tabela CKP – Parâmetros TOTVS Colaboração

|  |  |
| --- | --- |
| **Campo** | CKP\_FILIAL |
| **Tipo** | C |
| **Tamanho** | 2 |
| **Descrição** | Filial do sistema |
| **Título** | Filial |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Não |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Grupo de Campo** | 033 (Tamanho da Filial) |
| **Help de Campo** | Filial do Sistema. |

|  |  |
| --- | --- |
| **Campo** | CKP\_PARAM |
| **Tipo** | C |
| **Tamanho** | 10 |
| **Descrição** | Parâmetro do TOTVS Colab. |
| **Título** | Parâmetro |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Nome do parâmetro utilizado para as rotinas do TOTVS Colaboração. |

|  |  |
| --- | --- |
| **Campo** | CKP\_VALOR |
| **Tipo** | C |
| **Tamanho** | 100 |
| **Descrição** | Conteúdo do Parâmetro |
| **Título** | Conteúdo |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Conteúdo do parâmetro utilizado para as rotinas do TOTVS Colaboração. |

|  |  |
| --- | --- |
| **Campo** | CKP\_DESCRI |
| **Tipo** | C |
| **Tamanho** | 120 |
| **Descrição** | Descrição do parâmetro |
| **Título** | Descrição |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Descrição do parâmetro para auxílio no entendimento do funcionamento do parâmetro. |

* Tabela CKQ – Monitor de Documentos TOTVS Colaboração

|  |  |
| --- | --- |
| **Campo** | CKQ\_FILIAL |
| **Tipo** | C |
| **Tamanho** | 2 |
| **Descrição** | Filial do sistema |
| **Título** | Filial |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Não |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Grupo de Campo** | 033 (Tamanho da Filial) |
| **Help de Campo** | Filial do Sistema. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_MODELO |
| **Tipo** | C |
| **Tamanho** | 3 |
| **Descrição** | Modelo do documento |
| **Título** | Modelo |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Sim |
| **Obrigatório** | Não |
| **Help de Campo** | Modelo do documento. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_TP\_MOV |
| **Tipo** | C |
| **Tamanho** | 1 |
| **Descrição** | Tipo do Movimento |
| **Título** | Tp. Mov |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Tipo do movimento: 1 - Emissão e 2 - Recebimento. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_CODEDI |
| **Tipo** | C |
| **Tamanho** | 3 |
| **Descrição** | Código do EDI |
| **Título** | Código EDI |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Código do EDI, este código se refere ao tipo de documento/ transação que a NeoGrid aguarda receber. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_ARQUIV |
| **Tipo** | C |
| **Tamanho** | 30 |
| **Descrição** | Nome do arquivo gerado |
| **Título** | Nome Arquivo |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Sim |
| **Obrigatório** | Não |
| **Help de Campo** | Nome do arquivo gerado no diretório, para transmissão pelo Integrador da NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_STATUS |
| **Tipo** | C |
| **Tamanho** | 2 |
| **Descrição** | Status do Documento |
| **Título** | Status Doc. |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Nome do arquivo gerado no diretório, para transmissão pelo Integrador da NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_DESSTA |
| **Tipo** | C |
| **Tamanho** | 40 |
| **Descrição** | Descrição do STATUS |
| **Título** | Desc. STATUS |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Sim |
| **Obrigatório** | Não |
| **Help de Campo** | Descrição sobre o STATUS do documento. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_IDERP |
| **Tipo** | C |
| **Tamanho** | 50 |
| **Descrição** | ID gerado pelo ERP |
| **Título** | ID ERP |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | ID gerado pelo ERP, utilizado para manter as funcionalidades anteriores do ERP sem o uso do novo TOTVS Colaboração. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_SERIE |
| **Tipo** | C |
| **Tamanho** | 3 |
| **Descrição** | Série do documento |
| **Título** | Série |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Sim |
| **Obrigatório** | Não |
| **Help de Campo** | Série do documento, gerado somente para documentos que tenham esta informação. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_NUMERO |
| **Tipo** | C |
| **Tamanho** | 9 |
| **Descrição** | Número do documento |
| **Título** | Numero |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Sim |
| **Grupo de Campo** | 018 (Tamanho Documento Entrada e saída) |
| **Obrigatório** | Não |
| **Help de Campo** | Número do documento, gerado somente para documentos que tenham esta informação. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_DT\_GER |
| **Tipo** | D |
| **Tamanho** | 8 |
| **Descrição** | Data de Geração do Arquivo |
| **Título** | Data Geração |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Data de geração do arquivo no diretório para ser lido pelo integrador NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_HR\_GER |
| **Tipo** | C |
| **Tamanho** | 8 |
| **Descrição** | Hora da Geração |
| **Título** | Hora Geração |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Hora de geração do arquivo no diretório para ser lido pelo integrador NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_AMBIEN |
| **Tipo** | C |
| **Tamanho** | 1 |
| **Descrição** | Ambiente |
| **Título** | Ambiente |
| ***Validação*** | Pertence(‘12’) |
| **Contexto** | Real |
| **Opções** | 1=Producao;2=Ambiente |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Indica ambiente em que documento foi enviado. |

* Tabela CKO – Controle de Arquivos TOTVS Colaboração

|  |  |
| --- | --- |
| **Campo** | CKO\_FILIAL |
| **Tipo** | C |
| **Tamanho** | 2 |
| **Descrição** | Filial do sistema |
| **Título** | Filial |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Não |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Grupo de Campo** | 033 (Tamanho da Filial) |
| **Help de Campo** | Filial do Sistema. |

|  |  |
| --- | --- |
| **Campo** | CKO\_ARQUIV |
| **Tipo** | C |
| **Tamanho** | 30 |
| **Descrição** | Nome do arquivo gerado |
| **Título** | Nome arquivo |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Sim |
| **Obrigatório** | Não |
| **Help de Campo** | Nome do arquivo gerado no diretório, para transmissão pelo Integrador da NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKO\_STATUS |
| **Tipo** | C |
| **Tamanho** | 2 |
| **Descrição** | Status do Arquivo |
| **Título** | Status Arq. |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | STATUS do arquivo gerado. |

|  |  |
| --- | --- |
| **Campo** | CKO\_DESSTA |
| **Tipo** | C |
| **Tamanho** | 40 |
| **Descrição** | Descrição do STATUS |
| **Título** | Desc. STATUS |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Sim |
| **Obrigatório** | Não |
| **Help de Campo** | Descrição sobre o STATUS do documento. |

|  |  |
| --- | --- |
| **Campo** | CKO\_XMLENV |
| **Tipo** | M |
| **Tamanho** | 10 |
| **Descrição** | XML de envio para NeoGrid |
| **Título** | XML Envio |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | XML criado pelo ERP e gravado no diretório OUT do integrador da NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKO\_XMLRET |
| **Tipo** | M |
| **Tamanho** | 10 |
| **Descrição** | XML de retorno da NeoGrid |
| **Título** | XML Retorno |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | XML importado do diretório IN do integrador da NeoGrid, XML com a resposta do XML gravado no campo CKO\_XMLENV. |

|  |  |
| --- | --- |
| **Campo** | CKO\_DT\_GER |
| **Tipo** | D |
| **Tamanho** | 8 |
| **Descrição** | Data de Geração do Arquivo |
| **Título** | Data Geração |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Data de geração do arquivo no diretório para ser lido pelo integrador NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKO\_HR\_GER |
| **Tipo** | C |
| **Tamanho** | 8 |
| **Descrição** | Hora da Geração |
| **Título** | Hora Geração |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Hora de geração do arquivo no diretório para ser lido pelo integrador NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKO\_DT\_RET |
| **Tipo** | D |
| **Tamanho** | 8 |
| **Descrição** | Data de Retorno do Arquivo |
| **Título** | Data Retorno |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Data da gravação do arquivo no diretório de arquivos de retorno pelo integrador da NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKO\_HR\_RET |
| **Tipo** | C |
| **Tamanho** | 8 |
| **Descrição** | Hora de Retorno do Arquivo |
| **Título** | Hora Retorno |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Hora da gravação do arquivo no diretório de arquivos de retorno pelo integrador da NeoGrid. |

|  |  |
| --- | --- |
| **Campo** | CKO\_IDERP |
| **Tipo** | C |
| **Tamanho** | 50 |
| **Descrição** | ID gerado pelo ERP |
| **Título** | ID ERP |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | ID gerado pelo ERP, utilizado para manter as funcionalidades anteriores do ERP sem o uso do novo TOTVS Colaboração. |

|  |  |
| --- | --- |
| **Campo** | CKO\_TP\_MOV |
| **Tipo** | C |
| **Tamanho** | 1 |
| **Descrição** | Tipo do Movimento |
| **Título** | Tp. Mov |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Tipo do movimento: 1 - Emissão e 2 - Recebimento. |

|  |  |
| --- | --- |
| **Campo** | CKO\_FLAG |
| **Tipo** | C |
| **Tamanho** | 1 |
| **Descrição** | Flag de exportação |
| **Título** | Flag Exp. |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Flag de exportação utilizado para os recebimentos de documentos. Onde 1 - Exportado e 2 - Não Exportado. |

|  |  |
| --- | --- |
| **Campo** | CKQ\_CODEDI |
| **Tipo** | C |
| **Tamanho** | 3 |
| **Descrição** | Código do EDI NeoGrid |
| **Título** | Código EDI |
| ***Picture*** | @! |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Código do EDI, este código se refere ao tipo de documento/ transação que a NeoGrid aguarda receber. |

|  |  |
| --- | --- |
| **Campo** | CKO\_DT\_IMP |
| **Tipo** | D |
| **Tamanho** | 8 |
| **Descrição** | Data da Importação Arquivo |
| **Título** | Data Import. |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Data de leitura do arquivo no diretório de arquivos de retorno do integrador da NeoGrid pelo Schedule de leitura. |

|  |  |
| --- | --- |
| **Campo** | CKO\_HR\_IMP |
| **Tipo** | C |
| **Tamanho** | 8 |
| **Descrição** | Hora de Importação Arq. |
| **Título** | Hora Import. |
| **Contexto** | Real |
| **Propriedade** | Alterar |
| **Usado** | Sim |
| ***Browse*** | Não |
| **Obrigatório** | Não |
| **Help de Campo** | Hora de leitura do arquivo no diretório de arquivos de retorno do integrador da NeoGrid pelo Schedule de leitura. |

1. Criação de **Índices** no arquivo **SIX – Índices**:

* Tabela CKP – Parâmetros TOTVS Colaboração

|  |  |
| --- | --- |
| **Índice** | CKP |
| **Ordem** | 1 |
| **Chave** | CKP\_FILIAL + CKP\_PARAM |
| **Descrição** | Filial + Parâmetro |
| **Proprietário** | S |

* Tabela CKQ – Monitor de Documentos TOTVS Colaboração

|  |  |
| --- | --- |
| **Índice** | CKQ |
| **Ordem** | 1 |
| **Chave** | CKQ\_FILIAL+CKQ\_MODELO+CKQ\_TP\_MOV+CKQ\_IDERP |
| **Descrição** | Filial + Modelo + Tipo Movimento + ID do ERP |
| **Proprietário** | S |

|  |  |
| --- | --- |
| **Índice** | CKQ |
| **Ordem** | 2 |
| **Chave** | CKQ\_FILIAL+CKQ\_MODELO+CKQ\_TP\_MOV+CKQ\_SERIE+CKQ\_NUMERO |
| **Descrição** | Filial + Modelo + Tipo Movimento + Série +  Numero |
| **Proprietário** | S |

|  |  |
| --- | --- |
| **Índice** | CKQ |
| **Ordem** | 3 |
| **Chave** | CKQ\_FILIAL+CKQ\_MODELO+CKQ\_TP\_MOV+CKQ\_STATUS |
| **Descrição** | Filial + Modelo + Tipo Movimento + Status |
| **Proprietário** | S |

|  |  |
| --- | --- |
| **Índice** | CKQ |
| **Ordem** | 3 |
| **Chave** | CKQ\_FILIAL+CKQ\_MODELO+CKQ\_TP\_MOV+CKQ\_STATUS |
| **Descrição** | Filial + Modelo + Tipo Movimento + Status |
| **Proprietário** | S |
| **Índice** | CKQ |
| **Ordem** | 4 |
| **Chave** | CKQ\_FILIAL+CKQ\_MODELO+CKQ\_TP\_MOV+CKQ\_CODEDI |
| **Descrição** | Filial + Modelo + Tipo Movimento + Código EDI |
| **Proprietário** | S |

|  |  |
| --- | --- |
| **Índice** | CKQ |
| **Ordem** | 5 |
| **Chave** | CKQ\_FILIAL+DTOS(CKQ\_DT\_GER)+CKQ\_HR\_GER |
| **Descrição** | Filial + Modelo + Data de Geração + Hora da geração |
| **Proprietário** | S |

* Tabela CKO - Controle de arquivos TOTVS Colaboração

|  |  |
| --- | --- |
| **Índice** | CKO |
| **Ordem** | 1 |
| **Chave** | CKO\_ARQUIV |
| **Descrição** | Arquivo |
| **Proprietário** | S |

|  |  |
| --- | --- |
| **Índice** | CKO |
| **Ordem** | 2 |
| **Chave** | CKO\_ARQUIV+CKO\_TP\_MOV+CKO\_FLAG |
| **Descrição** | Arquivo + Tipo Movimento + Flag de retorno |
| **Proprietário** | S |

|  |  |
| --- | --- |
| **Índice** | CKO |
| **Ordem** | 3 |
| **Chave** | CKO\_IDERP+DTOS(CKO\_DT\_GER) |
| **Descrição** | ID do ERP + Data de geração |
| **Proprietário** | S |

|  |  |
| --- | --- |
| **Índice** | CKO |
| **Ordem** | 4 |
| **Chave** | CKO\_CODEDI+CKO\_FLAG+DTOS(CKO\_DT\_RET) |
| **Descrição** | ID do ERP + Flag de retorno +Data de retorno |
| **Proprietário** | S |

**Importante**

O tamanho dos campos que possuem grupo pode variar conforme o ambiente em uso.

## Procedimento para Configuração

### CONFIGURAÇÃO DE PARÂMETROS

1. No **Configurador (SIGACFG)** acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Configure o(s) parâmetro(s) a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| Nome | MV\_TCNEW |
| Tipo | C |
| Cont. Por. | 0 |
| Descrição | Documentos que utilizam o novo modelo TOTVS Colab. Onde:0-todos,1-NFe,2-CTe,3-NFSe,4-MDe,5-MDfe,6-Recebimento. |

**Importante**

O conteúdo deste parâmetro deve ser informado separado pelo caractere de vírgula (,), para que seja possível informar a utilização de mais de um tipo de documento. **Exemplo:** Será utilizado apenas NF-e e CT-e, o conteúdo informado será: **1,2.**

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| Nome | MV\_NGOUT |
| Tipo | C |
| Descrição | Indicar o caminho do diretório dentro do ROOTPATH do Protheus onde será gravado os arquivos a serem enviados para NeoGrid. Ex:'\NeoGrid\OUT' |

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| Nome | MV\_NGINN |
| Tipo | C |
| Descrição | Indicar o caminho do diretório dentro do ROOTPATH do Protheus onde será lido os arquivos de retorno recebidos da NeoGrid. Ex:'\NeoGrid\IN' |

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| Nome | MV\_NGLIDOS |
| Tipo | C |
| Descrição | Indicar o caminho do diretório dentro do ROOTPATH do Protheus onde será armazenado os arquivos após lidos e processados. Ex:\NeoGrid\Lidos' |

**Importante**

É de extrema importância para o funcionamento correto da solução que os caminhos dos diretórios sejam informados corretamente, conforme a instalação do Client da NeoGrid. **Obrigatoriamente,** o Client deve ser instalado a partir do RootPath de instalação do Microsiga Protheus®, para que o Schedule de importação possa localizar os arquivos recebidos e integrar de forma automática para a base do Protheus.

## Procedimento para Utilização

**Schedule de Importação**

Após a atualização, será necessário apenas a configuração do Schedule de importação. Este Schedule será o responsável pela importação dos arquivos XML que serão recebidos via Client Neogrid no diretório “IN”, localizado dentro da instalação do Client (este é o diretório que deve ser configurado no parâmetro **MV\_NGINN**). Os arquivos serão importados para a Tabela CKO - Controle de arquivos TOTVS Colaboração. Após a gravação do arquivo na tabela, o Schedule move o arquivo da pasta IN para a pasta configurada no parâmetro **MV\_NGLIDOS**.

1. No **Configurador (SIGACFG),** acesse **Ambiente/ Schedule/ Schedule**.
2. Clique em **Agent/ Cadastro**.
3. Em **Detalhes** clique em **Incluir**.
4. Informe um nome para o agente.
5. No campo **IP** e **Porta** informe os mesmos dados do **Microsiga Protheus®**.

 O ambiente é preenchido automaticamente.

1. Informe o grupo de empresas.
2. No campo **Número de Threads**, informe a opção **4**.
3. Confira dos dados e confirme.
4. Clique em **Agendamentos/Cadastro**.
5. Em **Detalhes** clique em **Incluir**.
6. Informe o nome da rotina (**colAutoRead**).
7. Selecione a empresa/ filial desejada e o módulo correspondente.
8. Clique na opção **Recorrência** e marque **Sempre Ativo**.
9. Clique em **Confirmar** para o agendamento.
10. Clique em **Agent** e clique em **Iniciar Todos os Serviços**.

É recomendável reiniciar o Server.

**Importante**

Não é necessária a configuração do Schedule para todas empresas e filiais cadastradas, podendo ser configurado para uma única empresa. Como a tabela CKO é única para todas empresas/ filiais e os arquivos que serão recebidos via Client também, se o Schedule for iniciado para uma empresa/ filial, processará todas as existentes.

Caso deseje que seja apresentado no console da aplicação o procedimento que o Schedule realiza, é possível habilitar o parâmetro abaixo no arquivo appserver.ini na seção “Enviroment”:

**COLAUTOREAD\_DEBUG=1**

**Emissão de NF-e e CC-e – TOTVS Colaboração 2.0**

**Importante**

Para informações sobre a utilização da Nota Fiscal Eletrônica, é fundamental a leitura do Manual para Documentos Eletrônicos, disponível no portal TDN pelo *link*: [http://tdn.totvs.com](http://tdn.totvs.com/), em: **Softwares de Gestão/ Linha Microsiga Protheus®/ Fiscal/ Notas Fiscais Eletrônicas/ Banco de Conhecimento/ Documentos Eletrônicos**.

Abaixo estão informadas as alterações realizadas na Nota Fiscal Eletrônica e na Carta de Correção Eletrônica da NF-e, quando configuradas para TOTVS Colaboração 2.0:

1. Foi retirado o **Wizard de Configuração,**que não será necessário pois a configuração do certificado deverá ser feita na NeoGrid. Os e-mails informativos também serão enviados por meio da plataforma NeoGrid.
2. Foram retirados o **Status Sefaz**, a **Consulta Chave e**a**Consulta Contribuinte,** visto que estes serviços não estão disponíveis via TOTVS Colaboração 2.0, pois se tratam de serviços **Síncronos**.
3. Usualmente, os processos de **Transmissão**, **Cancelamento/ Inutilização**e **Monitor** continuam da mesma forma. Internamente foram realizados tratamentos para que trabalhem corretamente via TOTVS Colaboração 2.0.
4. Foi retirada a validação de **Schema,**pois esta será realizada após a transmissão do arquivo para a NeoGrid, que retornará com o problema descrito de schema, caso exista.

**MD-e – TOTVS Colaboração 2.0**

**Importante**Para informações sobre utilização da Manifestação do Destinatário Eletrônica, é fundamental a leitura do Boletim Técnico **COM\_BT\_Manifestacao do Destinatario,** disponível no portal TDN pelo *link*: [http://tdn.totvs.com](http://tdn.totvs.com/), em: **Softwares de Gestão/ Linha Microsiga Protheus® /Materiais/ Compras e Suprimentos/ Boletim técnico/ Versão 11**.

Abaixo seguem as alterações realizadas na Manifestação do Destinatário, quando configurados para TOTVS Colaboração 2.0:

1. Foi retirado o **Wizard de Configuração,**que não será necessário pois a configuração do certificado deverá ser feita na NeoGrid. Os e-mails informativos também serão enviados por meio da plataforma NeoGrid.
2. Foi alterada a funcionalidade **Sincronizar.** Como se tratava de um serviço síncrono, foi necessário o ajuste para trabalhar de forma **assíncrona.** Assim, esta funcionalidade trabalhará junto com a funcionalidade **Atualizar.**
3. Foi inserida a funcionalidade **Atualizar,**queserá responsável por atualizar a tela para que quando os documentos forem sincronizados apareçam em tela.
4. Foi retirada a funcionalidade **Baixar Zip** e esta foi substituída pela funcionalidade **Exportar** para o TOTVS Colaboração 2.0. A Alteração foi realizada para que o processo funcione de forma **assíncrona**.
5. Inserida a opção **Exportar** com duas funcionalidades: **Solicitar** e **Monitorar.**
6. A funcionalidade **Solicitar**realiza a solicitação do **download** do XML para a NeoGrid.
7. A funcionalidade **Monitorar**abre um monitor para controle das solicitações de **downloads**, no qual é possível realizar o download por meio do botão **Baixar,**apenas quando estiver disponível.
8. Usualmente os processos de **Configurar**, **Manifestar**e **Monitorar** continuam da mesma forma. Internamente foram realizados tratamentos para que trabalhem corretamente via TOTVS Colaboração 2.0.

**Emissão de NFS-e – TOTVS Colaboração 2.0**

**Importante**Para informações sobre a utilização da Nota Fiscal Eletrônica, é fundamental a leitura do Manual para Documentos Eletrônicos disponível no portal TDN pelo *link*: [http://tdn.totvs.com](http://tdn.totvs.com/), em: **Softwares de Gestão/ Linha Microsiga Protheus®/ Fiscal/ Notas Fiscais Eletrônicas/ Banco de Conhecimento/ Documentos Eletrônicos**.

Abaixo seguem as alterações realizadas na Nota Fiscal de Serviços Eletrônica, quando configurados para TOTVS Colaboração 2.0:

1. Foi retirada a opção **Wizard de Configuração,**que não será necessário pois a configuração do certificado deverá ser feita na NeoGrid. Os e-mails informativos também serão enviados por meio da plataforma NeoGrid.
2. Foram retiradas as opções **Imp.Retorno, Abrir URL e Tabela AIDF,** visto que estes serviços não estão disponíveis via TOTVS Colaboração 2.0, pois se tratam de serviços **Síncronos**.
3. Usualmente os processos de **Transmissão**, **Cancelamento**e **Monitor** continuam da mesma forma. Internamente foram realizados tratamentos para que trabalhem corretamente via TOTVS Colaboração 2.0.
4. Foi retirada a validação de **Schema.**Esta será realizada após a transmissão do arquivo para a NeoGrid, que retornará com o problema descrito de Schema, caso exista.
5. A geração do arquivo conforme layout definido pela NeoGrid será realizada por meio da rotina customizável (**NFSEXMLUni.prw**).
6. Caso utilize uma condição de pagamento superior em duas vezes ou mais o parâmetro **MV\_1DUP** deve conter o conteúdo igual a **01 (numérico)** pois no acordo firmado com a Neogrid as parcelas devem ser geradas somente com conteúdo númerico.

**MDF-e – TOTVS Colaboração 2.0**

**Importante**Para informações sobre a utilização do Manifesto Eletrônico de Documentos Fiscais, é fundamental a leitura do Manual para Documentos Eletrônicos disponível no portal TDN pelo *link*: [http://tdn.totvs.com](http://tdn.totvs.com/), em: **Softwares de Gestão/ Linha Microsiga Protheus®/ Fiscal/ Notas Fiscais Eletrônicas/ Banco de Conhecimento/ Documentos Eletrônicos**.

Abaixo seguem as alterações realizadas na Manifestação do Destinatário, quando configurados para TOTVS Colaboração 2.0:

1. Foi retirado o **Wizard de Configuração**que não será necessário pois a configuração do certificado deverá ser feita na NeoGrid. Os e-mails informativos também serão enviados por meio da plataforma NeoGrid.
2. Foi retirado o **Status Sefaz**, visto que este serviço não está disponível via TOTVS Colaboração 2.0, pois se trata de serviço **Síncrono**.
3. Usualmente os processos de **Transmissão**, **Cancelamento, Encerramento**e **Monitorar** continuam da mesma forma. Internamente foram realizados tratamentos para que trabalhem corretamente via TOTVS Colaboração 2.0.
4. Retirada a validação de **Schema,**esta validação será realizada após a transmissão do arquivo para a NeoGrid, que retornará com o problema descrito de schema, caso exista.

**CT-e – TOTVS Colaboração 2.0**

**Importante**Para informações sobre a utilização do Conhecimento de Transporte Eletrônico de Documentos Fiscais, é fundamental a leitura do Manual para Documentos Eletrônicos, disponível no portal TDN pelo *link*: [http://tdn.totvs.com](http://tdn.totvs.com/), em: **Softwares de Gestão/ Linha Microsiga Protheus®/ Fiscal/ Notas Fiscais Eletrônicas/ Banco de Conhecimento/ Documentos Eletrônicos**.

Abaixo seguem as alterações realizadas no Conhecimento de Frete Eletrônico, quando configurados para TOTVS Colaboração 2.0:

1. Foi retirada a opção **Status**, visto que este serviço não está disponível via TOTVS Colaboração 2.0, pois se trata de serviço **Síncrono**.
2. Usualmente os processos de **Transmitir**, **Cancelamento, Inutilização**e **Monitor** continuam da mesma forma. Internamente foram realizados tratamentos para que trabalhem corretamente via TOTVS Colaboração 2.0

**EDI-Pedido – TOTVS Colaboração 2.0**

Abaixo seguem as alterações realizadas nas rotinas de Geração de Pedido de Venda e Programação de Entrega, quando configuradas para TOTVS Colaboração 2.0:

1. Configurar uma job que acione a função MA411Job(), utilizando o SIGACFG, no menu Ambiente/ Schedule/ Schedule.
2. Configurar uma job que acione a função MA412Job(), utilizando o SIGACFG, no menu Ambiente/ Schedule/ Schedule.
3. Configurar o parâmetro **MV\_TCNEW** igual a 6.
4. Configurar o parâmetro **MV\_NGINN** com o caminho da pasta para recebimento do XML da neogrid.
5. Configurar o parâmetro **MV\_NGLIDOS** com o caminho da pasta para mover os arquivos XML já processados da neogrid.
6. Usualmente os processos de **Geração do Pedido de Venda e Geração da Programação de Entrega** continuam da mesma forma. Internamente foram realizados tratamentos para que trabalhem corretamente via TOTVS Colaboração 2.0.

## Informações Técnicas

|  |  |
| --- | --- |
| **Tabelas Utilizadas** | CKP – Parâmetros TOTVS Colaboração.  CKQ – Monitor de Documentos TOTVS Colaboração.  CKO – Controle de arquivos TOTVS Colaboração.  CC0 – Manifesto Documentos Fiscais. |
| **Rotinas Envolvidas** | ColUpd001  ColabGeneric  ColabDocumentos  FISA022  SPEDNFE  SPEDCOL  DANFEII  DANFEIII  AutoNfeBusiness  AutoNfseBusiness  nfep11r1  colReadControl  colAutoRead  SPEDMDFE DAMDFE  TMSA500  TMSA190  TMSAE70  TMSAE73  TMSAE90  TmsXFunc  CTeSefaz  MDFSefaz  Rtmsr27  Rtmsr28  MATA412  MATA411 |
| **Sistemas Operacionais** | Windows®/ Linux® |

Link de Referencia:<http://tdn.totvs.com/pages/releaseview.action?pageId=187534008>
