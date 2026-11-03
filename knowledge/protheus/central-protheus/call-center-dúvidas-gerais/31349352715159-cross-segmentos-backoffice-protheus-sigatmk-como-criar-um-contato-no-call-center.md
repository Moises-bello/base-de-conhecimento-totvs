---
article_id: 31349352715159
category: Call Center - Dúvidas Gerais
content_hash: 56afd18e1f57aab6b2a0791180ce27815bbbc4eca5be9142294bf9b1a3fac11d
fetched_at: '2026-06-28T22:41:26.943758+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Como criar um contato no
  Call Center?
type: support-article
updated_at: '2025-04-11T19:05:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31349352715159-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Como-criar-um-contato-no-Call-Center
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31349352689303) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como criar um contato no Call Center e relacionar com o cliente?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões  
  
**Solução**

Existem algumas formas de se realizar a criação de contatos e efetuar o **vínculo entre cliente x contato no ambiente do Call Center.**  
  
Abaixo será detalhada algumas formas para esse processo:  
  
**1- Criação e vinculo através das rotinas de atendimento**A criação e vinculo do contato, pode ser realizada em uma dentre as diversas rotinas de atendimento do módulo, sendo elas do *Televendas,Telecobrança ou Telemarketing.*   
  
No exemplo abaixo, vamos utilizar como referência a rotina do "Call Center" (**TMKA271 - Televendas**) , onde é possível realizar a inclusão do cadastro e o vínculo com o Cliente (Entidade).  
**Importante:** Para utilizar o Televendas, o operador deve estar configurado para esse tipo de atendimento. Mais dúvidas sobre essa configuração acesse [Configuração: Atendimento Televendas](https://www.youtube.com/watch?v=XJY65XbuQ80)

**1.1** Realize o acesso através do Menu do Call Center (SIGATMK) em: Atualizações > Atendimento > Call Center (TMKA271).  
**1.2** Selecione o "Cliente" (UA\_CLIENTE) do qual gostaria de incluir o contato.   
**1.3** Selecione o campo "Contato" (UA\_CODCONT)  
**1.4** Efetue a inclusão e o preenchimento dos campos obrigatórios "Contato" **(U5\_CODCONT)** , "Nome"  (**U5\_CONTAT**) e os dados cadastrais (opcionais) de Endereço e Telefones, devem ser efetuados na aba inferior da rotina Contatos (**TMKA070**), realizando o preenchimento na **AGA (****Endereço X Entidade)** e **AGB (Telefone X Entidade)****.**

![TMK_SP01.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/31350350061847)

**2- Criando um contato diretamente no Cadastro do cliente (CRMA980)**

**2.1** Realize o acesso através do Menu do Call Center (SIGATMK) em: Atualizações > Gestão de Contatos > Clientes(CRMA980).  
**2.2** Posicione no browse o cliente do qual gostaria de incluir o contato

**2.3** Selecione Outras Ações > Contatos  
**2.4**  De um duplo clique no campo  de "Contato" (AC8\_CODCON)  
**2.5** Selecione "Incluir"   
**2.6** Efetue a inclusão e o preenchimento dos campos obrigatórios "Contato" **(U5\_CODCONT)** , "Nome"  (**U5\_CONTAT**) e os dados cadastrais (opcionais) de Endereço e Telefones, devem ser efetuados na aba inferior da rotina Contatos (**TMKA070**), realizando o preenchimento das informações na **AGA (****Endereço X Entidade)** e **AGB (Telefone X Entidade)****.   
2.7** Após o preenchimento clique em "Salvar"  
**2.8** Selecione o novo contato criado  
**2.9** Pressione "OK" e Confirme a operação

![TMK_SP02.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/31350355468055)

**3- Criação através da rotina de Contatos (TMKA070) efetuando o vínculo com o Cadastro do Cliente (CRMA980)**  
  
**3.1** Realize o acesso através do Menu do Call Center (SIGATMK) em: Atualizações > Gestão de Contatos > Contatos (TMKA070).  
**3.2** Efetue a inclusão e o preenchimento dos campos obrigatórios "Contato" **(U5\_CODCONT)** , "Nome"  (**U5\_CONTAT**) e os dados cadastrais (opcionais) de Endereço e Telefones, devem ser efetuados na aba inferior da rotina Contatos (**TMKA070**), realizando o preenchimento das informações **AGA (****Endereço X Entidade)** e **AGB (Telefone X Entidade)****.   
3.3** Após o preenchimento clique em "Salvar"  
**3.4** Realize o acesso através do Menu do Call Center (SIGATMK) em: Atualizações > Gestão de Contatos > Clientes(CRMA980).  
**3.5** Posicione no browse o cliente do qual gostaria de incluir o contato.  
**3.4** Selecione Outras Ações > Contatos  
**3.6**  De um duplo clique no campo  de "Contato" (AC8\_CODCON)  
**3.7** No campo "Contato" (AC8\_CODCON) insira diretamente o código do contato (U5\_CODCONT) criado ou realize a busca selecionando o contato manualmente.   
**3.8** Após a seleção do código do contato, clique em "Confirmar"

![TMK_SP03.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/31350355469719)

**IMPORTANTE:** Não necessariamente os dados de Endereço e Telefone devem ser preenchidos para criação de um novo contato.   
  
Contudo, sugerimos que realize o preenchimento do telefone de contato na tabela (AGB), conforme os exemplos mencionados anteriormente, visto que no processo do Call Center é fundamental em inúmeras rotinas o preenchimento do obrigatório do telefone.  
  
**Observação:** Pode se cadastrar vários endereços e telefones, entretanto apenas um deve ser definido como padrão, por meio do campo Padrão (Sim ou Não).   
  
**Saiba mais:**  
[Endereço e Telefone no cadastro de Contatos TMKA070](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018370332-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Endere%C3%A7o-e-Telefone-no-cadastro-de-Contatos-TMKA070)  
[TMK0085 - Cadastro de Contatos (TMKA070)](https://tdn.totvs.com/pages/viewpage.action?pageId=662072791)
