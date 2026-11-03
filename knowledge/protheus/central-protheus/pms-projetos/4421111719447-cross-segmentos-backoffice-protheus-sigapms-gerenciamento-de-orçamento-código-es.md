---
article_id: 4421111719447
category: PMS - Projetos
content_hash: 6b15e78175462f815b9a8a4cf171fc33f91a71293b767675a6700a082f9a4a7d
fetched_at: '2026-06-28T22:37:15.206484+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Gerenciamento de Orçamento
  - Código Estruturado
type: support-article
updated_at: '2024-03-21T13:48:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421111719447-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Gerenciamento-de-Or%C3%A7amento-C%C3%B3digo-Estruturado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22236730784151) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

O que é Código Estruturado ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as Versões

**Solução**

O código estruturado é utilizado para organizar a codificação do orçamento. Para ele pode ser definido um separador (ponto, traço, etc.) e deve ser definida a máscara (o número de dígitos para cada nível).   
Veja o seguinte exemplo para uma máscara “213” (dois dígitos para o primeiro nível, um para o segundo   
e três para o terceiro) com o ponto como separador:

![C_digo_Estruturado.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421111491991)

O que determina a visualização e estruturação é o MV\_PMSECOD : Indica o método de codificação automática utilizado na inclusão de EDTs/Tarefas.

**1= Estruturado:** método que utiliza uma máscara (definida no cadastro de orçamento/projeto) para estruturação dos níveis do projeto. Exemplo:  
Máscara: 234 Delimitador :   
Estrutura  
01 – Fundações   
01.01 – Fundação Prédio 1  
01.01.001 – Escavação  
01.01.002 – Limpeza  
01.02 – Fundação Prédio 2  
01.02.001 – Escavação  
01.02.002 – Limpeza  
**2 = Sequencial:** método que utiliza código sequencial único para codificação das EDTs e Tarefas.  
Estrutura  
0000001 – Fundações   
0000002– Fundação Prédio 1  
0000003– Escavação  
0000004– Limpeza  
0000005– Fundação Prédio 2  
0000006– Escavação  
0000007– Limpeza...
