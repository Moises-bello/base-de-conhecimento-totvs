---
article_id: 235301627
category: Gestão de Armazenagem (WMS)
content_hash: b22996315866a4cc7b674d6d750790d9170fe1249beb638df599dcb7820a09d1
fetched_at: '2026-06-28T22:45:48.175109+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Serviços que o WMS disponibiliza e como
  funcionam
type: support-article
updated_at: '2025-10-31T20:04:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235301627-Log%C3%ADstica-Linha-Protheus-WMS-Servi%C3%A7os-que-o-WMS-disponibiliza-e-como-funcionam
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35447185046807)***Tempo aproximado para leitura:**00:03:00 min  
  
Dúvida**Quais os serviços que o **WMS - Warehouse Management System** disponibiliza e como funcionam?  
  
**Ambiente**  
TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (SIGAWMS) - A partir da versão 11.80.  
  
**Solução**No **WMS** existem alguns serviços considerados padrões e que devem ser utilizados para executar algumas operações no armazém. Estes serviços são descritos por funções que são executadas dentro do Sistema e que efetuam um determinado processamento dependendo de cada utilização.   
  
As funções são as seguintes:

1. **DLEndereca()** - Serviço para o endereçamento ou armazenamento de produtos.
2. **DLCrossDoc()** -  Serviço para o endereçamento ou armazenamento de produtos em áreas c*rossdocking*.
3. **DLApanhe()** - Serviço para a separação dos produtos.
4. **DLApanheVL()** - Serviço para a separação dos produtos com montagem de volumes.
5. **DLApanheC1()** - Serviço para a separação dos produtos priorizando áreas c*rossdocking*.
6. **DLApanheC2()** - Serviço para a separação dos produtos, com montagem de volumes e priorizando áreas c*rossdocking*.
7. **DLGxAbast()** - Serviço para gerar o reabastecimento manual ou automático.
8. **DLConferen()** - Serviço para a conferência cega de entrada ou saída. Processo em fase de obsolescência, substituído pelo **DLConfSai** ou **DLConfEnt**.
9. **DLConfSai()** - Serviço para a conferência cega de saída.
10. **DLConfEnt()** - Serviço para a conferência cega de entrada.
11. **DLTransfer()** - Serviço para a transferência entre endereços.
12. **DLDesfrag()** - Serviço para a desfragmentação de estoque.

É possível ainda cadastrar uma função específica que execute uma determinada ação no Sistema, gerando atividades que poderão ser executadas pelos usuário via convocação.  
  
Todo serviço **WMS** é sempre composto por duas partes que é, a geração e a execução das atividades, quando utilizado o processo de rádio frequência.   
  
Nem sempre na execução das atividades serão chamadas as mesmas funções que foram utilizadas para a geração, pois a execução da atividade convocada é baseada numa rotina de passos que devem ser executados pelo operador do coletor para realizar a mesma.  
  
Quanto ao processo de geração das atividades, toda integração com o **WMS** através de um serviço gera uma ordem de serviço, que pode ser executada de forma automática ou manual e que irá gerar as atividades de convocação para os usuários do coletor. Quando a execução for manual estes serviços deverão ser executados pela **Execução de Serviços** **- WMSA150** e poderão ser acompanhados pelo **Monitor de Serviços - WMSA332**.  
  
Quanto ao processo de execução das atividades quando utilizado rádio frequência, a partir do módulo **SIGAACD** **- Automação e Coleta de Dados**, é possível acessar a rotina de **Convocação WMS - WMSV001**, a qual irá distribuir as atividades para os operadores, redirecionando cada serviço para sua respectiva rotina de passos para a execução da atividade, bem como efetuar as movimentações de estoque, quando for o caso.  
  
Todo serviço **WMS** recebe sempre dois parâmetros padrões que são:

```
// lRadioF - Indicador que utiliza RF  
// cStatRF - Ponto de chamada, onde: 1 - Geração; 2 - Execução;  
Function DLEndereca(lRadioF,cStatRF)  
Local lRet := .T.  
Default lRadioF := (SuperGetMV('MV_RADIOF')=='S') //-- Como Default o parametro MV_RADIOF e verificado  
Default cStatRF := '1' //-- Como Default a radio frequencia VAI gerar movimentos  
   
   If !lRadioF .Or (lRadioF .And. cStatRF == '1')  
      ... // Processa as regras de endereçamento e gera as movimentações de estoque  
   ElseIf lRadioF .And. cStatRF == '2'  
      ... // Executa a movimentação de estoque  
   EndIf  
Return lRet
```

**Saiba mais**  
Assista ao *Webinar* sobre o cadastro **Serviços** **Vs** **Tarefas** e conheça todas as configurações disponíveis: [Webinar TOTVS | Serviços](https://www.youtube.com/watch?v=f1K8WBRCUUc) [Vs Tarefas #TOTVS\_Logística\_Linha\_Protheus](https://www.youtube.com/watch?v=f1K8WBRCUUc)
