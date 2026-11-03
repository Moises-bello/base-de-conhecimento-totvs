---
content_hash: df586660032e13cc519f6cba2f0d2242ce5d59fc272ff4e3c91a5d590fd818b9
fetched_at: '2026-06-29T00:06:25.511323+00:00'
page_id: '224398546'
product: rm
source: tdn-rm
title: ER_CENTRALIZAR_OS_CODIGOS_DE_INTEGRACAO
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CENTRALIZAR_OS_CODIGOS_DE_INTEGRACAO
version: 141
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo:** EAI |  |
| **Segmento Executor** | Framework | | |
| **Projeto1** | R\_FRW004 | **IRM1** | **PCREQ-9634** |
| **Requisito1** | PCREQ-9644 | **Subtarefa1** | **[PDR\_FRW\_FRW002-22](http://jira.totvs.com.br/browse/PDR_FRW_FRW002-22)** |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
|  |  | | |

## Objetivo

Desenvolver no EAI um mecanismo para viabilizar a transferência dos códigos fontes das integrações (atualmente esses fontes estão localizados na tabela GsourceCode) para as dlls nativas dos produtos.  
Com essa mudança, os diversos fontes das integrações passarão a ser controlados pelo TFS, possibilitando com isso ganhos de segurança, histórico, controle de concorrência, etc.

## 

## Definição da Regra de Negócio

**1) - Mecanismo 1 (extensão de códigos)**

Atualmente o analista responsável pelo desenvolvimento da integração pode usar diversos "entry Points" disparados em pontos durante o processamento da mensagem.

Códigos C# (.NET) são criados e armazenados em uma tabela de banco chamada GSourceCode. Esses códigos podem ser "vinculados" a esses pontos.

Esse mecanismo continuará existindo pois integrações totalmente customizadas devem ainda utilizar esse modelo.

**2) - Mecanismo 2 (adapters) - A ser criado...**

As equipes dos produtos deverão criar projetos nas suas *solutions* contendo classes a serem executadas automaticamente durante o processamento da mensagem.

2.1 - Criação dos projetos:

Os projetos a serem criados nessas *solutions* deverão seguir o seguinte padrão de nomenclatura:

**RM.{Segmento}.TotvsMessage.Adapter.dll**,        onde:  Segmento = Sigla do segmento  
               **ex:  RM.Fin.TotvsMessage.Adapter.dll.**

2.2 - Criação das classes:

a) - Extensão de códigos:

       -  Herdar da classe: **AdapterBase**

        - Uso do atributo:  **AdapterAttr**

          Exemplo:

*[AdapterAttr(TransactionType.ttMensageriaUnica, "COSTCENTER", "2.000")]*  
*public class CostCenter : AdapterBase*

b) - Handles customizados:

       - Herdar da classe: **ReceiveMessageHandle**

       - Utilização do atributo **AdapterAttr**

      Exemplo:

*[AdapterAttr(TransactionType.ttMensageriaUnica, "FinancingTranding", "1.000")]*  
*public class FinancingTranding : ReceiveMessageHandle*

## Protótipo de Tela

Segue abaixo as telas do EAI na qual esses códigos poderão ser utilizados.

*fig: Mapa de transformação: Permite utilizar uma extensão de código*

*fig 2: Transformação: Permite utilizar um fonte para substituir a manipulação completa de uma mensagem de recebimento (chamado de customHandle).*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
