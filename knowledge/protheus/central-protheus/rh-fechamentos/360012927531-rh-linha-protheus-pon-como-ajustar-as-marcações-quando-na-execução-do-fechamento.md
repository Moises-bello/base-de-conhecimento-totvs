---
article_id: 360012927531
category: RH - Fechamentos
content_hash: 2699b322497ffeee2fd8f256561845e3989c1d187dd84a1369ea0ad55dc8cc4d
fetched_at: '2026-06-28T22:44:48.836894+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Como ajustar as marcações quando na execução do
  Fechamento Mensal, apresentar log de marcações ímpares
type: support-article
updated_at: '2025-06-13T17:57:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012927531-RH-Linha-Protheus-PON-Como-ajustar-as-marca%C3%A7%C3%B5es-quando-na-execu%C3%A7%C3%A3o-do-Fechamento-Mensal-apresentar-log-de-marca%C3%A7%C3%B5es-%C3%ADmpares
---

**Dúvida**Como ajustar as marcações quando na execução do Fechamento Mensal, apresentar *log* de marcações ímpares?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução** **Em alguns casos**, acessando em **Atualizações-Lançamentos-Marcações ou Integrados,** conseguirá ajustar cada batida do dia que está com a inconsistência demonsrada em fechamento. Em uma das rotinas, seja de Marcações ou Integrados. Sendo assim, inclua ou exclua uma marcação para ajustar com quantidade par neste dia. Efetuando a manutenção e incluindo a batida com a devida justificativa, completando o dia com entrada/saída e assim realizando o apontamento. Após isto, salve para gravar os ajustes.  
  
Em outros casos, **não sendo possível verificar diretamente nas rotinas citadas acima**, ou seja, ao acessar as marcações, aparentemente está tudo em quantidade par. Deverá validar os registros na tabela de marcações se estão ok. Por muitas vezes já ocorreram leituras de marcações dentro do período configurado no MV\_PONMES e por alguma necessidade pós realização de leitura há alteração do período de apontamento. Onde não recomendamos alterações neste cenário, veja mais na documentação:  
[RH - Linha Protheus - PON - Alteração de Período de Apontamento após ter efetuado leitura das marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058115614-RH-Linha-Protheus-PON-Altera%C3%A7%C3%A3o-de-Per%C3%ADodo-de-Apontamento-ap%C3%B3s-ter-efetuado-leitura-das-marca%C3%A7%C3%B5es)  
  
Caso ainda assim foi o caso, segue abaixo algumas orientações:  
  
Inicialmente, consulte e faça um filtro na matrícula no dia que demonstrou inconsistência da marcação ímpar, após verifique se:  
- O campo **P8\_ORDEM** está devidamente preenchido com a ordem daquele dia dentro do período de apontamento completo;  
- O campo **P8\_APONTA** está com o conteúdo S em todas as marcações. Se houver alguma marcação com N, poderá excluir o registro;  
- O campo **P8\_PAPONTA** está corretamente preenchido em todas as marcações. Este campo refere-se ao período de apontamento completo;  
- Os campos **P8\_DATA e P8\_DATAAPO** estão preenchidos.  
  
Após todas as verificações e ajustes devidos, executar a rotina de Fechamento Mensal novamente.  
  
**Saiba Mais**  
[Manual do ponto eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
