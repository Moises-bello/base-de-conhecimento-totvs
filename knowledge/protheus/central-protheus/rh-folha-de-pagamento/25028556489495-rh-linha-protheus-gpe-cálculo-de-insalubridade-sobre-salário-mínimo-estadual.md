---
article_id: 25028556489495
category: RH - Folha de Pagamento
content_hash: 7d96c35d62fce9591fb15a2c2a9a02ec74bae7ca5bf098690157dcdac08c3e8a
fetched_at: '2026-06-28T22:44:12.091616+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de insalubridade sobre salário mínimo estadual
type: support-article
updated_at: '2024-09-12T16:16:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25028556489495-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-insalubridade-sobre-sal%C3%A1rio-m%C3%ADnimo-estadual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25028556468503) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Cálculo de insalubridade sobre salário mínimo estadual  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) Gestão de Pessoal - A partir da versão 12.1.17  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

Para que o cálculo da insalubridade seja sobre salário mínimo estadual, é necessário parametrizar no cadastro de sindicato conforme abaixo:

IMPORTANTE: Esta alteração deve ser feita com Data Base do sistema no úlyimo dia do mês anterior ao mês do cálculo.

1. Entre na rotina Sindicato ( caminho > Atualização > Cadastros > Sindicato) posicione no Sindicato em questão e clique em Alterar:  
  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25028556470295)

2. Entre na aba Peric./Insal. e deixe o campo selecionado conforme print abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25127920027159)

3. Validar se o cadastro de funcionário possui o sindicato corretamente cadastrado na Aba funcionais: Ainda no cadastro de funcionários, verifique na Aba Adicionais a insalubridade:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25127897423383)

4. Acessar Atualizações > Definições de cálculo > Manutenção de Tabelas > Tabela S118 e informar o valor do salário mínimo estadual. No exemplo abaixo usamos o salário mínimo estadual de São Paulo referente ao ano de 2024.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25127897425175)

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
