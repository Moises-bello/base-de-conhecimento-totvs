---
article_id: 23764682329367
category: Financeiro - Contas a Pagar
content_hash: 73414db7cf0e4145cd622ab5f187a6bb5a0cf15ce6f7492e9ffc7b921b7d5456
fetched_at: '2026-06-28T22:38:08.307447+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA340 - Compensação
  entre moedas estrangeiras apresentando saldos divergentes
type: support-article
updated_at: '2024-05-27T17:55:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23764682329367-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Compensa%C3%A7%C3%A3o-entre-moedas-estrangeiras-apresentando-saldos-divergentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23764682315415) Tempo aproximado para leitura: **05:00 min****Dúvida**Porque o valor do saldo dos títulos, na compensação entre moedas estrangeiras, aparecem divergentes?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Isso ocorre por conta da **Paridade Cambial**:  
O **Financeiro**, assim como demais módulos que fazem integração com o módulo **Financeiro**, fazem a conversão de moedas considerando sempre a paridade com a moeda padrão (**Moeda 01**). Sendo assim, qualquer conversão de moedas é realizado primeiramente a conversão para a moeda padrão e posteriormente aplica-se a taxa de conversão para a moeda final do processo que está sendo realizado.  
  
**Exemplo:**  
Ao realizar a compensação entre uma **NF** e uma **PA**  
- **NF** em **Dólar** com o valor de 1000,00 e taxa de 4,00  
- **PA** em **Euro** com o valor de 1000,00 e taxa de 4,50  
  
**1.** Ao selecionar a **NF** para compensar, será apresentada a **PA** para ser selecionada e o valor do saldo da **PA** estará convertido em **Dólar** (1125,00), pois o sistema calcula a conversão para **moeda 01** e utiliza a **taxa** de 4,50, após divide pela **taxa do Dólar** 4,00:  
  
(**EUR**) 1000,00 x 4,50 = 4500,00 / 4,00 = (**USD**) 1125,00  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764690002327)  
  
**2.** Ao selecionar a **PA** para compensar, será apresentada a **NF** para ser selecionada e o valor do saldo da **NF** estará convertido em **Euro** (888,89)**,** pois o sistema realizará o mesmo procedimento, converte o valor para **moeda 01** e utiliza a taxa de 4,00, após divide pela **taxa do Euro** 4,50:  
  
(**USD**) 1000,00 x 4,00 = 4000,00 / 4,50 = (**EUR**) 888,89  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23764690003095)  
  
**Importante**  
O parâmetro **MV\_CMTXCON** permite realizar a **compensação a pagar/receber** entre títulos em outras moedas com taxas contratadas distintas. **T = Permite / F = Não permite**.  
  
**Saiba Mais**  
[Compensação contas a pagar - FINA340](https://tdn.totvs.com/pages/releaseview.action?pageId=504794483)  
[Padrão de gravação dos movimentos em moeda estrangeira](https://tdn.totvs.com/pages/releaseview.action?pageId=552097830)
