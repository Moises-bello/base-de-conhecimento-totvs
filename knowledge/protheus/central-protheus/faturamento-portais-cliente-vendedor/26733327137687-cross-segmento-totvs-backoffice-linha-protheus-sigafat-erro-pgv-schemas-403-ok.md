---
article_id: 26733327137687
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 81991fcff648640063f19f3ecd8227a6c5214d62aab518b19b1c73541e4d8f57
fetched_at: '2026-06-28T22:38:23.856617+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - ERRO PGV Schemas:
  403 OK.'
type: support-article
updated_at: '2024-09-30T20:32:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26733327137687-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-ERRO-PGV-Schemas-403-OK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26733327089431) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Erro de Schemas: 403 OK no Portal de Gestão de Vendas  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26733370399639)  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.33;  
  
**Causa**O erro "Schemas: 403" pode ocorrer por algumas causas, como:  
  
1- Cache cheio do navegador (solução 1 - Limpeza Cache)  
2- Cache cheio do navegador (solução 2 Limpeza DevTools)  
3- Erro de usuário relacionado a login da filial  
 **Solução**Verifique e aplique as 3 soluções abaixo:  
  
**1- Limpeza de Cache  
1.1 -** Para solucionar o problema relacionado o cache (Solução 1) efetue a limpeza do cache de seu navegador.  
Para o Google Chrome  siga os seguintes passos:  
**1.2** No computador, abra o Chrome.  
**1.3** No canto superior direito, clique na opção  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/26733327093015) e Excluir dados de navegação.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26733370404119)  
**1.4** Escolha um intervalo de tempo, como Última hora ou Todo o período.  
**1.5** Selecione os tipos de informação que você quer remover.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26733370405911)  
  
**1.6** Clique em Excluir dados.  
Obs: Esse processo de limpeza de cookies e cache, pode variar conforme o navegador utilizado. (Acima foi descrito o processo para o Google Chrome)  
  
 **2- Limpeza de Cache Devtools**Outra ação de limpeza relevante, seria através do Devtools "Clear Set Data". (Solução 2) **2.1 -** Ao apresentar o erro no portal de Vendas, pressione a tecla F12 na tela do Browser  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26733370399639)  
  
**2.1** Será aberta a tela de ferramentas Devtools de seu navegador  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26733370406807)

**2.2** Selecione a opção **Aplication** > **Storage**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26733327099031)

**2.3** Marque a opção do Storage, principalmente a de Cookies e pressione a opção "Clear site data"  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26733370408343)  
  
 **3- Usuário cadastrado para filial  
3.1** Acesse o SIGACFG   
**3.2** Acesse através do menu **Usuário>Senha>Usuários  
3.3** Na aba de Restrições de Acesso, verifique se o usuário possui acesso à filial da qual está tentando efetuar o login no portal (conforme a sua configuração de filial do Mingle)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26733370409239)  
  
   
Saiba mais: [Portal Gestão de Vendas: Guia de Referência](https://tdn.totvs.com/x/M-yJIg)
