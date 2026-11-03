---
content_hash: 9bfb95840bb267c3395a915f18e7581d10cde41d6b4a78d64c6618818e6475f4
fetched_at: '2026-06-29T00:08:04.012890+00:00'
page_id: '235333295'
product: rm
source: tdn-rm
title: TTIU33_DT_Importacao_De_Arquivo_XML_Buscar_CNPJ_No_Tomador
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIU33_DT_Importacao_De_Arquivo_XML_Buscar_CNPJ_No_Tomador
version: 2
---

# Importação De Arquivo XML Buscar CNPJ No Tomador

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque Compras e Faturamento* |
| **Função:** | *Importação de Arquivos - Totvs Colaboração* |
| **Situação/Requisito:** | Ao importar arquivo XML de CTe em que a empresa não é a destinatária do CTe o sistema emite mensagem de filial não encontrada. |
| **Solução/Implementação:** | Acerto na regra que identifica qual o CNPJ deverá ser utilizado para incluir o CTe. Caso a empresa que está incluindo  o CTe não seja a destinatária do serviço então o sistema verifica quem é o tomador do serviço no XML  (remetente, destinatário, expedidor ou recebedor) e então seleciona o CNPJ apropriado. |
| **Conversores e Parâmetros:** | *Não se aplica* |
| **Chamados relacionados:** | *Não se aplica* |
| **Requisito (ISSUE):** | *Não se aplica* |
