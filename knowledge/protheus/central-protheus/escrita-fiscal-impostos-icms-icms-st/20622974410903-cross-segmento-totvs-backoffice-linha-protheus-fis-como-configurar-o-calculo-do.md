---
article_id: 20622974410903
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: d0f833e49c66fbd8e901d70ae50e09e2d08f428253c63cb305f47c786814e800
fetched_at: '2026-06-28T22:39:20.317252+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  o calculo do ICMS ST na exceção fiscal para Nota fiscal de compras?
type: support-article
updated_at: '2024-01-16T19:18:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20622974410903-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-calculo-do-ICMS-ST-na-exce%C3%A7%C3%A3o-fiscal-para-Nota-fiscal-de-compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20622970322967) Tempo aproximado para leitura: **05:00min** **Dúvida**Como configurar o calculo do ICMS ST na exceção fiscal para Nota fiscal de compras ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Segue a configuração para o calculo do ICMS ST configurado na exceção fiscal

MV\_ESTADO = SP

Calculo da nota fiscal

Mercadoria = 1000,00

MVA = 30%

Alíquota do ICMS ST = 18%

Fornecedor = MG ( SA2 )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20622974352151)

O campo do cadastro de fornecedores Grp Tribut em branco na exceção fiscal em branco ( Grp Cli/For )

Cadastro de produtos ( SB1 )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20622974358679)

Exceção fiscal - ( SF7 )

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20622970330647)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20622974363927)

TES - ( SF4 )

Calcula icms = sim

L fiscal icms = Diferente = Não

MKPO icm comp = não

LF ICMS ST = não

Marg solid = em branco ou configuração

Si trib icm = 10

Agrega valor = sim

Agrega solid = sim

Documento de entradas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20622970341783)

Caso a Exceção Fiscal não funcione, verifique o tamanho dos campos abaixo:

**F7\_GRTRIB**= CARACTER, 6

**F7\_GRPCLI**= CARACTER, 3

**A1\_GRPTRIB**= CARACTER, 3

**A2\_GRPTRIB =**CARACTER, 3

**B1\_GRTRIB**= CARACTER, 6

Boletim

https://tdn.totvs.com/pages/releaseview.action?pageId=653415519
