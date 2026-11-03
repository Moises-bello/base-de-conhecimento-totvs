---
article_id: 360061935893
category: Funcionários
content_hash: 4872dc55011f599b49b0104366567a1dd3666fb8462508028c91220836c821cb
fetched_at: '2026-06-28T22:47:21.524042+00:00'
product: rm
section_id: 1500000861282
source: central-rm
title: RH - RM - RHU - Bloqueio do campo salário
type: support-article
updated_at: '2024-10-02T18:12:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061935893-RH-RM-RHU-Bloqueio-do-campo-sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15864343423639) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**É possível bloquear alterações no campo 'Salário' do Cadastro de Funcionários?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - Toda as versões  
  
**Solução**

Para bloquear o campo Salário dentro do cadastro do funcionário deve tirar permissão de acesso ao campo SALARIO da tabela PFUNC em todos os módulos (Gestão de pessoas, Automação de ponto, folha e Segurança e Saúde Ocupacional).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26789346682519)

**Importante**

Porém o sistema não permite que tire a obrigatoriedade do campo por se tratar de um campo indispensável para o cadastro de um funcionário (assim como o campo CPF), sendo assim não é possível realizar um cadastro de funcionário sem o campo estar preenchido. Dessa forma, retirando essas permissões, o usuário vinculado ao perfil em questão não poderá realizar o cadastro de um funcionário visto que é um campo obrigatório.

Além disso, através do uso de algumas parametrizações é possível realizar o bloqueio de alterações manuais no Salário dos funcionários diretamente no Cadastro de Funcionários  
  
As parametrizações são através do uso de **Requisição** e/ou **Tabelas Salariais**.  
  
O parâmetro de requisição que controla este acesso é: **TOTVS Gestão de Pessoas | Parametrizador | Requisições | Requisições - 1 | Controle de Processos | Requisiçaõ Obrigatória para alterar cargo e/ou salário.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26789397194519)**

​

O parâmetro de Tabela Salarial que controla este acesso é: **TOTVS Gestão de Pessoas | Parametrizador | Validações | Remuneração | Considerar os Salários das Tabelas Salariais e Permitir Alteração Manual de Salário.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26789346702231)**

**Saiba Mais**

Para maiores informações, acesse:

- [RH - RM - FOP - Como liberar acesso ao campo salário no cadastro de funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418616920727)
