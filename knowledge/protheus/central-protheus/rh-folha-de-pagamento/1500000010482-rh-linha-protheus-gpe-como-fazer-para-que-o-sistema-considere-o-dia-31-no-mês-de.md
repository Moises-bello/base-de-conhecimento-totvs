---
article_id: 1500000010482
category: RH - Folha de Pagamento
content_hash: cf28c4839216213006ed85bfd2941e50ddd914201590430ce9d1e70a7cb304c7
fetched_at: '2026-06-28T22:44:13.482049+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como fazer para que o sistema considere o dia 31
  no mês de retorno do afastamento para montagem do saldo de salário proporcional
  do empregado, mesmo que mensalista
type: support-article
updated_at: '2025-12-18T18:08:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000010482-RH-Linha-Protheus-GPE-Como-fazer-para-que-o-sistema-considere-o-dia-31-no-m%C3%AAs-de-retorno-do-afastamento-para-montagem-do-saldo-de-sal%C3%A1rio-proporcional-do-empregado-mesmo-que-mensalista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26304251164311)** Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**  
Como fazer para que o sistema considere o dia 31 no mês de retorno do afastamento para montagem do saldo de salário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para que o sistema considere o dia 31 no mês de retorno do afastamento para montagem do saldo de salário proporcional do empregado, mesmo que mensalista, realizar o procedimento abaixo:

- No **modulo Configurador** em **Base de Dados -> Dicionário -> Base de Dados** configurar o parâmetro **MV\_DIASPER**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101094693)  
  
Este parâmetro deve ser configurado com **"1"**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098889754)  
  
Após a configuração acessar o modulo Gestão de Pessoal e realizar o calculo.

OBS.: A alteração desse parâmetro impacta em todos os cálculos de folha, férias e rescisão.  
  
Em **Consultas -> Cálculos -> Por Funcionários** serão apresentados os valores calculados para conferência:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101100493)  
  
**Resumo do cálculo**:   
- Salário do funcionário R$ 2.646,09 / 30 dias no mês (pois no cadastro de períodos "Dias para Cálculo" consta 30) X 11 dias trabalhados (o sistema está considerando o retorno do afastamento em 21/10/2016 a 31/10/2016)= 970,33.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
