---
article_id: 20052539241879
category: Financeiro
content_hash: 5aa1b23ffe53b3829ddedb4f4226d31301216a4f4da84e113ab336903ad5a0a2
fetched_at: '2026-06-28T22:38:03.241347+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR150 - Código da
  natureza apresentado incorretamente
type: support-article
updated_at: '2023-12-22T11:30:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20052539241879-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR150-C%C3%B3digo-da-natureza-apresentado-incorretamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20052549405975) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**O relatório FINR150 está exibindo o código da natureza de forma incorreta mesmo no layout padrão.  
Está aplicando um pontos a mais. Exemplo:   
  
Cadastro do código da natureza:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20052549406231)

No relatório FINR150 está exibindo da seguinte forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20052549406487)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**O erro ocorre por conta da configuração do parâmetro MV\_MASCNAT. Por padrão, o conteúdo vem preenchido com a informação: 19  
O objetivo deste parâmetro é facilitar a identificação das naturezas nas consultas e relatórios do sistema, onde é definido uma máscara que é, na verdade, o formato para apresentação dos códigos de identificação das naturezas.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o módulo configurador;  
2. No menu do lado esquerdo, acesse Ambiente - Cadastros - Parâmetros e procure por MV\_MASCNAT;  
3. Deixe o conteúdo do parâmetro vazio;  
4. Ao imprimir novamente o relatório, apresentará a informação da natureza corretamente, conforme o cadastro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20052539236503)

**Saiba mais:**  
[Naturezas - FINA010](https://tdn.totvs.com/display/public/PROT/Naturezas+-+FINA010+-+Financeiro+-+P12)
