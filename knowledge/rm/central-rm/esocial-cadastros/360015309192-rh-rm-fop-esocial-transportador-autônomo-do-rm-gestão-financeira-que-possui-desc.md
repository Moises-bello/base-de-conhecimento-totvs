---
article_id: 360015309192
category: eSocial - Cadastros
content_hash: 218eba467213869dc0e3f0802fdee4d0bff791627781c0aae27501cfcbc92736
fetched_at: '2026-06-28T22:47:14.428266+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial -  Transportador autônomo do RM Gestão Financeira que
  possui desconto de SEST e SENAT
type: support-article
updated_at: '2024-06-28T12:39:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015309192-RH-RM-FOP-eSocial-Transportador-aut%C3%B4nomo-do-RM-Gest%C3%A3o-Financeira-que-possui-desconto-de-SEST-e-SENAT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24499310573207) Tempo aproximado para leitura: 00:02:30 min  
  
Dúvida**  
Como gerar os eventos **S-1200** e **S-1210** para transportadores autônomos cadastrados no TOTVS Gestão Financeira e que possuem o desconto **SEST** e **SENAT**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir da versão 12.1.23  
**Solução**  
Para realizar a geração dos eventos **S-1200** e **S-1210** para transportadores autônomos do RM Fluxus discriminando os valores de **SEST** e **SENAT**, o usuário deve realizar as seguintes parametrizações:  
1. Acesse **Configurações | Parametrizador | eSocial | Autônomos e Externos 1/2** e **Autônomos Externos 2/2** e informe os eventos previamente cadastrados;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042348834)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043197313)

2. Acesse **Administração de Pessoal | Cliente e Fornecedor** e preencha os dados do autônomo;  
3. Antes de realizar a geração dos eventos S-1200 e S-1210, verifique se os lançamentos estão baixados;  
4. Acesse **eSocial | Gerar XML** (Eventos Periódicos),  e execute o processo com o parâmetro **Gerar Autônomos Fluxus/Externos** marcado:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043198233)

**Importante**  
Deve-se utilizar os códigos de cálculo abaixo nos eventos de **SEST** e **SENAT**:  
   • [376 - SEST](https://tdn.totvs.com/pages/viewpage.action?pageId=452719076)   • [377 - SENAT](https://tdn.totvs.com/pages/viewpage.action?pageId=452719077)  
 **Saiba mais**  
Para mais informações acesse:  
- [Como gerar os eventos S-1200 e S-1210 para transportadores autônomos cadastrado no módulo de Gestão Financeira que tem desconto SEST e SENAT?](http://tdn.totvs.com/pages/releaseview.action?pageId=397382319)  
[Geração do S-1200 e S-1210 para transportador autônomo cadastrado no TOTVS Gestão Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342433-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-do-S-1200-e-S-1210-para-transportador-aut%C3%B4nomo-cadastrado-no-TOTVS-Gest%C3%A3o-Financeira)
