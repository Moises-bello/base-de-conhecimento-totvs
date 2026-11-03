---
content_hash: 0abb63bdcea47e8b65a4b7ae6f5642a7cacead16a101b9f3117e428c8ce94b35
fetched_at: '2026-06-29T00:08:04.543519+00:00'
page_id: '235574304'
product: rm
source: tdn-rm
title: ER_PCREQ-10842_Novo Parâmetro Controle na importação Brasíndice e SIMPRO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235574304
version: 11
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAUDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto** | R\_SAU\_RM\_V12\_1516 | **IRM** | PCREQ-10841 |
| **Requisito** | PCREQ-10842 | **Subtarefa** | SAU\_DEV-4621 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## Objetivo

Esta implementação tem como objetivo adicionar controle para preferência por tipo de preço a nível do Item, conforme lógica já existente na tabela de preços .

## Definição da Regra de Negócio

**RN001** - Permitir em nível de produto que seja possível dar preferência pelo tipo de preço definido no item

Cadastro de Produtos - Frame para parametrizar o tipo de preço entre Tabela, PFB ou PMC. Sendo o padrão Tabela.

        Importação / Atualização BRASÍNDICE - Considerar na rotina definição de tipo de preço em nivel de item.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Produtos | Alteração | Cadastros > Estoque > Produto | **RN001** |
| Importação / Atualização BRASÍNDICE | Alteração | Utilitários > Rotinas > Importação / Atualização BRASÍNDICE | **RN001** |

## **Exemplo de Aplicação:**

* Acessar o menu **"Cadastros > Estoque > Produto"**
* Clicar em **"Anexos > Informações TOTVS Saúde"**
* Selecionar em alguns itens o parâmetro **"Priorizar Preço"** para PMC ou PFB
* Acessar **"Utilitários > Rotinas > Importação / Atualização BRASÍNDICE" ,** importar e atualizar estoque

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
