---
content_hash: dfb2bf089924cfcd20cd69b6471794f65da184712ccb53fcef9db0ae3ac231aa
fetched_at: '2026-06-29T00:08:57.128831+00:00'
page_id: '353273932'
product: rm
source: tdn-rm
title: 2434341 FISCAL01-4017 DT Escrituração de Cupom Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353273932
version: 1
---

# Escrituração de Cupom Fiscal - Validação na geração do Doc. Inicial do Lançamento fiscal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Escrituração .Net |
| **Situação/Requisito:** | Ao realizar o processo de escrituração migrada de cupom fiscal o sistema apresenta erro:  Redução: 8622 Erro: O índice e o comprimento devem se referir a um local dentro da cadeia de caracteres. Nome do parâmetro: length Redução: 8589 Erro: O índice e o comprimento devem se referir a um local dentro da cadeia de caracteres. Nome do parâmetro: length Redução: 8591 Erro: O índice e o comprimento devem se referir a um local dentro da cadeia de caracteres. Nome do parâmetro: length Redução: 8625 Erro: O índice e o comprimento devem se referir a um local dentro da cadeia de caracteres. Nome do parâmetro: length |
| **Solução/Implementação:** | Alteração na escrituração de cupom fiscal. Validação para que caso a máscara do numero do documento seja menor que o Doc. Inicial gerado pela rotina, o cliente será avisado que não houve a escrituração destes itens e que ele necessita de alterar o tamanho da máscara para que o processo ocorra com sucesso. |
