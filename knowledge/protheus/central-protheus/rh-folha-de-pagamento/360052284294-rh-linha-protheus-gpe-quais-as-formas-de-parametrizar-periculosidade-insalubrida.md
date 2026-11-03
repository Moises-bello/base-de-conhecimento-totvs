---
article_id: 360052284294
category: RH - Folha de Pagamento
content_hash: c074c765fe9dbd9ebfe1e179a7f605173c074bb15a89b2794684035c801ad314
fetched_at: '2026-06-28T22:44:16.204097+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Quais as formas de parametrizar Periculosidade
  / Insalubridade
type: support-article
updated_at: '2025-08-13T15:00:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052284294-RH-Linha-Protheus-GPE-Quais-as-formas-de-parametrizar-Periculosidade-Insalubridade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26251718133655) Tempo aproximado para leitura: 00:01:30 min**  
**Dúvida**Quais as formas de parametrizar Periculosidade / Insalubridade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Existem formas diferentes para cálculo dos adicionais de periculosidade e insalubridade. Essa formas são configuradas através do cadastro de sindicatos.  
  
No cadastro de sindicatos Atualizações > Cadastros > Sindicatos , aba Perc/Insal podemos parametrizar a Base de Cálculo da Periculosidade, sendo as opções:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085576193)

1. Salário  
2. Salario+verbas  
3. Salário Minimo  
4. Salario Minimo Estadual  
5. Piso Sindicato  
6. Salario Minimo + Verbas  
7. Salario Minimo Estadual + Verbas  
8. Piso Sindicato + Verbas  
  
O salário utilizado como base será o salário contratual (cadastro) ou salário composto (incorporado), de acordo com a definição da verba.  
  
Para base de cálculo onde se diz **+ Verbas**, o sistema considera as verbas que estão com o campo **RV\_PERICUL**. ou campo **RV\_INSALUB** igual a **SIM**. Dessa maneira as verbas entrarão para base de cálculo da periculosidade. Em Atualizações > Definições Calculo > Verbas.   
No caso de horas extra por exemplo, o valor da hora extra que irá compor a base de cálculo da periculosidade, e não o inverso.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085583613)  
  
Para a parametrização da Insalubridades, também teremos as opções de Base para Cálculo e as opções de percentual para Mínimo, Médio e Máximo.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085580793)  
  
Na caso de salário, o sistema utiliza a verba de adicional para cálculo das demais verbas, como por exemplo hora extra, adicional noturno, entre outras.  
  
No sistema existem identificadores de cálculo para cada situação:  
  
Identificadores de **Insalubridade**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085582313)  
  
Identificadores de **Periculosidade  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084404834)**

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
