---
article_id: 360028196432
category: RH - Provisão
content_hash: f87d96cb79372689320199b5d953ea5df7d551aa40611f889923925a0254b10d
fetched_at: '2026-06-28T22:43:55.578083+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE -  Baixa de 1ª Parcela de 13º Salário na Provisão
type: support-article
updated_at: '2026-03-17T17:26:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028196432-RH-Linha-Protheus-GPE-Baixa-de-1%C2%AA-Parcela-de-13%C2%BA-Sal%C3%A1rio-na-Provis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23393464787735)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como funciona a baixa de 1ª Parcela de 13º Salário na provisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**À partir da versão 12, o sistema não gera Baixa de 1ª Parcel de 13º Salário, as baixas serão realizadas somente no mês de Dezembro (processamento do roteiro 132) ou no desligamento do funcionário.  
Porém é possível gerar o Desconto da 1ª parcela do 13º Salário na provisão.

Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse Miscelânea / Provisões / Provisão de Férias/13º Salário / Outras Ações / Cálculo / Outras Ações / Parâmetros;  
  
2. Nos parâmetros para cálculo das provisões, preencha a pergunta "**Desc. 1ªParc. 13o.?"** com a opção Sim:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077542314)  
  
3. Verifique o preenchimento das demais perguntas e clique em OK, para que o cálculo seja processado;  
  
4. Emitindo o Relatório de Provisão de 13º Salário, o sistema apresenta a coluna "**1o PARCELA**" que irá apresentar o valor recebido pelo funcionário de 1ª parcela de 13º salário, tanto nas Férias, como no roteiro 131:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077542374)

**Importante:**   
Como na 1ª Parcela de 13º Salário não há recolhimento do INSS Patronal, o valor do INSS continua sendo calculado considerando o valor de Provisão de 13º Salário + Adicionais.

**Valor Atual de INSS de 13º Salário**: Valor + Adicionais x % de INSS Patronal.  
1.574,62 x 27,8% = **437,74**  
  
Já o FGTS, como há recolhimento de FGTS no pagamento da 1ª Parcela de 13º Salário, o FGTS nas provisões será calculado sobre o valor Total 13o (Provisão de 13º + Adicionais - 1ª Parcela).

**Valor Atual de FGTS de 13º Salário:** Valor + Adicionais - 1ª Parcela x 8%  
1.574,62 - 1.349,68 = 224,94 x 8% = **17,99**

Considerando a Antecipação do 13º Salário, pode ser apresentado valor negativo na linha "No Mês", tendo em vista a diminuição do FGTS de 13º Salário.  
**Valor "No Mês" de FGTS**: Valor Atual - Anterior.  
17,99 - 107,97 = **-89,98**

5. No cabeçalho da Provisão, o valor da Antecipação do 13º Salário é apresentado na verba com Id de cálculo 0268 - Adiant. 1ª Parcela de 13º Salário Provisão :

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077542454)

**Saiba Mais:**[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
