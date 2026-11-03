---
content_hash: c3cebe64fec5cf308bf58c80422c9a198fe160080d787c4317f55c02d39a070e
fetched_at: '2026-06-29T00:09:22.010425+00:00'
page_id: '422545947'
product: rm
source: tdn-rm
title: Bloco E (Livro ICMS-LA)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545947
version: 5
---

**E001 - Abertura do Bloco E**   
Preenchido pela rotina

**E003 - Campos Adicionais**   
Considera lançamentos de entrada com CFOP sintético 1.651, 1.652, 1.653, 1.658, 1.659, 1.660, 1.661, 1.662, 1.663, 1.664, 2.651, 2.652, 2.653, 2.658, 2.659, 2.660, 2.661, 2.662, 2.663, 2.664, 3.651, 3.652 e 3.653.

**E020 - Lançamento - Nota Fiscal (CÓDIGO 01), Nota Fiscal de Produtor (CÓDIGO 04), Nota Fiscal Eletrônica (CÓDIGO 55) e Nota Fiscal Consumidor Eletrônica – NFC-e (CÓDIGO 65) Seleciona lançamentos de entrada e saída que possuem os códigos modelo de documento 01, 04 e 55 selecionado. E025 - Detalhe - Valores Parciais de lançamento - Nota Fiscal (CÓDIGO 01), Nota Fiscal de Produtor (CÓDIGO 04), Nota Fiscal Eletrônica (CÓDIGO 55) e Nota Fiscal Consumidor Eletrônica – NFC-e (CÓDIGO 65)**   
Este registro tem por objetivo representar a escrituração dos documentos fiscais totalizados por CST, CFOP e Alíquota de ICMS.

Será considerado as numerações inutilizadas para o modelo 55 e 65.

**E050 - Lançamento - Nota Fiscal de Venda a Consumidor (CÓDIGO 02)**   
Seleciona lançamentos de entrada e saída que possuem os códigos modelo de documento 02 selecionado.

**E055 - Detalhe - Valores Parciais**   
Este registro tem por objetivo representar a escrituração dos documentos fiscais totalizados por CST, CFOP e Alíquota de ICMS.

**E060: Lançamento - Redução Z - ICMS**   
Seleciona lançamentos de entrada e saída que possuem os códigos modelo de documento 2D selecionado.

**E065: Detalhe - Valores Parciais**   
Este registro tem por objetivo representar a escrituração dos documentos fiscais totalizados por CST, CFOP e Alíquota de ICMS.

**E080 - Lançamento – Mapa Resumo de ICMS**   
Nesse registro é gerada uma linha para cada lançamento de redução Z. E085 - Detalhe - Valores Parciais Este registro tem por objetivo representar a escrituração dos documentos fiscais totalizados por CST, CFOP e Alíquota de ICMS.

**E100 - Notas Fiscais de Energia Elétrica (CÓDIGO 06), (CÓDIGO 01 ou CÓDIGO 55), Serviço de Comunicação (CÓDIGO 21), Serviço de Telecomunicação (CÓDIGO 22), Fornecimento de Gás (CÓDIGO 28) e Fornecimento D'água (CÓDIGO 29)**   
Considera os lançamentos de entrada e saída onde código modelo de documento é igual a 06, 21, 22, 28, 29 e a natureza seja do tipo fiscal. E105 - Detalhe Valores Parciais Este registro tem por objetivo representar a escrituração dos documentos fiscais totalizados por CST, CFOP e Alíquota de ICMS.

**E120 - Notas Fiscais de Serviço de Transporte (CÓDIGO 07), Transporte Rodoviário de Cargas (CÓDIGO 08), Aquaviário de Cargas (CÓDIGO 09), Aéreo (CÓDIGO 10), Ferroviário de Cargas (CÓDIGO 11), Multimodal de Cargas (CÓDIGO 26), Eletrônico (CÓDIGO 57), Serviço de Transporte Ferroviário (CÓDIGO 27) e Resumo de Movimento Diário (CÓDIGO 18)**   
Considera os lançamentos de entrada e saída onde código modelo de documento é igual a 07, 08, 09, 10, 11, 18, 26, 27, 57 e a natureza seja do tipo fiscal.

**E140 - Lançamento - Bilhetes de Passagem Rodoviário (CÓDIGO 13), Aquaviário (CÓDIGO 14), Nota de Bagagem (CÓDIGO 15), Manifesto de Voo (CÓDIGO 30) e Ferroviário (CÓDIGO 16)**   
Considera lançamentos de entrada e saída onde código modelo de documento é igual a 13, 14, 15, 16, 30 e a natureza seja do tipo fiscal.

**E300 - Apuração do ICMS**   
Gerado a partir dos valores apurados do tributo ICMS.

**E305 - Mapa-Resumo de Operações**   
Gerado pela rotina.

**E310 - Consolidação por CFOP dos Valores do ICMS**   
Esse registro se refere ao totalizador das movimentações no período de apuração selecionado na geração da rotina. Os valores são agrupados até segundo nível do CFOP que é o fiscal. Serão considerados apenas lançamentos onde o CFOP selecionado é do tipo "Fiscal".

**E330 - Totalização das Operações do ICMS**   
Esse registro totaliza toda a movimentação dentro do período informado na geração da rotina, agrupando os valores de acordo com a opção Origem/Destino selecionada no cadastro do CFOP.

**E340 - Saldos da Apuração do ICMS**   
Gerado com os valores apurados do tributo ICMS.

**E350 - Ajustes da Apuração do ICMS**   
Gerado com os valores dos lançamentos de Outros Débitos/Créditos do período.

**E360 - Obrigações do ICMS a Recolher**   
Esse registro será gerado com as informações das guias geradas no período de apuração.

**E500 - Apuração do IPI (Modelo 8)**   
As informações da apuração do IPI serão retiradas do período de apuração do tributo.

**E520 - Consolidação por CFOP dos Valores do IPI**   
Esse registro será agrupado por CFIP, considerando os lançamentos fiscais com o tributo IPI, sendo diferente de do tipo "Sem IPI".

**E525 - Totalização das Operações do IPI**   
Sub-totaliza o valor contábil pelo primeiro nível do ou pelos campos Origem/Destino do CFOP selecionado nos lançamentos fiscais.

**E540 - Saldos da Apuração do IPI**   
Esse registro será gerado com as informações do Período de Apuração do IPI. E550 - Ajustes da Apuração do IPI Esse registro será gerado com os valores dos lançamentos de Outros Débitos/Créditos de IPI do período.

**E560 - Obrigações do IPI a Recolher**   
Esse registro será gerado com as informações das Guia de Apuração do Período geradas no Período de Apuração do tributo IPI.

**E990 - Encerramento do Bloco 8**   
Preenchido pela rotina.
