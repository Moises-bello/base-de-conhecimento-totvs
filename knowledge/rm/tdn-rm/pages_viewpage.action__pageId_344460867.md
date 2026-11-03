---
content_hash: 88ceb65ee99c08daf84dde2c00488cd314ec3b1569dda5e12e40ecbc00d9592f
fetched_at: '2026-06-29T00:08:53.156226+00:00'
page_id: '344460867'
product: rm
source: tdn-rm
title: RMCTB00006_Evoluções e Versões para atender a ECD Leiaute 6
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344460867
version: 7
---

# 

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.17 e posteriores |
| **Ocorrência:** | Evoluções e Versões para atender a ECD Leiaute 6 |
| **Ambiente:** |  |
| **Passo a passo:** | **Definição do Processo:**  O objetivo deste documento é demonstrar as novidades do TOTVS Gestão Contábil para atendimento a geração da ECD Leiaute 6.  **Parametrização Necessária:**  O Leiaute 6 foi disponibilizado nas seguintes versões:   * Versão 12.1.17: patch a partir da  12.1.17.237 * Versão 12.1.18: patch a partir da  12.1.18.168 * Versão 12.1.19: patch a partir da  12.1.19.121 * Versão 12.1.20   Neste Leiaute, o SPED Contábil (ECD) passou pelas seguintes evoluções:   * Inclusão do campo Notas Explicativas (NOTAS\_EXP\_REF) nos registros J100, J150 e J210.  Obs.: (Contempla as versões 12.1.17 e superiores). * Inclusão do cadastro de Notas Explicativas para as Demonstrações Contábeis.  Obs.: (Contempla apenas a versão 12.1.20 e superiores).   O cadastro de Notas Explicativas será feita **por Fato Contábil** sendo recuperada fato a fato no registro J100 e J150.  Já o registro J210 que se refere a demonstração e não apenas um fato contábil terá a informação recuperada a partir do Primeiro Fato Contábil cadastrado na demonstração.  Já o **Bloco  K** foi liberado somente na 12.1.20.107 ou posteriores.  Será necessário que executem os scripts referentes ao bloco k através do RM Atualizador presente na pasta RM.Net.  Documentação sobre a geração, disponivel no help: |
| **Observações:** | Para saber mais  sobre o processo de Demonstração Contábil acesse:   Para saber como gerar a ECD acesse: |
