---
content_hash: 5aa7b51b36c15fb3fb665597c38efc9654f25d6c09132832c73e0c0cffc20329
fetched_at: '2026-06-29T00:05:52.745333+00:00'
page_id: '1059323693'
product: rm
source: tdn-rm
title: Estados de Fornecimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Estados+de+Fornecimento
version: 3
---

Atenção

Recurso disponível na release 12.1.2606 ou superior.

## **01. VISÃO GERAL**

Estados de Fornecimentos permitem vincular o Cliente/Fornecedor aos estados aos quais tem fornecimento de produtos para compra.

## **02. EXEMPLO DE UTILIZAÇÃO**

Está localizado no menu: **Cadastros → Financeiros → Clientes/Fornecedores → Anexos → Estados de Fornecimento.**

**Tela principal:**São exibidos todos Estados de Fornecimento existentes de acordo com o filtro utilizado. Caso o estado esteja vinculado a uma Região será exibido um registro para cada região vinculada. Vale ressaltar que trata-se de um único registro de estado de fornecimento, o vínculo será sempre por estado e não por região (esta aparece somente para demonstração).

**Cotação:** No assistente de inclusão de cotação será possível filtrar incluir um novo fornecedor filtrando pelo Estado de Fornecimento.

IMPORTANTE: para ter acesso a este cadastro é necessário realizar a configuração do perfil de usuário no módulo TOTVS Gestão de Estoque, Compras e Faturamento.

## **03. TABELAS UTILIZADAS**

* TETDFORNECIMENTOCFO - Tabela responsável pelo vínculo entre o Cliente/Fornecedor e o Estado par qual fornece produtos para compra.
