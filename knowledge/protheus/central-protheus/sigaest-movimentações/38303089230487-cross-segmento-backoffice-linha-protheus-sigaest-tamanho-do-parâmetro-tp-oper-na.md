---
article_id: 38303089230487
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2e1145c712622c9fc8a5878021121a27e8a53c4eda7edfbbae17e79aca31946b
fetched_at: '2026-06-28T22:38:57.434378+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Tamanho do parâmetro
  Tp Oper. na Transferência entre Filiais (MATA310)
type: support-article
updated_at: '2026-02-10T17:49:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38303089230487-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Tamanho-do-par%C3%A2metro-Tp-Oper-na-Transfer%C3%AAncia-entre-Filiais-MATA310
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38303089214871) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como aumentar o tamanho dos parâmetros (SX1) "TP Oper. Saida ?" e "TP Oper. Entrada ?" da rotina de Transferência entre Filiais (MATA310)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
Com as mudanças relacionadas à Reforma Tributária, a tabela "DJ" da SX5, que guarda os **Tipos de Operação**, passa a comportar códigos de até 6 digitos.

Caso utilize mais que 2 dígitos na tabela "DJ" da SX5, é necessário realizar o ajuste dos perguntes "TP Oper. Saida ?" e "TP Oper. Entrada ?" da rotina de Transferência entre Filiais (MATA310).

Para realizar este ajuste, realize os seguintes passos:

* Acesse o **Configurador do Sistema (SIGACFG)**;
* Acesse as opções "**Base de Dados**", depois "**Dicionário**" e a opção "**Bases de Dados**";
* Selecione a opção perguntas, conforme imagem abaixo:

![TPOPER 01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38303072813847)

* Pesquise pelo Grupo de Perguntas "**MTA310**" e altere:

![TPOPER 02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38303072815255)

* Altere o tamanho das perguntas  "TP Oper. Saida ?" e "TP Oper. Entrada ?" conforme sua necessidade e confirme:

![TPOPER 03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38303072818455)

* Ao acessa a rotina de Transferência entre Filiais (MATA310) os parâmetros estarão com o tamanho ajustado:

![TPOPER 04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38303089220503)

**Atenção**:

Caso tenha realizado a alteração e, para um usuário específico, o tamanho dos parâmetros permanecer no tamanho anterior, verifique, em ambiente de homologação primeiramente, se é necessário realizar a [**Limpeza do Profiler do Usuário**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025097012-Framework-Linha-Protheus-Manuten%C3%A7%C3%A3o-de-Profile-de-Usu%C3%A1rios).

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Como definir o Preço de Venda do Pedido de Venda derivado do processo de Transferência entre Filiais ?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021390332-MP-SIGAEST-Custo-do-produto-derivado-do-processo-de-transfer%C3%AAncia-via-MATA311-)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
