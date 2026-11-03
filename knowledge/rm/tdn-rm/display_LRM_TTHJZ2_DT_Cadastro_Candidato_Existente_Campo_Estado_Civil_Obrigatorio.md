---
content_hash: dbba0c45122958d06e8d055ed36c107d5decb256aeb64b356266ee8ddd6f1f2d
fetched_at: '2026-06-29T00:06:11.748512+00:00'
page_id: '203770665'
product: rm
source: tdn-rm
title: TTHJZ2_DT_Cadastro_Candidato_Existente_Campo_Estado_Civil_Obrigatorio
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHJZ2_DT_Cadastro_Candidato_Existente_Campo_Estado_Civil_Obrigatorio
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Cadastro de candidato* |
| **Situação/Requisito:** | *Quando é feito o cadastro de um candidato que já existe no cadastro de pessoa do sistema, o portal retorna que é obrigatório o preenchimento do campo estado civil, sendo que este problema só ocorre em bases de dados Oracle.* |
| **Solução/Implementação:** | *Foi verificado que o sistema não removia os espaços no começo e no fim do nome do candidato, sendo assim, no momento de buscar a pessoa existente o sistema não conseguia encontrar pelos espaços a mais no registro da base de dados, ao ajustar a consulta para remover os espaços a comparação passou a ser feita corretamente..* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41* |
