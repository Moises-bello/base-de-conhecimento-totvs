---
article_id: 8503344656791
category: RH - CNAB
content_hash: ba539cbeb75ab908ffb90477de54d53249b49d0b5bb4eda51feb4fbee1eb5551
fetched_at: '2026-06-28T22:43:39.279027+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: 'RH - Linha Protheus - GPE - GPEM080: Existe um erro na fórmula digitada: Function
  day: GRAVADATA(MV_PAR20,'
type: support-article
updated_at: '2025-06-17T12:24:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8503344656791-RH-Linha-Protheus-GPE-GPEM080-Existe-um-erro-na-f%C3%B3rmula-digitada-Function-day-GRAVADATA-MV-PAR20
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32866848199191) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Geração de líquidos presenta a mensagem: Existe um erro na fórmula digitada: Function day: GRAVADATA(MV\_PAR20,  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.

**Solução**

O erro apresentado refere-se á uma fórmula dentro do arquivo de configuração para gravação da data de crédito, devido à busca do antigo campo do grupo de perguntas da rotina data de Crédito MV\_PAR20 (GPEM080R1).  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8503324367383)Será necessário ajustar o arquivo considerando a alteração do novo grupo de perguntas GPEM080R2 e tornando o MV\_PAR usado por um correspondente. Exemplo:  **MV\_PAR20 (GRUPO GPEM080R1) = MV\_PAR14 (GRUPO GPEM080R2).**Para realizar o comparativo em um outro campo, pode-se acessar a tabela SX1 via APSDU e observar os dois grupos GPEM080R1(antigo) e GPEM080R2, de modo que seja possível identificar qual o X1\_VAR01 foi usado no momento da configuração do arquivo e qual deverá ser usado após alteração do grupo de perguntas da rotina GPEM080.

[RH - Linha Protheus - GPE -](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5719944484759-RH-Linha-Protheus-GPE-Editar-Layout-CNAB-Pr%C3%A9-definido-atrav%C3%A9s-do-Wizard-CNAB-CFGX049a-SIGACFG-) [Editar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5719944484759-RH-Linha-Protheus-GPE-Editar-Layout-CNAB-Pr%C3%A9-definido-atrav%C3%A9s-do-Wizard-CNAB-CFGX049a-SIGACFG-) [Layout CNAB Pré definido através do Wizard CNAB (CFGX049a -](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5719944484759-RH-Linha-Protheus-GPE-Editar-Layout-CNAB-Pr%C3%A9-definido-atrav%C3%A9s-do-Wizard-CNAB-CFGX049a-SIGACFG-) [SIGACFG)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5719944484759-RH-Linha-Protheus-GPE-Editar-Layout-CNAB-Pr%C3%A9-definido-atrav%C3%A9s-do-Wizard-CNAB-CFGX049a-SIGACFG-)

**Saiba Mais:**  
[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
