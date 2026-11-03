---
article_id: 4402435789591
category: RH - Ambiente
content_hash: d25bf9afd97c463f62f560c2a27c78ad02b45a259403374fc809e0c9e6d446d6
fetched_at: '2026-06-28T22:44:55.927586+00:00'
product: protheus
section_id: 32302375681815
source: central-protheus
title: RH - Linha Protheus - PON - Como aumentar o tamanho do campo onde indica o
  caminho do arquivo no cadastro de relógio
type: support-article
updated_at: '2025-11-04T20:35:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402435789591-RH-Linha-Protheus-PON-Como-aumentar-o-tamanho-do-campo-onde-indica-o-caminho-do-arquivo-no-cadastro-de-rel%C3%B3gio
---

**Dúvida**Como aumentar o tamanho do campo onde indica o caminho do arquivo no cadastro de relógio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para aumentar o tamanho do campo **P0\_ARQUIVO,** onde indica o caminho do arquivo, é necessário acessar o **configurador (SIGACFG): Base de Dados>Dicionário>Base de Dados, em** Dicionário de Dados>Pesquisar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36106006054935)  
  
Pesquisar pela tabela SP0 (Relógio de Ponto)>Editar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36106021693719)  
  
Selecionar Campos>Procurar o campo **P0\_ARQUIVO** e editar: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/36106021696919)**Após isso, alterar o tamanho do campo (no exemplo abaixo alterei para 45):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36106006061079)  
  
Depois de clicar em **Salvar e Sair**, é necessário **Atualizar a base de dados ou agendar a atualização:  
\*\*Para salvar essa alteração é necessário acesso exclusivo no sistema  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36106021701143)**Caso a opção desejada seja **Atualizar Base de Dados** para finalizar a alteração  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36106021703959)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36106021708055)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36106021709463)  
  
**Importante:** Não é necessário alterar a tabela **RFB**, pois ela por padrão, já tem o campo **RFB\_ARQ** com tamanho 60.   
  
**Informações complementares**[RH - Linha Protheus - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o-?source=search)  
[RH - Linha Protheus - PON - Como cadastrar um Turno de Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410322419095-RH-Linha-Protheus-PON-Como-cadastrar-um-Turno-de-Trabalho?source=search)  
[RH - Linha Protheus - PON - Qual a funcionalidade do campo Sequência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004802732-RH-Linha-Protheus-PON-Qual-a-funcionalidade-do-campo-Sequ%C3%AAncia?source=search)  
[Pacote de Expedição Contínua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
