---
article_id: 20116860631959
category: Originação de Grãos (OG)
content_hash: 509412d5b082ca88e3c0fed8fa300d69283d42ce9049c1acdc2488780b63fe35
fetched_at: '2026-06-28T22:45:43.394732+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Procedimento para cadastrar uma balança
type: support-article
updated_at: '2025-06-13T20:10:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20116860631959-Agro-Linha-Protheus-AGR-Procedimento-para-cadastrar-uma-balan%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20116860598551) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao realizar o processo para cadastrar uma balança é apresentada a ocorrência **Procedimento para cadastrar uma balança**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para cadastrar uma balança no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, cadastre uma **Balança** e realize os seguintes passos:

**1.** Verifique via **hyperTerminal** do **Windows**, a conexão com a balança e aguardar o retorno.

![BALAN.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20116860599831)

![BALAN1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20116860600983)

**2.** Realize o cadastro da balança com as configurações do **hyperTerminal**. Após, fechar o **hyperTerminal**.

![BALAN2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20116875409303)

**3.** Teste o cadastro da balança.

![BALAN3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20116875410327)

**4.** Acesse em **Teste**, **Ações Relacionadas – Testar**, irá abrir a tela de pesagem, a mesma do romaneio, clicar em **Capturar** e aguardar a tela abaixo:

![BALAN4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20116860603671)

Nesse exemplo a balança está conectada e retornando **D001100.D001100.D00110.**É necessário identificar o **início** do retorno, o qual é sempre **D.**É necessário identificar o **peso** do retorno, o qual será **001100.**Após identificados o início e o peso é necessário gerar o *script*, e para isso são utilizados os caracteres de retorno **ASC**.  
  
O *script* será: **SUBSTR(cConteudo,AT(CHR(068),cConteudo)+1,6),**então:   
**cConteudo** = retorno da balança **(D001100.D001100.D00110).  
AT(CHR(068),cConteudo)+1** = da posição **D** e **+1** inicia-se o peso **(001100 =CHAR(02)).**6 = até aonde deve-se pegar o peso, sendo que o final é ponto **(.) (001100).**Informar o *script*, confirmar o cadastro e realizar os testes na rotina do **Romaneio com Pesagem - OGA250**.  
  
**Importante**Não pode haver nenhum tipo de comunicação ativa com a balança, somente o **Protheus**.  
É necessário atenção com a balança informada no **Romaneio - F12**, e se o usuário possui autorização para o manuseio dela.
