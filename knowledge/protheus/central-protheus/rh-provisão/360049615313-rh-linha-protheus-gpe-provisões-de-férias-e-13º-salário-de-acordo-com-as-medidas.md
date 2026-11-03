---
article_id: 360049615313
category: RH - Provisão
content_hash: 1999340dcfc308c85521118cdf1e9e0d7ce3a96d02010a3ed341c5fb0189efce
fetched_at: '2026-06-28T22:43:56.780221+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Provisões de Férias e 13º Salário de Acordo com
  as Medidas Provisórias de Suspensão de Contrato
type: support-article
updated_at: '2024-09-10T12:50:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615313-RH-Linha-Protheus-GPE-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio-de-Acordo-com-as-Medidas-Provis%C3%B3rias-de-Suspens%C3%A3o-de-Contrato
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26266077271447) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como Calcular Provisões de Férias e 13º Salário de acordo com a Medida Provisória 936/2020 de Suspensão de Contrato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução  
Importante: A Medida Provisória 936/2020 foi descontinuada.**

As Medidas Provisórias não trouxeram clareza com relação à tratativa do cálculo de Férias para funcionários com Contrato Suspenso, desta forma surgiram duas interpretações, uma de que esse período de suspensão não interfere nas férias, e a outra há o entendimento que deverão continuar contando, devendo existir a prolongação do período aquisitivo, tendo que trabalhar o mesmo período que foi suspenso.  
  
No que diz respeito ao 13° salário, o funcionário não terá direito do período em que houver a suspensão do contrato, uma vez que a legislação permite o pagamento a partir de 15 dias de serviço.

Para saber como configurar o sistema para que o cálculo das provisões atenda à estas regras, realize os seguintes passos:  
  
1. Caso a empresa entenda que as Férias deverão ser Congeladas acesse: Atualizações/ Definições de Cálculo / Tipos de Ausência, e Selecione o Tipo de Ausência Criado para a Suspensão de Contrato, pela MP-936 e clique em Alterar;  
   
- No campo "**Prov. Férias**" (RCM\_PROVFE), informe a opção "2 - Congela Após o Primeiro Mês";  
- No campo "**Dias Afa. Fer**" (RCM\_DIASFE), Insira a quantidade de dias a partir dos quais a provisão de Férias deverá ser congelada.  
- No campo "**Cong. Afas**" (RCM\_CONGAF), informe se o Congelamento será por Afastamento ou Período Aquisitivo.  
Para mais informações sobre este campo, [Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=305926077)  
2 - Caso a empresa entenda que o Período Aquisitivo deverá ser Prolongado, acesse: Atualizações/ Definições de Cálculo / Tipos de Ausência, e Selecione o Tipo de Ausência Criado para a Suspensão de Contrato, pela MP-936 e clique em Alterar;  
  
- No campo "**Tip.Aus.Feri.**" (RCM\_FERIAS), informe a opção "2 - Suspensão do Período";  
- No campo "**Prov. Férias**" (RCM\_PROVFE), informe a opção "1 - Não Congela";  
- No campo "**Dias Afa. Fer**" (RCM\_DIASFE), Insira a quantidade de dias a partir dos quais a provisão de Férias deverá respeitar o PEríodo Aquisitivo Prolongado .  
- No campo "**Cong. Afas**" (RCM\_CONGAF), informe se o Congelamento será por Afastamento ou Período Aquisitivo.

3 - Para congelar o Período de Afastamento para o 13º Salário, acesse: Atualizações/ Definições de Cálculo / Tipos de Ausência, e Selecione o Tipo de Ausência Criado para a Suspensão de Contrato, pela MP-936 e clique em Alterar;  
  
- No campo "**Prov. 13o**" (RCM\_PROV13) informe a opção "1 - Congela";  
- No campo "**Dias Afa. 13**" (RCM\_DIAS13) Insira a quantidade de dias a partir dos quais a provisão de 13º salário deverá ser congelada.

4. Após ajustar os campos citados acima, clique em Confirmar, para Salvar as alterações;  
  
5. Processe o Cálculo das provisões normalmente.  
  
**Importante**:  
Ao cadastrar um novo Tipo de Ausência, onde o campo "Tp. Ausência" deve estar preenchido com a opção 2 - Outras Ausências, por padrão os campos de Provisão de Férias e 13º Salário ficam desabilitados para Edição.  
Para preencher estes campos, realize os procedimentos abaixo:

1. Informe no campo "Tp. Ausência" a opção 1 - Afastamento;  
2. Preencha os campos de Provisão de Férias e 13º Salário;  
3. Altere o campo "Tp. Ausência" para 2 - Outras Ausências novamente, e clique em Confirmar.

**Saiba Mais:**  
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)   
[Consultoria sobrea MP 936/2020](https://tdn.totvs.com/pages/releaseview.action?pageId=547252166)
