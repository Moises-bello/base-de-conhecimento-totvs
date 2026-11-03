---
content_hash: 4011b578544b387b1a1062736b2be08c7401d4e5c0378274ea06ab60062fc594
fetched_at: '2026-06-29T00:09:02.262638+00:00'
page_id: '379299980'
product: rm
source: tdn-rm
title: 1420515 FISCAL01-1852 DT Impressão das informações Complementares na DANFE.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379299980
version: 3
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Emissão de NF-e/NFC-e |
| **Situação/Requisito:** | Impressão das informações Complementares na DANFE |
| **Solução/Implementação:** | Para geração do quadro de Informações Complementares do DANFE o ERP irá respeitar as seguintes regras:    Formato:   * Retrato  9 Linhas , 56 Colunas  * Paisagem  5 Linhas , 83 Colunas   Para que o ERP possa respeitar a regra de impressão, o mesmo irá considerar o parâmetro "Formato de Impressão" presente nos parâmetros do tipo de movimento de envio:     Gerando no XML :  1 = Retrato    2 = Paisagem     Obs: Para cada quebra de linha efetuada no histórico do movimento será considerado como uma linha.   Segundo o Manual de Orientação do Contribuinte versão 6.0 cita-se:  " 7.1.6 Informações Complementares Deverá conter todas as Informações Adicionais da NF-e incluídas nas TAGs <infAdFisco> e <infCpl>, ficando facultada a impressão das informações adicionais contidas nas TAGs <obsCont>. Na hipótese de insuficiência de espaço no quadro de “informações complementares”, a impressão destas deverá ser continuada no verso ou na folha seguinte, neste mesmo quadro ou no quadro “Dados dos Produtos/Serviços”.  " Obs: No comportamento citado acima, implementação a seguinte regra de preenchimento:  1- Preenchimento do quadro "Informações complementares" 2- Não cabendo o texto como todo no quadro "Informações complementares", continuamos a informação no quadro "Dados do Produto/Serviços" do ultimo item do DANFE. |
