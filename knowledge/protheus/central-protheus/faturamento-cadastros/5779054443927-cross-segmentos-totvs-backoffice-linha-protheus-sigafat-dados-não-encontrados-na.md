---
article_id: 5779054443927
category: Faturamento - Cadastros
content_hash: be19cef1126d8ca03ecee28040f3fdcc3dacc430fe843d7ccbbfa040fe77b5a9
fetched_at: '2026-06-28T22:38:35.516384+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Dados não encontrados
  na CAROL
type: support-article
updated_at: '2023-07-05T13:39:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5779054443927-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Dados-n%C3%A3o-encontrados-na-CAROL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15790870808343) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Ao incluir o CNPJ no cadastro de clientes com integração APICAROL, ocorre essa mensagem "Atenção Dados não encontrados na **CAROL**"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15790565855255)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Os dados que API da CAROL utiliza, são fornecidos pela própria Receita Federal.  
  
De acordo com a documentação fornecida, esses dados são atualizados mensalmente, pela própria equipe da Receita Federal, porém, por se tratar de uma base do Governo e do site da Receita Federal, podem não estar constando na integração ou foi alterado recentemente os dados do cliente na Receita Federal. 

Sendo assim, caso o CNPJ não seja localizado na verificação da API CAROL, é necessário aguardar o governo atualizar sua base, para que a CAROL replique os dados a cada trimestre ou realizar a inclusão manualmente dos dados deste Cliente clicando no botão "Abortar processo".

![api](https://centraldeatendimento.totvs.com/hc/article_attachments/15790870812183)

**Saiba mais:**  
Documentação da Receita Federal: **Dados Públicos CNPJ:** <https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj>
