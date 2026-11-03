---
article_id: 34420547549207
category: eSocial - Cadastros
content_hash: 33118a004e6bc685a6066f91d2ba91695a0ca8e18d91a06b732812270e07545c
fetched_at: '2026-06-28T22:47:14.505607+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro código 483: Logradouro invalido.Acao Sugerida:
  O valor informado no campo devera existir na Tabela 20 (Tipos de Logradouros)'
type: support-article
updated_at: '2026-06-05T17:17:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34420547549207-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-483-Logradouro-invalido-Acao-Sugerida-O-valor-informado-no-campo-devera-existir-na-Tabela-20-Tipos-de-Logradouros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34420521300375) Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**  
Ao integrar o evento S-2200 ou S-2300 é retornado o erro código 483:   
Logradouro inválido. Ação Sugerida: O valor informado no campo devera existir na Tabela 20 (Tipos de Logradouros). Localização: /eSocial/evtAdmissao/trabalhador/endereco/brasil/tpLograd.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**  
O erro ocorre quando a codificação do Logradouro não está correta e parametrizada dentro do RM, conforme tabela [Tabela 20 - Tipos de Logradouro](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/tabelas.html#20) do eSocial.  
  
**Solução**  
Para solucionar o erro em questão, será preciso:  
1. Acesse o módulo **Serviços Globais | Segurança | Perfis**e selecione o sistema**RH | Folha de Pagamento**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34421235211543)

2. Edite o perfil que está associado ao usuário do módulo de Folha de Pagamento;  
3. Na aba**Acesso a Menus** selecione o item **[09.01.03] Endereços** e clique em **Permitir Acesso** para liberar as permissões ao menu;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34421261137687)

4. Ainda no cadastro de perfis, selecione o sistema **BackOffice | Gestão Fiscal,** edite o perfil que está associado ao usuário do módulo de Gestão Fiscal;  
5. Na aba**Acesso a Menus** selecione os itens **[01.02.02.02] Países**, **[01.02.02.03] Estados**,**[01.02.02.04] Municípios**e **[01.02.02.05] Endereço**e clique em **Permitir Acesso** para liberar as permissões aos menus;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34421235217687)

6.Acesse o Módulo Folha de Pagamento novamente, entre em **Configurações | Parametrizador | eSocial | De/Para de Endereço** e preencha o campo **Conceito de Classificação para Códigos de logradouro.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34421261139863)

7. Acesse o caminho: **eSocial | Endereço | Logradouro**, selecione a rua, clicar em **Anexo - Codificação do Tipo de Rua** e cadastrar conforme abaixo:

* Código: **R**
* Classificação: Logradouro (o mesmo que está dentro do parametrizador De/Para Endereço)

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34421261143191)

8. Após isso, gere novamente o XML e o integre ao eSocial.

**Saiba Mais:**

[**RH - RM - FOP - eSocial - Liberação de acesso ao menu de endereços do eSocial**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004193791-RH-RM-FOP-eSocial-Libera%C3%A7%C3%A3o-de-acesso-ao-menu-de-endere%C3%A7os-do-eSocial?source=search)  
[**Como realizar a liberação de acesso aos cadastros de endereço na aba eSocial?**](https://tdn.totvs.com/pages/viewpage.action?pageId=361449123)
