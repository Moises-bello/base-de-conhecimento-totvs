---
content_hash: 395d69793a0d8227235a9d9d6a56374091359055f97b891ea617d4c8b0ee61a7
fetched_at: '2026-06-29T00:08:31.239974+00:00'
page_id: '273296698'
product: rm
source: tdn-rm
title: 581045 MSAU-6616 DT Criação do Campo Número da Credencial no Cadastro de Visitantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273296698
version: 116
---

# Criação do Campo Número da Credencial no Cadastro de Visitantes

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Controle de Visitantes | |
| **Cadastros Iniciais:** | Visitante, Número do Cartão e Tipo de Visitante |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Tabelas Utilizadas:** | SZVISITANTE, SZLOGVISITANTE |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Foi criado o campo: Número da Credencial na tela de Entrada de Visitantes do Controle de Visitantes, onde é possível informar um código para informações como números de integração com catracas, ou qualquer outro tipo de código do visitante.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.13.165 deste chamado.

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Saúde), acesse Atendimento / Controle de Visitantes

                      Clique para adicionar um visitante em algum leito após a tela de controle de visitantes ser aberta.

       2.            Informe os dados e o Número da Credencial e clique em Ok.

                      O Sistema irá salvar as informações do Visitante com o número da credencial.

divs
