---
content_hash: a3e8c1b7368c8c62a37f5af0d9bc49b373c3d4e4120e2333cd3bb428e0c18942
fetched_at: '2026-06-29T00:08:17.587687+00:00'
page_id: '256312282'
product: rm
source: tdn-rm
title: DT_Tags_Lacamento_Contabil
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Tags_Lacamento_Contabil
version: 5
---

# Tags do Laçamento Contábil

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | *RM* | | |
| ****Segmento Executor:**** | **Educacional** | | |
| **Módulo:** | **TOTVS Educacional** | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Geração do Lançamento Contábil.* | Mnemônico do Lançamentos Contábil |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Evento Contábil / Geração do Laçamento Contábil* | *Gerar Contabilização* | |  |  | | | |
| **Requisito (ISSUE):** | EDUEDU001-373/EDUEDU001-358 | | |
| **País:** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 Permite que o usuário adicione as tags que serão traduzidas no processo de contabilização de uma formas mais ágil.

## Definição da Regra de Negócio

# Contabilização por competência

Parametrizações necessárias (TOTVS Educacional):

Acessar os**Parâmetros | Integração | Contabilidade** e definir quais serão os eventos contábeis utilizados na contabilização:

Acessar o menu **Financeiro/Contábil | Contabilidade | Eventos Contábeis | Itens do Evento**  e editar o item do evento, mais especificamente o campo "Complemento Histórico" contido na aba de "Dados Complementares"

Nesta etapa fica a critério do cliente informar as tags(Mnemônicos) que serão traduzidas no processo de gerar a contabilização.

Informe as tags que serão traduzidas: 

Para executar a contabilização deve-se selecionar o contrato e acessar o processo "Gerar Contabilização".

Para verificar a informação gerada deve-se acessar o módulo Gestão Contábil no seguinte menu: **Escrituração contábil | Lotes | Laçamentos do Lote** e selecione o Lote parametrizado no TOTVS Educacional. Em seguida edite o lançamento para verificar que as tags parametrizadas no Item do Evento Contábil são traduzidas após o processo de contabilização.

# *Geração da Contabilização pelo Modulo Gestão Financeira.*

 Parametrizações necessárias (TOTVS Educacional):

 Acesse os **Parâmetros | Integração | Financeiro | Fin - Geral 2/3**.

Acessar o módulo Gestão financeira o menu **Financeiro | Cadastros | Eventos Contábil | Itens do Evento** e editar o item do evento, mais especificamente o campo "Complemento Histórico" contido na aba de "Dados Complementares"

No complemento do histórico o usuário poderá adicionar os Mnemônicos(Tag's) que serão traduzidas no processo de contabilizar. 

Observação: os Mnemônicos(Tag's) específicos do TOTVS Educacional só são exibidos se a integração entre os sistemas TOTVS Educacional e Gestão Financeira estiver ativo. Para verificar esta questão deve-se acessar **Ambiente | Parâmetros | Integrações de Sistemas** e verificar se  a Integração do RMClassis com o RMFluxus está ativa.

Após a parametrização da integração os Mnemônicos do Educacional serão exibidos juntamente com os Mnemônicos do Financeiro.

Informe as tag's que serão traduzidas no processo de Gerar a Contabilização.

Acessar  o módulo  TOTVS Educacional o menu Financeiro/Contábil | Contratos e filtrar o contrato ao qual será realizado a contabilidade. Acessar o anexos de "**Parcela"** e incluir uma nova parcela.

Selecionar a parcela e executar o processo "**Gerar Lançamento**", em seguida entrar na parcela e consultar o lançamento gerado (Clique na Ref:)

Acessar a aba Dados Adicionais | Contabilização | Inclusão | Editar os Item Contábil.

As tags parametrizadas no Item do Evento Contábil são traduzidas após o processo de contabilização.
