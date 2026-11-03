---
content_hash: 54e7d24d2d248f527988dd4eed57a44da732bde5957c5a5e9dc77fb8f350959e
fetched_at: '2026-06-29T00:08:59.656550+00:00'
page_id: '364908987'
product: rm
source: tdn-rm
title: 1888818 MATESTCNTFTOF01-1341 DT Cópia de Vendedor/Comissão para o Movimento
  no Faturamento de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908987
version: 2
---

# CÓPIA DE VENDEDOR/COMISSÃO NO FATURAMENTO DE CONTRATO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Faturamento de Contrato. |
| **Situação/Requisito:** | Ao marcar a **Prioridade de origem das tabelas do movimento** para Item de Contrato e realizar o faturamento do contrato, a informação do **Código do Vendedor** e da **Comissão** são carregadas para o movimento considerando os dados informados no **Contrato**, e não do **Item de Contrato** como parametrizado. |
| **Solução/Implementação:** | Realizado o ajuste no faturamento do contrato para considerar as informações do **Código do Vendedor** e **Comissão** informados no **Contrato** e no **Item de Contrato** de acordo com a prioridade definida na parametrização.  Para que seja considerada a informação preenchida no item de contrato, é necessário marcar o parâmetro **Editar Comprador** como **Edita** na parametrização do tipo de movimento na etapa **Item - Tab - Comprador**. |
| **Conversores e Parâmetros:** | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.05 - Contratos | 04.05.04 - Faturamento | Definições Fat. de Contrato 2/3 | **Prioridade de origem das tabelas do movimento.**  Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Acessar a parametrização do tipo de movimento | Etapa Mov - Tab - Funcionário | **Edição Funcionário** e **Edição Comissão.**  Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Acessar a parametrização do tipo de movimento | Etapa Item - Tab - Comprador | **Editar Comprador/Mostrar Comprador.** |
| **Tickets relacionados:** | 1888818. |
| **Requisito:** | Faturamento de Contrato. |
| **Documento de Referência:** | Não se aplica. |
