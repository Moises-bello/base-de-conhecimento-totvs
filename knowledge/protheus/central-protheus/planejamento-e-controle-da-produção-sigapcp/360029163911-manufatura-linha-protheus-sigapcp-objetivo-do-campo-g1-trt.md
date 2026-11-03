---
article_id: 360029163911
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: bdcb9b718a5f4b1562fd4ded4a2d8766c3da2340aa8db4b485113110d7c56b72
fetched_at: '2026-06-28T22:42:44.666008+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Objetivo do campo G1_TRT
type: support-article
updated_at: '2021-08-20T17:58:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029163911-Manufatura-Linha-Protheus-SIGAPCP-Objetivo-do-campo-G1-TRT
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:01:45 min****Dúvida**Qual o objetivo do campo **G1\_TRT - Sequencia** no **MATA200 - Estrutura**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Este campo permite que seja incluído mais de uma vez o mesmo componente no mesmo nível da estrutura.  
Essa possibilidade é importante quando o cliente utiliza o recurso **Operação x Componente**, no qual ele destaca em qual operação determinado componente deverá ser consumido, e assim, ao apontar a operação em questão o Sistema realiza o consumo do material indicado.  
Neste caso, como um mesmo produto pode ser consumido em diversos momentos será necessário cadastrar o mesmo componente conforme o número de operações em que o mesmo será consumido e nas quantidades de cada operação.  
  
**Exemplo**Na produção de um determinado produto são necessários 20 unidades do componente parafuso.  
Poderia cadastrar uma vez esse componente na estrutura com a quantidade 20, ou caso queira utilizar o recurso **Operação x Componente**, informar quanto é consumido do componente em questão em cada operação.  
Neste caso, pode ter três registros no **MATA200** para o mesmo componente com quantidades diferentes, conforme o consumo do componente em cada operação, e deste modo é obrigatório que cada registro possua o campo **G1\_TRT** preenchido com uma informação diferente.  
  
Então poderíamos ter os seguintes resultados:

|  |  |  |
| --- | --- | --- |
| Componente | Quantidade | Sequencia |
| Parafuso | 20 |  |

ou

|  |  |  |
| --- | --- | --- |
| Componente | Quantidade | Sequencia |
| Parafuso | 10 | 01 |
| Parafuso | 07 | 02 |
| Parafuso | 03 | 03 |

No caso acima, após registrar a estrutura será necessário vincular cada registro a uma operação cadastrada no **MATA632 - Roteiro de Operação** para que o Sistema faça a requisição ao apontar a operação correspondente.
