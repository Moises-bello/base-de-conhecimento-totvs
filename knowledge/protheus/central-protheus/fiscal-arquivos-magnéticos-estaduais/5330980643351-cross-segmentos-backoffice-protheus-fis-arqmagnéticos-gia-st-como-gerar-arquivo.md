---
article_id: 5330980643351
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 0d5fa9a508904eb6ab90bea0bc23ee210d236660e21c138e7c696b2e747a3d18
fetched_at: '2026-06-28T22:42:11.642711+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GIA-ST - Como
  gerar arquivo GIA ST?
type: support-article
updated_at: '2022-08-17T19:32:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5330980643351-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GIA-ST-Como-gerar-arquivo-GIA-ST
---

**Dúvida**Como gerar arquivo GIA ST?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12  
  
**Solução**

**1. Introdução:**

Disponível na rotina **Instruções Normativas (MATA950)** a geração do arquivo pré-formatado para a importação da **Guia de Informação e Apuração do ICMS Substituição Tributária dos estados brasileiros (GIAST-BR).**  
  
O programa disponível no sistema trata exclusivamente das informações referentes ao ambiente **Livros Fiscais (SIGAFIS)**, sendo adicionado a opção **“Aglutina Obrigação?”** que tem o objetivo de permitir ao usuário aglutinar as informações de duas ou mais **filiais** por **CNPJ**.

A partir da **Portaria CAT 92/98**, **Anexo V GIA-ST Nacional**, as Movimentações Fiscais Tipo B (Beneficiamento) serão consideradas na Geração da **GIASTBR**.

|  |  |
| --- | --- |
| **A quem se destina** | Aos contribuintes que possuem inscrição estadual em mais de uma UF, ainda que no período não tenham ocorrido operações sujeitas à substituição tributária. |
| **Objetivo** | Esta declaração tem por finalidade demonstrar o imposto apurado fora do Estado em cada período de apuração, bem como apresentar outras informações de interesse econômico-fiscal. |
| **Prazo de entrega** | A GIA-ST deverá ser transmitida até o dia 10 (dez) do mês subsequente ao da apuração do imposto. |
| **Competência** | Estadual |
| **Aplicativo disponibilizado pelo Fisco** | Existem 02 (duas) formas de se apresentar o arquivo magnético:   * Incluir a declaração por meio do programa gerador GIAST, gerar o arquivo texto e validar, sem a intervenção de outro sistema. * Gerar o arquivo texto por meio da implementação deste doumento e validar pela Internet. |
| **Versão do aplicativo contemplado** | A versão do aplicativo deve ser consultada de acordo com o Estado. |
| **Onde encontrar** | <https://www.sefaz.rs.gov.br/DWN/GIASTv3.aspx> |
| **Versão** | **3 - GIASTBR.INI** |
| **Legislação contemplada** | RESOLUÇÃO SEF N.º 6.351 DE 15 DE OUTUBRO DE 2001 |

**2 - Configurações para gerar o arquivo:**

Siga o manual completo: <https://tdn.totvs.com/pages/releaseview.action?pageId=643557353>

**3 - Arquivos INIs em anexo.**
