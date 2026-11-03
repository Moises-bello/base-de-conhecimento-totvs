---
article_id: 360015060191
category: Cadastros
content_hash: 4a5c740f144bcb0e443e60ef0f433136a975e9d657810c3069601ec6f7b4c45f
fetched_at: '2026-06-28T22:46:28.527195+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Tolerância diária de 10 minutos conforme artigo 58 da CLT
type: support-article
updated_at: '2025-01-20T19:12:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015060191-RH-RM-PTO-Toler%C3%A2ncia-di%C3%A1ria-de-10-minutos-conforme-artigo-58-da-CLT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16504346618007) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**  
Como realizar o cadastro de tolerância diária de 10 minutos conforme artigo 58 da CLT?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**Para realizar o cadastro da tolerância de 10 minutos diários, acesse o módulo de **Automação de Ponto** e realize os seguintes passos:

1. Acesse a guia **Cadastros** e selecione o menu **Limite de tolerância**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29371543084311)
2. Clique no botão **Incluir** ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29371543086487) e realize a parametrização do limite conforme print abaixo, alterando apenas o código do **Limite de tolerância** de acordo com sua demanda.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29371558222487)
3. Após as parametrizações, salve o cadastro e selecione o menu **Anexos** e a opção **Tipo da ocorrência**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29371558223767)
4. Insira as ocorrências que deseja considerar para o **Limite de tolerância**. Abaixo segue imagem de exemplo, as ocorrências devem ser cadastradas conforme demanda.  
     
   ![tipos de ocorrencia.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29371558228759)  
     
   **Observação**: é necessário incluir a ocorrência ***EN-Extra Normal Não Autorizado*** para que o sistema aplique o limite.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29371543093143)
5. Após a criação do **Limite de tolerância**, é necessário realizar a associação do cadastro do limite ao **Horário** do funcionário. Para isso, acesse novamente a guia **Cadastros** e selecione o menu **Horários por Intervalo**.    
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29371558231319)
6. Selecione o horário rígido desejado e acesse o menu **Anexos** e a opção **Limite de tolerância**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29371558235159)
7. O anexo será aberto, e a inclusão do registro deverá ser realizada. O código que utilizou no passo 2 deve ser informado nesta etapa.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29371558236311)
8. Após os cadastros, o funcionário que for associado a este horário já irá possuir este limite.
9. **Para o correto funcionamento do limite de tolerância, deve ser cadastro no horário o tempo de tolerância para cada batida.** No link a seguir contem o passo a passo de como realizar o cadastro:   
     
   [RH - RM - PTO - Cadastro de tolerância no horário por intervalo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045915194-TOTVS-RH-Linha-RM-PTO-Como-realizar-o-cadastro-de-toler%C3%A2ncia-no-hor%C3%A1rio-por-intervalo)

**Saiba mais**Para maiores informações sobre o cadastro de **Limite de tolerância**, acesse a documentação: [Limite de Tolerância.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719664)
