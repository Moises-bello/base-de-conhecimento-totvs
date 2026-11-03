---
content_hash: f36eb2bc60ad28fba0a3413358f45b1ad60675c9cb045ba4e78cff7129cd9339
fetched_at: '2026-06-29T00:08:26.479961+00:00'
page_id: '271180815'
product: rm
source: tdn-rm
title: ER SAUHRM02-589 Importação do xml de retorno de pagamento pelo número guia
  prestador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271180815
version: 109
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR - RM | **Módulo** | Faturamento / Fatura de Convênio |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM02 | **IRM/EPIC1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-346 |
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-589 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-750 |
| **Chamado2** | 198738 | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

Esta especificação tem como objetivo detalhar a melhoria à ser implementada na funcionalidade de Faturamento para Convênios do produto TOTVS Gestão Hospitalar. A melhoria consiste-se em disponibilizar a rastreabilidade dos itens processados por arquivo e suas respectivas falhas, durante a importação do XML de Retorno de Pagamento.

## Definição da Regra de Negócio

****RN001** -** Ao acessar a rotina de Recebimento de Lote Guias/Recurso (menu Faturamento > Faturamento para Convênios > Selecionar um Registro > Processos > Recebimento de Lote Guias/Recurso), o sistema deve criar um cabeçalho de rastreamento e cada item processado deve ser registrado na tabela que representa o seu respectivo grupo de gasto, associando o item (detalhe) ao arquivo (cabeçalho).

Para armazenar o cabeçalho, deve ser criada a tabela SZARQUIVOCONVENIO com os seguintes campos:

* CODCOLIGADA, correspondente ao Codigo da Coligada
* IDARQUIVO , correspondente ao ID do Arquivo
* IDCONVENIO, correspondente ao ID do Convenio
* NOMEARQUIVO, correspondente ao Nome do Arquivo

Para armazenar os detalhes do itens processados, devem ser criadas as tabelas SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSMATMEDARQUIVO**\***, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO com seguintes campos:

* CODCOLIGADA, que corresponde ao Codigo da Coligada
* SEQID, que corresponde ao Sequencial do ID
* IDARQUIVO, que corresponde ao FK (SZARQUIVOCONVENIO)
* NCONTA, que corresponde ao Numero da Conta
* SEQCONTA, que corresponde ao Sequencial da Conta
* SEQPARCIAL, que corresponde ao Sequencial da Parcial
* CODGASTO, que corresponde ao Codigo do Gasto
* SEQDEBITO, que corresponde ao Sequencial do Debito
* NUMEROREMESSA, que corresponde ao Numero da Remessa
* CODPROC, que corresponde ao Codigo do Processo
* IDPRD, que corresponde ao ID do Produto**\***

  **\*Campo exclusivo da tabela SZITENSMATMEDARQUIVO**

****RN002** -** Será criado um item de menu Faturamento > Faturamento para Convênios > Rastreabilidade do Recebimento de Lote guias/Recursos, para que o usuário possa acessar os arquivos que foram importados. 

**RN003** - Exibir os itens não importados no "Recebimento de Lote Guias/Recurso" (RN001), como um anexo da Rastreabilidade do Recebimento de Lote guias/Recursos.

Para o cadastro deste anexo, foi atualizada a tabela  SZLOGIMPRECGLOSAERRO, já existente no sistema, adicionando as seguintes colunas em propriedades:

* IDARQUIVO, que corresponde ao ID do Arquivo
* IDSEQ, que corresponde ao ID Sequencial
* Alteração da chave primária para (CODCOLIGADA, IDSEQ)

