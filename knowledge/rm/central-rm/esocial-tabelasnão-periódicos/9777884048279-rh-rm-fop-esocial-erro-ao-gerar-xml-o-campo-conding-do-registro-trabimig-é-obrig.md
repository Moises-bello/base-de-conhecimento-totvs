---
article_id: 9777884048279
category: eSocial - Tabelas/Não Periódicos
content_hash: c1d95e480e8213b628b5cbf71bee90ee7560657a225cc855c212ccadda1fe557
fetched_at: '2026-06-28T22:47:10.385442+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O campo ''condIng'' do registro
  ''trabImig'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2025-07-02T17:21:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9777884048279-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-campo-condIng-do-registro-trabImig-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23726136348567) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao gerar o XML do  evento S-2200, é exibido o erro: **O campo 'condIng' do registro 'trabImig' é obrigatório e não está preenchido.**  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Essa mensagem de erro ocorre ao gerar o evento S-2200 de um trabalhador imigrante e não foi preenchido a condição de ingresso do trabalhador imigrante no XML:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777686694679)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777552123799)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Acesse o cadastro do funcionário estrangeiro **Administração de Pessoal | Funcionários**,  na aba **Documentos Estrangeiros**, preencha o campo **Classificação da condição no Brasil:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9777633795607)

**2.** Em seguida, salve o cadastro, e gere novamente o XML S-2200.

**Importante**Quando o funcionário for brasileiro, deverá ser configurado o país como 105, seguindo os passos de classificação de país ([CLIQUE AQUI PARA SABER MAIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007501531-RH-RM-FOP-eSocial-Classifica%C3%A7%C3%A3o-de-pa%C3%ADses-conforme-layout-do-eSocial)).
