---
article_id: 360026581254
category: RH - Integração de Titulo
content_hash: 80f32188f38bb907ce56437f095edaf7849f86d61644e8fdd387671f624dc054
fetched_at: '2026-06-28T22:43:37.134710+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar um título de líquido de férias
type: support-article
updated_at: '2025-07-18T14:07:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026581254-RH-Linha-Protheus-GPE-Como-gerar-um-t%C3%ADtulo-de-l%C3%ADquido-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558702922135)Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Como gerar um título de líquido de férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para efetuar a geração de um título de líquido de férias, realize os seguintes passos:  
  
1.Calcule as férias:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042388173)  
  
2. Acesse Miscelânea -> Títulos -> Definição e configure um título de líquido de férias. No exemplo abaixo usaremos o agrupamento por funcionário (gerando 1 título para cada funcionário).   
Após as configurações iniciais, selecione "Definir título":  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042388433)  
  
3. Será apresentada uma janela para selecionarmos a verba para geração (verba Líquido Pago Férias = ID 0102) e a tabela onde buscaremos o cálculo para geração do título. **Tratando-se de férias, o cálculo estará na tabela SRR** e utilizaremos como filtro para busca a Data de Pagamento:  **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042389213)**

**Atenção:** A verba selecionada embora seja uma verba de desconto (ID 0102 De cor Vermelha), ao ser selecionada, deverá possuir a **legenda verde** (clicar duas vezes sobre a legenda, assim a cor irá mudar para verde) para que seja considerada na geração do título.  
  
4. Acesse Miscelânea ->Títulos -> Geração e configure os parâmetros de acordo com o título que será gerado:![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042389813)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041540894)  
 **Importante:**A data de busca de pagamento deve compreender a data de pagamento que foi informada no campo Data Recebimento Férias (RH\_DTRECIB) e gravada na data de pagamento do cálculo.   
  
5. Acesse Miscelânea -> Títulos -> Manutenção e verifique as informações do título gerado:   
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042394113)  
  
**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
