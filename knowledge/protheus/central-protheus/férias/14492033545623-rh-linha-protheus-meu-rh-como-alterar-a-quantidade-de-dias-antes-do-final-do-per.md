---
article_id: 14492033545623
category: FÉRIAS
content_hash: 2e2fc9924f9e74a3e19b9becb64346c177e274f98b384064fc1e83c91754ee13
fetched_at: '2026-06-28T22:44:34.537444+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como alterar a quantidade de dias antes do final
  do período concessivo para início da solicitação de férias
type: support-article
updated_at: '2026-05-13T14:03:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14492033545623-RH-Linha-Protheus-Meu-RH-Como-alterar-a-quantidade-de-dias-antes-do-final-do-per%C3%ADodo-concessivo-para-in%C3%ADcio-da-solicita%C3%A7%C3%A3o-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30647788816279) Tempo aproximado para leitura: **03:00 min**  
  
**Dúvida**  
Como alterar a quantidade de dias antes do final do período concessivo para início da solicitação de férias?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Para o App Meu RH é possível **definir** uma **quantidade de dias, antes** do **final do período concessivo** do funcionário, para solicitação férias, através do uso do parâmetro **MV\_DSOLFER**.  
  
Para o Meu RH, o sistema **soma o conteúdo do parâmetro MV\_DSOLFER com a quantidade de dias de direito do funcionário** e **subtrai** do período, trazendo uma data limite para a solicitação de férias.  
   
Ou seja, se o parâmetro **MV\_DSOLFER for definido como 30** e a **quantidade de dias de direito restante** para o período aquisitivo for de **11 dias**, será trazido a conta **subtraindo 41 dias do final do período concessivo**, para a **solicitação das férias** via App Meu RH.  
   
Segue um exemplo:  
O funcionário possui 10 dias já gozados de férias e 20 dias de direito já adquirido:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40439490736791)  
  
   
**Período aquisitivo de 01/03/2022 a 28/02/2023**  
**MV\_DSOLFER = 60**  
  
**60+20 = 80 dias antes**, no caso de 01/03/2024 para não causar o dobro de férias, resulta que a solicitação de férias precisa iniciar até o dia 12/12/2023:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40439490744343)  
  
   
Se for alterado o **MV\_DSOLFER** para 30 neste mesmo exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40439511032855)  
  
**Saiba Mais**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
