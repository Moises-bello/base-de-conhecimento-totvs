---
content_hash: 0e1d763ac230ff43766a61320a6e295c105b7863a9b1fc6dc3a6781d7799694d
fetched_at: '2026-06-29T00:09:52.823353+00:00'
page_id: '439692554'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-6031 DT Implementação da tag autXML para MDF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439692554
version: 7
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice. |
| **Módulo:** | Totvs Gestão de Estoque, Compras e Faturamento. |
| **Função:** | MDF-e |
| **Situação/Requisito:** | Em atendimento ao manual destes DF-e, a implementação desta *tag* se faz necessária, a fim de atender também às demandas  do mercado. |
| **Solução/Implementação:** | Implementação referente aos documentos fiscais eletrônicos (DF-e) geridos pelo TOTVS Gestão de Estoque, Compras e Faturamento,  contemplando movimento e envio. |
| **Conversores e Parâmetros:** | Ambiente | Gestão de Estoque, Compras e Faturamento | Parâmetros Vendas | Faturamento | Tipo de Mov, | Aba Fis - Conhecimento de Transporte |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | Stories: MATFATCMPCRM01-6031. |
| **Documento de Referência:** | N/A. |
| **Tabelas:** | TAUTDOC; |

# Descrição

Para esta implementação, dois pontos importantes sofreram alterações: Movimento e Envio de Documentos Eletrônicos (MDF-e).

Parametrização necessária: na Etapa 69 - Fis - Conhecimento de Transporte, a opção 'Tipo de Operação do Conhecimento de Transporte' deve ser 'Emitir MDF-e'.

### Movimento

Após parametrizado corretamente, o movimento deverá apresentar a aba 'XML - Autorizados para Download do DF-e' em seu menu, dentro do grupo 'Integrações'.

Nela estará contida uma Matriz Editável, responsável por armazenar as informações dos responsáveis autorizados para realizar download do XML.

Campos:

* Sequencial: Tipo inteiro de tamanho (4), não editável e auto incrementável;
* CNPJ/CPF do Autorizado: Tipo string de tamanho (20).

# Procedimento para Implantação

O sistema é atualizado logo após aplicação do pacote de atualizações 12.1.23.1 e posteriores à esta demanda.
