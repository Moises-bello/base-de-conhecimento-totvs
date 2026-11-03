---
article_id: 26569388950423
category: eSocial - Gerar XML/ Integração Evento
content_hash: 069b11e2130c5f2b135d4593e67458358501eda7c3e59637495324ae1afeecda
fetched_at: '2026-06-28T22:47:11.946926+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o XML S-2200/2300 ocorre o erro: O campo
  ''codMunic'' do registro ''Brasil'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2025-01-03T15:36:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26569388950423-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-2200-2300-ocorre-o-erro-O-campo-codMunic-do-registro-Brasil-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26569420828439) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o XML S-2200/2300 ocorre o erro O campo 'codMunic' do registro 'Brasil' é obrigatório e não está preenchido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26569388924695)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**O erro ocorre quando não existe codificação de município informado no cadastro de município, ou quando a codificação vinculada ao município não esta vinculado corretamente em: **Configurações | Parametrizador | eSocial | De/Para de Endereços.**

**Solução**Acesse: **Módulo Folha de Pagamento | Administração de Pessoal | Funcionários |** Cadastro do funcionário com erro | **Aba endereços**, verifique o município vinculado no cadastro do funcionário,

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26569420833559)

Acesse: **eSocial | Endereços | Município |** Localize o Município acima. Acesse: **Anexos | Codificação de município**e verifique a parametrização do mesmo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26570287893015)

 Após acesse: **Configurações | Parametrizador| eSocial | De/para de Endereços** e confirme se alguma codificação acima consta informado no campo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26570303597079)

Após ajuste acima, regere o XML e a tag será alimentado conforme esperado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26585163979799)

**Saiba mais**  
Para mais informações acesse:

[Como realizar a liberação de acesso aos cadastros de endereço na aba eSocial?](https://tdn.totvs.com/pages/releaseview.action?pageId=361449123)
