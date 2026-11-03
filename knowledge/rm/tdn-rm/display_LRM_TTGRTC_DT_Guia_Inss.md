---
content_hash: e47534688e7a5a253725ae3611c169c86ee33d6206123c756b99273862d87610
fetched_at: '2026-06-29T00:06:13.458914+00:00'
page_id: '208341983'
product: rm
source: tdn-rm
title: TTGRTC_DT_Guia_Inss
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGRTC_DT_Guia_Inss
version: 2
---

# Guia de INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Guia de INSS* |
| **Situação/Requisito:** | Ao gerar um lançamento financeiro através da Guia de INSS, selecionando a opção Importa Autônomos RM Fluxus / RM Nucleus, quando há um cliente/fornecedor global, tipo pessoa física que possui cadastro apenas no financeiro, o sistema apresenta um erro:  Violação de chave estrangeira  Possíveis causas:  - exclusão de registro que possui outros registros associados  - inclusão de registro detalhe sem um registro mestre associado  Detalhes:  The INSERT statement conflicted with the FOREIGN KEY constraint "FKPFITEMLAN\_FCFO". The conflict occurred in database "Exemplo118230", table "dbo.FCFO".  The statement has been terminated.  --FopRelGuiaINSSProcess |
| **Solução/Implementação:** | Criação de script que acerta a constraint FKPFITEMLAN\_FCFO, permitindo o cadastro de rastreabilidade no lançamento financeiro para fornecedor global |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTGRTC |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
