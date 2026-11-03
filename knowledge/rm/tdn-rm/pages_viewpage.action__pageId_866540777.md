---
content_hash: 8be6857637d188b842887e0a958afc8e028e965c9475c1d812d3e23cca594cc6
fetched_at: '2026-06-29T00:11:56.498770+00:00'
page_id: '866540777'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência INSS Patronal - Depósito do montante em juízo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866540777
version: 6
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Relatório de Conferência INSS Patronal - Depósito do montante em juízo |
| País: | Brasil |
| **Requisito/Story/Issue (informe o requisito relacionado) :** | [DRHROTRM-7815](https://jiraproducao.totvs.com.br/browse/DRHROTRM-7815 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2402.221
* 12.1.2406.149 e superiores

## **03. SITUAÇÃO/REQUISITO**

Viabilizar a conferência dos valores declarados no eSocial com os valores da folha de pagamento, considerando que, mesmo com a suspensão das contribuições, esses valores continuam sendo depositados em um processo legal. É necessário confrontar essas informações com os dados enviados na DCTFWeb.

## **04. SOLUÇÃO**

Foi implementado o campo **Depósito do Montante Integral** em Eventos | Anexos | Processo de Suspensão de Incidência. Ao marcar esse parâmetro, na geração do **Relatório de Conferência INSS Patronal**, os valores da base da folha passam a ser considerados para comparação com os valores retornados pela DCTFWeb.

**Passo 1 -** Após a atualização da versão será necessário executar o script para a criação do campo **Depósito do Montante Integral,** através do sistema RM.Atualizador.exe.

**Passo 2**- Acesse Administração de pessoal | Eventos | Eventos | Anexos | processo de suspensão de incidência, edite o processo cadastrado e marque o novo parâmetro **Depósito do Montante Integral.**

**Passo 3 -** Após marcar os eventos que serão considerados, basta gerar novamente o Relatório de Conferência INSS Patronal, disponível emeSocial | Relatório de Conferência INSS Patronal. Os valores serão comparados corretamente.

## **04.****ASSUNTOS RELACIONADOS**

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718749>
