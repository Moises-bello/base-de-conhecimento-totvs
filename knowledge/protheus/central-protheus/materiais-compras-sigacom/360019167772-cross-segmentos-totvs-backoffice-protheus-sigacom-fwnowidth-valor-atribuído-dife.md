---
article_id: 360019167772
category: Materiais - Compras (SIGACOM)
content_hash: 16dd07ff3316799c4537f14320a69de69f913b78e832174f18378c0149b2b097
fetched_at: '2026-06-28T22:41:07.383860+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  FWNOWIDTH Valor atribuído
  difere do tamanho do campo (Município) no cadastro de Fornecedores
type: support-article
updated_at: '2024-01-31T18:16:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019167772-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-FWNOWIDTH-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Munic%C3%ADpio-no-cadastro-de-Fornecedores
---

**Ocorrência**FWNOWIDTH Valor atribuído difere do tamanho do campo (Município) no cadastro do Fornecedor

**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Causa**

No módulo de Compras, ao cadastrar um novo Fornecedor, apresenta a seguinte mensagem após informar o campo A2\_MUN: FWNOWIDTH Valor atribuído difere do tamanho do campo (Município)

Esse incidente pode ocorrer, se o tamanho do campo do sistema ou base de dados estiver incorreto.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesso o Configurador do Protheus;  
![Screenshot_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015124611/Screenshot_5.png)

2. No menu do configurador acesse **Base de dados -> Dicionário de dados -> Base de Dados**;

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015086232/Screenshot_1.png)

3. Clique sobre a opção **Dicionário de Dados** e em seguida na lupa, busque pela tabela **SA2**. Ao localizar, clique sobre o botão editar;

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015086372/Screenshot_2.png)

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015124911/Screenshot_3.png)

4. Maximize a opção **Fornecedores**, clique em **Campos** e realize a busca pelo campo **A2\_MUN**;

![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015124971/Screenshot_4.png)

5. Clique sobre o campo após localiza-lo e novamente clique em editar;

![Screenshot_6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015125091/Screenshot_6.png)

6. Na janela que irá se abrir, altere o **Tamanho** do campo para 60 e clique em Salvar.

![Screenshot_7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015086852/Screenshot_7.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
