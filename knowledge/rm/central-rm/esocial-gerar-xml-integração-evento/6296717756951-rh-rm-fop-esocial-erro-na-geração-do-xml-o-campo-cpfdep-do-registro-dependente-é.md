---
article_id: 6296717756951
category: eSocial - Gerar XML/ Integração Evento
content_hash: 4b906e0243c2536e6643f1cfc420f3998dd5157f69a610e2bfe0b010c68be563
fetched_at: '2026-06-28T22:47:11.866352+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial  - Erro na geração do XML: O campo ''cpfDep'' do registro
  ''dependente'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2025-02-14T13:17:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6296717756951-RH-RM-FOP-eSocial-Erro-na-gera%C3%A7%C3%A3o-do-XML-O-campo-cpfDep-do-registro-dependente-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24453832233111) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao realizar a geração de XML de **Eventos Não Periódicos** é apresentada a mensagem de erro **O campo 'cpfDep' do registro 'dependente' é obrigatório e não está preenchido**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**O erro ocorre porque o CPF do dependente torna-se obrigatório para fins de imposto de renda quando o mesmo é **dependente de IRRF.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6297012239255)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o módulo **Folha de Pagamento | Administração de Pessoal | Funcionários** e localize o cadastro do funcionário que apresentou erro na geração;  
2. No cadastro do funcionário em **Dependentes,** deverá preencher o campo **CPF**;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6297114190487)

3. Após ajuste, gere novamente o XML.

**Importante**   
Valide o XML S-1210 onde existe a tag CpfDep vazio conforme exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29986557254551)

Para casos de desconto em plano médico/odontológico, acesse o histórico de assistência saúde do funcionário e verifique se existe o desconto de plano de saúde para algum dependente que consta na lista de dependentes e que não possui o CPF preenchido. 

Após identificar, verifique se o desconto é devido ou não e realize os ajustes necessários.
