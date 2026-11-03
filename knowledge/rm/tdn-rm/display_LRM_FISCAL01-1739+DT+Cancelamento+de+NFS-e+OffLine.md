---
content_hash: 187ba13f6a58ed36c4dfd4a04307de1de56f3accc6db5af3f523b4074783c9c3
fetched_at: '2026-06-29T00:08:43.567488+00:00'
page_id: '302416330'
product: rm
source: tdn-rm
title: FISCAL01-1739 DT Cancelamento de NFS-e OffLine
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-1739+DT+Cancelamento+de+NFS-e+OffLine
version: 96
---

# NFS-e (Municipal) - Cancelar

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Cancelar NFS-e OffLine |
| **Situação/Requisito:** | Implementação do Processo de Cancelamento OffLine de NFS-e |
| **Solução/Implementação:** | Foi implementado o processo de Cancelamento da NFS-e e Movimento quando o município não disponibiliza  integração eletrônica para o cancelamento da NFS-e.    Implementações:    - O Processo "Cancelar NFS-e" foi evoluído para tratar municípios que não disponibiliza integração eletrônica  para o cancelamento da NFS-e fazendo que a NFS-e nesta situação fique com o Status "Cancelamento Pendente".    - Foi implementado o processo "Confirmação de Cancelamento OffLine", este processo altera o Status da NFS-e  para "Cancelado" e também cancela o movimento.    Como fazer:  (1) O usuário deve selecionar a NFS-e TXT\XML Autorizado que não possui integração eletrônica para o cancelamento da NFS-e.  (2) Executar o processo "Cancelar NFS-e".  Após a execução do passo (2) a NFS-e deverá passar a apresentar o status "Cancelamento Pendente".  (3) Neste momento o usuário deve acessar a prefeitura para fazer o cancelamento da NFS-e  (4) Após ter certeza que a NFS-e está cancelada na prefeitura então executar o processo "Confirmação do Cancelamento OffLine". Atenção: Este processo cancelará também o movimento e é irreversível no ERP. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | Não se Aplica |
| **Requisito:** | FIS000252 |

divs
