---
content_hash: ad6a8c7413d292f151c68647d0adb19ebf5e25ad24823db5376e9263cbd7147a
fetched_at: '2026-06-29T00:08:17.103999+00:00'
page_id: '253984882'
product: rm
source: tdn-rm
title: ER_EDUCTB002-112_Parametros_Cadastro_de_Convenio
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_EDUCTB002-112_Parametros_Cadastro_de_Convenio
version: 113
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Financeira |
| **Segmento Executor** | Educacional | | |
| **Projeto** |  | **IRM** |  |
| **Requisito** |  | **Subtarefa** |  |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## Objetivo

Automatizar a configuração da geração e retorno do arquivo de remessa eletrônica (cobrança, débito automático e pagamento). No cadastro de Convênio, para cada um dos três processos, deve ser possível informar a composição do nome do arquivo de remessa, que aceitará uma parte fixa e tags para substituir por outras informações, a extensão do arquivo e o diretório destino onde ele será salvo. Também o caminho do diretório origem para buscar o arquivo do retorno da remessa de cada um dos três tipos.

## Definição da Regra de Negócio

1 - Criar os seguintes campos no Cadastro de Convênio.

1.1 - Cobrança Eletrônica:

* + Diretório de destino da remessa (FCONVENIO.DESTINOREMESSACOB): onde será informado o caminho de destinho dos arquivos de remessa de cobrança eletrônica.
  + Nome do arquivo (FCONVENIO.NOMEARQUIVOCOB): onde será informado o nome do arquivo de remessa de cobrança eletrônica.
  + Extensão do arquivo (FCONVENIO.EXTARQUIVOCOB): onde será informado a extensão do arquivo de remessa, com opções de .txt e .rem.
  + Diretório de destinho do retorno (FCONVENIO.DESTINORETORNOCOB): onde será informado o caminho de origem dos arquivos de retorno de cobrança eletrônica.

1.2 - Débito Automático

* + Diretório de destino da remessa (FCONVENIO.DESTINOREMESSADEBAUTO): onde será informado o caminho de destinho dos arquivos de remessa de débito automático.
  + Nome do arquivo (FCONVENIO.NOMEARQUIVODEBAUTO): onde será informado o nome do arquivo de remessa de débito automático.
  + Extensão do arquivo (FCONVENIO.EXTARQUIVODEBAUTO): onde será informado a extensão do arquivo de remessa, com opções de .txt e .rem.
  + Diretório de destinho do retorno (FCONVENIO.DESTINORETORNODEBAUTO): onde será informado o caminho de origem dos arquivos de retorno de débito automático.

1.3 - Pagamento

* + Diretório de destino da remessa (FCONVENIO.DESTINOREMESSAPAG): onde será informado o caminho de destinho dos arquivos de remessa de pagamento.
  + Nome do arquivo (FCONVENIO.NOMEARQUIVOPAG): onde será informado o nome do arquivo de remessa de pagamento.
  + Extensão do arquivo (FCONVENIO.EXTARQUIVOPAG): onde será informado a extensão do arquivo de remessa, com opções de .txt e .rem.
  + Diretório de destinho do retorno (FCONVENIO.DESTINORETORNOPAGAMENTO): onde será informado o caminho de origem dos arquivos de retorno de pagamento.

1.4 - O nome do arquivo poderá ser composto por uma parte fixa e por uma parte variavel definida pelas seguintes tags:

* + DDMMYYYY - informação da data de geração do arquivo.  
    Exemplo: R240\_COOP\_DDMMYYYY.REM => R240\_COOP\_13102016.REM
  + # - caracter para definir o número sequencial do arquivo.   
    Exemplo: R240\_COOP\_#####.TXT, sendo ##### um sequencial de 5 posições com zero a esquerda. => R240\_COOP\_00001.TXT

2 - Processos

2.1 - Alterar os processos da geração de remessa de cobrança eletrônica, débito automático e pagamento para gerar  os arquivos de acordo com as configurações. Caso os campos não seja informados manter o comportamento atual.

2.2 - Alterar os processos de retorno de cobrança eletrônica, débito automático e pagamento para buscar os diretórios de acordo com as configurações. Caso os campos não seja informados manter o comportamento atual.

***Tabelas Utilizadas***

*FCONVENIO – Cadastro de Convênio*

## Dicionário de Dados

**Arquivo ou Código do Script:** FS.2016.09\_02

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
