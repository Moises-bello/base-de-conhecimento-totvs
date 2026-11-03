---
article_id: 360013246451
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 406a9b68f37a59f1487413294809bd698549f36877feb135f22687975abe0bb7
fetched_at: '2026-06-28T22:42:43.625324+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A680QUANT
type: support-article
updated_at: '2022-02-07T14:19:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013246451-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A680QUANT
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:15 min  
  
Ocorrência**Ao realizar o apontamento através da rotina **MATA680 - Apontamento Modelo I** ou **MATA681 - Apontamento Modelo II** é apresentada a mensagem **A680QUANT**.  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - A partir da versão 11.80  
  
**Causa**  
A mensagem ocorre quando a quantidade da operação apontada está maior que a quantidade da operação anterior.  
  
**Solução**  
A mesma será apresentada dependendo da configuração do parâmetro, no **F12** da rotina de apontamento modelos 1 e 2: **MATA680/MATA681**, chamado **Verif. Sld. Oper. Anterior?**.  
Abaixo segue o exemplo do comportamento do Sistema utilizando cada um dos parâmetros:  
  
Temos uma **OP - Ordem de Produção** de 100 unidades de um produto que possui 02 operações, e realizamos um apontamento de 50 unidades com 10 unidades de perda da operação 01;

* Com o parâmetro **Produção+Perda**, só permitirá o apontamento de 60 unidades;
* Com o parâmetro **Produção-Perda**, só permitirá o apontamento de 50 unidades;
* Com o parâmetro **Não verifica**, o Sistema não faz nenhuma validação e permite o apontamento.

Diante desta regra será necessário analisar os apontamentos realizados para que consiga prosseguir com o novo apontamento.
