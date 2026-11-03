---
article_id: 35041323516183
category: Escrita Fiscal - Configurador de Tributos
content_hash: 42dbb240e4a4a242c3450a3955905bc9e28a7ad243b832882ebb01a4c7ed07c6
fetched_at: '2026-06-28T22:39:17.784240+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - Como garantir
  o cálculo correto do tributo na nota fiscal utilizando a Regra de Cálculo no Configurador
  de Tributos?
type: support-article
updated_at: '2025-11-13T22:06:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35041323516183-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-garantir-o-c%C3%A1lculo-correto-do-tributo-na-nota-fiscal-utilizando-a-Regra-de-C%C3%A1lculo-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35041323498007) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Quais são os critérios para ser aplicada a Regra de Calculo na nota utilizando o Configurador de Tributos?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Fis - Todas as versões

## Objetivo

Este artigo descreve os passos necessários para validar a correta configuração da Regra de Cálculo no Configurador de Tributos do Protheus, garantindo que o cálculo dos impostos seja realizado corretamente nas notas fiscais.

## Procedimentos

### 1. Validação do Status da Regra de Cálculo

Para que o cálculo do tributo seja efetuado corretamente na nota fiscal, o campo **Status** da Regra de Cálculo deve estar configurado como:

* **1 - Aprovado**: O cálculo do tributo será aplicado normalmente.
* **2 - Em Teste**: O cálculo dos impostos será exibido apenas no Simulador, não afetando as notas fiscais reais.

### 2. Validação dos Perfis cadastrados na Regra de Cálculo

Após a aprovação da regra, o sistema valida os perfis definidos para determinar se o cálculo será aplicado. Os perfis são:

* **Perfil de Origem/Destino**  
  Define a origem e o destino da nota fiscal.
* **Perfil de Participante**  
  Indica o Cliente ou Fornecedor para o qual o tributo será calculado.
* **Perfil de Operação**  
  Composto por três validações que devem ser conferidas:

  + **CFOP**: Deve corresponder ao CFOP utilizado na TES (Tabela de Escrituração Fiscal).
  + **Tipo de Operação**: Caso haja necessidade de especificar um tipo, este deve ser configurado; se não, deve permanecer como "TODOS".
  + **Código de Serviço (B1\_CODISS)**: Caso o produto esteja vinculado a um código de serviço, este deve ser informado e deve coincidir com o código cadastrado no produto.
* **Perfil de Produto**  
  Deve incluir todos os produtos que terão o cálculo do tributo aplicado.

## Observações

* A configuração incorreta de qualquer perfil pode impedir o cálculo correto do tributo.
* Sempre valide os perfis antes de aprovar a regra para evitar inconsistências no cálculo dos impostos.
