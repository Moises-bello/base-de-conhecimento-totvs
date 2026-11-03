---
content_hash: 0134a5462275220f40020a0f050abb4068c19194c4064f8507e769df2f0091e9
fetched_at: '2026-06-29T00:08:18.630578+00:00'
page_id: '266963537'
product: rm
source: tdn-rm
title: TVVESG_DT_HomologNet_Movimentacao_Afastamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/TVVESG_DT_HomologNet_Movimentacao_Afastamentos
version: 112
---

# HOMOLOGNET

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *HomologNet* |
| **Situação/Requisito:** | *Ao gerar o Homolognet o sistema está considerando o código de afastamento P1 para afastamentos com menos de 15 dias e o código de retorno de afastamento Z7, mas o correto seria considerar P3 como código de afastamento e Z18 como código de retorno de afastamento conforme o layout do Homolognet:*  <http://trabalho.gov.br/images/Documentos/Homolognet/homolognet02.pdf> |
| **Solução/Implementação:** | *Realizado o ajuste do campo CDMotivo da Movimentação dos Afastamentos para os afastamentos do tipo Previdenciário, Licença-Maternidade, Acidente de Trabalho e Doença Ocupacional.* |
| **Chamados relacionados:** | *TVVESG* |

divs
