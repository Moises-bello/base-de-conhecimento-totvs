---
article_id: 21676552286103
category: Anuais
content_hash: ca03e2014744280ef1aa837f9688e6c2e9dd171e1d4d00cfe741cd055debf141
fetched_at: '2026-06-28T22:46:51.017958+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - Comunicado IRRF Simplificado - Imposto de Renda Retido na Fonte
  (legal ou simplificado)
type: support-article
updated_at: '2024-10-04T20:51:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21676552286103-RH-RM-FOP-Comunicado-IRRF-Simplificado-Imposto-de-Renda-Retido-na-Fonte-legal-ou-simplificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21676591668759) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Comunicado IRRF simplificado.

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões e patchs abaixo:

* 12.1.2302.264
* 12.1.2306.228
* 12.1.2310.166
* 12.1.2402.106 ou superiores

**Solução**

Prezado Cliente,

Avaliamos suas dúvidas quanto às questões relacionadas ao desconto do Imposto de Renda Retido na Fonte (IRRF) simplificado.  Neste sentido gostaríamos de esclarecer o funcionamento de nosso produto a fim de que possam realizar as devidas análises e correções.

Foi observado que a informação sobre o regime de dedução do Imposto de Renda Retido na Fonte (legal ou simplificado), calculado no envelope de pagamento, não está refletindo os campos PFPERFF.IRRFSIMPLIFICADO e PFPERFF.IRRF13SIMPLIFICADO.

Nosso produto realiza o cálculo para avaliar se o IRRF é Simplificado somente no momento do lançamento da folha de pagamento ou no recálculo da mesma. O fato de haver esta divergência pode estar ligado a diversos fatores, desde mudanças na parametrização de cálculo do imposto após o fechamento do período, até operacionalização com patchs divergentes após criação dos campos mencionados.

 Por questão de integridade dos dados, atualmente esta informação (IRRF Simplificado) uma vez gravada, não pode ser alterada sistemicamente. Porém, salientamos que para entrega da DIRF é possível alterar estes dados diretamente no arquivo gerado ( DIRF.001) ou, após importar o arquivo da diretamente no programa da Receita.

Com o objetivo de apoiá-los em um ajuste sistêmico, estamos avaliando a construção de um processo que permitirá escolher os registros e igualar o cálculo com o que está gravado nos campos mencionados com o cálculo de envelope de pagamento. Porém trata-se de um processo extremamente complexo e que dificilmente conseguiremos entregar antes do fim do prazo (29/02), mas que poderá ser utilizado caso haja necessidade de retificações.

Atenciosamente  
Equipe de Atendimento TOTVS
