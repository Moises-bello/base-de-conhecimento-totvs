---
content_hash: 486b733fdd3d8777983204b1647ebba1af3728f96fbb63af36300521d036c7e1
fetched_at: '2026-06-29T00:10:12.330429+00:00'
page_id: '454449598'
product: rm
source: tdn-rm
title: '4751311 FISCAL01-7737 DT Processo de Escrituração - Cupom Fiscal Erro: Cupom
  Inicial já incluído'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454449598
version: 2
---

# Processo de Escrituração - Cupom Fiscal Erro: Cupom Inicial já incluído

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Processo de Escrituração Fiscal |
| **Situação/Requisito:** | Erro escriturar Redução Z Ao tentar Escriturar Redução Z o sistema está retornando a seguinte mensagem: Erros no Serviço de Inclusão de Lançamentos Erro na Inclusão do Registro: Documento 00101339 - Série ECF5 - Data 01/12/2018: Cupom Inicial já incluído. |
| **Solução/Implementação:** | 1 - Foi retirada do Serviço de Inclusão de Lançamentos a validação do  sequencial de Cupom para Lançamentos vindos da Escrituração Fiscal  2 - Foi alterada a forma de atualização do campo CONTADORORDEMOP do cadastro de Maquina  para que o mesmo seja atualizado somente se o sequencial do Lançamento for maior que o sequencial  do Cadastro da Maquina. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