Faturamento > Faturamento para Convênios > Rastreabilidade do Recebimento de Lote guias/Recurso

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Recebimento de Lote Guias/Recurso | [Alteração] | Faturamento > Faturamento para Convênios > Registro\* > Processos > Recebimento de Lote Guias/Recurso | RN001 |
| Rastreabilidade do Recebimento de Lote guias/Recursos | [Criação] | Faturamento > Faturamento para Convênios > Rastreabilidade do Recebimento de Lote guias/Recursos | RN002 |
| Logs de itens não Importados | [Atualização] | Faturamento > Faturamento para Convênios > Rastreabilidade do Recebimento de Lote guias/Recursos > Registro\* > Anexos > Logs de itens não Importados | RN003 |

 \*Necessário selecionar um registro

**Exemplo de Aplicação:**

* Disponibilização da Rastreabilidade do Recebimento de Lote guias/Recursos.

**Tabelas Utilizadas**

* SZARQUIVOCONVENIO - Tabela de Cabeçalho (Arquivo x Convênio)
* SZITENSDIARIAARQUIVO - Tabela de detalhe Itens de Diária (Itens x Arquivo)
* SZITENSHONORARIOARQUIVO - Tabela de detalhe Itens de Honorário (Itens x Arquivo)
* SZITENSMATMEDARQUIVO - Tabela de detalhe Itens de Mat/Med (Itens x Arquivo)
* SZITENSSADTARQUIVO - Tabela de detalhe Itens de SADT (Itens x Arquivo)
* SZITENSTAXASERVICOSARQUIVO - Tabela de detalhe Itens de Taxas/Serviços (Itens x Arquivo)

### Dicionário de Dados

 

**Arquivo ou Código do Script:**

 

Tabela: SZARQUIVOCONVENIO 

 

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Tabela de Referência |
| 1 | <CODCOLIGADA + IDARQUIVO> (PK) |  |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZARQUIVOCONVENIO | CODCOLIGADA | DCODCOLIGADA |  |  | Sim (X) Não ( ) | Código da Coligada |
| SZARQUIVOCONVENIO | IDARQUIVO | Inteiro | 4 |  | Sim (X) Não ( ) | ID do Arquivo |
| SZARQUIVOCONVENIO | IDCONVENIO | Inteiro | 4 |  | Sim (X) Não ( ) | ID do Convênio |
| SZARQUIVOCONVENIO | NOMEARQUIVO | Varchar | 255 |  | Sim (X) Não ( ) | Nome do Arquivo |

Tabela:  SZITENSMATMEDARQUIVO 

 

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Tabela de Referência |
| 1 | <CODCOLIGADA + SEQID> (PK) |  |
| 2 | <CODCOLIGADA + IDARQUIVO> (FK) | SZITENSMATMEDARQUIVO |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZITENSMATMEDARQUIVO | CODCOLIGADA | DCODCOLIGADA |  |  | Sim (X) Não ( ) | Código da Coligada |
| SZITENSMATMEDARQUIVO | SEQID | Inteiro | 4 |  | Sim (X) Não ( ) | Sequencial do ID |
| SZITENSMATMEDARQUIVO | IDARQUIVO | Inteiro | 4 |  | Sim (X) Não ( ) | FK (SZARQUIVOCONVENIO) |
| SZITENSMATMEDARQUIVO | NCONTA | Varchar | 14 |  | Sim (X) Não ( ) | Numero da Conta |
| SZITENSMATMEDARQUIVO | SEQCONTA | Inteiro | 4 |  | Sim (X) Não ( ) | Sequencial da Conta |
| SZITENSMATMEDARQUIVO | SEQPARCIAL | Inteiro | 4 |  | Sim (X) Não ( ) | Sequencial da Parcial |
| SZITENSMATMEDARQUIVO | CODGASTO | Varchar | 2 |  | Sim (X) Não ( ) | Código do Gasto |
| SZITENSMATMEDARQUIVO | SEQDEBITO | Inteiro | 4 |  | Sim (X) Não ( ) | Sequencial do Debito |
| SZITENSMATMEDARQUIVO | NUMEROREMESSA | Varchar | 4 |  | Sim (X) Não ( ) | Numero da Remessa |
| SZITENSMATMEDARQUIVO | CODPROC | Varchar | 10 |  | Sim (X) Não ( ) | Código do Processo |
| SZITENSMATMEDARQUIVO | IDPRD | Inteiro | 4 |  | Sim (X) Não ( ) | ID do Produto |

