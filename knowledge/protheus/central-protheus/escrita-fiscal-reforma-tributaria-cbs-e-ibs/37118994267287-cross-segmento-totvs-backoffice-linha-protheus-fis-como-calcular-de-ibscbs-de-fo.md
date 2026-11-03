---
article_id: 37118994267287
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 28c387bcc36e11e1ef25d318e987e31e783777a74b0ee82f8accf5e85478da05
fetched_at: '2026-06-28T22:39:15.669894+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular de
  IBS/CBS de forma Hibrida  na NF importação ?
type: support-article
updated_at: '2026-06-12T19:30:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37118994267287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-de-IBS-CBS-de-forma-Hibrida-na-NF-importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37118994255767) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
 Como calcular de IBS/CBS de forma Hibrida  na NF importação ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

MV\_estado = SP  
MV\_EIC0064 = .F.  
   
Fornecedor = EX  
Tipo = outros

Produto

Aliq ipi =5,20%

origem = 1

   
TES

|  |  |
| --- | --- |
| Calcula ICMS (F4\_ICM) | Sim |
| Calcula IPI (F4\_IPI) | Sim |
| Cod.Fiscal (F4\_CF) | Algum Iniciado por “3” Ex: 3101 |
| L. Fisc. ICMS (F4\_LFICM) | Tributado |
| L.Fisc. IPI (F4\_LFIPI) | Tributado |
| IPI na base (F4\_INCIDE) | Sim |
| Agrega Valor (F4\_AGREG) | I – ICMS+Merc |
| PIS/COFINS (F4\_PISCOF) | 3- Ambos |
| Cred. PIS/COF (F4\_PISCRED) | 1 – Credita |
| Agr. Cofins (F4\_AGRCOF) | C – COF+Merc |
| Agr. PIS (F4\_AGRPIS) | P – PIS+ Merc |
| PS/CF Import (F4\_INTBSIC) | 3 - Ambos |
| Calc.Ipi.Frete (F4\_IPIFRET) | N - Não |

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Nota fiscal de Importação pelo Documento de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022575671-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-fiscal-de-Importa%C3%A7%C3%A3o-pelo-Documento-de-Entrada)  
   
TES  
**Valor do Produtos = 12987,95**  
II = 2104,05  
SISCOMEX = 154,23  
ICMS = 3854,00  
IPI = 784,78  
PIS= 272,75  
COFINS = 1253,34  
**Valor NF Entrada/ Livros Fiscais= 21411,09**  
   
IBS/CBS  
Carga Automatica  
   
**Importante**  
   
Os cadastros incluídos na **Regra de Cálculo - Documentos Fiscais** pela funcionalidade de **Carga Regras de Cálculo CBS/IBS** apresentarão a **Vigência Inicial (F2B\_VIGINI)** para 01/01/2026 e a **Vigência Final (F2B\_VIGFIM)** para 31/12/2026 e o **Status (F2B\_STATUS)** será **"Em Teste".**  
Alterar a data de inicio para 01/11/2025 e status de teste para aprovado

https://tdn.totvs.com/pages/releaseview.action?pageId=955482625  
   
Perfil de Produto

* **Cód Perfil (F24\_CODIGO)**: TPP001
* **Descrição**: PERFIL DE PRODUTOS: TODOS

  + **Cód. Produto (F24\_CDPROD)**: TODOS
  + **Desc. Prod.**: TODOS OS PRODUTOS

Perfil de Participantes

* **Cód Perfil (F22\_CODIGO)**: TPP001
* **Descrição**: PERFIL DE PARTICIPANTES: TODOS CLIENTES TODOS FORNECEDORES
* **Tipo (F22\_TPPART)**: Fornecedor
  + **Participante (F22\_CLIFOR)**: TODOS
  + **Loja (F22\_LOJA)**: ZZ
  + **Razão Social**: TODOS OS FORNECEDORES
* **Tipo (F22\_TPPART)**: Cliente
  + **Participante(F22\_CLIFOR)**: TODOS
  + **Loja (F22\_LOJA)**: ZZ
  + **Razão Social**: TODOS OS CLIENTES

Base de Cálculo:

* **Cód. Regra (F27\_CODIGO)**: TB0001
* **Descrição (F27\_DESC)**: BASE DE CALCULO: CBS FED/IBS EST
* **Valor Origem (F27\_VALORI)**: 11 - Formula Manual
* Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICMS + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS )

Alíquota:

* **Cód. Regra (F28\_CODIGO)**: TA0001
* **Descrição (F28\_DESC)**: ALÍQUOTA 0.9%
* **Valor Origem (F28\_VALORI)**: 04 - Aliquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 0,90

* **Cód. Regra (F28\_CODIGO)**: TA0002
* **Descrição (F28\_DESC)**: ALÍQUOTA 0.1%
* **Valor Origem (F28\_VALORI)**: 04 - Aliquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 0,10

Regras de Cálculo: **TR0001 / TR0002**

**Base de calculo do IBS/CBS**

**Fórmula: ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICMS + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS )**

12.987,95+2.104,05+154,23 =15.246,23 -3854,00-272,75-1253,34 = 9.866,14

9.866,14 \*0,90= 88,80

9866,14 \*0,10 = 9,87

**Nota fiscal de compras**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37118994256279)

CJ3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37118994256919)

F2D

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37118994257687)

Para transmitir a nota fiscal estar atualizado de acordo com a documentação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

XML

IBSCBS>

<CST>**000**</CST>

<cClassTrib>**000001**</cClassTrib>

<gIBSCBS>

<vBC>**9866.14**</vBC>

<gIBSUF>

<pIBSUF>**0.1000**</pIBSUF>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<vIBSUF>**9.87**</vIBSUF>

</gIBSUF>

<gIBSMun>

<pIBSMun>**0**</pIBSMun>

<vIBSMun>**0**</vIBSMun>

</gIBSMun>

<vIBS>**9.87**</vIBS>

<gCBS>

<pCBS>**0.9000**</pCBS>

<gDevTrib>

<vDevTrib>**0**</vDevTrib>

</gDevTrib>

<vCBS>**88.80**</vCBS>

</gCBS>

</gIBSCBS>

</IBSCBS>

</imposto>

<vItem>**21411.10**</vItem>
