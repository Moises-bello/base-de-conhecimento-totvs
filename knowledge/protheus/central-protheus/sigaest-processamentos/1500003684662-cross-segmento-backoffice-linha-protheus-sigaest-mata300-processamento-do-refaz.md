---
article_id: 1500003684662
category: SIGAEST - PROCESSAMENTOS
content_hash: 2def9526af31f613cde3cc4fa83371030cb00741775e5122453f7de7adc34004
fetched_at: '2026-06-28T22:39:04.969164+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - Processamento
  do Refaz Saldos via EXECAUTO
type: support-article
updated_at: '2025-07-31T14:48:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003684662-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Processamento-do-Refaz-Saldos-via-EXECAUTO
---

O artigo aborda a execução da rotina MATA300 no sistema TOTVS Protheus, utilizada para recalcular saldos de estoque com base em movimentos. A execução pode ser feita em modo automático (EXECAUTO) ou via Job, com a possibilidade de ser realizada enquanto o sistema está em uso ou em modo exclusivo, controlado pelo parâmetro MV\_CUSTEXC. O artigo destaca a importância de preparar o ambiente e oferece um exemplo de código para execução da rotina, além de links para mais informações sobre agendamento e execução de rotinas no sistema.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33847852509975) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como executar a rotina `MATA300 - Refaz Saldos` via execução automática (`EXECAUTO`) ou Job?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**  
A rotina **MATA300** tem como finalidade recalcular os saldos de estoque com base nos movimentos (entradas, saídas e movimentações internas), reconstruindo saldos iniciais e finais em quantidade e valor para cada produto.

### **Importante**

|  |
| --- |
| O comportamento da rotina é controlado pelo parâmetro `MV_CUSTEXC`:   * `MV_CUSTEXC = "N"` → Permite execução com o sistema em uso por outros usuários. * `MV_CUSTEXC = "S"` → Exige execução em modo exclusivo (recomendado).   Esta rotina pode ser executada com o sistema em uso por todos os usuários. Nesse caso, as movimentações que estejam acontecendo simultaneamente ao cálculo podem influenciar no resultado. Para que a rotina seja executada dessa forma o parâmetro MV\_CUSTEXC deve estar com o conteúdo igual a "N".  Outra forma de execução (mais segura) é com o sistema em modo exclusivo, sem outros usuários utilizando os arquivos necessários ao cálculo. Para que a rotina seja executada dessa forma, o parâmetro MV\_CUSTEXC deve estar com o conteúdo igual a "S'. |

|  |
| --- |
| **Parâmetros** **Nome:** PARAMIXB **Tipo:** Lógico **Descrição:** Define se a execução será em modo batch (`.T.`) ou interativo (`.F.`). **Obrigatório:** Sim |
| **Programa Fonte** `MATA300.PRX` **Sintaxe** `MATA300(PARAMIXB) -- Nil` **Retorno** `Nil` (sem retorno direto; efeitos visíveis nos saldos recalculados) |

**Observações**

* É possível executar via rotina customizada usando `MSExecAuto`.
* É obrigatório preparar o ambiente com `PREPARE ENVIRONMENT`.

**Exemplo:**

```
#include "rwmake.ch"
#include "TbiConn.ch"

User Function jobm300()

    Local PARAMIXB := .F. // Executa em modo interativo
    Local aemp := {"99", "01"} // Empresa e Filial

    PREPARE ENVIRONMENT EMPRESA aemp[1] ;
                         FILIAL aemp[2] ;
                         USER 'Administrador' ;
                         PASSWORD '' ;
                         TABLES "SB1","SB2","SB9","SD1","SD2","SD3","SF4" ;
                         MODULO "EST"

    MSExecAuto({|x| mata300(x)}, PARAMIXB)

    RESET ENVIRONMENT

Return Nil
```

### **Como apagar os registros SBF onde BF\_QUANT esta Zero?**

Para que os saldos por endereço sejam zerados, basta fazer uso do parametro MV\_M300NG, com o parâmetro **MV\_MT300NG** ativo e **Procedure 18** instalada, sempre que um endereço na hora do movimento ou durante o **Refaz Saldos ficar zerado (0) ou negativo (-1 em diante)**, ele de fato apaga de forma lógica do banco de dados, ele não ira SETAR o campo **D\_E\_L\_E\_T\_** com o conteudo =  **,** indicando que esta deletado, IRA simplesmente DELETAR o registro fisico! e caso voce não use procedure ele vai setar o campo com delet preenchido com asterisco.

### **Pontos de entrada**

[PE M300SB8 Grava campos específicos no arquivo SB8](https://tdn.totvs.com/x/EjnZN)  
[PE MA300OK Valida execução da rotina](https://tdn.totvs.com/x/kTnZN)  
[PE M300SBF Função utilizada para recalcular o saldo atual dos movimentos](https://tdn.totvs.com/x/cjvZN)

**Saiba Mais**  
[Refaz Empenhos via Schedule (MATA215)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003543821)  
[Execução do Custo Médio via Schedule (MATA330)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048543893)  
[Como agendar a execução de Rotinas?](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)
