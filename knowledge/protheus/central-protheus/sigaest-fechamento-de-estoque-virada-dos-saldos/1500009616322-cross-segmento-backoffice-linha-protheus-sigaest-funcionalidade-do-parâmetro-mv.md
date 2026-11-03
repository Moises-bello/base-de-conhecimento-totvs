---
article_id: 1500009616322
category: SIGAEST - FECHAMENTO DE ESTOQUE (VIRADA DOS SALDOS)
content_hash: 25623990a6dec071600b256e5c47339968132bfb5b9715aa59f3c441a813f379
fetched_at: '2026-06-28T22:38:52.731646+00:00'
product: protheus
section_id: 1500001538921
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Funcionalidade do
  parâmetro MV_ULMES
type: support-article
updated_at: '2025-12-22T14:01:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009616322-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Funcionalidade-do-par%C3%A2metro-MV-ULMES
---

O parâmetro MV\_ULMES registra a data do último fechamento de estoque realizado e bloqueia movimentações em estoque com datas iguais ou anteriores a essa data. Já o MV\_DBLQMOV impede movimentações na data do fechamento para evitar interferências. Em ambientes com múltiplas filiais, cada unidade deve ter seu próprio MV\_ULMES configurado no módulo Configurador, sem compartilhamento entre filiais.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31604226040855) Tempo aproximado para leitura: **00:02:00 min**  
   
**Dúvida**

Qual a funcionalidade do parâmetro MV\_ULMES? Qual a relação dele com o parâmetro MV\_DBLQMOV e o processo de Fechamento de Estoques?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O parâmetro **MV\_ULMES** tem por finalidade declarar a data do último fechamento de estoque realizado. Assim que é processada a Virada de Saldos (MATA280), o Protheus atribui no parâmetro **MV\_ULMES** conforme a data delegada na pergunta "data base para executar o fechamento".

Outra função importante deste parâmetro é que ele bloqueia a inclusão/alteração/estorno de movimentos nas tabelas

SD1 – Itens do documento de entrada,

SD2 – Itens do documento de saída

SD3 – Movimentos internos com datas iguais ou anteriores à data gravada em seu conteúdo.

E demais, que façam movimentações no estoque.

*Exemplo:*

**MV\_ULMES = 20241231**  
Nesse exemplo, o último fechamento de estoque foi efetuado na data de 31/12/2024. Desta forma, o sistema não permite que sejam realizadas movimentações no estoque com data igual, ou anterior à 31/12/2024.

Quanto ao [**parâmetro MV\_DBLQMOV**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-o-bloqueio-de-Movimenta%C3%A7%C3%B5es-no-Estoque-durante-o-Fechamento-de-Estoque), a sua função é basicamente impedir/bloquear que usuários entrem com movimentações na data delegada no parâmetro. Normalmente é colocado, no parâmetro, a data ao qual está sendo feito o processo de fechamento. Desta forma nenhum outro usuário poderá entrar com movimentações e consequentemente influenciar na Virada de Saldos que está sendo feita paralelamente ao movimento.

|  |
| --- |
| **OBSERVAÇÕES IMPORTANTES:** |

**-** Com a nova Jornada de Fechamento quando utilizamos a rotina **Acompanha Custos (MATA038)** o parâmetro **MV\_ULMES** ***não deve*** **ser manipulado diretamente pelo Configurador ou ASPDU**, a responsabilidade de atualização desse parâmetro é da rotina de Fechamento de Custos (MATA280) no momento do processamento do Fechamento.

Em ambientes que compreendem múltiplas filiais, torna-se imperativa a criação do parâmetro **MV\_ULMES** de forma exclusiva para cada unidade. Ressalta-se que, nestes casos, não deve haver o referido parâmetro configurado de maneira compartilhada para todas as filiais.

A configuração deve ser realizada via módulo **Configurador (SIGACFG)**, onde o usuário deve definir a data de fechamento conforme a necessidade da operação. Por se tratar da implementação de uma nova unidade sem histórico anterior, o período de bloqueio inicial fica a critério da gestão, mas não pode ser em branco!.

É fundamental observar que, ao definir a data do parâmetro, se houver a necessidade de contabilização no período correspondente, o calendário contábil e as respectivas moedas devem estar devidamente vinculados e configurados para o intervalo em questão.

**OCORRENCIAS MAPEADAS:**

**type mismatch on compare on AC.ACCALC.SERVICE.ACCALCSERVICE:AREBRANCHESVALID(ACCALCSERVICE.TLPP)**

Valide o parametro MV\_ULMES esta devidamente configurada para cada uma de suas filiais, onde a data seja exatamente a mesma data da ultima SB9 de cada filial correspondente.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Roteiro para Fechamento de Estoque (virada de saldos)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048372754-MP-SIGAEST-Roteiro-para-fechamento-dos-estoques)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar o bloqueio de Movimentações no Estoque durante o Fechamento de Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844351-MP-SIGAEST-Como-realizar-o-bloqueio-de-movimenta%C3%A7%C3%B5es-no-estoque-?source=search)

[*Clique aqui e veja mais artigos sobre Fechamento de Estoque (Virada de Saldos)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538921-SIGAEST-FECHAMENTO-DE-ESTOQUE-VIRADA-DOS-SALDOS-)