Tabela:   SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO  

* Estas tabelas possuem os mesmos campos, chave-primária e chave-estrangeira, sendo separadas apenas para armazenar itens de grupos de gastos distintos.

 

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Tabela de Referência |
| 1 | <CODCOLIGADA + SEQID> (PK) |  |
| 2 | <CODCOLIGADA + IDARQUIVO> (FK) | SZITENSMATMEDARQUIVO |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | CODCOLIGADA | DCODCOLIGADA |  |  | Sim (X) Não ( ) | Código da Coligada |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | SEQID | Inteiro | 4 |  | Sim (X) Não ( ) | Sequencial do ID |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | IDARQUIVO | Inteiro | 4 |  | Sim (X) Não ( ) | FK (SZARQUIVOCONVENIO) |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | NCONTA | Varchar | 14 |  | Sim (X) Não ( ) | Numero da Conta |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | SEQCONTA | Inteiro | 4 |  | Sim (X) Não ( ) | Sequencial da Conta |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | SEQPARCIAL | Inteiro | 4 |  | Sim (X) Não ( ) | Sequencial da Parcial |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | CODGASTO | Varchar | 2 |  | Sim (X) Não ( ) | Código do Gasto |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | SEQDEBITO | Inteiro | 4 |  | Sim (X) Não ( ) | Sequencial do Debito |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | NUMEROREMESSA | Varchar | 4 |  | Sim (X) Não ( ) | Numero da Remessa |
| SZITENSDIARIAARQUIVO, SZITENSHONORARIOARQUIVO, SZITENSSADTARQUIVO, SZITENSTAXASERVICOSARQUIVO | CODPROC | Varchar | 10 |  | Sim (X) Não ( ) | Código do Processo |

Tabela:    SZLOGIMPRECGLOSAERRO

 

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Tabela de Referência |
| 1 | <CODCOLIGADA + IDSEQ> (PK) |  |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZLOGIMPRECGLOSAERRO | CODCOLIGADA | DCODCOLIGADA |  |  | Sim (X) Não ( ) | Coligada |
| SZLOGIMPRECGLOSAERRO | NUMEROCONTA | varchar | 14 |  | Sim () Não (X) | Número da conta do paciente |
| SZLOGIMPRECGLOSAERRO | IDLOG | Inteiro | 4 |  | Sim () Não (X) | Identificador do log |
| SZLOGIMPRECGLOSAERRO | SEQUENCIALCONTA | Inteiro | 4 |  | Sim () Não (X) | Sequencial da conta do paciente |
| SZLOGIMPRECGLOSAERRO | SEQPARCIAL | Inteiro | 4 |  | Sim () Não (X) | Sequencial da parcial |
| SZLOGIMPRECGLOSAERRO | DESCITEM | varchar | 100 |  | Sim () Não (X) | Descrição do item |
| SZLOGIMPRECGLOSAERRO | CODITEM | varchar | 10 |  | Sim () Não (X) | Código do item |
| SZLOGIMPRECGLOSAERRO | CODCONVENIO | Inteiro | 8 |  | Sim () Não (X) | Código do Convênio |
| SZLOGIMPRECGLOSAERRO | NUMEROREMESSA | varchar | 14 |  | Sim () Não (X) | Número da remessa |
| SZLOGIMPRECGLOSAERRO | IDARQUIVO | Inteiro | 4 |  | Sim () Não (X) | ID do Arquivo |
| SZLOGIMPRECGLOSAERRO | IDSEQ | Inteiro | 4 |  | Sim (X) Não ( ) | ID Sequencial |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
