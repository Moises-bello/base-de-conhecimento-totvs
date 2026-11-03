---
article_id: 25147638074647
category: SIGAEST - SALDOS
content_hash: 082a2b6df6485f8a4bd74b553a5ca8d7381a3daa5f0aa361943bf641bbb55b11
fetched_at: '2026-06-28T22:39:14.844426+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Divergencia entre
  saldo atual x kardex por periodo
type: support-article
updated_at: '2025-03-12T12:23:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25147638074647-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Divergencia-entre-saldo-atual-x-kardex-por-periodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25147647006487) Tempo aproximado para leitura: **00:04:10 min****Dúvida**Filtrei o relatorio Kardex por periodo/Diario, mas não bate com o saldo atual, o que fazer?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**Primeiro precisamos entender os conceitos sobre **saldos atual** e **saldos por movimentos**.

**O que é saldo atual?**

O saldo atual, é tudo aquilo que voce tem no dia atual, ou seja a data do dia vigente, esse saldo sera apresentado no campo da tabela **SB2 -> B2\_QATU(Saldo Atual) / através do relatorio [MATR260](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018559171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Import%C3%A2ncia-da-pergunta-Saldo-do-produto-a-considerar-para-correta-emiss%C3%A3o-do-relat%C3%B3rio) considerando Saldo atual, ou através do [F4 do produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto).**

**O que é saldo por movimento?**

O saldo por movimento, é tudo aquilo que é efetuado de movimentações no sistema, calculando as entradas e saidas do estoque, no periodo de seleção desejado, o sistema utiliza a funçã **CalcEst** para realizar essa operação, e então apresentado o saldo calculado por movimento, apresentado no campo da tabela **SB2 -> B2\_QFIM(Qtd. Fim Mes)**.

**Gerei o relatorio Kardex, mas não reflete com meu saldo atual:**

O Erro mais comum nessa situação, é não entender, que o saldo atual **pode ser diferente** de saldo por movimento.

Nesse caso, certifique-se que o seu **[Karde](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)****[x](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)** **[por](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)** **[periodo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)**, esteja trazendo exatamente o calculo até a data atual do dia, na parametrização **de/ate da data limite**.

Considerei a data atual, mas mesmo assim é divergente do saldo atual do produto, onde verifiquei diretamente no **[F4 do produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto)**, ou no campo **B2\_QATU:**

* **Certifique-se que não existem movimentações posteriores**, ou seja, movimentações que foram digitadas com a data incorreta, filtre o Karde com data até **31/12/9999** e valide se por acaso, não existe um movimento com data posterior ao saldo atual, caso exista basta estornar o movimento que esta incorreto.
* **Efetue o processamento da rotina Refaz Saldos(MATA300)**, para que o sistema busque efetuar a atualização correta do saldo atual.

**Essas são as considerações para avaliação do saldo atual e por movimento, caso ainda sim encontre divergencias apresentadas, basta efetuar a abertura de um ticket, para uma avaliação mais precisa junto ao time de suporte.**

**Relacionados:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Utilização do parâmetro MV\_TPSALDO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013215531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utiliza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-TPSALDO)

[Sessão sobre avaliação de saldos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)

***Saiba mais**:*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
