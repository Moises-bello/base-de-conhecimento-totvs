---
content_hash: 2e6c4686d0a6d2b035c5731c84f4e2aaf5ec0af14f3e6d46fc9eff8a5ea4365c
fetched_at: '2026-06-29T00:06:03.545208+00:00'
page_id: '198956251'
product: rm
source: tdn-rm
title: TSWXMP_DT_Rescisao_Por_Transferencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWXMP_DT_Rescisao_Por_Transferencia
version: 1
---

# RESCISÃO POR TRANSFERÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Totvs Folha de Pagamento* |
| **Função:** | *Rescisão por Transferência.* |
| **Situação/Requisito:** | Quando marcado o parâmetro "Incrementar 4 dígitos de controle no final da chapa dos demitidos" o campo "Nro. Ficha de Registro" fica desabilitado e vazio na tela de transferência e o sistema gera novo Nro. mesmo com o parâmetro "Nro. de Ficha de Registro gerado pelo sistema" desmarcado. |
| **Solução/Implementação:** | Quando marcado o parâmetro "Incrementar 4 dígitos de controle no final da chapa dos demitidos" o campo "Nro. Ficha de Registro" fica desabilitado e vazio na tela de transferência e o sistema gera novo Nro. mesmo com o parâmetro "Nro. de Ficha de Registro gerado pelo sistema" desmarcado. Agora mesmo com o parâmetro marcado o campo "Nro. Ficha de Registro" na tela de transferência fica habilitado e preenchido com o Nro. da Ficha de Registro anterior. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSWXMP* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
