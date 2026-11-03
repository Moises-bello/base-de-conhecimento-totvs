---
content_hash: a11956e4884f383ff0b3765cd446afd6d0d21bfe9b53ce10e820935155005c64
fetched_at: '2026-06-29T00:06:09.903990+00:00'
page_id: '203758948'
product: rm
source: tdn-rm
title: TTGLSN_DT_PARAMETRO_MASCARA_CLIENTE_FORNECEDOR_MDI_NET
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGLSN_DT_PARAMETRO_MASCARA_CLIENTE_FORNECEDOR_MDI_NET
version: 1
---

# Parametrizador

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Configuração da Máscara Cliente / Fornecedor* |
| **Situação/Requisito:** | *Tratamento da Máscara Cliente / Fornecedor com e sem integração com o Fluxus* |
| **Solução/Implementação:** | O Labore passa validar a máscara para  o parâmetro "Máscara do código Clientes/Fornecedores", permitindo apenas caracteres diferentes de '#', 'l', 'L', 'a', 'A', 'Q', 'q'. Caso seja informado caracteres diferente destes o sistema emitirá a mensagem de erro "Máscara do Cliente/Fornecedor inválida.". Este comportamento se dará quando estiver parametrizado para usar tomador de serviço e não estar integrado com o Fluxus. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTGLSN |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
