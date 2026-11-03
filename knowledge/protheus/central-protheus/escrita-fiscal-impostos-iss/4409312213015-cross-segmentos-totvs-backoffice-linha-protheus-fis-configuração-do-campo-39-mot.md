---
article_id: 4409312213015
category: Escrita Fiscal - Impostos - ISS
content_hash: b7f4c9d7502e2f45e0b57ac08f160762b1d38eb206d37ec5166247e472a28667
fetched_at: '2026-06-28T22:39:35.218194+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração do Campo
  "39 Motivo de Não Retenção" Serviços Tomados de prestadores de outros municípios
  para São José dos Campos (Fisa305)
type: support-article
updated_at: '2021-09-23T20:23:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409312213015-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-do-Campo-39-Motivo-de-N%C3%A3o-Reten%C3%A7%C3%A3o-Servi%C3%A7os-Tomados-de-prestadores-de-outros-munic%C3%ADpios-para-S%C3%A3o-Jos%C3%A9-dos-Campos-Fisa305
---

**Dúvida**  
Como preencher o campo "39 Motivo de Não Retenção" na rotina Serviços Tomados de prestadores de outros municípios para São José dos Campos (Fisa305)  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para preencher o campo "**39 Motivo de Não Retenção"** é necessário realizar a seguinte configuração:  
1. Preencher no TES o campo **Mt Ret DESBH (F4\_MTRTBH)** com as opções abaixo:

* Tabela **SF4 – Tipos de Entrada e Saída**

| **Campo** | F4\_MTRTBH |
| --- | --- |
| **Tipo** | Caractere |
| **Tamanho** | 2 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Cabeçalho** | Mt Ret DESBH |
| **Definição** | Mt Ret DESBH |
| ***Help*** | A - Não Indência no Municipio B - Não Tributável C - Pago pelo Prestador/Não Incidente D - Imune E - Isento F - Sociedade de Profissionais G - Profissional Autônomo Inscrito H - Estimativa I - Depósito em Juízo J - Medida Liminar/Cautelar V - Valor de Serviços Menor que o Mínimo |

**Obs.**: O campo também possui opções de **Motivo de não retenção** que servem a outras rotinas, portanto é necessário garantir que o **TES** utilizada esteja com a opção correta como detalhado no layout para o **campo 39 - Motivo da não retenção.**

Mais informações no link abaixo:

https://tdn.totvs.com/pages/releaseview.action?pageId=578632139
