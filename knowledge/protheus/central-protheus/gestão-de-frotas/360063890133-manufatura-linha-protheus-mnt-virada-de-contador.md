---
article_id: 360063890133
category: Gestão de Frotas
content_hash: 0ee2fe83e79d37b2a3c93644221055e22b04120f62eb03b673b3f5588a5ee8dc
fetched_at: '2026-06-28T22:42:39.626117+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Virada de Contador
type: support-article
updated_at: '2021-08-31T11:14:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063890133-Manufatura-Linha-Protheus-MNT-Virada-de-Contador
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:40 min****Dúvida**Como funciona a **Virada de Contador** na rotina de **Informa Contador - MNTA830**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas – Versão 12  
  
**Solução**Primeiramente é necessário compreender o que é **Virada de Contador** e a **diferença** entre **posição**e **acumulado**:  
  
**Virada de Contador**  
Todo bem com contador próprio tem um limite de dígitos a ser apresentado no dispositivo de medição - quantidade máxima de números possíveis para visualizar no dispositivo **Limite Contador - T9\_LIMICON**, desta forma quando chegar ao seu limite ocorre o que chamamos de virada.  
**Exemplo**

| Bem | Pos. Contador | Cont. Acum. | Limite Cont. |
| --- | --- | --- | --- |
| BEM001 | 500 | 500 | 999.999 |

Imaginamos que este bem, já possua em seu **Histórico de contador - STP/TPP** e atualmente está com a posição do contador em 999.800. Seguindo nesta linha, no dia seguinte a esta medição, observa-se que no dispositivo lê-se a informação 20. Isto significa que ocorreu uma virada de contador, ou seja, chegou a seu limite máximo.  
  
**Posição do Contador**  
Corresponde a informação apresentada no dispositivo de medição do bem, informação visual e medida em um determinado momento. Como trata-se de um equipamento e o mesmo poderá sofrer quebras/viradas. Quando ocorrer uma quebra, corresponde apenas a alteração da posição do contador e nunca alteração do acumulado.  
  
**Contador Acumulado**Corresponde a somatória dos apontamentos medidos no bem. Esta informação sempre terá um crescimento cronológico, nunca podendo regredir.  
  
**Informa - MNTA830**Programa de atualização da posição do contador do bem. Caso o bem selecionado seja **Bem Pai** de estrutura, todos os filhos que são controlados por contador também serão atualizados. São atualizados campos de **Acumulação**, **Datas** e **Variação/dia**. Cada informação de contador confirmada irá gerar um registro de reporte de contador do arquivo **Histórico do Contador - STP**.  
  
**Informa / Outras Ações / Virada**Através do botão **Virada** o usuário poderá informar ao Sistema que o contador do veiculo sofreu uma virada, quer dizer que o **hodômetro** físico do veiculo chegou a seu limite, zerou e iniciou novamente a contagem. O único ponto do Sistema que aceita o contador menor com data maior é através desta tela e do botão **Virada**.  
  
**Importante**Para calcular a contador acumulado, ele o Sistema busca o **Limite de Contador -T9\_LIMICON** e soma com o contador informado **Virada**.  
O valor de contador informado na **Virada** passa a ser a posição do contador do bem.  
Para melhor entendimento, segue exemplo abaixo:  
  
**Cadastro do bem**

| Bem | Pos. Contador | Cont. Acum. | Limite Cont. |
| --- | --- | --- | --- |
| BEM001 | 500 | 500 | 999.999 |

**Realizar a Virada**

| Bem | Contador 1 | Hora Leitura |
| --- | --- | --- |
| BEM001 | 1 | 18:00 |

**Verificar cadastro do Bem**

| Bem | Pos. Contador | Cont. Acum. | Limite Cont. |
| --- | --- | --- | --- |
| BEM001 | 1 | 1.000.000 | 999.999 |
