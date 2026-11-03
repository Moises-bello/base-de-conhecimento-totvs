---
article_id: 360021669392
category: MDFe - Manifesto de Carga
content_hash: b1d4774a5af72c55162f3112ba46f4f9cc05e9b601a5b43cc05179fb9401e5fd
fetched_at: '2026-06-28T22:40:08.295960+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Gerar o código
  RNTRC no MDF-e quando o veículo for de terceiro ou agregado
type: support-article
updated_at: '2025-06-17T17:56:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021669392-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Gerar-o-c%C3%B3digo-RNTRC-no-MDF-e-quando-o-ve%C3%ADculo-for-de-terceiro-ou-agregado
---

**Dúvida**Como gerar o código RNTRC no MDF-e quando o veículo for de terceiro ou agregado?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**   
Primeiramente é necessário cadastrar o motorista como fornecedor.

Segue exemplos abaixo dos campos que devem ser preenchidos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018581751) 

Na aba **TMS** necessário preencher o **RNTRC**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018581771)

Caso não tenha esta aba **TMS** no seu cadastro de fornecedor será necessário entrar via configurador (**SIGACFG**) em Base de Dados -> Dicionário -> Base de Dados -> pesquisar a tabela **SA2** e filtrada pelo campo **A2\_RNTRC** e clicar em editar, deixar como os exemplos abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018581791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018581831)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018709032)

No cadastro do veículo (**DA3**) será necessário vincular o motorista (o mesmo que usou para criar o cadastro do fornecedor).

No campo Frota (**DA3\_FROVEI**) preencha com 2 ou 3.

No campo Proprietário (**DA3\_CODFOR**) preencha com o código do fornecedor (o mesmo que criou para o motorista).

Segue exemplo do cadastro do motorista usado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018581891)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018709072) Após gerar o **MDF-e** será gerado o grupo **<Prop>** nele constará o **RNTRC** ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018581911)

No **DAMDFE** também será destacado o **RNTRC** no grupo do Veiculo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360018581951)

**Importante**: Quando o veículo for próprio o **RNTRC** não é gerado, segue link com maiores detalhes:  
[MP - MDFE - RNTRC Veículo Própio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035553413-MP-MDFE-RNTRC-Ve%C3%ADculo-Pr%C3%B3pio?source=search)
