---
article_id: 360004253171
category: RH - Relatórios
content_hash: fc74a52e760ce0cdf63da3190c2e2b85de73772976f85cee5cdd03affddfbc17
fetched_at: '2026-06-28T22:44:43.498573+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Como imprimir o Espelho de Ponto
type: support-article
updated_at: '2025-06-13T17:24:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004253171-RH-Linha-Protheus-PON-Como-imprimir-o-Espelho-de-Ponto
---

**Dúvida**Como imprimir o Espelho de Ponto individualmente ou em lote.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Para impressão do Espelho de Ponto, acesse a rotina **Relatórios > Mensais > Espelho de Ponto.**  
Para que o espelho seja impresso corretamente, o usuário deve validar a **Troca de Turno,** realizar a **Leitura/Apontamento** das marcações, realizar todas as manutenções necessárias e processar o **Cálculo Mensal** para consolidar todos os ajustes.  
  
Nos parâmetros, se a pergunta **Eventos do Resultados** estiver como **Sim**, o relatório exibe as **verbas dos Resultados no rodapé** do Espelho de Ponto. Segue um exemplo abaixo:  
  
Resultados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221521175319)  
  
Parâmetros para geração do Espelho de Ponto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19206172688151)  
  
Espelho de Ponto com as verbas no rodapé:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221521178647)  
  
Cabe ressaltar que a rotina de Resultados mostra os lançamentos em **Centesimal**.  
  
Se a pergunta **Eventos do Resultados** estiver como **Não**, o relatório exibe os apontamentos do período no rodapé do Espelho de Ponto. Segue um exemplo abaixo:  
  
Parâmetros para geração do Espelho de Ponto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19206172704663)  
  
Espelho de Ponto com os Apontamentos do período:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221545399959)  
  
Para emitir o espelho d eponto com a seção banco de horas e as movimentações precisará utilizar a opção "Imprime Banco de Horas" ? igual à 'Sim', veja:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26093137005335)

Para a coluna de**“Absent**.” O sistema verifica o cadastro de eventos em Atualizações / Cadastro Ponto / Eventos, tabela SP9, aba Geral**, campo Classific. “P9\_CLASEV**, as opções são:

**02-Falta**

**03-Atraso**

**04-Saída no expediente**

**05-Saída antecipada**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31742311013527)  
  
Apresentará a seção como no exemplo abaixo no rodapé do espelho:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26093149221655)  
  
Importante:** o rodapé com as verbas ou apontamentos só é exibido quando o Espelho de Ponto é impresso para o **Período de Apontamento completo**, por exemplo: período de 01 à 30.09.2023. Se o usuário imprimir o Espelho com datas de 01 à 15.09, o relatório é gerado parcialmente, porém, sem nenhuma informação no rodapé.Para impressão de **Espelhos de Ponto de períodos abertos**, é necessário que a data base do Protheus esteja no último dia do Período de Apontamento, ou seja, se o período for de 01 à 30.09.2023, a data base deve estar no dia 30.09.2023.  
  
Para **períodos já fechados,** a data base não é validada.  
  
Por fim, é **indispensável** que exista um registro de **Troca de Turno** com o primeiro dia do Período de Apontamento que está utilizando para impressão do relatório, caso contrário, o relatório não poderá ser impresso.  
Por exemplo, se está tentando gerar o Espelho de Ponto do período de 01 à 30.09.2023, deve existir registro de **Troca de Turno** com a data de **01.09.2023**, mesmo que o funcionário não tenha tido efetivamente uma troca de Turno/Sequência/Regra de Apontamento.  
O registro é necessário para a correta montagem do calendário mensal do Período.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19206188904343) **Saiba mais:**[RH - Linha Protheus - PON - Espelho de Ponto de acordo com a Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9324927169559-RH-Linha-Protheus-PON-Espelho-de-Ponto-de-acordo-com-a-Portaria-671)[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
