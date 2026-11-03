---
article_id: 360060107393
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 098dd6e6d0807803ce79cc554a0f3dba3e1cc1e8bcf38d557e8a5a70c589107a
fetched_at: '2026-06-28T22:42:04.928152+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Cálculo PIS/COFINS
  para geração de crédito sobre depreciação de Ativo
type: support-article
updated_at: '2022-08-31T12:54:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060107393-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-C%C3%A1lculo-PIS-COFINS-para-gera%C3%A7%C3%A3o-de-cr%C3%A9dito-sobre-deprecia%C3%A7%C3%A3o-de-Ativo
---

**Dúvida**

Como deve ser efetuado o cálculo do PIS/COFINS para geração de crédito sobre a depreciação de Ativo?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Considerando a depreciação de PIS/COFINS **(N1\_CALCPIS = 1 - Sim)**

**N3\_TXDEPR1 \* 12** =**(A)** Coeficiente para cálculo mensal a depreciar;  
**N3\_VORIG1 \*** **(A)** = **(B)** Valor Bruto Depreciado;  
**(B) Valor Bruto Depreciado \* (P/C) Alíquota de PIS/COFINS =** **(F)** Valor a ser depreciado.  
**(F)** Valor a ser depreciado será demonstrado na Apuração de PIS/COFINS na aba deduções PIS e deduções COFINS com o código **008 - ATF | DEPRECIAÇÃO.**  
  
  
Depreciação de Pis/Cofins **(N1\_CALCPIS = 3 - Fração)**  
  
**N3\_VORIG1 / N1\_MESCPIS\*\* = (B)** Valor Bruto a Depreciar  
**(B) Valor Bruto Depreciado \* (P/C) Alíquota de PIS/COFINS** = **(F)** Valor a ser depreciado   
**(F)** Valor a ser depreciado será demonstrado na apuração de PIS/COFINS aba deduções PIS e deduções COFINS com o código **010 - ATF | Créditos Ativo.**  
  
  
Se o campo**N1\_MESCPIS,** no cadastro do ativo, estiver preenchido com 0 será considerado o padrão 48 meses para depreciação fracionada.  
  
  
O parâmetro **MV\_BSCREPC** define a base de cálculo para Crédito de PIS/COFINS sobre Depreciação de Ativo:  
  
  
1 = Valor do bem Imobilizado;

2 = Valor de Aquisição do Ativo;

**Importante:**

Conforme determina atualmente o Guia Prático EFD-Contribuições:

-Para que o Crédito seja calculado com base nos Encargos de Depreciação e Amortização deverá ser utilizado Código da Base de Cálculo do Crédito sobre Bens Incorporados ao Ativo Imobilizado, conforme a Tabela indicada no item 4.3.7:

**09 = Crédito com Base nos Encargos de Depreciação**  
**11 = Crédito com Base nos Encargos de Amortização**

- Para que o Crédito seja calculado com base no Valor de Aquisição/Contribuição deverá ser utilizado Código da Base de Cálculo do Crédito sobre Bens Incorporados ao Ativo Imobilizado, conforme a Tabela indicada no item 4.3.7:

**10= Crédito com Base no Valor de Aquisição**

Esta informação deve ser preenchida a partir do cadastro do**TES(Cod. BC Cred(F4\_CODBCC))** ou do cadastro do **Ativos(Cod.BC Cred.(N1\_CODBCC))**.

Informações adicionais:

Manual de Apuração EFD Contribuições

<https://tdn.totvs.com/pages/releaseview.action?pageId=212896468>

Arquivo EFD Contribuições

<https://tdn.totvs.com/pages/releaseview.action?pageId=212895074>

Relatório Crédito de PIS/COFINS na Depreciação Ativos - MATR927

<https://tdn.totvs.com/pages/releaseview.action;jsessionid=1ED70F196014F00182DEEFDD3890833C?pageId=6076807>

IMP0009\_Cálculo\_PIS/COFINS\_para\_geração\_de\_crédito\_sobre\_depreciação\_de\_Ativo

<https://tdn.totvs.com/pages/viewpage.action?pageId=51253269>
