---
content_hash: a87b71e1151e355326d5ec78316b6a60a93e7718876760b4451ee05336272116
fetched_at: '2026-06-29T00:06:23.929674+00:00'
page_id: '224108515'
product: rm
source: tdn-rm
title: TTV768_DT_Diferenca_1Centavo_Ferias_TRCT
type: documentation
url: https://tdn.totvs.com/display/LRM/TTV768_DT_Diferenca_1Centavo_Ferias_TRCT
version: 2
---

# DIFERENÇA DE 1 CENTAVO NO EVENTOS DE FÉRIAS PARA O TRCT

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo de Rescisão* |
| **Situação/Requisito:** | *No cálculo da rescisão a soma dos valores dos eventos de férias do TRCT, CC's 329 e 330, está retornando 1 centavo a mais que o todal do valor dos eventos pagos, CC's 24 e 25, mais médias.* |
| **Solução/Implementação:** | *No cálculo da rescisão, já existe uma verificação final do arredondamento dos eventos de férias para o TRCT.*  *Mas devido a uma situação específica criada pelo cliente, de utilização do grupo de média do Sindicato para discriminar o adicional de 1/3 sobre as médias, a verificação não funcionou neste caso.*  *Esta situação será tratada na verificação já existente no processo de rescisão..* |
| **Chamados   relacionados:** | *TTV768, TUBYNP* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
