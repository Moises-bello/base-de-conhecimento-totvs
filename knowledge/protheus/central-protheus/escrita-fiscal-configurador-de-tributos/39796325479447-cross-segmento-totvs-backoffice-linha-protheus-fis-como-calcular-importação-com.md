---
article_id: 39796325479447
category: Escrita Fiscal - Configurador de Tributos
content_hash: cc2e83c387cd9c13836bf695c28f9b770015b96dbab63c6ee71ef7fd66a511ac
fetched_at: '2026-06-28T22:39:17.139992+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular importação
  com redução de base, cbenef de  forma hibrida ?
type: support-article
updated_at: '2026-04-16T15:13:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39796325479447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-importa%C3%A7%C3%A3o-com-redu%C3%A7%C3%A3o-de-base-cbenef-de-forma-hibrida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39796346741527) Tempo aproximado para leitura: 00:08**min**  
  
**Dúvida**  
Como calcular importação com redução de base forma hibrida ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
Essa documentação vai auxiliar o cliente a configurar o icms com redução de base de calculo  pelo legado para gerar o cBenef , vamos usar o exemplo do estado de SP

**Parâmetros**

MV\_ESTADO = SP

MV\_MTCLF3K =0

MV\_REDIMPO = .T.

MV\_EIC0064 = .T.

**Fornecedor**

Estado = EX

Tipo = outros

**TES**

Calcula icms = sim

Agrega valor = I

Calcula ipi = sim

L fiscal ipi = tributado

IPI na base = sim

% red icm = 48,88

L fiscal icms = Isento ou Outras

pis/cof = ambos

Cred pis/cof = credita

Agr. Cofins (F4\_AGRCOF) = C

Agr. PIS (F4\_AGRPIS) = P

PS/CF Import (F4\_INTBSIC) = 3

Desp. Ac. IPI (F4\_DESPIPI) = Não  
Desp. Ac. PIS (F4\_DESPPIS) = Não  
Desp. Ac. COF (F4\_DESPCOF) = Não

Desp. Ac. ICMS = sim

Exemplo de uma Importação com alíquota de ICMS 18% e redução de base calculo 48,88%.

FOB = 5.000,00

II = 300,00

IPI = 10% = 530,00

PIS = 2,10% = 105,00

Cofins = 9,65% = 482,50

Despesas = 214,50 Taxa Siscomex

Total da importação = 6.632,00

6.632,00/0,912 = 7.271,93

7.271,93 \*48,88% = 3.554,52

3.554,52 \*18% = 639,81

cBenef = SP020110

Cadastrar na rotina Fisa156 de forma manual, conforme orientação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39796346742295)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar os Códigos de Valores Declaratórios de São Paulo no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38006107103639-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-os-C%C3%B3digos-de-Valores-Declarat%C3%B3rios-de-S%C3%A3o-Paulo-no-Protheus)

Fisa140

3102 - CST20 - SP020110 - reflexo com redução de base de calculo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39796325462551)

Reflexo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39796325464471)

IBS/CBS

<https://tdn.totvs.com/pages/releaseview.action?pageId=1025239075>

**Manutenção manual da formula Base de Cálculo:**

* Cód. Regra (F27\_CODIGO): TB0001
* Descrição (F27\_DESC): BASE DE CALCULO: CBS FED/IBS EST
* Valor Origem (F27\_VALORI): 11 - Formula Manual
* Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICM\_TRIBUTADO + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS\_TRIBUTADO + O:VAL\_IPI\_TRIBUTADO )

cClasstrib = 000001

Nota fiscal de compras

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39796325465367)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39796346745623)

cbenef

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39796346746007)
