---
article_id: 4420659401751
category: SIGAEST - PROCESSAMENTOS
content_hash: 1bc2029451456e263c8a3ecef20c3ad035502d59cea031184ffc78608ce0a74b
fetched_at: '2026-06-28T22:39:04.979843+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - Refaz Saldos
  - Conceito e Informações
type: support-article
updated_at: '2025-03-12T12:17:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420659401751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Refaz-Saldos-Conceito-e-Informa%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28425505162903)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Para que serve a rotina de Refaz Saldos (MATA300), e o seu conceito para processamento?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O Refaz Saldos Atual tem como objetivo principal calcular e fornecer a posição do estoque mediante os movimentos do sistema **(NFs de entrada e saída e movimentos internos no periodo em aberto)**. Para cada item em estoque o sistema recalcula estoque, **saldos iniciais em quantidade e valor**.

Ou seja, o processamento parte da **data do ultimo fechamento de estoque + 1 dia**, até uma data futuro ao dia atual.

Esta rotina pode ser executada com o sistema em uso por todos os usuários. Nesse caso, as movimentações que estejam acontecendo simultaneamente ao cálculo podem influenciar no resultado. Para que a rotina seja executada dessa forma o parâmetro **MV\_CUSTEXC**deve estar com o conteúdo igual a "N".

Outra forma de execução (mais segura) é com o sistema em modo exclusivo, sem outros usuários utilizando os arquivos necessários ao cálculo. Para que a rotina seja executada dessa forma, o parâmetro **MV\_CUSTEXC**deve estar com o conteúdo igual a "S'.

**Essa rotina Zera os saldos dos produtos MOD?**

Sim, a rotina pode zerar os saldos dos produtos MOD/GGF **sem integração**, zerar ou recalcular, tanto saldos quanto custo médio, conforme o pergunte da rotina, caso sua MOD/GGF possua integração contabil, quem determinada os valores é a **CONTABILIDADE**.

**Zera o saldo de produtos MOD?**

Identifica se o programa deve zerar saldos de produto MOD ou nao, ja que estes produtos acumulam saldo negativo mes a mes. Opções Disponiveis:  
**Sim** - Zera os saldos dos produtos MOD  
**Nao** - Mantem os saldos dos produtos MOD  
**Recalcular** - Recompoe o saldo da MOD

**Zera o CM de produtos MOD?**

Identifica se o programa deve zerar o custo medio de produto MOD ou nao, ja que estes produtos acumulam saldo negativo mes a mes e sofrem variacao de custo a cada processamento.  
Opções Disponiveis:   
**Sim** - Zera o CM dos produtos MOD   
**Nao** - Mantem o CM dos produtos MOD  
**Recalcular** - Recompoe o CM da MOD

O produto **MOD/GGF**, são tipos de produtos que **NÃO CONTROLAM ESTOQUE**, ou seja, **é comum seus saldos negativarem** em decorrencia dos periodos, pois são sempre consumidos.

Para ZERAR os saldos do **MOD/GGF com integração contabil**, somente no ato do processamento da Virada de saldos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30092613336087)

**Esses saldos da MOD recalculados/zerados são levados para o fechamento, como?**

Existe uma sessão na rotina "Acompanha Custos" na sessão "Configurar Parametros" chamado "Fechamento", la contem 2 checks para você decidir oque quer fazer com os saldos zerados/recalculados do produto MOD.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28917991469335)

|  |
| --- |
| **Importante:**  A rotina Saldo Atual considera o conteúdo atual (“Sim” ou “Não”) do campo “Atualiza estoque”, obtido diretamente do cadastro de T.E.S., portanto, quando este campo é alterado, há reprocessamento no cálculo do saldo (também) para os movimentos que utilizaram este T.E.S. no período. |

 

|  |
| --- |
| **Dica:**  Para aumentar a velocidade de processamento desta rotina, utilize o recurso thread em conjunto com o parâmetro [MV\_A300THR](https://tdn.totvs.com/display/public/PROT/MATA300+-+Processamento+mult-thread+na+rotina+de+Saldo+Atual), que define a quantidade de threads a serem processadas, observando o limite máximo de 20 threads em execução.  Entretanto, verifique a real necessidade do número de thread a ser utilizado, pois a quantidade excessiva de thread pode deixar o processamento muito lento. |

**Procedimentos**

Para efetuar o Recálculo do saldo atual:

|  |  |
| --- | --- |
| 1. | Na janela de Manutenção de Saldo Atual, preencha os parâmetros apresentados conforme orientação do help de campo. |

Para selecionar as filiais a serem processadas em uma única execução, na pergunta "Seleciona Filiais", informe "Sim" e ao confirmar a execução da rotina, será apresentada a janela para seleção das filiais.

|  |
| --- |
| Observação:  A seleção de filiais está disponível somente para o Brasil. |

|  |  |
| --- | --- |
| 2. | Confira os dados e confirme a parametrização. |

O sistema apresenta uma tela solicitando que todos os usuários saiam do sistema, já que o recálculo necessita dos arquivos relacionados a materiais.

Caso o parâmetro **MV\_CUSTEXC**esteja preenchido como "S" = exclusivo, é importante que os usuários estejam fora do sistema. Caso contrário o  recálculo pode não estar correto, já que outras rotinas podem estar ainda recebendo informações, não apresentando assim uma posição do saldo atual correta.

Se este parâmetro for informado como "N" = compartilhado, não haverá necessidade de os usuários abandonarem o sistema para a execução desta rotina e os passos 2 e 3 a seguir devem ser ignorados.

|  |  |
| --- | --- |
| 3. | Confirme a solicitação quando todos os usuários estiverem fora do sistema. |

O sistema apresenta a tela descritiva da rotina.

|  |  |
| --- | --- |
| 4. | Confira os dados e confirme. |

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)*
