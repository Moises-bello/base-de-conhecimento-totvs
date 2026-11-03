---
article_id: 39572750887447
category: RH - Funcionários
content_hash: c33dd66250863f23d06a60cbd393216bacff5820f0bc830b9ea756106dec5ddf
fetched_at: '2026-06-28T22:43:27.403693+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro de funcionário apresenta mensagem de HELP
  PISINVALID
type: support-article
updated_at: '2026-04-07T18:16:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39572750887447-RH-Linha-Protheus-GPE-Cadastro-de-funcion%C3%A1rio-apresenta-mensagem-de-HELP-PISINVALID
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39572758702487) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao realizar o cadastro de um funcionário é apresentada mensagem de HELP PISINVALID.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572758703127)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
No padrão o campo PIS não é obrigatório para preenchimento no cadastro do funcionário. A mensagem apresentada demonstra que o campo RA\_PIS está com a opção Obrigatório selecionada, assim, validando o preenchimento do campo.

**01**. Acesse o **Configurador** **SIGACFG** em **Base de Dados > Dicionário > Base de Dado**s **(CFGX031)**;

**02.** **Pesquise** pela tabela **SRA** e clique em **Editar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572758707735)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572750849815)

**03.** **Pesquise** pelo campo **RA\_PIS** e clique em **Editar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572750851479)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572750852247)

Verifique na aba **Uso** se a opção **Obrigatório** está selecionada, caso esteja seleciona **desmarque** a opção, pois por **não ser obrigatório** o preenchimento não deve estar selecionada a opção, clique em **Salvar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572750855575)

**Observação:** Após alterações realizadas no configurador é necessário clicar no ícone de disquete para atualizar o dicionário com as alterações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39572758718999)

**Saiba mais:**

[RH - Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909593-RH-Funcion%C3%A1rios)
