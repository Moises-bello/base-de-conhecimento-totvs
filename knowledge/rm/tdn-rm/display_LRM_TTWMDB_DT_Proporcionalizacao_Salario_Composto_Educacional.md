---
content_hash: 5941afba6b6b543a3d8feb78eb6740e224a1bdaedd2aee88916cbb1fb36ebb84
fetched_at: '2026-06-29T00:06:22.426759+00:00'
page_id: '223917208'
product: rm
source: tdn-rm
title: TTWMDB_DT_Proporcionalizacao_Salario_Composto_Educacional
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWMDB_DT_Proporcionalizacao_Salario_Composto_Educacional
version: 2
---

# PROPORCIONALIZAÇÃO DO SALÁRIO COMPOSTO LANÇADO PELO EDUCACIONAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Grupo de Eventos* |
| **Situação/Requisito:** | *Quando os eventos de salário composto são lançados pelo processo de 'Reprogramação Salarial', os valores são proporcionalizados conforme a data de encerramento das atividades.*  *Ao realizar o lançamento de salário composto pelo Grupo de Eventos, o valor é proporcionalizado novamente considerando dias de férias no mês. Assim, o mesmo evento está sendo proporcionalizado duas vezes.* |
| **Solução/Implementação:** | *Ajuste no lançamento de salário composto pelo Grupo de Eventos, para não efetuar a proporcionalização pelos dias trabalhados no mês, quando usa integração com o Educacional e está parametrizado para proporcionalizar número de dias, na pasta Integraçao/Gestão Educacional, do Parametrizador.* |
| **Chamados   relacionados:** | *TTWMDB, TTZEBC* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
