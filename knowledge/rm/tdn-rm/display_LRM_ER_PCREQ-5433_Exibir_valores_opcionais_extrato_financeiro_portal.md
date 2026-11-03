---
content_hash: 0c9dda357f68c1d67432b3dd17c17a57b4d16fb18fd539cfea8a4760625d1d6e
fetched_at: '2026-06-29T00:06:19.414655+00:00'
page_id: '219697764'
product: rm
source: tdn-rm
title: ER_PCREQ-5433_Exibir_valores_opcionais_extrato_financeiro_portal
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5433_Exibir_valores_opcionais_extrato_financeiro_portal
version: 8
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | WBS\_R\_EDU016\_1219 | **IRM1** | PCREQ-5432 |
| **Requisito1** | PCREQ-5433 | **Subtarefa1** | PDR\_EDU\_EDU011-520 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Permitir que o cliente possa parametrizar quais campos devem ser exibidos para o usuário na tela de consulta do extrato financeiro do Portal Educacional, incluindo os 8 (oito) valores opcionais existentes no TOTVS Gestão Financeira.

## Definição da Regra de Negócio

Atualmente, no TOTVS Gestão Financeira temos 8 (oito) valores opcionais que podem ser parametrizados pelo cliente. A partir da release 12.1.9 deverá ser possível que o cliente parametrize quais desses valores deverão ser exibidos na tela de extrato financeiro e impressão de segunda via do boleto do Portal Educacional.

No modelo atual, todos os campos existentes na tela são fixos e não é permitido ao cliente definir quais deles serão exibidos. Essa limitação será retirada, possibilitando que o cliente escolha dentre os campos "situação", "serviço", "parcela", "cota", "Competência", "data de baixa", "Valor bruto", "juros", "multa", "desconto" e "baixado", quais serão exibidos. Os campos "responsável financeiro" e "vencimento" continuam sempre sendo exibidos.

Os campos fixos "bolsas até o vencimento", "bolsas" correspondem a valores opcionais definidos pelo usuário nos parâmetros da integração financeira do educacional "Bolsas válidas ATÉ o vencimento" e "Bolsas válidas APÓS o vencimento", por isso, esses campos deixarão de ser fixos e passarão a ser parametrizados conforme os valores opcionais. Um script foi criado e disponibilizado na versão para ler os parâmetros da integração financeira do educacional e já marcar os valores opcionais que estiverem parametrizados.

Além das alterações já citadas, o nome "IPTE" deve ser substituído por "Linha Digitável" e só deverá ser exibido caso haja valor, caso contrário não deve ser mostrado.

Para permitir que o cliente configure quais campos serão exibidos deverá ser criada uma nova pasta no grupo de parâmetros do portal (TOTVS Educacional | Configurações | Parâmetros | RM Portal | RM Portal - Gerais) onde deverão ser agrupadas as opções já existentes de parametrização para emissão de boleto bancário com as opções de visualização dos campos na tela. Um novo agrupador chamado "Extrato financeiro" será criado, contendo os campos que antes eram fixos (Colunas a exibir) e os valores opcionais do financeiro (Valores opcionais a exibir).

O usuário poderá selecionar todos os campos para exibição, totalizando dezenove. Uma mensagem será emitida, no momento da parametrização, caso o mesmo selecione mais de 12 campos. Essa mensagem será apenas uma alerta indicando ao usuário que, ao selecionar mais de 12 campos, o layout da tela de extrato financeiro poderá ser comprometido.

Serão exibidos os oito valores opcionais do TOTVS Gestão Financeira com o texto "Valor opcional X", onde X corresponde ao número do valor opcional (ex: Valor opcional 7). Esse texto será seguido pelo nome parametrizado no TOTVS Gestão Financeira, caso esteja sendo utilizado. Se o valor opcional não estiver configurado no TOTVS Gestão Financeira, seu nome não será exibido após o texto "Valor opcional X".

Se o usuário marcar um valor opcional no TOTVS Educacional que não esteja configurado no TOTVS Gestão Financeira, o valor será exibido zerado.

Com base nessa parametrização a tela de extrato financeiro do portal deverá ser desenhada dinamicamente respeitando as opções de visualizações de campos definidas nos parâmetros*.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Parâmetros] | [Alteração] | [TOTVS Educacional -> Configurações -> Parâmetros -> RM Portal -> RM Portal - Gerais] | - |
| [Extrato Financeiro] | [Alteração] | [Portal Educacional -> Financeiro -> Extrato Financeiro] | - |

***Tabelas Utilizadas***

* *SPARAM – Cadastro de parâmetros do TOTVS Educacional*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
