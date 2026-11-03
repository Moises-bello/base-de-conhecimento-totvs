---
article_id: 5666156054935
category: Meu RH - Login
content_hash: b6058af8e27c31dbf42c6ca566b89ada6f7955675a5ae7eebe7a5d3f3761a890
fetched_at: '2026-06-28T22:47:27.284842+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: 'RH - RM - Meu RH - Erro ao logar no Meu RH: Valor não pode ser nulo nome do
  parâmetro value'
type: support-article
updated_at: '2026-01-16T15:19:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5666156054935-RH-RM-Meu-RH-Erro-ao-logar-no-Meu-RH-Valor-n%C3%A3o-pode-ser-nulo-nome-do-par%C3%A2metro-value
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15915877533591) Tempo aproximado para leitura: **00:04:57 min**  
  
**Ocorrência**  
Na aplicação Meu RH realizar o login retorna a mensagem de erro: 500 - Valor não pode ser nulo. Nome do parâmetro: value  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas versões  
  
**Causa**  
O erro é retornado por alguns fatores como a ausência da instalação do Portal RM, usuário utilizado ainda não possui validade para acesso e outros.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique a versão instalada do RM e Portal RM do servidor do Meu RH e também das máquinas (clientes) que irão realizar acesso, para o correto funcionamento a mesma versão deve ser instalada em todas as máquinas. Caso necessário auxílio para verificar a versão dos ambientes o artigo a seguir orienta como realizar essa verificação: [RH - RM - Meu RH - Como verificar Versão e Patch da Biblioteca RM e Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402311146263)  
  
2. Caso os ambientes estejam todos na mesma versão com o Portal RM devidamente instalado, o erro é retornado quando a validade do Usuário que está realizando o login está em data futura, por exemplo:

* Usuário com **Início de Validade** em **01/05/2022**
* Login sendo realizado na data de **25/04/2022**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5666017533719)**

O acesso ocorre conforme a data atual e não verifica a competência do ambiente RM.

3. Para realizar o ajusta da validade do Usuário acesse o módulo **Serviços Globais | Segurança | Usuários** e edite o Usuário que está realizando acesso:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22321112285463)

4. Verifique se dentro do arquivo **RM.Host.Service.exe.config** localizado em **C:\TOTVS\CorporeRM\RM.Net** existe a tag **DEFAULTDB** informando o alias no campo value, caso já exista a tag em seu arquivo, verifique se o campo value possui o mesmo alias utilizado no RM.

* **<add key="DEFAULTDB" value="CorporeRM" />**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5694621067671)

5. Por fim, o erro pode ser retornado também caso o Perfil de Acesso vinculado ao Usuário (Perfil de conexão ao banco de dados) esteja com o Usuário e Senha do Banco incorreto.  
Essa configuração pode ser visualizada em **Serviços Globais | Segurança | Usuários** editando o usuário que retorna erro ao logar, edite seu **Código de Acesso** e informe um usuário e senha para conexão ao banco de dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15915823825687)
