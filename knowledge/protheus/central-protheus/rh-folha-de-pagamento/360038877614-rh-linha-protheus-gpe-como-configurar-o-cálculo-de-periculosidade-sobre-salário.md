---
article_id: 360038877614
category: RH - Folha de Pagamento
content_hash: 56ec69bd029a337f39ece18423ee4c2fadf5f2473cdeaeb9623afb30b7a2cbce
fetched_at: '2026-06-28T22:44:13.307921+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o cálculo de periculosidade sobre
  Salário + Verbas
type: support-article
updated_at: '2025-07-23T17:07:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038877614-RH-Linha-Protheus-GPE-Como-configurar-o-c%C3%A1lculo-de-periculosidade-sobre-Sal%C3%A1rio-Verbas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25992034359191)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como parametrizar o sistema para que o cálculo da periculosidade seja sobre salário base mais verbas, salário mínimo mais verbas, salário mínimo estadual mais verbas ou piso sindicato mais verbas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**Para que o cálculo da periculosidade seja sobre **salário base** mais **verbas, salário mínimo** mais **verbas,**  **salário mínimo** estadual mais **verbas** ou **piso sindicato** mais **verbas,** faça a parametrização conforme abaixo:  
  
**IMPORTANTE: Esta alteração deve ser feita com a Data Base do sistema no primeiro dia do mês do inicio do cálculo vigente.**  
1. Acesse no menu **Atualizações >Cadastros > Sindicato**, posicione no Sindicato em questão e clique em Alterar:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051830413)  
  
2. Acesse a aba **Peric./Insal**. e deixe o campo **Bs. Cálc Per** conforme a necessidade de cálculo (2 - Salário+verbas, 6 - Salário minimo+verbas, 7 - Salário minimo estadual+verbas ou 8 - Piso sindicato+verbas), no exemplo abaixo deixei como 2 - Salário+verbas;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051831053)  
  
3. Para as verbas que deverão fazer base para a Periculosidade (por exemplo verba de falta, atraso, HE, entre outras), entre no cadastro da verba na **rotina Verbas** e na aba **Incidência**, deixe o campo **Periculosidade** com **SIM**:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051831253)  
  
Lembrando que o valor do **salário mínimo** deve ser informado em Manutenção de Tabelas > **S004** e o valor do **salário mínimo estadual** deve ser informado em Manutenção de Tabelas > **S118.**Saiba mais:

[RH - Linha Protheus - GPE - Como cadastrar a tabela S118 tabela de salário mínimo estadual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19456278734487-RH-Linha-Protheus-GPE-Como-cadastrar-a-tabela-S118-tabela-de-sal%C3%A1rio-m%C3%ADnimo-estadual?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar ou alterar a tabela de Salário Mínimo no gestão de pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061657733-RH-Linha-Protheus-GPE-Como-cadastrar-ou-alterar-a-tabela-de-Sal%C3%A1rio-M%C3%ADnimo-no-gest%C3%A3o-de-pessoal?source=search)  
[RH - Linha Protheus - GPE - Pagamento da Periculosidade Integral no mês da Admissão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018668311-RH-Linha-Protheus-GPE-Pagamento-da-Periculosidade-Integral-no-m%C3%AAs-da-Admiss%C3%A3o?source=search)
