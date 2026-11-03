---
article_id: 17323558689303
category: RH - Integração de Titulo
content_hash: 87c2a82ee49a498d8bac22a883b579c5e1573edbf93f48cea66dd59254934a66
fetched_at: '2026-06-28T22:43:36.230724+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como Gerar Título de IRRF de PLR
type: support-article
updated_at: '2025-07-14T21:07:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17323558689303-RH-Linha-Protheus-GPE-Como-Gerar-T%C3%ADtulo-de-IRRF-de-PLR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17323569679895) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como gerar um título de IRRF de PLR?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todos os Releases  
  
**Solução**A Definição Padrão de Geração de Títulos de IRRF não contempla o IRRF de PLR, portanto, será necessário criar um título Definido Por usuário, para gerar o Título de IRRF com código 3562.  
   
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse o Módulo Gestão de Pessoal > Miscelânea > Títulos > Definição (GPEM640), e inclua uma nova Definição de Títulos, selecionando a opção Definido por Usuário e o Código de Retenção 3562:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17322876067223)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17322877713175)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17322890882071)  
  
  
2. Clique em Definir Título e informe o código da verba de Desconto de IRRF de PLR e a tabela para busca da verba.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17323149574679)  
Observação: Caso o roteiro PLR esteja Aberto, deverá ser selecionada a tabela SRC, e caso esteja Fechado selecione a tabela SRD.  
  
3. Salve a Definição do Título;  
  
4. Acesse: Miscelânea > Títulos > Geração (GPEM650) e preencha as perguntas para geração do Título;  
  
5. Para verificar o título gerado acesse: Miscelânea > Títulos > Manutenção (GPEM660), Selecione o Título gerado e clique em Visualizar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17323178516119)

6. Para conferir o valor do título, emita o relatório DIRF Mensal/DARF (GPER050), e verifique o Total da coluna IRRF de PLR:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17323482200983)  
  
  
**Saiba Mais:**[RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo) [- Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
