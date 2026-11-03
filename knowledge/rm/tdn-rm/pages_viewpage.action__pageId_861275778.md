---
content_hash: 2c709262a0f2c9d4d67add403ceb0feef02f9b7d3ee4737535f4e71b726ad31f
fetched_at: '2026-06-29T00:11:55.452841+00:00'
page_id: '861275778'
product: rm
source: tdn-rm
title: DT - Dependente - Alteração da descrição do grau de parentesco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=861275778
version: 11
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Dependente - Alteração da descrição do grau de parentesco |
| País: | Brasil |
| **Requisito/Story/Issue (informe o requisito relacionado) :** | [DRHROTRM-9736](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9736) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.237
* 12.1.2402.195
* 12.1.2406.122 e superiores

## **03. SITUAÇÃO/REQUISITO**

Alterar a descrição dos graus de parentesco conforme RFB [Lei 13.146/2015](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/imposto-de-renda/dirpf/deducoes/29-despesa-com-dependente#:~:text=Podem%20ser%20dependentes%3A&text=Filho(a)%20ou%20enteado(a)%2C%20se%20ainda,as%20dedu%C3%A7%C3%B5es%20autorizadas%20por%20lei.):

| De | Para |
| --- | --- |
| Filho(a) Válido | Filho(a) sem deficiência |
| Filho(a) Inválido | Filho(a) com deficiência |

## **04. SOLUÇÃO**

 Após a liberação da versão será necessário executar os scripts de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe** para que seja atualizada a tabela PCODPARENT.
