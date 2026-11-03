---
content_hash: c75aafbf1accb104e5582373e9d46f6381c6b69612354c5f418d95ff9862ad7f
fetched_at: '2026-06-29T00:12:02.098419+00:00'
page_id: '899189200'
product: rm
source: tdn-rm
title: DT - S-2206 - Tratar a geração da tag <dtAlteracao> quando for dissídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=899189200
version: 14
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-2206: Tratar a geração da tag <dtAlteração> quando for dissídio |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10835](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10835) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.260
* 12.1.2406.208
* 12.1.2410.136 e superiores

## **03. SITUAÇÃO/REQUISITO**

Permitir que, na alteração salarial por dissídio, seja possível definir a data a ser preenchida no campo "Data de Inclusão", pois atualmente, esse campo é automaticamente preenchido com a data  da execução do aumento (data do sistema operacional). No entanto, em situações onde a alteração não é processada no mesmo dia em que o dissídio foi liberado, a data inserida fica incorreta, resultando em inconsistências na geração do evento S-2206, que utiliza este campo para preencher a tag `<dtAlteracao>`.

## **04. SOLUÇÃO**

1) Menu Administração de Pessoal | Alteração Global de Salários

Ao selecionar o motivo **"Dissídio"** no campo **"Motivo alteração salarial"**, o parâmetro **"Alterar Data de Inclusão"** será exibido, e:

* Se este parâmetro for marcado, o campo **"Data de Inclusão"** será habilitado, permitindo ao usuário informar a data real de liberação do dissídio.
* Caso o parâmetro não esteja marcado, o sistema preencherá automaticamente o campo com a data atual do sistema operacional.

**ATENÇÃO:**

* + É obrigatório preencher o campo **"Data de Inclusão"** caso o parâmetro **"Alterar Data de Inclusão"** esteja marcado.
  + Por padrão, o campo **"Data de Inclusão"** será preenchido com a data atual do sistema operacional.

2) Menu eSocial | Gerar XML

Na geração do evento **S-2206**, a tag `<dtAlteracao>` será preenchida com a data informada no campo **"Data de Inclusão"** presente no histórico salarial do funcionário.

**05. DEMAIS INFORMAÇÕES**
