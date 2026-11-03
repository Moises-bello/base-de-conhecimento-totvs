---
content_hash: 0972df45d43354fc48425ab7f46f4b26e45d879e1fdb40250f6cc07314103474
fetched_at: '2026-06-29T00:11:56.491595+00:00'
page_id: '866532675'
product: rm
source: tdn-rm
title: DT - Fórmula Visual - Função ISFVISUAL - Histórico de Assistência a Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866532675
version: 16
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Fórmula Visual |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-11273](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11273 "View this issue") |

## **02.** **VERSÕES**

Lembrando que, será a partir dos patches:

* 12.1.2310.2547
* 12.1.2402.220
* 12.1.2406.147 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

Ao tentar criar registro de histórico de assistência saúde utilizando a atividade "adicionar registro" via fórmula visual, o sistema apresenta o seguinte erro: "**A coluna 'FOIALTERADO' é somente leitura.**"

## **04.** **SOLUÇÃO**

Identificamos o problema principal que estava afetando a coluna **FOIALTERADO** no dataserver **FopHstAssistenciaSaudeData**. Para corrigir, foi criada a função **ISFVISUAL**, e para que os registros sejam corretamente gravados, é necessário incluir o **ISFVISUAL** na estrutura da fórmula visual.

Você pode fazer isso de forma simples, preenchendo o campo "Dados do Usuário" na opção "Ler Registro".

Para facilitar esse processo, preparamos alguns prints que mostram o passo a passo.

**Passo 1**: Atividade que lê os registros **rmsReadRecordActivity1**

É necessário preencher o campo "Dados do Usuário" com valor "ISFVISUAL" na atividade "Ler Registro".

**IMPORTANTE:** A função **ISFVISUAL** só funcionará para o datasever **FopHstAssistenciaSaudeData**

**Passo 2**: Atividade irá preencher os dados **rmsAddTableRowActivity1**

Preencha normalmente os dados a serem cadastrados.

**Passo 3**: Atividade irá salvar os dados **rmsSaveRecordActivity1**

Após salvar, basta executar a fórmula que os dados serão gravados corretamente.

## **05.****DEMAIS INFORMAÇÕES**
