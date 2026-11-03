---
article_id: 360054351314
category: RH - Dissídio
content_hash: 60bbcc7f1f4f9a68da88022f8eed8302b7261498da03c65fc39e2640b04c153d
fetched_at: '2026-06-28T22:43:44.320403+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Quando executar a rotina de dissídio retroativo
  (GPEM690)
type: support-article
updated_at: '2021-04-30T00:19:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054351314-RH-Linha-Protheus-GPE-Quando-executar-a-rotina-de-diss%C3%ADdio-retroativo-GPEM690
---

**Dúvida**Quando e para quais funcionários deve ser executado a rotina de dissídio retroativo (GPEM690)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Qual a diferença entre Reajuste Salarial e Dissidio?  
Quando fala-se de reajuste salarial é automaticamente condicionado a pensar em dissidio retroativo. Porém só é considerado dissidio coletivo quando o reajuste anual não foi acordado naturalmente por empregadores e empregados.  
  
O que é: "Dissídios coletivos são ações propostas à Justiça do Trabalho por pessoas jurídicas (Sindicatos, Federações ou Confederações de trabalhadores ou de empregadores) para solucionar questões que não puderam ser solucionadas pela negociação direta entre trabalhadores e empregadores."  
  
**Fonte**: <http://www.guiadedireitos.org/index.php?option=com_content&view=article&id=242%3Adissidios-coletivos&catid=21%3Adireitos-do-trabalhador&Itemid=46>  
  
Por isso deve ser alinhado, quais os casos que caberiam o calculo do dissidio, abaixo mais detalhes dos casos que enquadram-se e os que não enquadram-se:

|  |  |  |  |
| --- | --- | --- | --- |
| **CENÁRIOS QUE SE ENQUADRAM OU NÃO NO CÁLCULO DE DISSIDIO RETROATIVO** | | | |
| **Situação** | **Exemplo** | **Resultado esperado** | **Executa rotina de dissídio (GPEM690)** |
| Quando a data base de dissidio foi ultrapassada e o sindicato x sindicato patronal chegou num acordo | Data base em 04/2020 e estamos em junho houve acordo e a empresa terá que pagar os % dos meses anteriores em 06/2020. | Dentro da rotina de dissídio será calculada as diferenças de Abril e Maio. Após a geração do dissídio o salário será atualizado para que a folha de Junho já o considere. | Sim. |
| Funcionário demitido após a data base de dissidio | Data base de dissidio: 04/2020 e o funcionário foi demitido em 05/2020 e o acordo saiu no mês 06/2020. | Dentro da rotina de dissídio será calculado apenas as diferenças da competência 04. Após geração e atualização do salário a rescisão complementar será calculada para pagamento das diferenças rescisórias. | Sim |
| Foi antecipado um % anteriormente, e agora será necessário calcular as diferenças de dissidio. | Data base 06/2020, antecipação em 07/2020. Divulgação do percentual 09/2020. | Mês atual 09/2020, é necessário calcular as diferenças dos meses 06,07,08 e 09/2020, sendo que no mês 06 as diferenças serão pagas pelo % integral, pois neste mês não houve reflexo da antecipação. | Sim |
| Funcionário demitido no mês anterior a data base de dissidio | Data base de dissidio: 04/2020 e o funcionário foi demitido em 03/2020. | De acordo com a lei 7238/84, é devido uma multa no valor de 1 salario base do funcionário em caso de dispensa faltando 30 dias para a data base da categoria. Isso é calculado na própria rescisão, e não é necessário o calculo do dissidio. \*\*\*Há não ser que haja projeção do aviso e a data final de demissão recaia sobre o mês da data base (nesse caso também será necessário executar a rotina de dissidio retroativo GPEM690). | Não |
| Funcionário demitido no mês da data base do dissidio | Data base de dissidio em 04/2020 e demissão em 04/2020 e o acordo foi finalizado em 06/2020 | É necessário calcular o dissidio, nesse cenário o sistema não vai gerar diferenças de valores já que a demissão ocorreu na data base, mas vai gerar informações que serão utilizadas no S-1200 do eSocial. Depois deve ser calculada a rescisão por dissidio. | Sim |
| Acordo saiu no mês da data base | Data base em 04/2020 e o acordo saiu no mesmo mês | Calcular reajuste salarial e não dissidio. | Não |
| Quando a data base de dissidio foi ultrapassada mais o sindicato x sindicato patronal ainda não chegaram em um acordo (ANTECIPAÇÃO DE % e pagamento dos meses anteriores) | Data base em 04/2020 e estamos em junho porém não houve acordo e a empresa deseja adiantar um % em 06/2020. com o % adiantado. | Deve ser feito apenas o reajuste salarial e quando sair o % oficial calcular o dissidio retroativo para todos os meses. Nos meses que não foram calculados já com o % antecipado será calculada a diferença de dissidio a maior (Ou seja com o salario base dissidio anterior a antecipação. | Não |
| Quando a empresa decide antecipar um % pois chegou a conclusão que o acordo pode demorar. | Data base 06/2020, antecipação em 06/2020. | Deve ser feito apenas o reajuste salarial e quando sair o % oficial calcular o dissidio retroativo para todos os meses. | Não |

**Observação**:  
O dissídio retroativo só deve ser executado quando houve atraso na definição do aumento anual e o sindicato patronal juntamente com o sindicato laboral chegou a uma conclusão após a data base.  
  
**Saiba mais**: <https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>
