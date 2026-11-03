---
content_hash: c70053cdd75f1e5b11b1a064ffaf781da46cb17f8259a981d6f32693295126ce
fetched_at: '2026-06-29T00:06:08.133495+00:00'
page_id: '201746640'
product: rm
source: tdn-rm
title: TTFLAW_DT_PARAMETRO_MASCARA_CLIENTE_FORNECEDOR_LABORE
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFLAW_DT_PARAMETRO_MASCARA_CLIENTE_FORNECEDOR_LABORE
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
| **Chamados relacionados:** | TTFLAW |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
