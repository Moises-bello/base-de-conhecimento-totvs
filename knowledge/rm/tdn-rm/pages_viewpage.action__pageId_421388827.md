---
content_hash: 8bde40c33edd4b4c4b26e842e07e08a02f8c016514b73e0e378a8db46c03b46a
fetched_at: '2026-06-29T00:09:19.213553+00:00'
page_id: '421388827'
product: rm
source: tdn-rm
title: FIN - Download de Cotações 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388827
version: 4
---

Através desta funcionalidade é possível realizar o download das cotações via Internet com o objetivo de atualizar a tabela de cotações da Moeda ou as variações do Índice. Disponível no Menu: Movimentações Bancárias | Moedas | Download das cotações.  
A tabela atualizada será a GCOTACAO.  
Para realizar o processo necessário:

1. No wizard do processo marcar as moedas que serão atualizadas através do download de cotações.
2. Preencher os dados essenciais para o download, será informada apenas na primeira vez. Os dados serão armazenados no banco de dados para os próximos downloads.

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Símbolo de Referência | Moeda de referência |
| URL | Endereço do arquivo texto na Internet de onde se deve buscar as cotações.   Ex: [{+}](http://www.bndes.gov.br/Moedas/um006.txt)<http://www.bndes.gov.br/Moedas/um006.txt+>  (URTJLP) |
| Formato do Arquivo de Origem | Formato do arquivo texto: CSV (significa campos separados por ponto e vírgula). |
| Campo Data de Origem | Mapeamento do campo data para alimentar a tabela GCOTACAO. |
| Campo Valor de Origem | Mapeamento do campo valor para alimentar a tabela GCOTACAO. |
| Possui Cabeçalho | Indica se a primeira linha do arquivo texto representa os nomes das colunas. |

**Para os campos:                                Informar:**

Campo Data de Origem                                                      Data  
 Campo Valor de Origem                                                     Valor   
 Possui Cabeçalho                                                               Sim

Necessário aguardar o processo de download da cotação.

Este download deverá sobrepor as cotações informadas manualmente pelo usuário, supondo que a fonte de dados da Internet esteja sempre correta.
