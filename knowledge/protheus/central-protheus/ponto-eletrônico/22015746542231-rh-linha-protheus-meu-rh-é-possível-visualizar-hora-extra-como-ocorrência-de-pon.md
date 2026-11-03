---
article_id: 22015746542231
category: PONTO ELETRÔNICO
content_hash: 37d0eedbe6493711fc3ea056c42a8e4f7a189c753fa361e789513ee051da01ba
fetched_at: '2026-06-28T22:44:36.513351+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - É possível visualizar Hora Extra como Ocorrência
  de Ponto no Meu RH
type: support-article
updated_at: '2026-06-26T21:24:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22015746542231-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-visualizar-Hora-Extra-como-Ocorr%C3%AAncia-de-Ponto-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22015746522263) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
É possível visualizar Hora Extra como Ocorrência de Ponto no Meu RH  
  
**Ambiente**  
TOTVS RH Linha Protheus - Meu RH – Todas as versões  
  
**Solução**  
No Meu RH será possível exibir as **horas extras dentro das Ocorrências.**  
Para buscar corretamente os **eventos de horas extras cadastrados no módulo Ponto Eletrônico**, a classificação é OBRIGATÓRIA **(P9\_CLASEV)** no cadastro de eventos, e precisa ser 01.  
![](https://tdn.totvs.com/download/attachments/795095167/image2023-10-13_9-32-49.png?version=1&modificationDate=1697200369657&api=v2)  
  
As horas extras serão agrupadas em alguns tipos, conforme os tipos de horas extras **cadastrados no módulo SIGAPON - Ponto Eletrônico.**  
![image2023-10-13_9-36-4.png](https://tdn.totvs.com/download/attachments/795095167/image2023-10-13_9-36-4.png?version=1&modificationDate=1697200564640&api=v2)  
  
Caso o tipo seja **1, 5, A, B** → serão classificadas como horas extras **normais**.  
![image2023-10-13_9-16-55.png](https://tdn.totvs.com/download/attachments/795095167/image2023-10-13_9-16-55.png?version=1&modificationDate=1697200184773&api=v2)

Caso o tipo seja **2, 6, C, D** → serão classificadas como horas extras de **descanso**.  
![image2023-10-13_9-16-29.png](https://tdn.totvs.com/download/attachments/795095167/image2023-10-13_9-16-29.png?version=1&modificationDate=1697200184947&api=v2)

Caso o tipo seja **3, 7, E, F** → serão classificadas como horas extras **compensadas**.  
![image2023-10-13_9-18-6.png](https://tdn.totvs.com/download/attachments/795095167/image2023-10-13_9-18-6.png?version=1&modificationDate=1697200184447&api=v2)

Caso não se enquadre em **nenhum dos tipos acima** mencionados, então será classificadas como **hora extra de feriado.**  
![image2023-10-13_9-29-10.png](https://tdn.totvs.com/download/attachments/795095167/image2023-10-13_9-29-10.png?version=1&modificationDate=1697200184253&api=v2)

No filtro, é possível escolher a opção **Horas Extras**:  
![image2023-10-13_9-54-49.png](https://tdn.totvs.com/download/attachments/795095167/image2023-10-13_9-54-49.png?version=1&modificationDate=1697201689363&api=v2)

Haverá o totalizador das horas extras.  
![image2023-10-13_10-5-50.png](https://tdn.totvs.com/download/attachments/795095167/image2023-10-13_10-5-50.png?version=1&modificationDate=1697202350587&api=v2)  
  
**IMPORTANTE**:   
A hora extra será agrupada de acordo com o cadastro da tabela SP4 - Tipos de horas extras.  
Caso não exista classificação na SP4, todas as horas serão classificadas como horas extras normais.

**Saiba Mais**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
