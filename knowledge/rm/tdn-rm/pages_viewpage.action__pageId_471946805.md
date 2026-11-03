---
content_hash: 545046cafabccb681caf6d7f18a1cba18da788f7f09dbddebcd02c80e6738e13
fetched_at: '2026-06-29T00:10:16.547229+00:00'
page_id: '471946805'
product: rm
source: tdn-rm
title: FISCAL01-7866 DT Cadastro de Tabela Dinâmica da ECF - Lalur Parte B
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=471946805
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro de Tabela Dinâmica da ECF |

## **02. SITUAÇÃO/REQUISITO**

No cadastro da tabela dinâmica será necessário realizar a seguinte alteração:

1. Campo "Grupo": criar a opção "**Lalur Parte B**"
2. No campo "Indica qual o tributo", criar a opção "**Ambos**". Essa opção poderá ser marcada somente quando o Grupo for Lalur parte B.

## **03. SOLUÇÃO**

- No cadastro de tabela dinâmica da ECF foi criado o grupo Lalur Parte B e o no campo "indica qual tributo" a opção Ambos, também foi implementado validação onde ambos deve ser selecionado somente quando o grupo for Lalur Parte B.

- No processo de Importação da tabela dinâmica também foi implementado a validação acima.

- Foi desabilitado o botão de excluir no cadastro de tabela dinâmica da ECF porque já existe o processo com o mesmo propósito e com mensagens amigáveis.

Novos registros do plano paralelo do M010 importado.
