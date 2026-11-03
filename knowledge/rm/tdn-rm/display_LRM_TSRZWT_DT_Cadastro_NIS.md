---
content_hash: a480f71ff2e9aeba1a6b8a02edd9d26324058af1476ccee41556cadb2afc2377
fetched_at: '2026-06-29T00:06:01.406447+00:00'
page_id: '198937833'
product: rm
source: tdn-rm
title: TSRZWT_DT_Cadastro_NIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TSRZWT_DT_Cadastro_NIS
version: 2
---

# CADASTRO NIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro Nis* |
| **Situação/Requisito:** | *Ao gerar arquivo NIS em lote, funcionários saem duplicados.* |
| **Solução/Implementação:** | Verificamos que a inconsistência na duplicidade de registros no arquivo deve-se ao fato existir mais de uma ocorrência do mesmo município (tabela GMUNICIPIO) para o mesmo Estado. Foi realizado ajuste na consulta SQL para evitar problema de duplicidade de registros quando existirem dois municípios cadastrados com o mesmo nome e para o mesmo Estado. Ex: Rio de Janeiro |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** |  |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.83.55* |
