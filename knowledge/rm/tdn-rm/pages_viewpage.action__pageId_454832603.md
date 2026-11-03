---
content_hash: 8fd90c93085427ce2b57852568904cd23561154b5e61caeba572879a02e19edb
fetched_at: '2026-06-29T00:10:12.639110+00:00'
page_id: '454832603'
product: rm
source: tdn-rm
title: 4994706 FISCAL01-7888 DT Geração de Dados TAF - Data Início Validade REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454832603
version: 3
---

# Geração de Registros TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Geração de Registros TAF |
| **Situação/Requisito:** | Ao transmitir o R-1000, EFD Reinf, foi apresentado a seguinte mensagem: \***MS1228**\*Prezado contribuinte, somente é permitido o envio de seus eventos da EFD-Reinf para períodos a partir de 01/2019.  Verificamos que a rejeição ocorre pois na integração RM x TAF o campo 21-IND\_PER do registro T001 foi gerado com 05/2018. Porém, a obrigatoriedade do cliente é 01/2019 (empresas com faturamento abaixo de 78 milhões). |
| **Solução/Implementação:** | Foi implementado o Parâmetro "Data de Início de Validade REINF" no Layout TAF.  Este parâmetro foi terá efeito nos registros\Campos abaixo:  No registro T001 campo (21)INI\_PER e T001AB campo (16)INIVALID serão gerados observando as regras abaixo:  **SE** "Data Maior Log Alteração Filial" **É MAIOR QUE** 05/2018 **E** "Data Maior Log Alteração Filial" **É MAIOR QUE** "Data de Início de Validade REINF"  **ENTÃO** "Data Maior Log Alteração Filial"] **SENÃO SE** "Parâmetro Data Inicial" **É MENOR QUE** 05/2018   **ENTÃO** "Parâmetro Data Inicial"  **SENÃO SE EXISTE** "Data de Início de Validade REINF"  **ENTÃO** "Data de Início de Validade REINF"  **SENÃO** 05/2018    *Observação :* Se não existir uma "Data Log Última Alteração Filial" **MENOR QUE**  "Data Final" o valor do "Data Log Última Alteração Filial" será a menor possível (01/01/0001) |
