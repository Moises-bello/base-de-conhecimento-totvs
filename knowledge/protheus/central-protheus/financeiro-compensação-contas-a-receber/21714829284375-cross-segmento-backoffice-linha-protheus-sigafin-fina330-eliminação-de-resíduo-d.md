---
article_id: 21714829284375
category: Financeiro - Compensação Contas a Receber
content_hash: 139b19298d7edd0dee4922e424d55ae89239dac3839254c33fce8d6fd4f8d0ac
fetched_at: '2026-06-28T22:37:40.448050+00:00'
product: protheus
section_id: 35056224784407
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA330 - eliminação
  de resíduo de RA após compensação
type: support-article
updated_at: '2026-03-04T17:45:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21714829284375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA330-elimina%C3%A7%C3%A3o-de-res%C3%ADduo-de-RA-ap%C3%B3s-compensa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21714821319063) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Como eliminação de resíduo de RA após compensação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Em situações em que é compensada uma NF com o RA, e no título de antecipação resta um valor em centavos, podemos fazer a baixa automática desse resíduo, fazendo com que ele fique baixado e não apareça em aberto.

1. Exemplo:

* -Através da rotina **FINA330**, é selecionado um título de partida do tipo RA (adiantamento) em dólar. **Seu valor convertido em reais é de R$ 1000,05** ;
* Na tela de seleção de títulos a serem compensados, são selecionados alguns títulos em reais **totalizando R$ 1000,03** (diferença de 2 centavos em relação ao RA);
* Para que todos os títulos envolvidos tenham seus saldos zerados ao final do processo de compensação, o parâmetro [MV\_TOLERPG](https://tdn.totvs.com/pages/releaseview.action?pageId=225949954) deve estar configurado com um valor igual ou maior a 0,02 (dois centavos), caso contrário a diferença remanescente ficará no saldo do título de adiantamento (ficando este em aberto).

2. Cadastrei o meu parâmetro com 0.60, ou seja, se o meu resíduo do RA for igual ou menor que esse valor, o sistema deve baixá-lo automaticamente.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21714829269527)

3. Tenho meu RA, no valor de R$ 100,00, e meu título NF no valor de R$ 99,80, restando R$ 0,20 no meu RA, que é um valor menor do que cadastrado no parâmetro, sendo assim, deve baixar o RA também após a compensação.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21714829270295)

4. Ao realizar a compensação, ele baixa os dois títulos.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21714829272599)
