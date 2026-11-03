---
article_id: 360045281513
category: MDT - EPI
content_hash: aec9553b79f31b4df30a76c60de18813e021cd9ac677d3888db8885122d3a617
fetched_at: '2026-06-28T22:44:25.441683+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Entendendo o conceito do uso de Equipamento de
  Proteção Individual Genérico (EPI)
type: support-article
updated_at: '2025-07-29T17:55:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045281513-RH-Linha-Protheus-MDT-Entendendo-o-conceito-do-uso-de-Equipamento-de-Prote%C3%A7%C3%A3o-Individual-Gen%C3%A9rico-EPI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372358859159)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Entendendo o conceito do uso de Equipamento de Proteção Individual Genérico (EPI)  
Quando um Equipamento de Proteção Individual é definido como Genérico devemos utilizar o conceito de EPI Pai x EPI Filho.  
Explicação sobre o campo TN3\_GENERI  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Como pré condição deverá possuir os cadastros dos Fornecedores (**MATA020**) e Produto/epi (**MATA010**). É considerado um facilitador da rotina, não é obrigatório o uso deste conceito, apenas se for agilizar os cadastros e entregas de epis para a empresa.  
  
**Epi Pai** = Tem como objetivo generalizar determinados EPIs filhos.  
Exemplo: Bota  
  
Para cadastrar um EPI pai é necessário:  
  
Acessar a rotina de EPI x Fornecedor(**MDTA620**);

1. Selecionar um fornecedor;
2. Clicar em EPIs
3. Na aba, presente no campo inferior da tela, informar o código do EPI e, obrigatoriamente, selecionar a opção "2 - Sim" no campo "Genérico?" (TN3\_GENERI), conforme imagem abaixo:  
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061491154)  
    ****Epi Filho =****É aquele que serve de especificação de um EPI pai.  
   Exemplo: Bota M  
   **Obs**.: O exemplo acima serve para identificar uma bota de proteção tamanho M (Médio).  
     
   Para cadastrar um EPI Filho, é necessário:  
     
   1. Efetuar o passo a passo presente no **EPI PAI**
   2. Selecionar um Fornecedor;
   3. Clicar em Outras Ações > Grupos de Epis;
   4. Selecionar um EPI e, obrigatoriamente, um número referente ao Certificado de Aprovação, conforme imagem abaixo:  
        
      ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062394373)  
        
        
      A gestão de EPI se torna mais ágil, já que nas rotinas de: Epi X Funcao (**MDTA625**), Epi X C. Custo (**MDTA725**) e Epi X Tarefa (**MDTA626**), é possível selecionar apenas o EPI pai de forma que este representará seus respectivos EPI filhos. Em outras palavras, as configurações aplicadas ao EPI pai serão replicadas para seus EPIs filhos. Exemplo apresentado na imagem abaixo:  
        
      ![image2018-5-25_10-29-16.png](https://tdn.totvs.com/download/attachments/364907949/image2018-5-25_10-29-16.png?version=1&modificationDate=1527254832000&api=v2)  

      Uma vez cadastrados, é possível realizar a entrega de EPIs por meio da rotina de Funcionário X Epi (**MDTA695**) ou de Epi X Funcionário (**MDTA630**).  
        
      Ao selecionar a rotina que melhor atende sua necessidade, é possível a seleção do EPI pai para então identificar seus respectivos EPIs filhos, conforme imagem abaixo:  
        
      ![](https://tdn.totvs.com/download/attachments/364907949/image2018-5-25_8-40-49.png?version=1&modificationDate=1527248325000&api=v2)

      ![](https://tdn.totvs.com/download/attachments/364907949/image2018-5-25_9-51-21.png?version=1&modificationDate=1527252557000&api=v2)  
        
      Caso exista integração com o módulo de estoque (**SIGAEST**)  é necessário ativas os parâmetros (**MV\_NGMDTES e MV\_NG2SA**), a quantidade baixada será com relação à quantidade atual em estoque do EPI filho, desconsiderando a quantidade em estoque presente no cadastro do EPI pai, conforme imagem abaixo:  
        
      ![](https://tdn.totvs.com/download/attachments/364907949/image2018-5-25_9-42-4.png?version=1&modificationDate=1527252000000&api=v2)  

      **Obs**.: O saldo inicial dos EPIs BOTA, BOTA G, BOTA M, BOTA P, eram, respectivamente, 500, 100, 100, 100.  
        
      Na imagem identifica-se que, EPI pai (BOTA), permanece com seu respectivo saldo porém, os EPIs filhos sofreram a baixa do estoque.  
        
      **Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
      [Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
