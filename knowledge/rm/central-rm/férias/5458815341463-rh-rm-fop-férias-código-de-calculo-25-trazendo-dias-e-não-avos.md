---
article_id: 5458815341463
category: Férias
content_hash: 4b3859e998323d2134ba17e14d02663b28908e238a7dcf5e0b308a85123bf439
fetched_at: '2026-06-28T22:46:56.306901+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Código de calculo 25 trazendo dias e não avos'
type: support-article
updated_at: '2022-04-18T14:21:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5458815341463-RH-RM-FOP-F%C3%A9rias-C%C3%B3digo-de-calculo-25-trazendo-dias-e-n%C3%A3o-avos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao lançar o evento com código de calculo 25, na referência está dias e não avos, como corrigir?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Realizar a seguinte parametrização, conforme abaixo:  
  
Quando no sindicato do funcionário o parâmetro **Permite antecipação de dias de férias do próximo período aquisitivo** estiver marcado, as férias proporcionais na rescisão são demonstradas em dias.  
  
Isso porque, quando ocorrer situação do número de dias de férias não representar um número inteiro de avos, não teria como demonstrar corretamente estes avos na referência.  
   
**Veja exemplo:**   
O funcionário tem direito a 3/12 avos de férias e já antecipou 1 dia. Na rescisão é pago 6.5 dias de férias proporcionais. Não tem como representar este número em avos.   
            
**![](https://totvssuporte.zendesk.com/attachments/token/5JuqrPqMDMBsGGtdft5XJK0mJ/?name=inline-561261889.png)**  
Outra sugestão é, caso seu parâmetro esteja marcado e você precise que mostre avos na referência das férias proporcionais, pode criar uma fórmula de referência dentro do cadastro do evento, para converter dias em avos.  
  
**Saiba mais**  
[Cálculo de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452719160)
