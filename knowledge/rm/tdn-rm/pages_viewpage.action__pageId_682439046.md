---
content_hash: c38b742fa40d00148ede8a863f0f804a7ad76d6e065ec64e7ce3db00067280dc
fetched_at: '2026-06-29T00:11:17.956984+00:00'
page_id: '682439046'
product: rm
source: tdn-rm
title: FAQ - Portal Gestão Educacional (PGE)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=682439046
version: 10
---

Mesmo após a parametrização do config, habilitando o EnableRealtime = True, ainda é exibido o TimeOut para atualização do painel de conversas.

# **Solução:**

Alterar a configuração do Rewrite ***Outbound rules that applied to the...*** seguindo os passos abaixo.

**1º-** Acessar o IIS, selecionando a pasta: FrameHTML | Portal Gestão Educacional | URL Rewrite

**2º-**Acessar a regra do rewrite: *Outbound rules that applied to the....*

**3º-** Selecionar a regra e clica em "Edit" 

**4º-** Acessar a opção Conditions

**5º-** Selecionar a opção destacada abaixo e clicar em "Edit"

**6º-** Alterar as informações conforme a descrição abaixo.

**Condition input:** {URL} 

**Pattern:** aliasname\.(.\*)/api/framework/v1/realtime/

Em seguida, clicar em OK

**7º-** Em seguida, clicar em Apply

As mensagens são duplicadas ao acessar a Sala de Atendimento

# **Solução:**

Verificar se no cadastro do Aluno e seus Responsáveis,  o Código do Usuário vinculado em seus cadastros estão associados a mais de uma PPESSOA. Se tiver, acessar os cadastros correspondentes e remover o vinculo duplicado.

 

```
             Cadastro do Aluno                            Cadastro do Responsável Temporário                  Cadastro do Responsável (Pai, Mãe, Financeiro)
```

        

Cadastro de Pessoa no RH

Esta validação deve **incluir também no cadastro de Pessoa** no módulo de RH, pois pode existir outra pessoa que esteja relacionada ao mesmo usuário, **porém** **ela não esteja relacionada no cadastro do Aluno e seus Responsáveis**.

```
Cadastro de Pessoa no RH
```

Mesmo após a parametrização, ao logar no portal ocorre o erro: Ocorreu um erro ao fazer o login 

# **Solução:**

Esse erro ocorre devido a parametrização divergente da Regra do **Rewirite URL** com o RM.host.service.exe.config.

Na Regra Rewrite **URL**, deverá está informado a mesma nomenclatura (**nome** ou o **IP** da máquina)  informado na tag: SubDomainMask  do RM.Host.exe.config. Isso é, se na TAG: SubDomainMask  está informado o nome do servidor onde o host está sendo executado,na regra do Rewrite (URL) deverá conter a mesma descrição.
