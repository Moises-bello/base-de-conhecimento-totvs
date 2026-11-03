---
article_id: 360020863132
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: bf9e56e19424d56c9e6b5cf720fe9b139c9776068851477705154cfd9285f2ca
fetched_at: '2026-06-28T22:42:02.245127+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar os Registros C140 e C141
type: support-article
updated_at: '2025-02-11T21:08:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020863132-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-os-Registros-C140-e-C141
---

**Dúvida**Como gerar os registros **C140 -** Fatura (Código 01) e **C141 -**Vencimento da fatura (Código 01)?  
   
 **Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para solucionar a dúvida acima, verifique as orientações:

Registro **C140**: Fatura (Código 01)

Este registro é gerado a partir dos Livros Liscais quando há uma fatura para este documento (**SE1**/**SE2**), e é composto de Notas Fiscais dos seguintes modelos:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “**NF** ou **NFE**”

Registro **C141**: Vencimento da Fatura (Código 01)

É gerado um registro **C141** para cada **C140**, contendo informações complementares da fatura (valor, data do vencimento), e é composto de Notas Fiscais dos seguintes modelos:

* Nota Fiscal Modelo 1 ou 1-A – Espécie “**NF** ou **NFE**”

Importante: Disponibilizado o **Ponto de Entrada SPDFIS09** para gravar informações nos **Registros C140 e C141**.   
Para mais detalhes sobre este ponto de entrada, acesse:   
[SPDFIS09 - Grava informações nos Registros C140 e C141](http://tdn.totvs.com/pages/releaseview.action?pageId=6077180)
