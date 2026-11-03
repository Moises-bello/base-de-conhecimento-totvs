---
article_id: 26560545096343
category: SIGAEST - INTEGRAÇÕES
content_hash: b8c069176db49691d388f64000fa2bf79ffa6514e609618aa16ab56f87d9d65b
fetched_at: '2026-06-28T22:38:46.221834+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Falha ao enviar apontamento
  de serviço de oficina para integração variable is not array - Type [U] on MATI105
type: support-article
updated_at: '2024-09-23T14:45:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26560545096343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Falha-ao-enviar-apontamento-de-servi%C3%A7o-de-oficina-para-integra%C3%A7%C3%A3o-variable-is-not-array-Type-U-on-MATI105
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26560528327703) Tempo aproximado para leitura: **00:02:12min****Ocorrência**Ao realizar a Integração Protheus x PIMS de Apontamento de Serviço de Oficina, é retornado o erro "Falha ao enviar apontamento de serviço de oficina para integração variable is not array - Type [U] on MATI105":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26560545070103)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Esse erro normalmente é apresentado quando dentro do Processo de Solicitação ao Armazém (MATA105) é gerado uma Solicitação de Compra (MATA110) porém o Adapter não foi cadastrado ou está incorreto.   
  
**Solução**Ao analisar o Manual do PIMS, relacionado a Integração de Serviço de Oficina, podemos ver o seguinte trecho:  
   
![](https://totvssuporte.zendesk.com/attachments/token/jPFYNFcRrhvOg1j2ALwyc71DE/?name=image.png)  
 

Ou seja, dependendo do tipo de movimentação que está sendo gerado no PIMS, será gerado uma Solicitação de Compras no Protheus, ao realizar a Integração.

[Clique aqui](https://tdn.totvs.com/x/7YAGDg) para visualizar o Manual completo.  
   
Sendo assim é necessário ter os Adapters Cadastrados no Protheus para que todos os processos funcionem provavelmente o processo que está fazendo no PIMS é gerado solicitação de compra e o Adapter não existe, gerando erro.

Segue abaixo exemplo do cadastro:  
   
![](https://totvssuporte.zendesk.com/attachments/token/TvQyP33M45sYJcE163pW12ehc/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/iyJOeoMPpSgHOeZB3WES3hQgK/?name=image.png)

Caso tenha dúvidas sobre qual processo deve ou não gerar a solicitação de compras recomendamos abertura de um chamado pontual com o Suporte do Sistema PIMS.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Integrações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)*
