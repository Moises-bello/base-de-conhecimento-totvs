---
article_id: 360021660952
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 570c52018088e4c21da5fcca2067b9c628e302a381742eeac11ead0bb6f0e8a8
fetched_at: '2026-06-28T22:39:20.459536+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração para
  o cálculo de Substituição Tributária estabelecido pelo Convênio 142/18  '
type: support-article
updated_at: '2021-07-13T17:30:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021660952-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-para-o-c%C3%A1lculo-de-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria-estabelecido-pelo-Conv%C3%AAnio-142-18
---

**Dúvida**Qual a configuração para atender o cálculo do ICMS ST estabelecido pelo convênio 142/18?   
   
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.16  
  
 **Solução**Configure conforme abaixo:

**Parâmetros:**

MV\_UFBDST    
MV\_BASDSSE   
MV\_UFSTALQ

Nos parâmetros acima informe o estado de destino da mercadoria.

Informe no**Cadastro do Produto** *(Solid. Saida - B1\_PICMRET)* ou da**Exceção Fiscal** *(Margem Lucro / F7\_MARGEM)* o percentual de ICMS-ST (MVA) estabelecido por norma legal, caso não exista, informe um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial: 

**Cadastro do cliente:**

Tipo (A1\_TIPO) = Consumidor Final

**TES**

Calcula ICMS (F4\_ICM) = Sim   
L. Fiscal. ICMS (F4\_LFICM) = Tributado  
Calc Dif ICM. (F4\_COMPL) = Não   
Mat Consumo (F4\_CONSUMO) = Sim   
Agrega Solid (F4\_INCSOL) = Sim  
Mkp.ICM.Comp (F4\_MKPCMP) = Não   
Marg. Solid. (F4\_MKPSOL) = Nunca (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)  
Ded.ICM.ST (F4\_ICMSTMT) = Não

**Exemplo da memória de Calculo:**

Valor da Mercadoria: R$ 1.000,00  
Alíquota interestadual: 7  
Alíquota do Destino: 18  
Diferença de alíquotas: 11

Base de calculo: R$ 1.000,00 / 0,89 = R$ 1.123,60  
ICMS interestadual: R$ 1.000,00 \* 7% = R$ 70,00  
Calculo ICMS ST: R$ 1.123,60 \* 11% = R$ 123,60  
Valor ICMS ST: R$ 123,60

Link do parecer elaborado pela consultoria da TOTVS

<http://tdn.totvs.com.br/pages/releaseview.action?pageId=450143442>
