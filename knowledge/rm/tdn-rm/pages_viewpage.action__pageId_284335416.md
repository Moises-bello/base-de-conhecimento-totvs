---
content_hash: 50d857c62e55e69777e76d37eb5bbea14992b17d21d95d34cdffe3f1bd173fa4
fetched_at: '2026-06-29T00:08:36.058452+00:00'
page_id: '284335416'
product: rm
source: tdn-rm
title: RMFIS00002_Diferencial de Alíquota - Guias por nota fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284335416
version: 33
---

# APURAÇÃO DIFAL - GUIAS POR NOTA FISCAL

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO FISCAL |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | APURAÇÃO ICMS - DIFAL |
| **Ambiente:** | -- |
| **Passo a passo:** | **1 - Apuração com os parâmetros marcados.**  Se o parâmetro estiver Habilitado indica que o Valor do Diferencial de Alíquota – Dos Lançamentos de Entrada e o Valor da Parcela do Estado de Origem dos Lançamentos de Saída, deverá ser totalizado como Débito na Apuração.  IMPORTANTE: DEVEM SER MARCADOS OS DOIS PARÂMETROS CONFORME A IMAGEM.  ***ACESSAR: AMBIENTE > TOTVS GESTÃO FISCAL > 03.02 APURAÇÃO DE TRIBUTOS > ICMS > APUR. ICMS POR FILIAL "clique duplo na filial desejada" > AVANÇAR:***  ***Com os parâmetros marcados não será possível gerar as “Guias Difal Destino” automaticamente.***        O valor DIFAL Origem é o valor gerado para o Estado da sua Filial e pode ser verificado na tela "Valores Diferencial de Alíquota" do período de apuração quando o mesmo estiver encerrado, a coluna "Remetente" fica igual a "Sim" para o estado de Origem:        Será necessário incluir os seguintes Lançamentos de Outros Débitos\Créditos para zerar o Valor do Débito do Difal gerada para UF Origem:  ***- DÉBITO: Fazer lançamento de Outros Débitos com o Subtipo “Não se aplica”, usar o código de ajuste adequado, (exemplo: SP000202), com o valor do DIFAL ORIGEM.***  ***- CRÉDITO: Fazer lançamento de Outros Créditos com o Subtipo “DIFAL – Origem Destino”, usar o código de ajuste adequado, (exemplo: “SP229999”), com o valor do DIFAL ORIGEM.***  IMPORTANTE: PARA QUE NÃO OCORRAM ERROS DE VALIDAÇÃO, OS CÓDIGOS DE AJUSTE DEVEM ESTAR DE ACORDO COM A [TABELA 5.1.1 DO SPED.](http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal)  Lançamentos Outros Débitos\Créditos        No período de apuração, Incluir manualmente as guias de DIFAL e FECP na tela GUIAS GNR.        Na tela "Guias Normal" foi gerada a guia do ICMS próprio Automaticamente. (Menu PROCESSOS > GERAÇÃO DE GUIAS AUTOMATICAMENTE):        **2 - Apuração com os parâmetros desmarcados:**  **IMPORTANTE: COM OS PARÂMETROS DESMARCADOS, NÃO É NECESSÁRIO CRIAR OS LANÇAMENTOS DE OUTROS DÉBITOS\CRÉDITOS.**      O sistema não vai totalizar o valor do Diferencial de alíquota na apuração, vai ser considerado apenas o valor do ICMS Próprio:        As guias DIFAL dos estados de Destino vão ser geradas na tela GUIAS GNR automaticamente:      As guias podem ser agrupadas por ESTADO ou geradas por NOTA caso seja marcado o parâmetro **“Gerar Difal por nota”** esteja marcado.    Na tela GUIAS normal, vão ser geradas as guias do ICMS Próprio e do DIFAL do estado de Origem separadamente:        **3 - Marcando o parâmetro para gerar o DIFAL por Nota Fiscal:**        Guias de DIFAL Destino geradas por nota Fiscal na tela Guias GNR:        Na tela GUIAS normal, vão ser geradas as guias do ICMS Próprio e do DIFAL do estado de Origem separadamente: |
| **Observações:** |  |
