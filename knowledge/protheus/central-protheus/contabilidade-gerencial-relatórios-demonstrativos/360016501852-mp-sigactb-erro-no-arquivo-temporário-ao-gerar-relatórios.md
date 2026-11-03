---
article_id: 360016501852
category: Contabilidade Gerencial - Relatórios Demonstrativos
content_hash: ec9072a12b24357debe63890a1c306e9846d9bfedd907aa7f1ae39eda861f12f
fetched_at: '2026-06-28T22:40:38.917005+00:00'
product: protheus
section_id: 1500001548882
source: central-protheus
title: 'MP - SIGACTB - Erro no arquivo temporário ao gerar relatórios '
type: support-article
updated_at: '2021-04-28T15:25:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016501852-MP-SIGACTB-Erro-no-arquivo-tempor%C3%A1rio-ao-gerar-relat%C3%B3rios
---

**Ocorrência**

* Erro apresentado ao emitir Relatório

Alias already in use: CARQTMP  
 on FWOPENTEMP(CRIATRAB.PRG)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012743272/mceclip0.png)

**Ambiente**  
Protheus  – Contabilidade  – A partir da versão 11.80  
   
 **Causa**

* Erro no arquivo temporário

**Solução**

* Atualize Lib, Build e Binário
* Para solucionar essa ocorrência, realize os seguintes passos:  
    
  **Passo 1 -** Realize o Filtro do erro apresentado no exemplo citado é "FWOPENTEMP"  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012744032/mceclip1.png)  
     
    
  **Passo 2 -** Dessa forma é possívelencontrar "STACK FWOPENTEMP(CRIATRAB.PRG)**"** onde o erro esta sendo apresentado
* Veja que o erro esta sendo apresentado no arquivo temporário (cArqTmp) " \_SC14 "  
    
  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012746271/mceclip2.png)**  
    
  **Passo 3**.
* Acesse a pasta System
* Realize um backup e delete os arquivos temporários criados
* excluir o arquivo  \_\_SC14.tmp

Veja mais :

[MP - SIGACTB - CTBA102: on FWOPENTEMP(CRIATRAB.PRG)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006664312-MP-SIGACTB-CTBA102-on-FWOPENTEMP-CRIATRAB-PRG-?source=search)

[Arquivos e Índices Temporários](http://tdn.totvs.com/pages/viewpage.action?pageId=23888863)

[Criatrab- Retorna arquivo de trabalho](http://tdn.totvs.com/display/public/PROT/Criatrab-+Retorna+arquivo+de+trabalho)

[Criando Arquivo Temporário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020440451-MP-SIGACTB-CTBR040-Criando-Arquivo-Tempor%C3%A1rio?source=search)

[CARQTMP -ARQUIVO TEMPORÁRIO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016507572-MP-SIGACTB-CARQTMP-ARQUIVO-TEMPOR%C3%81RIO?source=search)
