---
article_id: 33512207948567
category: eConsignado (Crédito do Trabalhador)
content_hash: 6e5be66d2aab8b4be2fb81766c6c2711d8a566badab56b3e2908098280862c81
fetched_at: '2026-06-28T22:43:07.126705+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH  - Linha Protheus - GPE - Provisionamento do eConsignado  no ADI com calculo
  e provisionamento nas férias dentro da mesma competência - Econsignado MP(1.292/2025)
type: support-article
updated_at: '2026-04-02T13:26:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33512207948567-RH-Linha-Protheus-GPE-Provisionamento-do-eConsignado-no-ADI-com-calculo-e-provisionamento-nas-f%C3%A9rias-dentro-da-mesma-compet%C3%AAncia-Econsignado-MP-1-292-2025
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33512207931415) Tempo aproximado para leitura: **00:02:00min**  
  
**Dúvida**  
Como realizar o provisionamento de forma proporcional no Adiantamento quando já foi provisionado no calculo das férias dentro da mesma competência ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
1. Realizar a importação do arquivo  (como exemplo utilizamos o tipo de arquivo Json)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33512207934615)  
  
2. Gravar os empréstimos   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33512207935127)

3. Na SRK vai ser apresentado todos os empréstimos importado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33514713874071)

4. Calcular as férias e após calculo integrar o roteiro FER  
Nesse exemplo temos calculo de férias em JULHO o provisionamento total foi de: R$ 379,17  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33514668559383)  
  
5. Calculo do ADI com o roteiro FER devidamente Integrado conforme orientação do passo 4.   
O provisionamento no ADI vai ser:  
Total das parcelas R$ 758,36 - 379,17 (já provisionado nas férias) = R$ 379,19 \* 40% = R$ 151,68  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33514668560535)  
**OBS. Nesse cenário o parâmetro MV\_ADTOPRO estava definido com S, porem independente de S ou N , o provisionamento é realizado sobre o saldo da parcela multiplicado pelo percentual do adiantamento.**  
  
**"**No caso de ocorrência simultânea de férias e adiantamento no mesmo período, o valor total provisionado não deve ultrapassar o valor da parcela. Ou seja, se a provisão for realizada integralmente nas férias, não haverá provisão no adiantamento. Caso a provisão nas férias seja parcial, o valor restante será provisionado no adiantamento.  
Importante ressaltar que a provisão deve ser calculada com base nos dias de férias e no percentual do adiantamento, podendo resultar em valores menores que a parcela, mas nunca superiores."

**Saiba Mais:**  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[RH - Linha Protheus - GPE - eConsignado - Informações e atualizações sobre Credito do Trabalhador (MP1.292/2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32304010436119-RH-Linha-Protheus-GPE-eConsignado-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-Credito-do-Trabalhador-MP1-292-2025)  
[Econsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)  
<https://tdn.totvs.com/pages/releaseview.action?pageId=944703898>
