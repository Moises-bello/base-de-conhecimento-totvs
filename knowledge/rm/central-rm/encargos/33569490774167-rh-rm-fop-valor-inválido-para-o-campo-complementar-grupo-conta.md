---
article_id: 33569490774167
category: Encargos
content_hash: 4e5077d33a6461387f25d878d991c91fab7f60d04e2925d704c84427100b13f8
fetched_at: '2026-06-28T22:46:52.195784+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Valor Inválido para o campo complementar "Grupo Conta"
type: support-article
updated_at: '2025-07-18T20:15:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33569490774167-RH-RM-FOP-Valor-Inv%C3%A1lido-para-o-campo-complementar-Grupo-Conta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33569479632919) Tempo aproximado para leitura: **00:01:04 min**  
  
**Dúvida**

Como ajustar o erro "Valor Inválido para o campo complementar "Grupo Conta" quando realizar a inclusão de um novo agrupamento de Contas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**  
Ao incluir um Agrupamento de contas localizado em **Encargos | Cadastros | Cadastros Contábeis | Agrupamento de Contas** no momento de preencher o campo **Grupo de Contas**, pode ocorrer o erro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33569585824151)

Isso ocorre pois não existe o Grupo de contas cadastrado na tabela dinâmica **GRPCONT.**

Para ajustar o erro será necessário realizar os seguintes passos:

1. Acesse **Administração de Pessoal | Cadastros Globais | Tabelas Dinâmicas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33569479634327)

2. Selecione **Sistema: Folha de Pagamento**. Depois procure a tabela **GRPCONT** e crie um novo item na tabela com o código e descrição desejado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33569490752407)

**Saiba mais**

[RH - RM - FOP - Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019748711-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o)

[RH - RM - FOP - Dúvidas frequentes: Agrupamento Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23721913419799-RH-RM-FOP-D%C3%BAvidas-frequentes-Agrupamento-Cont%C3%A1bil)
