---
article_id: 36312155068823
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 54ffdc9e871d63a1503feeffa04bdc1f75d08ff9247daa097782ba03563d5175
fetched_at: '2026-06-28T22:39:15.798460+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o
  cClasstrib 410 para operações Isentas no fisa170 forma Hibrida?
type: support-article
updated_at: '2026-03-13T14:31:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36312155068823-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-cClasstrib-410-para-opera%C3%A7%C3%B5es-Isentas-no-fisa170-forma-Hibrida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36312155042583) Tempo aproximado para leitura: 00:10**min**  
  
**Dúvida**  
Como configurar o cClasstrib 410 para operações Isentas no fisa170 forma Hibrida?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Nesse exemplo vamos trabalhar com a forma Hibrida de calculo, sendo ICMS, PIS e COFINS pelo TES e IBS/CBS pelo Configurador de tributos

<https://tdn.totvs.com/pages/releaseview.action?pageId=955482625>

**Exemplo de Calculo**

Mercadoria = 1000,00

Coluna isento ICMS = 1000,00

Coluna isento IPI = 1000,00

TES

CFOP = 5915 - Remessa para conserto

Calcula ICMS = não

L fiscal ICMS = Isento

CST = 40

PIS/COF = ambos

Cred PIS/COF = calcula

CST PIS= 06

CST COF= 06

IBS - zerado

CBS - zerado

ID tributos

CBSFED

IBSEST

Perfil de Produtos: **TPP001**

Perfil de Participantes: **TPP001**

Perfil Origem x destino = 000002 - todas as origens

Perfil Operações - criei uma especifica para o CFOP 5915/6915

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312140438295)

Regra de Base de calculo IBS/CBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312155044759)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312140441495)

Regra de Aliquota IBS/CBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312155046295)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312140443799)

Regra de escrituração IBS/CBS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312155047703)

Regra de Calculo Documentos Fiscais - IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312140448279)![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312155049495)

Regra de Calculo Documentos Fiscais - CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312155050135)

Perfis são os mesmos

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312155050647)

Gravação na CJ3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312140454807)

F2D

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36312140456343)

<IBSCBS>

<CST>**410**</CST>

<cClassTrib>**410004**</cClassTrib>

</IBSCBS>

Teste de transmissão de acordo com a documentação abaixo:

https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS
