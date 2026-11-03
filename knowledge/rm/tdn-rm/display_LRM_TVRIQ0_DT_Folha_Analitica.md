---
content_hash: 66a482427e958e2196799ac935aaffefdbdb3d2afdfc6b9b978608e3aaf4f752
fetched_at: '2026-06-29T00:08:17.852803+00:00'
page_id: '259555612'
product: rm
source: tdn-rm
title: TVRIQ0_DT_Folha_Analitica
type: documentation
url: https://tdn.totvs.com/display/LRM/TVRIQ0_DT_Folha_Analitica
version: 115
---

# FOLHA ANALÍTICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Folha Analítica* |
| **Situação/Requisito:** | Quando a folha analítica é gerada com um filtro especifico somente de uma seção ou uma filial, o sistema traz no campo Totais gerais o código do CNPJ da coligada, porém o correto, como era feito no delphi é trazer quando existir somente um CNPJ na geração da folha analítica, o número do CNPJ da seção que está sendo gerada no processo. |
| **Solução/Implementação:** | *Foi realizado o ajuste no sistema para que no momento em que a Folha Analítica for gerada para somente uma filial (Seções com o mesmo CNPJ) o sistema utilize para o CNPJ que e listado no cabeçalho, da filial em que está sendo gerada a folha analítica , porém se a folha analítica for gerada para mais de uma filial o sistema irá utilizar o CNPJ da coligada.*     Exemplo :     CNPJ Coligada : 12.345.678/0001-00     Na geração da folha analítica no código de quebra de seção foi informado o filtro da seção 02 que possui o CNPJ : 98.765.432/0001-00     No campo de Totais gerais o CNPJ que deve ser levado é 98.765.432/0001-00.     Porém quando no código de quebra for informado o código ??, assim seriam buscadas as filiais 01,02,03 .     Desta forma o CNPJ levado seria 12.345.678/0001-00. |
| **Chamados relacionados:** | *TVRIQ0.* |

divs
