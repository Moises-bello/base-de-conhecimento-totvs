---
article_id: 360015781712
category: RH - FGTS / SEFIP
content_hash: 3d86c7decc68769010286ab831b4600d929a1f4a21435a56fa2cad0854c3dec3
fetched_at: '2026-06-28T22:43:41.378699+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar SEFIP referente ao cálculo de 13º
type: support-article
updated_at: '2025-08-19T14:39:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015781712-RH-Linha-Protheus-GPE-Como-gerar-SEFIP-referente-ao-c%C3%A1lculo-de-13%C2%BA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34286261222295) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**Como gerar SEFIP (Sistema Empresa de Recolhimento do FGTS e Informações à Previdência) referente ao cálculo de 13º?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

* **SEFIP 1º PARCELA**  
  O recolhimento do FGTS - Fundo de Garantia por Tempo de Serviço da primeira parcela **é feito na SEFIP da folha normal**. Não há SEFIP especifica para o 13º pois os lançamentos pagos encontram-se na folha de pagamento. No log de Ocorrências da SEFIP na primeira parcela, os valores de 13º são apresentados na coluna **Rem. Sobre. 13º** conforme imagem abaixo:  
  ![](http://tdn.totvs.com/download/attachments/219682468/image2015-12-8%2014%3A3%3A2.png?version=1&modificationDate=1449579816000&api=v2)
* **SEFIP 2º PARCELA**  
  No caso da segunda parcela é necessário **gerar todas as Guias para pagamento** normalmente.   
  É gerada uma SEFIP da folha de pagamento em dezembro envolvendo os valores de 13º para fim de recolhimento do FGTS separadamente.  
  Posteriormente, é gerada uma SEFIP de 13º apenas para confirmação dos valores já enviados levando as informações referentes a Previdência Social (INSS), conforme exemplo abaixo:  
  Log de Ocorrências SEFIP da FOLHA com 13º segunda parcela (Dezembro)  
  ![](http://tdn.totvs.com/download/attachments/219682468/image2015-12-8%2013%3A59%3A43.png?version=1&modificationDate=1449579617000&api=v2)  
    
  **• SEFIP Declatória do 13º**  
  LOG de ocorrências SEFIP do 13º DECLARATÓRIA (Enviada até dia 31/01 do ano seguinte)  
    
  **Observações:**  
  Parâmetros importantes na SEFIP Declaratória d 13º:  

  **Gerar Tipo? = 13º Salário****Tipo de Modalidade? = Declaração**  
  ![](http://tdn.totvs.com/download/attachments/219682468/image2015-12-8%2014%3A1%3A4.png?version=1&modificationDate=1449579698000&api=v2)  
    
  **Saiba Mais**  
  [Roteiro de Análise 13º Salário - Primeira e Segunda Parcela](http://tdn.totvs.com/pages/viewpage.action?pageId=219682468)

  [RH  - FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
