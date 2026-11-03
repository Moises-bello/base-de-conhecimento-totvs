---
article_id: 39763890515479
category: Movimento
content_hash: 688efdf9be61f0dd7536700e38f1bc3c8796e779033d8ee749dc887815c05431
fetched_at: '2026-06-28T22:46:36.045541+00:00'
product: rm
section_id: 1500000861602
source: central-rm
title: RH - RM - PTO - Erro FOREIGN KEY FKABANCOHORFUNDETALHE_AEVECALC na transferência
  de funcionário
type: support-article
updated_at: '2026-04-15T18:00:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39763890515479-RH-RM-PTO-Erro-FOREIGN-KEY-FKABANCOHORFUNDETALHE-AEVECALC-na-transfer%C3%AAncia-de-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39763874433047) Tempo aproximado para leitura: **00:00:30 min**  
  
**Ocorrência**  
Ao realizar o processo de transferência de funcionário entre coligadas, o sistema apresenta a seguinte mensagem de erro: "Houve um erro de incompatibilidade de informações entre as coligadas, não foi encontrado o código na coligada destino. The INSERT statement conflicted with the FOREIGN KEY constraint "FKABANCOHORFUNDETALHE\_AEVECALC". The conflict occurred in database "CorporeRM", table "dbo.AEVECALC". The statement has been terminated."  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Causa**  
O erro ocorre porque o processo de transferência exige a paridade de configurações entre a coligada de origem e a de destino. Especificamente, os eventos (códigos de cálculo) vinculados ao Sindicato no módulo Automação de Ponto devem existir com a mesma codificação em ambas as coligadas. A inconsistência na tabela **AEVECALC** indica que o sistema tentou inserir um registro de banco de horas referenciando um evento que não foi localizado na coligada de destino.

**Passos**

1. Acesse a coligada de **origem** e identifique o Sindicato vinculado ao funcionário;
2. Verifique todos os eventos (códigos de cálculo) configurados para este Sindicato no módulo de Automação de Ponto;
3. Acesse a coligada de **destino** e valide se os mesmos códigos de eventos estão cadastrados e configurados no Sindicato correspondente;
4. Caso algum evento esteja ausente na coligada de destino, realize o cadastro do mesmo com o código idêntico ao da origem;
5. Após equalizar os cadastros de eventos entre as coligadas, realize o processo de transferência novamente.

**Saiba mais**  
[RH - RM - PTO - Cadastrar eventos para cálculo do ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025095672-RH-RM-PTO-Cadastrar-eventos-para-c%C3%A1lculo-do-ponto)  
[RH - RM - PTO - Cópia de Sindicato entre coligadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044450933-RH-RM-PTO-C%C3%B3pia-de-Sindicato-entre-coligadas)  
[RH - RM - PTO - Cópia de parâmetros dos Sindicatos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044450373-RH-RM-PTO-C%C3%B3pia-de-par%C3%A2metros-dos-Sindicatos)
