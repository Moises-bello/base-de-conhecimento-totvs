---
content_hash: 4f98950e7348157ff0873315bd6c0fe8df9f87c92d5240bd5adfa9dd82bdbcd2
fetched_at: '2026-06-29T00:08:04.574831+00:00'
page_id: '235574862'
product: rm
source: tdn-rm
title: ER_PCREQ-10848_Detalhamento_de_Glosas
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10848_Detalhamento_de_Glosas
version: 117
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Detalhamento de Glosas

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_RM\_V12\_1516 | **IRM1** | PCREQ-10847 |
| **Requisito1** | PCREQ-10848 | **Subtarefa1** | SAU\_DEV-4631 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

O objetivo desta especificação é disponibilizar uma maneira de detalhar as informações do controle de glosa recebidas dos convênios. O sistema deve disponibilizar campos para se informar o valor da glosa, o valor do desconto, o pagamento a maior e o valor irrecuperável.

### (Obrigatório)

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Gerais | [Alteração] | Opções -> Parâmetros | RN01 |
| Controle de Glosas | [Alteração] | Faturamento -> Controle de Glosas | RN02 |
| Recurso de Glosas | [Alteração] | Faturamento -> Recurso de Glosas | RN03 |

**RN01:**Criação do parâmetro "Permite informar o valor da glosa ou do pagamento a maior (O sistema não calculará esses valores automaticamente (Valor pago - valor apresentado))", na aba Controle e recurso de glosas, com o valor default como desmarcado.

**RN02:** No controle de glosas, ao efetuar uma glosa, na tela em que são informados o valor pago, o motivo da glosa, incluir mais dois campos: o valor da glosa e o valor do pagamento a maior. O valor unitário aprovado não sofrerá mais recálculo quando o valor do desconto for informado. Os dois novos campos serão preenchidos pelo sistema com o Valor pago - valor apresentado,  porém o usuário poderá alterar da maneira que convier. Algumas validações devem ser feitas: valor irrecuperável não pode ser maior que o valor da glosa e (Valor unitário cobrado + valor a maior - desconto - valor da glosa = Valor unitário aprovado). Este funcionamento deve ocorrer somente se o parâmetro informado na regra 01 estiver marcado.

**RN03:**No recurso de glosa, recalcular o valor a ser recursado baseado apenas no valor da glosa menos o valor irrecuperável. O valor do desconto não pode ser recursado.

**Tabelas Utilizadas**

* SZCONTROLEGLOSAITEM
  + Adicionar o campo VALORGLOSA e VALORAMAIOR

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
