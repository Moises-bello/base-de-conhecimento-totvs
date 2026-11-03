---
article_id: 28085510022295
category: Financeiro
content_hash: 0b68e9fab960882915aa7ebd638a5a7e8a9054a1b56869f65f69a689f5183421
fetched_at: '2026-06-28T22:38:00.889833+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Atualização do dicionário
  SX1 - UPDDISTR e migrador de versão
type: support-article
updated_at: '2024-11-26T20:49:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28085510022295-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Atualiza%C3%A7%C3%A3o-do-dicion%C3%A1rio-SX1-UPDDISTR-e-migrador-de-vers%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28085481190551) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

Ao executar o comando **UPDDISTR** no sistema, o campo de pergunta é atualizado e retorna ao padrão?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

A tabela abaixo descreve quais as regras para atualização dos campos do dicionário de perguntas **SX1**, quando executada atualização via ferramenta **UPDDISTR** ou migrador de versão.

O objetivo destas regras é efetuar as atualizações de dicionários e ao mesmo tempo respeitar as personalizações efetuadas por nossos clientes utilizando ferramentas como por exemplo o configurador.

As regras são válidas apenas para alteração de grupos e ordens de perguntas existentes. Grupos / ordens novos são gravados integralmente.

**Dicionário destino**: dicionário do cliente.

**Novo dicionário**: dicionário do pacote de atualização ou da nova versão (SXSppp.TXT ou SDFppp.TXT, onde **ppp** refere-se à sigla da localização).

| Campo | Descrição | Regra |
| --- | --- | --- |
| X1\_PRESEL | Item pré-selecionado (sugerido) do combobox | Nunca atualiza |
| X1\_CNT01 | Conteúdo 1 | Nunca atualiza |
| X1\_CNT02 | Conteúdo 2 | Nunca atualiza |
| X1\_TAMANHO | Tamanho | Atualiza se não possuir grupo de campos (SXG) vinculado. Se possuir, sempre será respeitado o tamanho definido pelo grupo do dicionário destino. |
| Demais campos |  | Sempre atualiza |

**Saiba mais**

[Regras para atualização do dicionário SX1 - UPDDISTR e migrador de versão](https://tdn.totvs.com/pages/releaseview.action?pageId=189313016)
