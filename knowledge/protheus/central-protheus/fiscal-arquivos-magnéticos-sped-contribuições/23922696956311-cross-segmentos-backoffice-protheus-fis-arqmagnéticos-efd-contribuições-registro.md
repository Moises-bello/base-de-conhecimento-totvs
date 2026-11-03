---
article_id: 23922696956311
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: d8f3914dcd0d706461f4da84f4d0fd4f393183966a7a531ded9ae872dca5e70c
fetched_at: '2026-06-28T22:42:06.660500+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  Registros M105 / M505: ''Deverá existir um registro M105 - "Detalhamento da Base
  de cálculo do Crédito para Código da Natureza da Base de Cálculo do Crédito e Código..."'
type: support-article
updated_at: '2024-06-03T20:39:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23922696956311-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Registros-M105-M505-Dever%C3%A1-existir-um-registro-M105-Detalhamento-da-Base-de-c%C3%A1lculo-do-Cr%C3%A9dito-para-C%C3%B3digo-da-Natureza-da-Base-de-C%C3%A1lculo-do-Cr%C3%A9dito-e-C%C3%B3digo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23922644675863) Tempo aproximado para leitura: 00:05:00 min

**Dúvida**  
Como corrigir o erro de validação ao importar o arquivo txt do **EFD Contribuições**:  
"**Deverá existir um registro M105 - Detalhamento da Base de Calculo do Crédito para cada Código da Natureza da Base de Cálculo do Crédito e Código de Situação Tributária informados nos documentos e operações,**  
**agrupados pelo Código do Tipo de Crédito, Alíquota (em percentual) e Alíquota (em reais)(COD\_CRED = 101, ALIQ\_PIS = 1.6500, ALIQ\_PIS\_QUANT = , NAT\_BC\_CRED = 05, CST\_PIS = 50)**."

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões

**Solução**  
Geralmente este erro ocorre, quando há algum **produto com crédito de PIS e COFINS**, porém o **CFOP** **utilizado não permite esse crédito**, ou também poderá ocorrer para lançamentos **com vínculo de Crédito incorreto nas notas de entrada**.  
   
Diante disso, primeiramente avalie com o fiscal da empresa, e **localize as Notas Fiscais** que compõe o erro e avalie as informações contidas na linha do erro, verifique a **Base do Crédito, CST e Base de Cálculo** que ocorre o erro, na **escrituração avalie o CFOP, o CST de PIS e COFINS, o Código da Base de Cálculo do Crédito (tabela 4.3.7 da Receita Federal)** se estão condizendo com a operação.  
   
Referente as Notas Fiscais do período e faça a análise das configurações dos campos dos códigos de crédito do campo **FT\_CODBCC** e a **CFOP** que foi configurada.  
O código é gravado no campo **FT\_CODBCC** esse campo é alimentado pela **TES** campo **Cod. BC Cred. (F4\_CODBCC).**  
  
Verifique o **CFOP** utilizado no lançamento da **Nota Fiscal**, se existe na **Tabela CFOP - Operações Geradoras de Créditos**.   
   
Utilize um **CST**, **geradora de credito intervalo 50 a 66.**  
Exemplo: **50, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64 e 66**, nos campos abaixo da **TES**:  
**Sit. Trib. PIS (F4\_CSTPIS)= 50 a 66**  
**Sit. Trib. COF (F4\_CSTCOF) = 50 a 66**  
   
Exclua e reprocesse a **Apuração do EFD Contribuições**,  após as informações serão gravadas na **tabela CL9.**

Gere um novo **arquivo txt do EFD Contribuições** para a correta geração dos registros **M105/M505**.

*Link* Boletim complementar:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/7630668843287-Cross-Segmentos-Backoffice-Protheus-FIS-Como-gerar-os-Registros-M100-M105-M500-e-M505-do-EFD-Contribui%C3%A7%C3%B5es>
