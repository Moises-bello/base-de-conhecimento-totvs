---
article_id: 4404768843031
category: Call Center - Telecobrança
content_hash: 2d483a878f52349a9e5a0e8c2b49c210ef1c76fe0a77a1a734f30f9161572ee7
fetched_at: '2026-06-28T22:41:28.722807+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Processamento da Seleção
  de Título (TMKA180)
type: support-article
updated_at: '2026-04-06T19:35:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404768843031-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Processamento-da-Sele%C3%A7%C3%A3o-de-T%C3%ADtulo-TMKA180
---

**Dúvida**  
Como funciona o processamento dos títulos do "Contas a Receber" (**SE1**) na "Seleção do Títulos" (**SK1**)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

Ao acionar o botão **Gerar**, o sistema apresentará a tela de **Filiais,** para escolher de qual filial deseja visualizar os títulos disponíveis para o atendimento de Telecobrança:

![fi.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4404768380823)

Na tela Parâmetro é possível definir os títulos de quais filiais deseja processar na "Seleção de Titulos" (**SK1**)**:**

![param.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4404768517271)

A rotina de "Seleção de Títulos" (TMKA180) permite que uma filial do sistema realize a cobrança de seus títulos vencidos e/ou dos títulos de outra filial dos sistema. Dessa forma, empresas que realizam vendas em diversas filiais, porém possuem a cobrança centralizada em uma única filial, podem utilizar a rotina sem necessidade de compartilhamento das tabelas do módulo financeiro.

Também é possível que todas as filiais realizem a cobrança dos títulos umas das outras, ou seja, um mesmo título pode ficar disponível para várias filiais. Dessa forma, empresas que realizam a cobrança dos títulos de forma unificada entre suas filiais, podem realizar o processo sem manter um título como exclusivo de uma única filial de cobrança.

Na tabela SK1, o campo "Filial" (K1\_FILIAL) grava a filial logada, onde foi realizada a seleção dos títulos, ou seja, a filial escolhida no inicio do processo, e o campo "Filial Orig." (K1\_FILORIG) grava a filial que o títulos foi gerado no "Contas a Receber" (SE1).
