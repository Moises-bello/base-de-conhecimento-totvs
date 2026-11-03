---
article_id: 31353232455191
category: Originação de Grãos (OG)
content_hash: 3302571eca4410cf12078c37c039bc22d61cb26ba6350f8c0a3d013db69054b5
fetched_at: '2026-06-28T22:45:42.960536+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para incluir variáveis ​​no
  documento modelo de impressão do Certificado de Peso
type: support-article
updated_at: '2025-06-25T19:06:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31353232455191-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-incluir-vari%C3%A1veis-no-documento-modelo-de-impress%C3%A3o-do-Certificado-de-Peso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31353232416535) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Para que serve o **Ponto de Entrada** **para incluir variáveis ​​no documento modelo de impressão do Certificado de Peso**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGR730 | Impressão Certificado de Peso | |
| **Ponto de entrada:** | AGR730VAR |
| **País(es):** | Todos |
| **Pacote:** | 12.1.23 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao gerar o arquivo de Certificado de Peso no modelo MS-WORD por meio do programa OGA710 - Instrução de Embarque. |
| **Programa Fonte:** | OGR730VAR |
| **Função:** | Permitir adicionar novas variáveis ​​para impressão do Certificado de Peso. |
| Parâmetros: | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | PARAMIXB | Variedade | Matriz com as variáveis ​​do documento MS-WORD que são geradas no padrão. | Sim | |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aCampos** | Variedade | Mesmo array de parâmetros de entrada e com variáveis ​​específicas selecionadas. | Sim | |

****Exemplo:****

|  |
| --- |
| `USER FUNCTION AGR87001()`     Local aMenu := {}  `//customizações` `aAdd( aMenu, { "Solicitar" , "AGRA870SOL()" , 0, 4, 0, Nil } )`   `RETURN aMenu` |
