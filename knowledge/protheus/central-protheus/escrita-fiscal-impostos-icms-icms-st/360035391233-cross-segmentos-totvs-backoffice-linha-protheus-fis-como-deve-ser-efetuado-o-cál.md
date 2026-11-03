---
article_id: 360035391233
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: fc79c6aac155ffa9db633c0645a27037fdfe96d76bbbd8d617b7f6287193431c
fetched_at: '2026-06-28T22:39:20.412931+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como deve ser efetuado
  o cálculo do diferencial de alíquota por ICMS-ST para que seja somado ao total da
  Nota Fiscal?
type: support-article
updated_at: '2022-06-06T17:32:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035391233-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-deve-ser-efetuado-o-c%C3%A1lculo-do-diferencial-de-al%C3%ADquota-por-ICMS-ST-para-que-seja-somado-ao-total-da-Nota-Fiscal
---

**Dúvida**

Como deve ser efetuado o cálculo do Diferencial de alíquota por ICMS-ST para que seja somado ao total da Nota Fiscal?  
   
 **Ambiente**

Microsiga Protheus -  Livros Fiscais -  a partir da 11.80  
  
**Solução**

Informe no Cadastro do Produto ou da Exceção Fiscal o percentual de ICMS-ST (MVA) estabelecido por norma legal, caso não exista, informe um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial:

TES

Calcula ICMS (F4\_ICM) = SIM

L. FISC. ICMS (F4\_LFICM) = TRIBUTADO

Calc Dif ICM. (F4\_COMPL) = NÃO

MATL CONSUMO (F4\_CONSUMO) = SIM

AGREGA SOLID. (F4\_INCSOL) = SIM

MKP.ICM.COMP (F4\_MKPCMP) = NÃO

MARG. SOLID. (F4\_MKPSOL) = NUNCA (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)

CLIENTE (SA1) deve ser um dos tipos preenchido no parâmetro MV\_TPSOLCF, o CLIENTE deve ser de um Estado diferente do emitente (MV\_ESTADO) e ter a Inscrição Estadual preenchida.

IPI na Base (F4\_INCIDE): Este campo permite informar se valor de IPI incide na base de ICMS. Para o exemplo a seguir o IPI entrou na base de cálculo do ICMS, desta forma pode ser definido como "Consumidor Final" ou como "Sim/Não

Para tratar Base Dupla deverá configurar o parâmetro MV\_UFBDST informe os estados que devem ter base dupla para o ST e o cadastro do cliente/pedido de venda o tipo de cliente deve ser Consumidor Final.

Note que o sistema irá demonstrar a alíquota Interna do Estado, no entanto o cálculo será realizado pelo diferencial.

Exemplo:

**ICMS Próprio**

Base de Cálculo = R$1000,00

Alíquota interestadual 12%

Valor do ICMS Próprio - R$120,00

**Diferencial de alíquota:**

Base de Cálculo = R$1000,00

Alíquota Interna 18%

Valor do ICMS complementar - R$60,00

**Calculo apresentado pelo sistema com base dupla**

Valor de Mercadoria – R$ 1.000,00 – IPI 5% - Incide na base de ICMS

**ICMS Próprio**

ICMS – 1.050,00 \* 12% = 126,00

IPI – 1.000,00 \* 5% = 50,00 - IPI na base de ICMS

**Diferencial de alíquota:**

Alíquota Interna 18%

((1.050,00 - 126)/0,82) = 1.126,83

ICR – 1.126,82 = 76,82

Valor de Mercadoria R$ 1.126,83

Assuntos Relacionados:

<https://tdn.totvs.com/pages/viewpage.action?pageId=51249690>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034832354>

<https://tdn.totvs.com/pages/viewpage.action?pageId=513418899>
