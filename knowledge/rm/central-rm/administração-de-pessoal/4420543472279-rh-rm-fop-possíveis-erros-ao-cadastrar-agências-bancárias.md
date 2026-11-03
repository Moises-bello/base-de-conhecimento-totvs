---
article_id: 4420543472279
category: Administração de Pessoal
content_hash: f20452d413cecfaff029f0c89e2a2ec45fbd212f524652a0399c89f0e2f1ba87
fetched_at: '2026-06-28T22:47:01.377028+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Possíveis erros ao cadastrar agências bancárias
type: support-article
updated_at: '2025-03-05T18:10:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420543472279-RH-RM-FOP-Poss%C3%ADveis-erros-ao-cadastrar-ag%C3%AAncias-banc%C3%A1rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Ao tentar realizar o cadastro de agências bancárias ou vincular a agência a um funcionário é possível que apresente as seguintes mensagens de erros:

**Chave duplicada. Possíveis causas:**  
**- inclusão de registro cujo valor da chave primária já existe**  
**- inclusão de registro cujo valor do índice único já existe.**

O motivo desse erro ocorre quando o código que está tentando cadastrar já existe na base de dados.

ou

**Valor Inválido para o campo Agência de Pagamento.**

Esse erro é apresentado pelo fato da agência que está tentando vincular no funcionário, não está com o campo Tipo de Agência, definido.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Para a correção dos erros mencionados acima, acesse o menu: **Administração de Pessoal | Cadastros Globais | Bancos /Agências:****![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420552733207/mceclip0.png)**Localize o banco do funcionário, edite o seu cadastro e clique em **Anexos | Agência**:![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420558201623/mceclip2.png)  
  
Em seguida será disponibilizada a relação de agências cadastradas para o banco. Para que a agência seja disponibilizada no cadastro do funcionário de forma que não apresente erros, ​basta acessar o cadastro da agência e verificar na aba **Identificação** se o campo **Tipo de agência** está parametrizado como **Agências Pagto. de folha:****![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4420561549079/mceclip3.png)**Após o processo citado acima, os erros deixarão de ser apresentados.  
  
**Saiba mais**[RH - RM - FOP - Como Cadastrar Agência e Banco de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007348332-RH-RM-FOP-Como-Cadastrar-Ag%C3%AAncia-e-Banco-de-Pagamento-?source=search)
