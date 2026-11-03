---
content_hash: a77147715e43aabe4021e85d6379fd56fb9f75a240116608c1d7576fac252db6
fetched_at: '2026-06-29T00:08:08.294764+00:00'
page_id: '238029641'
product: rm
source: tdn-rm
title: ER_SAUHRM01-164_Integração_ACH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=238029641
version: 21
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Projeto** | * SAUHRM01 | **IRM** | * [SAUHRM01-21](http://jiraproducao.totvs.com.br/browse/RHRM01-21) |
| **Requisito** | * [SAUHRM01-42](http://jiraproducao.totvs.com.br/browse/RHRM01-42 "RM HOSP - Integração ACH SUS ( PROCEMPA )") | **Subtarefa** | * [SAUHRM01-160](http://jiraproducao.totvs.com.br/browse/RHRM01-160) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

   Este documento tem como objetivo especificar o requisito de Integração ACH, onde o sistema deverá prover ferramentas para que o usuário consiga importar e exportar arquivos no padrão exigido pela SMS POA (Secretaria Municipal da Saúde de Porto Alegre), bem como processar os dados retornados e fornecer ao usuário uma visualização dos fluxos do processo de entrega e recebimento destes arquivos.

## Definição da Regra de Negócio

 **RN001 - Parametrização**

1. Em "**Parâmetros SUS**", em uma nova aba chamada ACH, criar quatro novos parâmetros, cujas funções serão as seguintes:
   * Armazenar o caminho do diretório onde será salvo o arquivo exportado;
   * Armazenar o valor para o código do hospital na SMS POA;
   * Informar o relatório que será associado à impressão de etiquetas.

**RN002 - Geração/Importação do Arquivo**

1. No menu "**Faturamento**", criar um novo Sub-menu que terá as seguintes funcionalidades:
   * Exportação de ACH, onde o sistema permitirá ao usuário selecionar os laudos elegíveis para exportação. Os Laudos exportados deverão ter persistidas as informações referentes a **data de exportação, número do laudo ACH (sequencial), tipo do laudo e status do laudo.**
   * Importação ACH, onde o sistema solicitará o local do arquivo de retorno e processará o mesmo após a seleção. inconsistências de layout deverão ser tratadas antes da importação. Após a importação, todos os laudos importados deverão ter  seus status atualizados de acordo com o retorno. **Se o retorno for Aprovado, a AIH provisória deverá ser substituída por uma permanente. Se negado, a AIH provisória permanece. Ao final do processo, o sistema deverá notificar o usuário sobre os laudos aprovados e reprovados.**
   * Geração de Etiquetas de ACH, onde o sistema buscará pelo relatório definido para **impressão de etiquetas,**em "**Parâmetros SUS**" e fará a impressão das etiquetas de acordo com os laudos selecionados;

Laoyout\_ACH.docx250

***\*\*Anexo à esta especificação, consta o arquivo com o layout do padrão ACH, disponibilizado pela SMS POA.***     

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros SUS | Alteração | Opções > Parâmetros > Parâmetros SUS | **RN001** |
| Integração ACH | Alteração | Faturamento > Padrão ACH | **RN002** |

**Exemplo de Aplicação:**

1. Acessar o menu "**Opções > Parâmetros > Parâmetros SUS**";
2. Acessar a aba "ACH" e preencher as informações referentes a **Código do Hospital, Relatório de Etiquetas e Diretório****;**
3. Acessar o menu "**Faturamento > Padrão ACH > Exportação de ACH**";
4. Avançar o processo e selecionar os laudos elegíveis para exportação (Atendimentos SUS que contemplem os pré-requisitos exigidos pelo padrão);
5. Finalizar a geração e verificar no diretório parametrizado se o arquivo foi gerado corretamente, seguindo os padrões descritos nas RN's e no documento de Layout, que está em anexo;
6. Acessar o menu "**Faturamento > Padrão ACH > Geração de Etiquetas de ACH**";
7. Avançar o processo e selecionar o arquivo já gerado (informação da tabela **SZSUSACHCAB**), onde está o laudo que deseja imprimir;
8. Selecionar os laudos desejados, clicar em "**Processos > Impressão de Etiquetas**" e avançar até a conclusão do processo;
9. Verificar se as etiquetas foram impressas de acordo com o esperado;
10. Após o retorno do arquivo processado pela **SMS POA**, acessar o menu  "**Faturamento > Padrão ACH > Importação de ACH**";
11. Selecionar o diretório e o arquivo que deseja importar;
12. Avançar o processo até sua conclusão. Após a conclusão do processo, deverá ser listado para o usuário o status da conclusão, com os laudos que foram aprovados e os que não foram;
13. O sistema deverá também, na importação, atualizar os status dos laudos e substituição de AIH's provisórias pelas definitivas, de acordo com o descrito na **RN002.**

**Tabelas Utilizadas**

* **SZSUSACHCAB - Tabela responsável pelo agrupamento dos laudos.**
* **SZSUSACH - Tabela responsável pelo registro e controle dos laudos.**
* **SZSUSAIH**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
