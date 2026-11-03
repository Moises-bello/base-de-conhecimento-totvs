---
article_id: 5399434378391
category: MDT - EPI
content_hash: ea4b994e05d0bbee32a917bc023f1df5c762d94e21cea3a8945756a62cb321fb
fetched_at: '2026-06-28T22:44:25.270205+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - A configuração do parâmetro está incorreta. O parâmetro
  deve ser preenchido com um código válido para requisição ou devolução
type: support-article
updated_at: '2025-03-12T20:54:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5399434378391-RH-Linha-Protheus-MDT-A-configura%C3%A7%C3%A3o-do-par%C3%A2metro-est%C3%A1-incorreta-O-par%C3%A2metro-deve-ser-preenchido-com-um-c%C3%B3digo-v%C3%A1lido-para-requisi%C3%A7%C3%A3o-ou-devolu%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25582421550359) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao fazer entrega ou devolução de EPI ocorre os avisos:   
"A configuração do parâmetro está incorreta. O parâmetro deve ser preenchido com um código válido para **requisição**".  
"A configuração do parâmetro está incorreta. O parâmetro deve ser preenchido com um código válido para **devolução**".  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**O aviso ocorre devido ao preenchimento dos códigos **499** e **999** em parâmetros do **SIGAMDT**.   
O códigos de movimentação interna do estoque **499** e **999** são de uso exclusivo e interno do sistema. Eles representam respectivamente uma entrada e uma saída padrão, e não podem ser utilizados nos parâmetros **MV\_NG2D3RE** e **MV\_NG2D3DE** quando existe integração com o estoque.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**Configuração movimentação de Requisição**  
1. Acesso o modulo SIGAEST (04) no caminho: atualizações > cadastros > movimentações > internas (MATA230);  
2. Clique em incluir para **Requisição (Saída)** o cadastro da movimentação deve ter maior que **500** e não pode ser utilizado o código **999**;  
  
Exemplo  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5398937840535)  
  
3. No modulo configurador (SIGACFG) acesse o caminho: ambiente > cadastros > parâmetros;  
4. Pesquise pelo parâmetro **MV\_NG2D3RE**e informe o mesmo código utilizado no cadastro do tipo de movimentação **Requisição**.  
  
Exemplo  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5399270416791)  
  
**Configuração movimentação de Devolução**  
1. Acesso o modulo SIGAEST (04) no caminho: atualizações > cadastros > movimentações > internas (MATA230);  
2. Clique em incluir para **Devolução (Entrada)** o cadastro da movimentação deve ter menor ou igual a **500**, e não pode ser utilizado o código **499**;  
  
Exemplo  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5399017161239)  
  
3. No modulo configurador (**SIGACFG**) acesse o caminho: ambiente > cadastros > parâmetros;  
4. Pesquise pelo parâmetro **MV\_NG2D3DE** e informe o mesmo código utilizado no cadastro do tipo de movimentação **Devolução**.  
  
Exemplo  
**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5399231633431)  
  
Observação**Essas são orientações básicas para inclusão ou devolução de **EPI** no **SIGAMDT** sem que ocorra o aviso nos casos que a empresa faz a integração com o estoque. Para orientações sobre os demais campos na rotina movimentação interna (**MATA230**) dentro to estoque abra um ticket para o atendimento de **estoque/custos** (SIGAEST) com a sua duvida sobre a configuração ou regra de utilização.  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
