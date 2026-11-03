---
content_hash: 4c94efb1998006a10ae8a1ede09a5ab192b2427d904dcf6a5d243c63f7bd165e
fetched_at: '2026-06-29T00:09:52.957723+00:00'
page_id: '439704863'
product: rm
source: tdn-rm
title: FISCAL01-7067 DT Sped Fiscal - Bloco K - Modelo 2019
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-7067+DT+Sped+Fiscal+-+Bloco+K+-+Modelo+2019
version: 1
---

# Geração de Arquivo EFD ICMS\IPI

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Arquivo EFD ICMS\IPI |
| **Situação/Requisito:** | segue alterções do Bloco K no Layout de 2019:  Alteração na quantidade de casas decimais para 6 casas nos seguintes registros/campos: K235, K250, K255, K291, K292, K301 e K302 campo QTD; K210, K215 e K220 campo QTD\_ORI; K215 e K220 campo QTD\_DEST; K230 campo QTD\_ENC; K260 campos QTD\_SAÍDA e QTD\_RET; K265 campos QTD\_CONS e QTD\_RET; K270 e K275 campos QTD\_COR\_POS e QTD\_COR\_NEG. |
| **Solução/Implementação:** | Ajuste nos registros do Bloco K para que gere os valores decimais com a quantidade de casas decimais corretamente a partir de 2019, conforme manual Versão 3.0.1 da EFD ICMS\IPI.  Registros Alterados: K210, K215, K220, K230, K235, K250, K255, K260 e K265. |
| **Requisito:** | FIS000212 |
