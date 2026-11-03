---
content_hash: 5920c658fcdcc71db0b3d36f3ff66628adcbdd3292a3aadf3aab17e5d48e9e41
fetched_at: '2026-06-29T00:08:28.168878+00:00'
page_id: '271665194'
product: rm
source: tdn-rm
title: RMFIS00001_SEF II - Bloco 8 - Prodepe
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00001_SEF+II+-+Bloco+8+-+Prodepe
version: 2
---

# Assunto

|  |  |
| --- | --- |
| Produto: | Totvs Gestão Fiscal |
| Versões: | 12.1.X |
| Ocorrência: | Geração do Bloco 8 - Prodepe - GIAF – SEF II |
| Ambiente: |  |
| Passo a passo: | * **Parametrização Necessária**   Deverá executar script para habilitar o Parâmetro Prodepe.  Utilizar layout gerador de saídas correspondente a ICMS Guias Prodepe   * **Informações necessárias para a geração do Bloco 8**   Após habilitar o parâmetro será exibido no menu principal uma nova opção para realização dos cadastros de Benefícios e Sub-Apurações.           * **Cadastros de Benefícios Fiscais / Sub-Apurações ICMS**   No cadastro de Benefícios Fiscais deverá cadastrar todos os benefícios concedidos para a sua empresa.        No cadastro de Sub-Apurações deverá parametrizar os seus percentuais de incentivo vinculados ao Benefício sendo eles do tipo Indústria, Importação ou Centro de Distribuição.        Para cada Sub-Apuração, poderá informar os Produtos e Naturezas que compõe a Sub-Apuração.         * **Processo de cálculo das Sub-Apurações**    Processo no Período de Apuração para cálculo dos Incentivos da Prodepe.  No Período de Apuração foi incluído um novo processo para que os incentivos sejam calculados para o Tributo de ICMS depois que o mesmo estiver Encerrado.        Neste processo o sistema irá calcular os valores do Prodepe conforme a parametrização de Itens e CFOP’s realizadas nos cadastros de Benefícios Fiscais e Sub-Apurações.    Após este cálculo os valores apurados poderão ser vistos em uma Aba no Período de Apuração “Prodepe – Sub-Apurações ICMS”.            Nesta visão irá conter um registro para cada Sub-Apuração cadastrada, com todos os seus valores que serão utilizados na geração do Bloco 8 da SEF II – GIAF.       * **Geração do Bloco 8 GIAF SEF II**   Através do gerador de saídas deverá gerar a rotina utilizando o layout importado referente ao Bloco 8 da SEF II - GIAF Prodepe. |
| Observações: |  |
