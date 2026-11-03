---
content_hash: 131820ecad4c6947217e1e2e9b5f17d02b5b50bc343fe6cc0ab062bf5c967414
fetched_at: '2026-06-29T00:05:51.585317+00:00'
page_id: '1052325494'
product: rm
source: tdn-rm
title: DT - S-2200 e  S-2006 - Tratativa na geração da tag <observação>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1052325494
version: 11
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-2200 e  S-2006 - Tratativa na geração da tag <observação> |
| País: | Brasil |
| Issue: | [DRHROTRM-15563](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15563) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2506.280
* 12.1.2510.200
* 12.1.2602.123 e superiores

## **03. SITUAÇÃO/REQUISITO**

Na geração do XML do evento S-2206, a tag `<observação>` está sendo enviada em todas as gerações, inclusive quando a informação já foi transmitida anteriormente em outro evento S-2206.

Como consequência, essa repetição está sendo refletida na CTPS Digital do funcionário, gerando duplicidade de informações.

## **04. SOLUÇÃO**

Para tratar a situação, foi implementado o campo **“Data de Mudança”** no menu Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Observações Contratuais.

Com essa implementação, a geração dos arquivos XML dos eventos S-2200 e S-2206 passa a considerar a tag `<observação>` apenas quando houver vínculo com a competência processada, evitando o envio indevido de informações já declaradas anteriormente.

**Atenção:** registros com o campo de data não preenchido continuarão sendo considerados na geração do arquivo, sendo enviados normalmente.

**Exemplo:**

Foi inserindo uma observação no momento da admissão e com o campo data de mudança nulo.

Ao gerar o XML, a tag <observacoes> será apresentada corretamente, assumindo a data de admissão para geração da informação.

Ao inserir um novo registro com o campo **"Data de Mudança"** preenchido, será disparado o gatilho do evento S-2206.

Ao gerar o XML, a tag <observacoes> terá as duas observações observações incluídas, pois o primeiro registro possui o campo nulo.

## **05. DEMAIS CONSIDERAÇÕES**
