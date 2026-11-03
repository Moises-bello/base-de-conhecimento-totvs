---
article_id: 1500000621761
category: RH - Folha de Pagamento
content_hash: 33f93e2ed131dd6cc4309d0fec6b55a0f7bb31845066b8e5f5e377d672efe25a
fetched_at: '2026-06-28T22:44:14.995188+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Importação de variáveis tabela RHO, não soma valores
  de coparticipação
type: support-article
updated_at: '2025-05-12T16:36:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000621761-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RHO-n%C3%A3o-soma-valores-de-coparticipa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26247533298327) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Ao efetuar importação de Coparticipação na tabela RHO o sistema não soma os valores quando possui mais de um lançamento para o Titular ou Dependente.  
  
**Ambiente**Microsiga Protheus - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, devido a pergunta **Sobrepõe** em paramentos, se a mesma estiver como SIM ela não irá somar os valores e sim considerar apenas a primeira linha do lançamento do Titular/Dependente.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse: **Atualizações > Definições de Calculo >** ***Layout* de Importação**  
  
Preencher conforme imagem abaixo:  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5727924438039)**  
2. Crie um **TXT** compatível**.**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5728003831191)

3. Acesse: Miscelânea > Importação > **Importação****Variáveis**  
  
Clique em Parâmetros  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5728033788695)

Preencher os **Parâmetros¹**:

Arquivo? = Acessar o local onde está salvo o TXT e selecionar o TXT desejado.

Código? = 004 (Código referente ao Layout criado anteriormente)

Sobrepõe? = **NÃO**

Situações? = ADFT  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5728086925463)

Clique em **OK**

Preencher os **Parâmetros²:**

Tipos Lançamento? = 1 - Co-Particip.

Competência Pagamento? = 2021/07 (Mês ativo no ato da importação)  
  
Clique em **OK**  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5728109949591)  
  
Clique em **OK**  
**Log de Importação:**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5728212999447)  
  
4. Acesse: Atualizações > Benefícios > Planos de Saúde > **Co-participações**

Selecione o **Funcionário** e Visualizar

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5728237510039)  
  
**Saiba Mais**

[RH - Linha Protheus - GPE - Importação de variáveis tabela RGB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058289233-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RGB?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis tabela SRK](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000579482-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-SRK?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis Coparticipação, dependentes ficam deletados na RHO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036186414-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-Coparticipa%C3%A7%C3%A3o-dependentes-ficam-deletados-na-RHO?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis tabela RHO - Coparticipação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5743820814487-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-tabela-RHO-Coparticipa%C3%A7%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Importação de variáveis de coparticipação quando houver mais de 1 dependente ou agregado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038792513-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-de-vari%C3%A1veis-de-coparticipa%C3%A7%C3%A3o-quando-houver-mais-de-1-dependente-ou-agregado?source=search)
