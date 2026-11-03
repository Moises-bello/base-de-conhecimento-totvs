---
article_id: 4405251779223
category: PMS - Dúvidas Gerais
content_hash: 33c815fc905959dcf720392b3131e5a1c4e270e299aef42219d6f3b47b08413f
fetched_at: '2026-06-28T22:37:17.735194+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - PMS - Mudar Formato do
  Código da Tarefa
type: support-article
updated_at: '2025-01-10T20:00:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405251779223-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-PMS-Mudar-Formato-do-C%C3%B3digo-da-Tarefa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Como alterar o formato do código da tarefa no PMS?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Projetos - Todas as versões  
  
**Causa**O parâmetro **MV\_PMSECOD** esta preenchido para mostrar o campo como estruturado, você pode alterar para mostrar como sequencial.  
  
**Solução**O parâmetro **MV\_PMSECOD** indica o método de codificação automática utilizado na inclusão de EDTs/Tarefas.

**1= Estruturado:** método que utiliza uma máscara (definida no cadastro de orçamento/projeto ) para  
estruturação dos níveis do projeto .

* Exemplo:  
  Máscara: 234 Delimitador :
  + Estrutura  
    01 – Fundações  
    01.01 – Fundação Prédio 1  
    01.01.001 – Escavação  
    01.01.002 – Limpeza  
    01.02 – Fundação Prédio 2  
    01.02.001 – Escavação  
    01.02.002 – Limpeza

**2 = Sequencial**: método que utiliza código sequencial único para codificação das EDTs e Tarefas.

* Estrutura  
  0000001 – Fundações  
  0000002– Fundação Prédio 1  
  0000003– Escavação  
  0000004– Limpeza  
  0000005– Fundação Prédio 2  
  0000006– Escavação  
  0000007– Limpeza...  
    
  OBS:   
  Para realizar o posicionamento sequencial das  EDT e tarefas , o cursos deve estar posicionado na EDT/Tarefa de origem.   
    
  Exemplo:  
  Ao posicionarmos o cursor na EDT 01 , a mesma seguira a sequencia proposta sendo a próxima tarefa vinculada a essa EDT e continuando o sequencial de 01.01 , conforme imagem abaixo:  
    
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9554128376855)  
    
  Ao incluirmos uma nova tarefa , realizamos no mesmo posicionamento de origem (01) , para prosseguir com a próxima sequencia 01.02.
