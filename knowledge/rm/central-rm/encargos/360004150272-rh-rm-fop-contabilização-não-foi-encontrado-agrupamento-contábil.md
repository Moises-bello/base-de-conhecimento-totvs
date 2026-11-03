---
article_id: 360004150272
category: Encargos
content_hash: 30b734ccc42e0ad8962438b907c1bb022635adcc09507e6077469dfc0fcc94e5
fetched_at: '2026-06-28T22:46:53.429816+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Contabilização: Não foi encontrado Agrupamento Contábil'
type: support-article
updated_at: '2025-07-04T15:57:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004150272-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-N%C3%A3o-foi-encontrado-Agrupamento-Cont%C3%A1bil
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24284299867671)**Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**No módulo **Folha de Pagamento**, ao executar a geração dos lançamentos contábeis que está localizado em Encargos | Geração dos Lançamentos, é apresentada a seguinte mensagem de erro:  
  
Não foi encontrado Agrupamento Contábil com a seguinte parametrização:  
  
Grupo contábil: 2050   
Integração contábil: Sem preencher   
Integração funcionário: Sem preencher   
Conta Saldus: Sem preencher  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse erro ocorre pois, na geração dos lotes contábeis o sistema está buscando por um agrupamento com as parametrizações conforme apresentado no erro, conforme abaixo:  
  
Integração contábil: Sem preencher   
Integração funcionário: Sem preencher   
Conta Saldus: Sem preencher   
  
**Solução**Para solucionar essa ocorrência, existem duas opções, além de outros itens a serem conferidos:  
  
1. Criar um novo Grupo Contábil com código informado na mensagem de erro. Para criar, veja os passos A e B:  
  
A) Acesse **Folha de pagamento | Encargos | Cadastros Contábeis | Agrupamento de contas**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602426462743)

B) Clique em Incluir e preencha os campos **Grupo de conta**, **Código de integração**, **Código de Integração por Funcionário** e **Conta Saldus**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602414540567)

2. Outra opção é acessar o cadastro do encargo ou evento, acessar a aba **Dados Contábeis** e configurar de acordo com a parametrização abaixo:  
  
- Integração contábil: sem preencher, ou conforme informado na mensagem apresentada ao final da contabilização;  
- Integração por funcionário: sem preencher, ou conforme informado na mensagem apresentada ao final da contabilização;  
- Conta Saldus: sem preencher, ou conforme informado na mensagem apresentada ao final da contabilização;  
  
- Caso esteja contabilizando eventos, acesse **Folha de Pagamento | Administração de Pessoal | Eventos | Eventos**, selecione o evento e clique em **Editar**.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602705386263)

No cadastro do evento, acesse a aba **Dados Contábeis;**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602734762391)

Além do grupo contábil, verificar também se a opção **Tem integração contábil** está marcada. Ou, caso este grupo não tenha integração contábil, pode ser que algum evento do grupo conste como marcado indevidamente.  
  
- Caso esteja contabilizando encargos, acesse **Folha de Pagamento | Encargos | Cadastros | Encargos**;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602677645463)

Selecione o encargo e clique em editar e acesse aba **Dados contábeis**;

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602732461719)

Além do grupo contábil, verificar também se a opção **Tem integração contábil** está marcada. Ou, caso este grupo não tenha integração contábil, pode ser que algum evento do grupo conste como marcado indevidamente.

- Acesse o cadastro de seção que o funcionário esta alocado e verifique se existe informação na aba de dados contábeis que estão parametrizadas incorretamente. Para localizar a seção acesse: **Administração de Pessoal | Seções**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602807386135)

Acesse a seção que o funcionário esta alocado e verifique a parametrização.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602795003799)

**Outras validações**:  
- Verificar se consta Centro de Custo na empresa. Se sim, verificar se consta o código de integração contábil informado no Centro de Custo: Para isso acesse: **Administração de Pessoal | Centro de custo**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602832807703)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602850674583)

- Sendo o grupo contábil por funcionário, validar se no cadastro do funcionário consta preenchida a integração contábil, conforme demonstrado abaixo. Se o grupo contábil não for por funcionário, verificar mesmo assim e retirar caso esteja preenchida:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602853874455)

- Se o grupo é referente a Integração Gerencial, verificar se foi criado um grupo contábil para a conta gerencial, ou se consta algum evento sem a informação preenchida e o flag desmarcado, conforme abaixo:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11602908071319)

**Importante**- Deverá ser conferida a Integração Contábil. Caso utilize o rateio por Centro de Custo, o Agrupamento Contábil deverá possuir a mesma Integração Contábil que o Centro de Custo do funcionário. Caso não trabalhe com o rateio por Centro de Custo, deverá conferir na Seção, a Integração Contábil da Seção deverá ser o mesmo do Agrupamento Contábil.  
- Para facilitar a conferência e encontrar a origem do erro mais facilmente, sugere-se a geração do lançamentos separando por filial ou seção.  
  
**Saiba mais**  
Para mais informações, acesse:

[Contabilização - Log do Processo](https://tdn.totvs.com/pages/viewpage.action?pageId=945393365#1-3)

[Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019748711-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o)

[Parametrização contabilização](https://tdn.totvs.com/pages/releaseview.action?pageId=110428888)
