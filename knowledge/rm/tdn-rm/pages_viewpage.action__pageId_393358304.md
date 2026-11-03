---
content_hash: d32e69c3d9537f0e910d596527993aa2e15dda878ecb140749fff41b5b2b8c66
fetched_at: '2026-06-29T00:09:09.275852+00:00'
page_id: '393358304'
product: rm
source: tdn-rm
title: 3638498 MATESTCNTFTOF01-3130 DT Requisição de Materiais - Tabelas de Classificação
  valor default
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393358304
version: 4
---

# REQUISIÇÃO DE MATERIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Manutenção. |
| **Função:** | Requisição de Materiais. |
| **Situação/Requisito:** | Ao gerar Requisição de Material para uma Ordem de Serviço os campos de Tabelas de Classificação são copiados do movimento de Ordem de Serviço (OS). Quando o movimento de OS não utiliza ou utiliza tabelas de classificação mas não possui valores definidos, ao criar o movimento de Requisição de Material o sistema não está considerando o Default das Tabelas de Classificação definidas no Tipo de Movimento de Requisição de Material. |
| **Solução/Implementação:** | Ao gerar a Requisição de Material para Ordem de Serviço, caso o movimento de OS não possuir valores dos campos de Tabelas de Classificação e o movimento de Requisição de Material estiver configurado com valor default, este valor default será utilizado na criação do movimento de requisição de material. |
| **Conversores e Parâmetros:** | Configurações necessárias para utilizar Tabela de Classificação no Movimento  Acesse o módulo Gestão de Estoque, Compras e Faturamento menu Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento.   1. Parâmetros Gerais \ Tabelas \ Classificação e defina que a tabela será utilizada em movimento, marcar a opção **Usar em Movimento.** 2. Selecione o processo onde está localizado o tipo de movimento utilizado como Requisição de Material, acesse a opção de parametrizar o tipo de movimento e na **Etapa Movimento - Tabelas - Classificação** no campo **Editar** selecione **Edita** ou **Mostra** e defina um valor no campo **Default** da respectiva tabela. |
| **Tickets relacionados:** | 3638498 |
| **Requisito:** | MntRequisicaoMaterialProcAction |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/MNT/MNT.RequisicaoMaterial.aspx>. |
