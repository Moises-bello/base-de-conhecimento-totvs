---
content_hash: cb8077095333fc6d1535ae02b19799c36d873dd18f38d7e056e12b434866cf46
fetched_at: '2026-06-29T00:06:10.422886+00:00'
page_id: '203762981'
product: rm
source: tdn-rm
title: TTDIS1_DT_Lancamento_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDIS1_DT_Lancamento_Financeiro
version: 1
---

# Lançamento financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Lançamento financeiro* |
| **Situação/Requisito:** | Ao realizar um lançamento financeiro para um autônomos no RMFluxus, utilizando um cadastro de Cliente e Fornecedor Global e gerar a guia de INSS no RMLabore marcando o parâmetro de importar autônomos do RMFluxus, ocorre mensagem de erro restrição de integridade (RM.FKPFITEMLAN\_FCFO) violada |
| **Solução/Implementação:** | Verificamos que a chave estrangeira FKPFITEMLAN\_FCFO na tabela PFITEMLAN está ligando as colunas CODCOLIGADA e CODCFO. Mas na verdade as colunas deveriam ser CODCOLCFO e CODCFO. Pois o cliente fornecedor pode ser global (coligada igual a zero), e nesse caso deve ser possível inserir o cliente fornecedor global para CODCOLIGADA igual a 1 por exemplo.  Foi solicitado script, que sairá no conversor da 12.1.8, para corrigir o problema da chave |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTDIS1 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
