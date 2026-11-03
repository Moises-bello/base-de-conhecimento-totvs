---
content_hash: d4fe90a49cbb72d933e2fe2e802b3075f7a6b166dededcb92401a1796662f61c
fetched_at: '2026-06-29T00:09:52.806909+00:00'
page_id: '439684985'
product: rm
source: tdn-rm
title: 4042666 FISCAL01-6897 Tipo do Bairro C1H_TPBAIR não existe na base de dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439684985
version: 1
---

# Integração com TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Integrações |
| **Situação/Requisito:** | Tipo do Bairro C1H\_TPBAIR não existe na base de dados |
| **Solução/Implementação:** | Foi inserido um de/para no campo 14 do registro T003 para a lista dos valores permitidos para o campo no TAF. A conversão inicia no 01 e vai até o número 19. Tudo que não existe na lista do TAF deve ser gravado como 99. Após o ajuste os valores serão convertidos da seguinte maneira: 1 - Bairro = 01 2 - Bosque = 02 3 - Chácara = 03 4 - Conjunto = 04 5 - Desmembramento = 05 6 - Distrito = 06 7 - Favela = 07 8 - Fazenda = 08  9 - Gleba = 09 10 - Horto = 10  11 - Jardim = 11 12 - Loteamento = 12  13 - Núcleo = 13 14 - Parque = 14 15 - Residencial = 15 16 - Sítio = 16 17 - Tropical = 17 18 - Vila = 18 19 - Zona = 19 Qualquer valor que não pertença ao intervalo de 1 até 19 ou seja 99 será gravado como 99 (Outros) no registro T003. |
