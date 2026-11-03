---
article_id: 360049697274
category: RH - Folha de Pagamento
content_hash: 277f4122ad44bc561a4e71c81e62f0ea6278f699ecdd42f7150c6f7e736ea3f2
fetched_at: '2026-06-28T22:44:16.216834+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Quais possíveis rotinas para cadastro dos Encargos
  da Empresa ( % de Acidente de Trabalho, Terceiros e INSS Empresa)?
type: support-article
updated_at: '2024-09-12T17:58:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049697274-RH-Linha-Protheus-GPE-Quais-poss%C3%ADveis-rotinas-para-cadastro-dos-Encargos-da-Empresa-de-Acidente-de-Trabalho-Terceiros-e-INSS-Empresa
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19404142566551) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Quais possíveis rotinas para cadastro dos Encargos da Empresa ( % de Acidente de Trabalho, Terceiros e INSS Empresa)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**Geralmente o cadastro destes encargos é efetuado pelas Tabelas S037 e S038:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074923294)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074923134)  
  
Mas existe a possibilidade de efetuar o cadastro pelo Cadastro de Centro de Custo, na aba Tomador:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074923494)

Para o acidente de trabalho, também pode ser efetuado o cadastro do percentual, no Cadastro do Funcionário, na aba Funcionais, campo % Acid.Trab.:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076131693)  
  
O sistema sempre validará o cálculo dos encargos na ordem abaixo:

**1º** - Cadastro do Funcionário

**2º** - Cadastro do Centro de Custo

**3º** - Cadastro das Tabelas S037 e S038  
  
Ou seja, se tiver percentuais cadastrados no Cadastro do Funcionário e Centro de Custo, o percentual utilizado para o calculo da folha será o que está nestas rotinas, desta forma, desprezando as informações cadastradas nas Tabelas S037 e S038.   
  
Importante validar as informações no cadastro do funcionário e cadastro do centro de custo, aba tomador quando o valor destes encargos não corresponder aos percentuais cadastrados nas tabelas S037 e S038.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Cadastro da tabela S037 - Encargos Empresa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053697053-RH-Linha-Protheus-GPE-Cadastro-da-tabela-S037-Encargos-Empresa-?source=search)

[RH - Linha Protheus - GPE - O que verificar quando os encargos da empresa não são calculados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048711673-RH-Linha-Protheus-GPE-O-que-verificar-quando-os-encargos-da-empresa-n%C3%A3o-s%C3%A3o-calculados?source=search)

[RH - Linha Protheus - GPE - Como cadastrar os percentuais de INSS terceiros rateados pelas entidades na Tabela S038](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13008616340887-RH-Linha-Protheus-GPE-Como-cadastrar-os-percentuais-de-INSS-terceiros-rateados-pelas-entidades-na-Tabela-S038?source=search)
