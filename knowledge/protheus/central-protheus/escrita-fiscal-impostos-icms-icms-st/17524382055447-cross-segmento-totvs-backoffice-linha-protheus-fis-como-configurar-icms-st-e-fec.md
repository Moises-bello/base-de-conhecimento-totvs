---
article_id: 17524382055447
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: a0fee7edee4f9914a4744af702680be634947227cdf7f6a69ff955fa527eb679
fetched_at: '2026-06-28T22:39:20.311684+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -  FIS - Como configurar
  ICMS ST e FECP ST para simples nacional?
type: support-article
updated_at: '2024-03-19T20:27:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17524382055447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-ICMS-ST-e-FECP-ST-para-simples-nacional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17524376361751) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como configurar ICMS ST e FECP ST para simples nacional?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Empresa adquire mercadoria de fornecedor simples nacional e precisa calcular o ICMS st e FECP st sem calcular o ICMS Próprio

Valor da mercadoria = 56,80

MVA = 92,78%

Alíquota ICMS ST = 25%

Alíquota FECP ST = 2%

MV\_ESTADO = RS

MV\_UFBDST = em branco

Fornecedor = RS

A1\_simpnac

![](https://totvssuporte.zendesk.com/attachments/token/TTKWUZ22YK2bBYoP68qwPFtd1/?name=image.png)

UF x UF

![](https://totvssuporte.zendesk.com/attachments/token/vBeH4JFUr6q3WUo9EpbNGnsWX/?name=image.png)

Exceção fiscal

![](https://totvssuporte.zendesk.com/attachments/token/7Z98NVAxqiBY3tAWU5L6LSZ1K/?name=image.png)

TES

Calcula icms = não

L fiscal icms = outros

MKP ICM COMP = não

Marg solid = configuração.

Sit trib icm = 10/30

icms s/ st = não

![](https://totvssuporte.zendesk.com/attachments/token/Pz8uHqt0b4R3YSZvreN9k3Bax/?name=image.png)

Documento de entradas

![](https://totvssuporte.zendesk.com/attachments/token/eZ9umnGqPw3mPf1Tc8BtHxVmn/?name=image.png)

Para o calculo do FECP ST precisa configurar o campo da TES Sit trib icm = 10/70

O sistema demonstra 27% porém grava nas tabelas o valor do icms st e fecp st

ICMS ST = 13,18 + 2,19 = 15,37

<https://tdn.totvs.com/pages/releaseview.action?pageId=701693062>

Obs: Para fazer a devolução com o mesmo calculo configure o parametro MV\_DEVRET = .T.
