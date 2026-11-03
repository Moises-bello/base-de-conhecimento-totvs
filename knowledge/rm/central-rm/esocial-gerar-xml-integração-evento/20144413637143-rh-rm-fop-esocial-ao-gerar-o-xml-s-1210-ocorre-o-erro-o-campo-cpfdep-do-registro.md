---
article_id: 20144413637143
category: eSocial - Gerar XML/ Integração Evento
content_hash: fdcaaf1127694475810f8e52c5731cc217f18360a3721de724ee7b44b22ddf8c
fetched_at: '2026-06-28T22:47:11.872498+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial -  Ao gerar o XML S-1210 ocorre o erro O campo 'cpfDep'
  do registro 'infoDepSau' é obrigatório e não está preenchido (S-1.2)
type: support-article
updated_at: '2025-12-29T14:18:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20144413637143-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-1210-ocorre-o-erro-O-campo-cpfDep-do-registro-infoDepSau-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20144399011991) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao gerar o XML S-1210 ocorre o erro **O campo 'cpfDep' do registro 'infoDepSau' é obrigatório e não está preenchido**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20144413609111)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões.  
  
**Causa**  
O erro ocorre quando há cadastro de dependente com incidência de Assistência de Saúde e não consta cadastrado o CPF na identificação do dependente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20144413612183)

Sendo essa informação obrigatória , no *Leiaute S-1.2*, quando houver a incidência.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20144399021847)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Selecione o funcionário com erro em **Folha de Pagamento | Administração de Pessoal | Funcionários**;  
2. No cadastro do funcionário em **Dependentes |  Identificação**, preencha o campo **CPF** do Dependente;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20144399026711)

3. Após ajuste, gere novamente o XML.

**Importante**  
Após o preenchimento do CPF será gerado o evento de alteração S-2205, será necessário este evento S-2205 com as informações do dependente para o governo.

**Saiba mais**  
Para mais informações, acesse:

[RH - RM - FOP - eSocial - Como cadastrar evento de plano de saúde para gerar os dados do dependente no XML S-2200 ou S-2205 – Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19752807239191)
