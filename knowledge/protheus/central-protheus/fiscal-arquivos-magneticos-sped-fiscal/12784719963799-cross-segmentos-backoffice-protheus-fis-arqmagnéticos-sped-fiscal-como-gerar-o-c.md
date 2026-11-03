---
article_id: 12784719963799
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: ded5246116820ec4fbad2ebc2adb4196a5afc868143275e12a770577458eec98
fetched_at: '2026-06-28T22:42:03.540969+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Como gerar o campo campo 19 (Indicador de período de apuração de IPI) no registro
  C170?
type: support-article
updated_at: '2023-03-02T12:46:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12784719963799-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-o-campo-campo-19-Indicador-de-per%C3%ADodo-de-apura%C3%A7%C3%A3o-de-IPI-no-registro-C170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o campo **19 (Indicador de período de apuração de IPI)** no registro **C170** do **Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**O campo **19 (IND\_APUR)** do registro **C170** é gerado com preenchimento quando o documento fiscal contém o campo **Valor IPI - FT\_VALIPI** maior que zero e é carregado conforme a pergunta **Período de Apuração** configurada na w*izard* do **Sped Fiscal**.   
   
Os documentos que alimentam o campo **Valor IPI - FT\_VALIPI** são aqueles escriturados com cadastro  de **TES** com **Cálculo de IPI** e o campo **L Fiscal IPI (F4\_LFIPI) = Tributado.**  
   
Abaixo pergunta, **Quanto a Apuração do IPI Período de Apuração = 0-Mensal** da w*izard* do **SPED Fiscal**:  
   
![](https://totvssuporte.zendesk.com/attachments/token/y6yXZFh9pOZCVal6f2K6WKIyI/?name=inline513104016.png)
