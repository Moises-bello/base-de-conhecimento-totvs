---
article_id: 33398792665239
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 5ce3f8d77c426ec95c1a1c67ca80b926b4c835a32d021c48bd60c5664a012960
fetched_at: '2026-06-28T22:39:09.456884+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como desativar
  a mensagem: "Existem perfis tributários cadastrado nesta filial. Deseja vincular
  este produto a um ou mais perfis?"'
type: support-article
updated_at: '2026-03-25T18:43:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33398792665239-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-desativar-a-mensagem-Existem-perfis-tribut%C3%A1rios-cadastrado-nesta-filial-Deseja-vincular-este-produto-a-um-ou-mais-perfis
---

Ao acessar o cadastro de produto no TOTVS Backoffice (Linha Protheus) - Estoque/Custos, pode aparecer a mensagem sobre vincular o produto a perfis tributários. Esta mensagem está ligada ao Configurador de Tributos (FISA170) e pode ser desativada configurando o parâmetro MV\_FACAUTO como .F.. Isso impede a exibição da mensagem, mas o registro ainda pode ser vinculado aos perfis tributários por outros meios, se necessário.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33398792656279) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao acessar o cadastro de produto é gerado a mensagem: **Existem perfis tributários cadastrado nesta filial. Deseja vincular este produto a um ou mais perfis?** Como desativar essa mensagem?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33398792656919)

No menu do cadastro de produtos, ao efetuar a inclusão de um novo produto, na aba de **"Outras Ações"**, não será apresentado a relação **"Perfis Tributários",** somente na **"Alteração">"Outras Ações"**.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Essa mensagem está relacionada ao facilitador para vincular as regras do **Configurador de Tributos (FISA170).** Quando é incluído um novo cliente, fornecedor ou produto é questionado se quer incluir em alguma regra definida na rotina.  
   
Caso não vincule, não terá impactos. Somente não será validado a regra na **FISA170**. Esta funcionalidade é controlada pelo parâmetro **MV\_FACAUTO (Default = .F.).**  
   
Se o parâmetro for configurado como .F. então a mensagem não será exibida e o registro deverá ser vinculado aos perfis, se necessário, utilizando-se qualquer uma das outras formas mencionadas.

[**CFGTRIB - Configurador de Tributos**](https://tdn.totvs.com/x/5SApK)  
[**[CFGTRIB] - FISA166 - Cadastro de perfil tributário de produtos**](https://tdn.totvs.com/x/00wBLw)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
