---
content_hash: 70b3a8f0ac19a26069b23d0bb98fa3eb7bb5219a770ee405e95063b9fbbab540
fetched_at: '2026-06-29T00:09:54.279956+00:00'
page_id: '444600599'
product: rm
source: tdn-rm
title: 4588713 FOPCALCULO01-5655 TRCT
type: documentation
url: https://tdn.totvs.com/display/LRM/4588713+FOPCALCULO01-5655+TRCT
version: 1
---

# TRCT

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Plataforma RH |
| **Módulo:** | Folha de Pagamento |
| **Função:** | TRCT |
| **Situação/Requisito:** | Ao gerar a rescisão com código de saque FGTS 03 o sistema não valida as informações da tabela de conversão para os códigos de movimentação criados pelo MTE - Novo TRCT X FGTS. No campos 22 e 27 da TRCT. A ocorrência trata-se da sobre a Portaria nº 1057 de 06 de julho de 2012, publicada no DOU de 09/07/2012 e Retificação no DOU de 12/07/2012, em conformidade com o anexo onde determina o código FE2 - Rescisão do contrato de trabalho por falecimento do empregador individual sem continuação da atividade da empresa. |
| **Solução/Implementação:** | Ajuste no campo 22 (código) e 27 (descrição do código) para considerar a rescisão de funcionário com o código de saque FGTS 03 atendendo as causas FE1 e FE2, conforme descrito na legislação |
| **Tickets relacionados:** | 4588713 |
