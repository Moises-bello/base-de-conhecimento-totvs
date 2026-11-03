---
article_id: 1500002188701
category: Anuais
content_hash: c4792652b18c7ea14a580fa277224adb3c7eac586b19a48da813b86f66f43b32
fetched_at: '2026-06-28T22:46:51.196937+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - DIRF/Informe de Rendimentos: Ajuda Compensatória Mensal na
  DIRF conforme Lei nº 14.020, de 6 de julho de 2020'
type: support-article
updated_at: '2025-03-05T18:37:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002188701-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Ajuda-Compensat%C3%B3ria-Mensal-na-DIRF-conforme-Lei-n%C2%BA-14-020-de-6-de-julho-de-2020
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:04:00 min  
  
Dúvida**  
Como declarar a Ajuda Compensatória na DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões**Solução**O pagamento, pelo empregador, de Ajuda Compensatória Mensal, em decorrência da redução proporcional de jornada de trabalho e de salário ou da suspensão temporária de contrato de trabalho tem natureza indenizatória e **não** integra a base de cálculo do imposto sobre a renda retido na fonte ou da declaração de ajuste anual do imposto sobre a renda da pessoa física, conforme estabelece o art. 9º da Lei nº 14.020, de 6 de Julho de 2020, que dispõe sobre o Programa Emergencial de Manutenção do Emprego e da Renda como medida complementar aplicável durante o estado de calamidade pública reconhecido pelo Decreto Legislativo nº 6, de 20 de março de 2020, e da emergência de saúde pública de importância internacional decorrente do coronavírus.  
  
O rendimento pago como Ajuda Compensatória não integrará o salário devido pelo empregador na hipótese de redução proporcional de jornada de trabalho e de salário e deverá ser informado separadamente no campo 'Outros (especificar)' da subficha 'Rendimentos Isentos' do beneficiário do declarante como especificação da rubrica no campo descrição.  
  
Na hipótese do beneficiário ter recebido mais de uma rubrica referente a rendimentos isentos que devam ser informadas no campo 'Outros (especificar)', o declarante poderá informar cada uma, detalhadamente, na ficha 'Informações Complementares - comprovante de rendimentos'.  
  
Para solucionar essa dúvida, verifique o procedimento conforme o **exemplo** abaixo.  
  
1. O evento está lançado na Ficha Financeira nas seguintes competências:  
  
![](https://tdn.totvs.com/download/attachments/592552831/image2021-1-29_17-48-34.png?version=1&modificationDate=1611931714720&api=v2)

![](https://tdn.totvs.com/download/attachments/592552831/image2021-1-29_17-49-9.png?version=1&modificationDate=1611931749833&api=v2)  
  
2. O evento deverá ser informado na aba 'Campo 4 - Rend. Isentos e não Tribut.' sub aba 'Outros (especificar) - Campo 5/Linha8:  
  
![](https://tdn.totvs.com/download/attachments/592552831/image2021-1-29_17-46-56.png?version=1&modificationDate=1611931616793&api=v2)

3. Quando gerado o Informe de Rendimentos, o evento sairá na Linha 07 - Outros: Outros (especificar) - Campo 5/ linha 8, campo 4 - RENDIMENTOS ISENTOS E NÃO TRIBUTÁVEIS:  
  
![](https://tdn.totvs.com/download/attachments/592552831/image2021-1-29_17-47-33.png?version=1&modificationDate=1611931654053&api=v2)

**Informe de Rendimentos com descrição:**Para que no Informe de Rendimentos o campo 'Outros (especificar) - Campo 5/Linha8', retorne com a informação referente a ajuda compensatória mensal, basta editar o nome do campo na tabela dinâmica INT41, conforme exemplo abaixo:  
  
![](https://tdn.totvs.com/download/attachments/592552831/image2021-1-29_18-13-8.png?version=1&modificationDate=1611933188433&api=v2)

No processo de geração da DIRF/Informe de Rendimentos, na aba 'Campo 4 - Rend. Isentos e não Tribut.' a sub aba será retornada com a descrição alterada:

![](https://tdn.totvs.com/download/attachments/592552831/image2021-1-29_18-14-16.png?version=1&modificationDate=1611933256677&api=v2)

Ao gerar o Informe de rendimentos, o campo será retornado com Descrição:  
  
![](https://tdn.totvs.com/download/attachments/592552831/image2021-1-29_18-15-5.png?version=1&modificationDate=1611933305507&api=v2)

**Importante**

Para detalhar no programa da DIRF 2021 as informações complementares detalhando cada rubrica que compõe o campo 'Outros especificar', deverá fazer de forma manual, editando o respectivo campo no programa da Receita. Assim, ao gerar o Comprovante de Rendimentos pelo programa da Receita, irá descriminar cada rubrica, como no exemplo abaixo:

![](https://tdn.totvs.com/download/attachments/592552831/image2021-1-29_18-28-14.png?version=1&modificationDate=1611934094683&api=v2)  
  
Comprovante de Rendimentos gerado no programa da Receita Federal:  
  
![](https://tdn.totvs.com/download/attachments/592552831/image2021-1-29_18-29-9.png?version=1&modificationDate=1611934149377&api=v2)  
  
**Saiba mais**[Ajuda Compensatória Mensal – Lei nº 14.020, de 6 de julho de 2020](https://tdn.totvs.com/pages/releaseview.action?pageId=592552831)
