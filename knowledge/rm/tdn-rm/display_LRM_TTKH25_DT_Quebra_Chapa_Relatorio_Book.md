---
content_hash: 002989592ef20be30f91553871b6ce202a9a13068f06f240729346e649bd7f73
fetched_at: '2026-06-29T00:06:20.184358+00:00'
page_id: '221548979'
product: rm
source: tdn-rm
title: TTKH25_DT_Quebra_Chapa_Relatorio_Book
type: documentation
url: https://tdn.totvs.com/display/LRM/TTKH25_DT_Quebra_Chapa_Relatorio_Book
version: 1
---

# NÃO QUEBRAR CHAPA NO RELATÓRIO DO BOOK

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Campo Chapa relatório book* |
| **Situação/Requisito:** | Ao gerar o relatório FOPREL00031 - Escala Anual de Férias.TotvsReport quando a chapa do funcionário possui mais de 9 caracteres o sistema quebra a chapa do funcionário enviando para a linha de baixo deixando a chapa desalinhada. |
| **Solução/Implementação:** | Realizado alteração no tamanho do campo Chapa do relatório FOPREL00031 - Escala Anual de Férias, para que seja permitido apresentar sem quebra o campo Chapa. Para isso foi realizado a alteração do nome do campo DATA VENCIOMENTO para DT VENCTO |
| **Chamados relacionados:** | TTKH25 |
| **Versões/Release:** | *12.1.9* |

divs
