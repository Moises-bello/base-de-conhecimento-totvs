---
article_id: 360035247153
category: Contabilidade Gerencial - Relatórios Demonstrativos
content_hash: 0ffa5de0786a12a071360b1758e935612ff529e8b289ee4a5c7be8900e49f2c1
fetched_at: '2026-06-28T22:40:38.892984+00:00'
product: protheus
section_id: 1500001548882
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Termo de abertura ou
  Encerramento dos relatórios  Diários (CTBR110),Razão (CTBR400) e Balanço(CTBR500),
  arquivo .TRM
type: support-article
updated_at: '2021-05-17T12:38:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035247153-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Termo-de-abertura-ou-Encerramento-dos-relat%C3%B3rios-Di%C3%A1rios-CTBR110-Raz%C3%A3o-CTBR400-e-Balan%C3%A7o-CTBR500-arquivo-TRM
---

**Dúvida**Como configurar o Termo de abertura ou Encerramento para os relatórios Diários (CTBR110),Razão (CTBR400) e Balanço(CTBR500), arquivo .TRM?

**Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão 11.80  
  
**Solução**

|  |  |  |
| --- | --- | --- |
| **MV\_LBALABE** | Arquivo que contém o texto do Termo de Abertura do Balanço Patrimonial. | LDIARAB.TRM |
| **MV\_LBALFEC** | Arquivo que contém o texto do Termo de Encerramento do Balanço Patrimonial. | LDIAREN.TRM |
| **MV\_LDIARAB** | Arquivo que contém o texto do Termo de Abertura do Diário Geral. | DIARAB.TRM |
| **MV\_LDIAREN** | Arquivo que contém o texto do Termo de Encerramento do Diário Geral. | LDIARAB.TRM |
| **MV\_LRAZABE** | Arquivo que contém o texto do Termo de Abertura do Razão Contábil. | LRAZABE.TRM |
| **MV\_LRAZENC** | Arquivo que contém o texto do Termo de o Geral. | LRAZENC.TRM |

Necessário criar os arquivos  e salvá-lo no diretório da maquina que será impresso o relatório

* crie um arquivo Bloco de Notas.
* mude a extensão para:LDIARAB.TRM,LDIAREN.TRM,LDIARAB.TRM,LDIAREN.TRM,LRAZABE.TRM,LRAZENC.TRM.
* Ao imprimir os relatórios selecione “**Imprimir termo auxiliar= Sim**” e selecione o arquivo. TRM criado.

Verifique junto ao seu contador o conteúdo necessário para criar o arquivo.

Obs: A Totvs não possui Modelo disponível de termo auxiliar

Veja mais :

* [Como realizar a alteração da fonte dos relatórios Contábeis?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006871951-MP-SIGACTB-Como-realizar-a-altera%C3%A7%C3%A3o-da-fonte-dos-relat%C3%B3rios-Cont%C3%A1beis-?source=search)

* [Qual o parâmetro controla a exibição do botão personalizar nos relatórios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019682831-MP-SIGACTB-Qual-o-par%C3%A2metro-controla-a-exibi%C3%A7%C3%A3o-do-bot%C3%A3o-personalizar-nos-relat%C3%B3rios-?source=search)

* [Como realizar a extração/impressão do Razão Contábil no PROTHEUS (CTBR400)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006683712-MP-SIGACTB-Como-realizar-a-extra%C3%A7%C3%A3o-impress%C3%A3o-do-Raz%C3%A3o-Cont%C3%A1bil-no-PROTHEUS-CTBR400-?source=search)

* [Quais os relatórios oficiais do modulo contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018012592-MP-SIGACTB-Quais-os-relat%C3%B3rios-oficiais-do-modulo-cont%C3%A1bil?source=search)
