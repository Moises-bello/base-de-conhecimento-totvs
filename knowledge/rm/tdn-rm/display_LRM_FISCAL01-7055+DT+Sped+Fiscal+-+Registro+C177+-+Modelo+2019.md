---
content_hash: 7193b60bfe837159f5a81c18f3a2b9f31cd311bf5f8cadf7175b6e6165bbfc73
fetched_at: '2026-06-29T00:09:52.366156+00:00'
page_id: '439357351'
product: rm
source: tdn-rm
title: FISCAL01-7055 DT Sped Fiscal - Registro C177 - Modelo 2019
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-7055+DT+Sped+Fiscal+-+Registro+C177+-+Modelo+2019
version: 5
---

# Geração de Arquivo EFD ICMS\IPI

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Geração de Arquivo EFD ICMS\IPI |
| **Situação/Requisito:** | Implementar a geração do registro C177 na EFD ICMS\IPI a partir do ano de 2019 |
| **Solução/Implementação:** | Implementação do registro C177 na EFD ICMS\IPI modelo 2019.  A informação do C177 - complemento do Item será proveniente do código de ajuste informado no Item do Lançamento Fiscal.  Cadastrar o Código em:    Observação: Selecionar C177 no campo Registro e no Campo Código de Ajuste informar o código constante na Tabela 5.6 do SPED Fiscal conforme determinação da UF da Filial declarante.  No arquivo texto gerado o campo 02 (COD\_INF\_ITEM) será o código informado no campo Código de Ajuste.    Informar o código no Item do Lançamento Fiscal:    Ao gerar o sped fiscal dos modelos de documentos 01 ou 55 no exercício maior ou igual a 2019, o registro C177 do Item será gerado com o código de ajuste informado. |
| **Requisito:** | FIS000212 |
