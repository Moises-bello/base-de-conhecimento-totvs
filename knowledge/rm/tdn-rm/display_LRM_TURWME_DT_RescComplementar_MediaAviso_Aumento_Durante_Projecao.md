---
content_hash: d44da9e5a4ffdd6f5d7c92bc56af1a960e50cd8031dd7f804703b2a4494581f0
fetched_at: '2026-06-29T00:08:04.802513+00:00'
page_id: '235582208'
product: rm
source: tdn-rm
title: TURWME_DT_RescComplementar_MediaAviso_Aumento_Durante_Projecao
type: documentation
url: https://tdn.totvs.com/display/LRM/TURWME_DT_RescComplementar_MediaAviso_Aumento_Durante_Projecao
version: 2
---

# MEDIA DE AVISO NÃO PROPORCIONALIZA NA RESCISÃO COMPLEMENTAR COM AUMENTO SALARIAL DURANTE PROJEÇÃO DO AVISO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *Na rescisão complementar, quando o aumento salarial é posterior à data da demissão, durante a projeção do aviso prévio indenizado, o valor de diferença da média de aviso prévio não está sendo proporcionalizado de acordo com o número de dias após a data do aumento no salário.*  *O problema só ocorre quando as médias não são discriminadas no envelope, ou seja, o valor é todo acumulado no grupo zero.* |
| **Solução/Implementação:** | *Ajuste no cálculo da diferença de média de aviso prévio, na rescisão complementar, para proporcionalizar o valor de acordo com o número de dias após a data do aumento no salário, independente de discriminar ou não as médias no envelope do funcionário.* |
| **Chamados   relacionados:** | *TURWME, TURZOF* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
