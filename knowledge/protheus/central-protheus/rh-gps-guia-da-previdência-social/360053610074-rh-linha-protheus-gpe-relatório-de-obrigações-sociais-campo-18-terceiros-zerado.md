---
article_id: 360053610074
category: RH - GPS (Guia da Previdência Social)
content_hash: dee29593a9ea26a26520fc0eccd2c9c37095f1ad379de29e404f5117f42dd327
fetched_at: '2026-06-28T22:43:11.630027+00:00'
product: protheus
section_id: 360011996273
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de obrigações sociais, campo 18 - terceiros
  zerado
type: support-article
updated_at: '2021-06-08T21:06:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053610074-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-obriga%C3%A7%C3%B5es-sociais-campo-18-terceiros-zerado
---

**Dúvida**Ao gerar o relatório de obrigações sociais não está trazendo valor no campo 18 (terceiros).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091741933/mceclip1.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal -  A partir da Versão 12.1.17  
  
**Solução**

O sistema exibirá valor neste campo quando as verbas de ID de cálculo 0149 e 0944 forem geradas na folha de pagamento. Em relação ao cálculo da folha, somente será gerado essas verbas, caso a diferença entre os valores distribuídos na S038, for menor que o total preenchido no campo %terceiro.

Exemplo: %tercerios 5,8 - % SalEduc - % Incra - % Senai - % Sesi - % Senac - % Sesc - %Sebrae  
Se essa conta resultar em valor maior que zero, as verbas são geradas e o valor exibido no relatório;

O  Sistema realiza a dedução dos valores distribuídos e exibe no campo 18 a diferença de percentual. Conforme ocorre na GPS e no GPER240;  
Referência: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014263931>

O valor de terceiros no relatório será exibido em contribuição de terceiros  conforme abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091742733/mceclip2.png)  
  
**Saiba Mais:** <https://tdn.totvs.com/display/public/PROT/FGTS>
