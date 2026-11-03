---
content_hash: 244dbd9a47bb5124c27308beb8a3a2a7c693297a25c3052cbb7add33494fa8d8
fetched_at: '2026-06-29T00:06:08.088225+00:00'
page_id: '201745834'
product: rm
source: tdn-rm
title: TTAVHB_DT_PARAMETRO_MASCARA_CLIENTE_FORNECEDOR_LABORE
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAVHB_DT_PARAMETRO_MASCARA_CLIENTE_FORNECEDOR_LABORE
version: 1
---

# PARAMETRIZADOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Parametrização* |
| **Situação/Requisito:** | *Sistema não valida máscara de cliente fornecedor na parametrização. Porém ao incluir um cliente fornecedor é validado a máscara* |
| **Solução/Implementação:** | O Labore, na MDI Delphi em "Opções / Parâmetros / RH" na aba Financeiro, passa validar a máscara para  o parâmetro "Máscara do código Clientes/Fornecedores", permitindo apenas caracteres diferentes de '#', 'l', 'L', 'a', 'A', 'Q', 'q'. Caso seja informado caracteres diferente destes o sistema emitirá a mensagem de erro "Máscara do Cliente/Fornecedor inválida.". |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTAVHB |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
