---
article_id: 360029173833
category: RH - Integração de Titulo
content_hash: 89c3fabc8bad0003d8d1d5540921943d08c2a58a712335143ea81b0fa872c4f2
fetched_at: '2026-06-28T22:43:36.251231+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar um título de líquido de rescisão
type: support-article
updated_at: '2025-07-29T18:49:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029173833-RH-Linha-Protheus-GPE-Como-gerar-um-t%C3%ADtulo-de-l%C3%ADquido-de-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33799263608343) Tempo aproximado para leitura: **00:02:00 min****

**Dúvida**Como gerar um título de líquido de rescisão  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Versão 12.  
  
**Solução**Para efetuar a geração de um título de líquido de rescisão, realize os seguintes passos:  
1. Realize o cálculo da rescisão:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041933534)  
  
2. Acesse Miscelânea -> Títulos -> Definição e configurar um título de líquido de rescisão. No exemplo abaixo, usaremos o agrupamento por funcionário (gerando 1 título para cada funcionário).   
Após as configurações iniciais, selecione "Definir título":  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041933974)  
  
3. Será apresentada uma janela para selecionarmos a verba e a tabela onde buscaremos o cálculo para geração do título. **Tratando-se de rescisão, o cálculo estará na tabela SRR**e utilizaremos como filtro para busca a Data de Pagamento:   
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042777733)  
**Atenção:** A verba selecionada com ID de cálculo 0126 deverá possuir a legenda verde para que seja considerada como positiva.

4. Acesse Miscelânea ->Títulos -> Geração e configure os parâmetros de acordo com o título que será gerado:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042778893)  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042778993)

**Importante:** A data de busca de pagamento deve compreender a data de pagamento que foi informada no campo Dt. Homologa (RG\_DATAHOM) e gravada na data de pagamento do cálculo.   
5. Acesse Miscelânea -> Títulos -> Manutenção e verifique as informações do título gerado:   
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042791073)

**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
