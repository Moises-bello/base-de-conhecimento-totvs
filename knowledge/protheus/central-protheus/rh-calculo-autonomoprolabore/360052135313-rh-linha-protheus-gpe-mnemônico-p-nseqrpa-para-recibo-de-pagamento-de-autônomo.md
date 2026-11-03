---
article_id: 360052135313
category: RH - Calculo Autonomo/Prolabore
content_hash: fc69da931ebb209aeba09627aea93be8cef573c6f3925346f0464f54bfc82704
fetched_at: '2026-06-28T22:43:15.190686+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Mnemônico P_NSEQRPA  para recibo de pagamento de
  autônomo
type: support-article
updated_at: '2025-10-06T13:47:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052135313-RH-Linha-Protheus-GPE-Mnem%C3%B4nico-P-NSEQRPA-para-recibo-de-pagamento-de-aut%C3%B4nomo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35435125819543) Tempo aproximado para leitura: 00:01:00min**

**Ocorrência**Mnemônico P\_NSEQRPA para recibo de pagamento de autônomo.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Ao executar o RDMAKE IMPRPA pela ferramenta CodeAnalysis é apresentado o erro "Assignment not allowed in data dictionary".  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Foi criado o mnemônico de sistema **P\_NSEQRPA** para controlar a numeração dos recibos que anteriormente ao ajuste era feita pela pergunta "Nro. do 1º Recibo";
2. Caso a pergunta "**Nro. do 1º Recibo**" esteja preenchida com um sequencial maior que o conteúdo do mnemônico P\_NSEQRPA, será respeitado o número preenchido na pergunta, mas em qualquer outro caso o sequencial utilizado será o do P\_NSEQRPA;
3. Como o mnemônico criado é de usuário (P\_), se necessário o seu conteúdo poderá ser alterado. Para alterar o mnemônico acesse **Atualizações > Definições de Cálculos > Mnemônicos (GPEA300)**;  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33015666369303)

**Sabia mais:**

[RH - Calculo Autônomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
