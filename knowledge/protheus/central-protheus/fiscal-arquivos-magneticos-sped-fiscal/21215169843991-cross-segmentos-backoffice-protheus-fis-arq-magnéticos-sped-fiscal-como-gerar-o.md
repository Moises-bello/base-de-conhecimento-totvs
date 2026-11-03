---
article_id: 21215169843991
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: aefeb9376ef812e1575197ea1211afc8af0e00f756453a1c2429892aeeb022b8
fetched_at: '2026-06-28T22:42:01.160755+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro 0221 para produtos individuais?
type: support-article
updated_at: '2024-02-08T19:52:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21215169843991-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-0221-para-produtos-individuais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21215169799575) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gerar o registro **0221** para **produtos individuais** (sem possuir amarração na **D4C** para Kit/Cestas)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Em primeiro momento é necessário a aplicação dos pacotes do **Fiscal** e **Estoque** para consequentemente realizar a criação da rotina **MATA039** e tabela **D4C** seguindo orientações abaixo.

Pacote da expedição contínua do estoque e fiscal, para realizar da atualização e execução do **UPDDISTR:**

**12.1.33 (Garantia contínua):**  
Estoque:  <https://suporte.totvs.com/portal/p/10098/download?e=1039086>  
Fiscal:  <https://suporte.totvs.com/portal/p/10098/download?e=1039088>  
**12.1.2210:**  
Estoque:  <https://suporte.totvs.com/portal/p/10098/download?e=1080339>  
Fiscal:  <https://suporte.totvs.com/portal/p/10098/download?e=1080345>

**12.1.2310:**  
Estoque:  <https://suporte.totvs.com/portal/p/10098/download?e=1123875>  
Fiscal:  <https://suporte.totvs.com/portal/p/10098/download?e=1123881>

**Documentação:**

[https://tdn.totvs.com/pages/releaseview.action?pageId=816317717](https://tdn.totvs.com/display/public/PROT/SPDFIS+-+Sped+Fiscal#SPDFISSpedFiscal-Bloco0-Abertura,Identifica%C3%A7%C3%A3oeRefer%C3%AAncias)

<https://tdn.totvs.com/display/public/PROT/SPDFIS+-+Sped+Fiscal#SPDFISSpedFiscal-Bloco0-Abertura,Identifica%C3%A7%C3%A3oeRefer%C3%AAncias>

Este processo acima é essencial devido ser necessário ter a tabela **D4C** na **SX2** para obter sucesso na geração do registro neste cenário.

Nas documentações referente à rotina **MATA039** informa que tem o propósito para amarrar produtos referente à Kits/Cestas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21215169801623)

Para produtos que se enquadram neste **exemplo 02** do **Guia Prático**, segue configuração:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21215169805591)

Para gerar o registro neste cenário, não há amarração de produto na **D4C**, é necessário que o campo **B1\_TIPO** do produto utilizado = **ME** - **Mercadoria de Revenda:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21215169806743)

Após isso, realizar a escrituração da nota com o produto mencionado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21215169809047)

Ao gerar o arquivo TXT, deixar a pergunta **0221 = 1 -Sim** ou **03 - Gerar com dados de 2023:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21215169810071)

Ao gerar o Sped Fiscal, segue registro apresentado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21224494590231)
