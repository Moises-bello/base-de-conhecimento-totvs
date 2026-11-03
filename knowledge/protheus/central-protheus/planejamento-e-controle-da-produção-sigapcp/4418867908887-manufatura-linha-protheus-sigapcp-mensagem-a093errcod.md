---
article_id: 4418867908887
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d25fa510f7fc868d03636a13db1443b786003a431b96c0f1355fe6e9745adcd2
fetched_at: '2026-06-28T22:42:43.572822+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A093ERRCOD
type: support-article
updated_at: '2022-01-20T10:46:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418867908887-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A093ERRCOD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:15 min****Ocorrência**Ao tentar disponibilizar uma família de produtos para uso no **MATA093 - Configurador de produtos**, é apresentada a mensagem **A093ERRCOD - Alguma característica foi omitida na expressão do código do produto**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem ocorre quando é determinado que o produto ao ser criado não terá o código formado pelo padrão do Sistema, campo **BP\_CODPAD - Código padrão** possui o conteúdo **N.** Neste caso é especificada na tela **Descrição** como o código é formado, porém na especificação do código não constam todas as características da família de produto.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Com a família seleciona no *browse* do **MATA093**, clique em **Outras Ações > Descrição**;  
2. No campo **BP\_ESTCOD - Resultado - estrutura do código**, adicione todas as características da família, elas são apresentadas no campo **cVariavel - Variavel** e podem ser adicionadas através do botão **Adicione**;  
3. Ao concluir a inclusão de todas as característica, disponibilize novamente para uso através do campo **BP\_DISPUSO - Disponível p/ uso** com o conteúdo **S**.
