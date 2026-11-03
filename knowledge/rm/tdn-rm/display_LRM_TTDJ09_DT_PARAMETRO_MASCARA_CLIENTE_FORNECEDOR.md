---
content_hash: 9a664d266e4521d3e276a06d96841da5bd580d952bf21216547e36fbd2339b60
fetched_at: '2026-06-29T00:06:08.900456+00:00'
page_id: '203555311'
product: rm
source: tdn-rm
title: TTDJ09_DT_PARAMETRO_MASCARA_CLIENTE_FORNECEDOR
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDJ09_DT_PARAMETRO_MASCARA_CLIENTE_FORNECEDOR
version: 3
---

# Parametrizador

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Configuração da Máscara Cliente / Fornecedor* |
| **Situação/Requisito:** | *Tratamento da Máscara Cliente / Fornecedor com e sem integração com o Fluxus* |
| **Solução/Implementação:** | O Labore passa validar a máscara para  o parâmetro "Máscara do código Clientes/Fornecedores", permitindo apenas caracteres que segue a regra do sistema, que são: '#', 'l', 'L', 'a', 'A', 'Q', 'q'.  Caso seja informado caracteres diferente destes o sistema emitirá a mensagem de erro "Máscara do Cliente/Fornecedor inválida.". Este comportamento se dará quando estiver parametrizado para usar tomador de serviço e não estar integrado com o Fluxus. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTDJ09 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.40.116* |
