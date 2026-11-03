---
content_hash: bd768683187a36324ccd3c24582a640f42c683855b21d767e4f191fa6c0005e2
fetched_at: '2026-06-29T00:08:57.785925+00:00'
page_id: '354477289'
product: rm
source: tdn-rm
title: 2606687 FINANCEIRO01-6311 DT Geração do código de barras da CEF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354477289
version: 4
---

# Geração do código de barras da CEF quando o Nosso Número é gerado pelo Banco e Código de Barras pelo RM

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Geração de Código de Barras |
| **Situação/Requisito:** | Cliente entrou em contato relatando que o sistema está gerando um código de barras diferente do código de barras gerado pelo banco CEF. |
| **Solução/Implementação:** | Sistema agora consegue gerar o código de barras de acordo com as regras do Manual quando o nosso número é gerado pelo Banco e a impressão do código de barras é gerado pelo beneficiário.  Importante: Existe um parâmetro interno no sistema para habilitar essa funcionalidade.    CCCCCC: Beneficiário(Cedente)  D: Dig Verificador Beneficiário(Cedente)  NNN: 3ª a 5ª posição do Nosso Número  X: 1ª posição do Nosso Numero - Tipo de Cobrança(1 - Registrada / 2 - Sem Registro)  NNN: 6ª a 8ª posição do Nosso Número  Y: 2ª posição do Nosso Número - Identificador de Emissão do Boleto(4-Beneficiário)  NNNNNNNNN: 9ª a 17ª posição do Nosso Número  V: DV do campo livre |
| **Tickets relacionados:** | 2606687  <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7078> |
| **Requisito:** | FIN000024 |
