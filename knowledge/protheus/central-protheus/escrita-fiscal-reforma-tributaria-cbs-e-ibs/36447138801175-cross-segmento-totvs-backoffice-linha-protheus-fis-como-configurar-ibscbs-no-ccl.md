---
article_id: 36447138801175
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 4a0196abf6c28730274e1e13a2646c32be7f15190ceee047917d9c32ff317b77
fetched_at: '2026-06-28T22:39:15.728654+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  IBS/CBS no cClasstrib 550001 de forma Hibrida?
type: support-article
updated_at: '2026-06-10T13:50:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36447138801175-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-IBS-CBS-no-cClasstrib-550001-de-forma-Hibrida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126461847) Tempo aproximado para leitura: 00:10**min**  
  
**Dúvida**  
Como configurar IBS/CBS no cClasstrib 550001 de forma Hibrida?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Nesse exemplo vamos trabalhar com a forma Hibrida de calculo, sendo ICMS, PIS e COFINS pelo TES e IBS/CBS pelo Configurador de tributos

<https://tdn.totvs.com/pages/releaseview.action?pageId=955482625>

Tabela cClasstrib atualizada , conforme instrução

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)

**Exemplo de Calculo**

Mercadoria = 1000,00

TES  
CFOP : 5501  
Calcula icms = não  
L fiscal icms = outros  
CST = 41  
pis/cof = ambos  
Cred pis/cof = não calcula  
CST pis =09  
CST cof = 09  
   
 Quando a tag `ind_gTribRegular` possui o valor "1", significa que a classificação tributária (cClassTrib) informada exige o preenchimento detalhado do grupo de tributação regular para aquele item específico da nota fiscal.

O código **cClassTrib 5500001** refere-se a uma situação de **suspensão do IBS (Imposto sobre Bens e Serviços) e da CBS (Contribuição sobre Bens e Serviços)**  
 

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 550 | Suspensão | 550001 | Exportações de bens materiais | Exportações de bens materiais, observado o art. 82 da Lei Complementar nº 214, de 2025. | Art. 82. Poderá ser suspenso o pagamento do IBS e da CBS no fornecimento de bens materiais com o fim específico de exportação a empresa comercial exportadora que atenda cumulativamente aos seguintes requisitos: | Art. 82 | Sem alíquota | 0 | 0 | N/A | 1 |

   
Dessa forma devem ser usados os impostos abaixo:  
IBSERG CBSREG IBSEST CBSFED

* IBSMUN
* IBSMRG  
     
     
  Perfil de Produtos  
  TP0001

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126463895)  
   
Perfil de Operação  
Remessa P/ fim especifico de exportação   
5501

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126464535)  
   
Perfil de Participantes  
Todos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447138777239)  
   
Perfil de Origem x destino  
000002 - todas as ufs

   
Regra de base de calculo  
O:ZERO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126465687)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447138778135)

Regra de alíquota  
O:ZERO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126466455)  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126466839)  
Regra de escrituração  
Incidência = outros  
cClasstrib = 550001  
CST = 550

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126467607)  
   
Regra de Calculo Documentos Fiscais - IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126468247)  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126468375)

Regra de Calculo Documentos Fiscais - IBSERG

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126468631)  
Regra de Calculo Documentos Fiscais - CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447138783895)

Regra de Calculo Documentos Fiscais - CBSREG

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36447126469271)

Regra de Calculo Documentos Fiscais - IBSMUN

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36780901410711)

Perfis os mesmos

Regra de Calculo Documentos Ficais - IBSMRG

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36780918089751)

Perfis os mesmos

Parecer da Consultoria Totvs para o imposto Regular

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=935633509>

Pedido de Venda

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36780901413783)

Sistema atualizado para a transmissão de acordo com a instrução

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS>

* Por padrão MV\_CSTGXML vem com os seguintes CST: **000/200/210/220/510/550/830**

IBSCBS>  
<CST>**550**</CST>  
<cClassTrib>**550001**</cClassTrib>  
<gIBSCBS>  
<vBC>**0**</vBC>  
<gIBSUF>  
<pIBSUF>**0**</pIBSUF>  
<gDevTrib>  
<vDevTrib>**0**</vDevTrib>  
</gDevTrib>  
<vIBSUF>**0**</vIBSUF>  
</gIBSUF>  
<gIBSMun>  
<pIBSMun>**0**</pIBSMun>  
<vIBSMun>**0**</vIBSMun>  
</gIBSMun>  
<vIBS>**0**</vIBS>  
<gCBS>  
<pCBS>**0**</pCBS>  
<gDevTrib>  
<vDevTrib>**0**</vDevTrib>  
</gDevTrib>  
<vCBS>**0**</vCBS>  
</gCBS>  
<gTribRegular>  
<CSTReg>**550**</CSTReg>  
<cClassTribReg>**550001**</cClassTribReg>  
<pAliqEfetRegIBSUF>**0**</pAliqEfetRegIBSUF>  
<vTribRegIBSUF>**0**</vTribRegIBSUF>  
<pAliqEfetRegIBSMun>**0**</pAliqEfetRegIBSMun>  
<vTribRegIBSMun>**0**</vTribRegIBSMun>  
<pAliqEfetRegCBS>**0**</pAliqEfetRegCBS>  
<vTribRegCBS>**0**</vTribRegCBS>  
</gTribRegular>  
</gIBSCBS
