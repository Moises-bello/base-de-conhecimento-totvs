---
article_id: 20836622273687
category: Financeiro - Viagens
content_hash: 86f08a68aee4b89b0aed08cf35f558ddd46c437bc2fcd47d81bcdaeacaa48f0f
fetched_at: '2026-06-28T22:38:21.326631+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAFIN - FINA677 - Prestação
  não aparece para o aprovador
type: support-article
updated_at: '2024-01-25T14:00:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20836622273687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA677-Presta%C3%A7%C3%A3o-n%C3%A3o-aparece-para-o-aprovador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20836622232471) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**  
No módulo Financeiro, ao tentar realizar a aprovação de uma prestação de contas não aparece para o aprovador liberar.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Viagens - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois deve-se adicionar o usuário (RD0\_USER). EX: "000123" na rotina FINA691 - Assistente de Configuração com o código de usuário do Protheus.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Entre na rotina **Assistente de Configuração (FINA691)** e adicione o código de usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20836622241815)

2. O Usuário acesse a rotina **Prestação de Contas** **(FINA677)** e avalie se a viagem aparece.

3. Caso queira que os aprovadores visualizem somente as viagens do seu grupo, precisa configurar o **grupo de acesso**.

**Saiba mais**

[Viagens - Financeiro - P12](https://tdn.totvs.com/display/PROT/Viagens+-+Financeiro+-+P12)
