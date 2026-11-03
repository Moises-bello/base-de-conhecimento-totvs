---
content_hash: 15b8eddb96a3ef3b83e1a76801a7db2859bbf7ccf79a93d68671e32cec323c86
fetched_at: '2026-06-29T00:06:21.132467+00:00'
page_id: '223162026'
product: rm
source: tdn-rm
title: DT_Exibir_valores_opcionais_extrato_financeiro_portal
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Exibir_valores_opcionais_extrato_financeiro_portal
version: 5
---

# EXIBIR VALORES OPCIONAIS NO EXTRATO FINANCEIRO DO PORTAL

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Portal* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Extrato financeiro* | *Extrato financeiro no portal* | |
| **Parâmetro(s):** | [TOTVS Educacional -> Configurações -> Parâmetros -> RM Portal -> RM Portal - Gerais] |
| **Requisito (ISSUE):** | PCREQ-5433 |
| **País(es):** | *Brasil* |
| **Versões/Release:** | *12.1.9* |

## Descrição

Permitir que o cliente possa parametrizar quais campos devem ser exibidos para o usuário na tela de consulta do extrato financeiro do Portal Educacional, incluindo os 8 (oito) valores opcionais existentes no TOTVS Gestão Financeira.

## Procedimento para Utilização

Atualmente, no TOTVS Gestão Financeira temos 8 (oito) valores opcionais que podem ser parametrizados pelo cliente. A partir da release 12.1.9 será possível parametrizar quais desses valores serão exibidos na tela de extrato financeiro e impressão de segunda via do boleto do Portal Educacional. 

No modelo atual, todos os campos existentes na tela são fixos e não é permitido ao cliente definir quais deles serão exibidos. Essa limitação foi retirada, possibilitando que o cliente escolha dentre os campos"situação", "serviço", "parcela", "cota", "Competência", "data de baixa", "Valor bruto", "juros", "multa", "desconto" e "baixado", quais serão exibidos. Os campos "responsável financeiro" e "vencimento" continuam sempre sendo exibidos.

Os campos fixos "bolsas até o vencimento", "bolsas" correspondem a valores opcionais definidos pelo usuário nos parâmetros da integração financeira do educacional "Bolsas válidas ATÉ o vencimento" e "Bolsas válidas APÓS o vencimento", por isso, esses campos deixarão de ser fixos e passarão a ser exibidos conforme parametrização dos valores opcionais.

O nome "IPTE" passa a ser definido como "Linha Digitável" e só será exibido caso haja valor, caso contrário não deve ser mostrado.

Para permitir que o cliente configure quais campos serão exibidos foi criada uma nova pasta no grupo de parâmetros do portal (TOTVS Educacional | Configurações | Parâmetros | RM Portal | RM Portal - Gerais) agrupando as opções já existentes de parametrização para emissão de boleto bancário com as opções de visualização dos campos na tela. Um novo agrupador chamado "Extrato financeiro" foi criado, contendo os campos que antes eram fixos (Colunas a exibir) e os valores opcionais do financeiro (Valores opcionais a exibir).

Serão exibidos os oito valores opcionais do TOTVS Gestão Financeira com o texto "Valor opcional X", onde X corresponde ao número do valor opcional (ex: Valor opcional 7). Esse texto será seguido pelo nome parametrizado no TOTVS Gestão Financeira, caso esteja sendo utilizado. Se o valor opcional não estiver configurado no TOTVS Gestão Financeira, seu nome não será exibido após o texto "Valor opcional X".

Se o usuário marcar um valor opcional no TOTVS Educacional que não esteja configurado no TOTVS Gestão Financeira, o valor será exibido zerado.

Com base nessa parametrização a tela de extrato financeiro do portal será desenhada dinamicamente respeitando as opções de visualizações de campos definidas nos parâmetros*.*

divs
