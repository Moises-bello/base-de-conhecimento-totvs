---
article_id: 4916801234583
category: Integrações Outros BackOffice
content_hash: 96c93524e0b4e13e39b5b85fa5cccf75d41ffba11795563465c25cd5438039f7
fetched_at: '2026-06-28T22:46:42.157047+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RM - FOP - Integração RM Labore x BackOffice Protheus: Coligada no RM não
  foi mapeada para empresa'
type: support-article
updated_at: '2025-02-10T16:47:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4916801234583-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Coligada-no-RM-n%C3%A3o-foi-mapeada-para-empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Quando o Protheus tenta enviar algum dado para o RM, ao receber os dados o RM retorna a mensagem de erro: **Coligada no RM não foi mapeada para empresa -X** ou **A coligada -X no RM não foi mapeada para empresa XX|XX****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro é apresentado pois o RM não conseguiu encontrar a Coligada que vai ser inserido os dados enviados pelo Protheus, neste caso existe um problema na configuração do De/para da Coligada e/ou Filial no RM.  
  
**Solução**Para solução é necessário criar/ajustar os De/Para de Empresa e Filial, através do **RM / Integração / Mensagem única / De-Para**.  
  
Segue abaixo **um exemplo** para maior entendimento da configuração:

No RM temos a Coligada 1 chamada Empresa Martins e a Filial 1 de Belo Horizonte.  
  
No Protheus essa mesma Empresa é representada no Protheus como Grupo 99 e Filial 01.  
  
Seguindo esse exemplo, a criação dos De/Para ficarão da seguinte forma:  
  
1- Primeiramente deverá ser criado o De/para da Empresa, interligando a Empresa 1 do RM com a 99 do Protheus, segue:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5072071957143/mceclip0.png)  
  
2- Será necessário cadastrar também um mapeamento da coligada RM **para ela mesma** (conforme exemplo abaixo). Esse cadastro é necessário para o correto funcionamento dos códigos de *extensions* criados nas integrações.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5072058492951/mceclip1.png)  
  
3- Para finalizar, também é necessário criar o De/Para da Filial:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5072299565079/mceclip2.png)
