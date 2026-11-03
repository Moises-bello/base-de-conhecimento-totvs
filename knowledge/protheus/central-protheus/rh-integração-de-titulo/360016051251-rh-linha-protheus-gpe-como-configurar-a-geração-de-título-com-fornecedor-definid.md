---
article_id: 360016051251
category: RH - Integração de Titulo
content_hash: 0d1e7fbbc264c66eb7f7d63a3c3a46efaee17d1a3570dd018f6c0b1e4f5c60a0
fetched_at: '2026-06-28T22:43:36.180421+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar a geração de título com fornecedor
  definido por funcionário
type: support-article
updated_at: '2025-07-14T21:07:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016051251-RH-Linha-Protheus-GPE-Como-configurar-a-gera%C3%A7%C3%A3o-de-t%C3%ADtulo-com-fornecedor-definido-por-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33463290778135)**Tempo aproximado para leitura: 00:02:00 min

**Dúvida**Como fazer uma geração de título criando amarração do funcionário com o fornecedor, ou seja, gerando um título por funcionário e o sistema identificando código fornecedor campo (RD0\_FORNEC)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
1- No Configurador, acesse: Ambientes > Cadastros > Parâmetros. Localize o parâmetro **MV\_CADFORA** e verifique se o mesmo está preenchido com **.T.** , como no exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17267143934871)

2 - No Módulo 07 (SIGAGPE), acesse o cadastro de funcionários Atualizações > Funcionário > Funcionários **![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011196252)**3 - No Módulo 01 (Ativo Fixo) acesse: Atualizações > Cadastro de Pessoas (APDA020) e clique em Alterar no funcionário em questão e na aba Viagem, inclua o cósigo do Fornecedor:

**![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011230731)**  
4 - No Módulo 07 (SIGAGPE) acesse: Miscelânea > Títulos > Definição de Títulos. O títulos deverá ter a configuração no campo Agrupamento para o tipo  **4 – Funcionário** e o Cod. Fornecedor com **RA\_MAT:**  
  
**![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011196272)**

**Obs:**  Na definição de Títulos (GPEM640), no campo Agrupamento (RC0\_AGRUPA) deve estar configurado por Funcionário e no campo  Cod. Fornec. (RC0\_FORNEC) deve constar o campo RA\_MAT ou RA\_CIC (caso o tamanho do campo A2\_COD esteja maior que 15) da tabela de Cadastro de Funcionários (SRA):  
  
5 - Acesse: Miscelânea > Títulos > Geração (GPEM650) e realize a geração do título.  
  
6 - Acesse: Miscelânea > Títulos > Manutenção (GPEM660) e consulte o título gerado:  
  
**![6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360011196292)** **Saiba Mais**[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
