---
article_id: 14193509486871
category: SIGAACD - Automação e Coleta de Dados
content_hash: 587ee017a4cc072c65ae155d6b8978561d74a700f9deadccc4eec12824e79b9f
fetched_at: '2026-06-28T22:39:11.405727+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - App Meu Coletor de
  Dados com lentidão na Sincronização de Dados
type: support-article
updated_at: '2026-05-25T13:58:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14193509486871-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-App-Meu-Coletor-de-Dados-com-lentid%C3%A3o-na-Sincroniza%C3%A7%C3%A3o-de-Dados
---

A sincronização lenta do app Meu Coletor de Dados pode ser otimizada restringindo os registros sincronizados via parâmetros MV\_MCDPRSL e MV\_MCDTPPR, que filtram produtos pela tabela de saldos SB2 e tipos de produto, melhorando a performance em ambientes com muitos itens.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38158661340695) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
A Sincronização de dados do app Meu Coletor de Dados está lenta. O que fazer para melhorar a performance?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados- Todas as versões.

**Solução**

Em ambientes com **muitos produtos**, a sincronização e utilização do aplicativo **Meu Coletor de Dados** é prejudicada, pois em muitos casos, grande parte dos registros não é passível de movimentação. Devido a este cenário, foi solicitado alguns mecanismos para **restringir os registros a sincronizar** com o aplicativo. Seria uma maneira de ganhar performance durante a Sincronização de Dados.

Com isso, foi feito um ajuste no **webservice** de sincronismo de produtos do **Meu Coletor de Dados** para permitir a restrição dos registros através do uso dos seguintes **parâmetros**:

**-** **MV\_MCDPRSL****:** Se **habilitado**, serão sincronizados **somente** os produtos **presentes na tabela de saldos - SB2**, independente do saldo.

**-** **MV\_MCDTPPR****: Somente** produtos com os **tipos de produto - B1\_TIPO** informados no parâmetro serão sincronizados. Os itens devem ser **separados por vírgula e sem espaço**. Exemplo de preenchimento: **PA,ME,MC**

Para utilizar esta opção no **Meu Coletor de Dados**, é necessário verificar se os parâmetros **MV\_MCDPRSL**e **MV\_MCDTPPR**estão criados no ambiente, **seguindo a especificação abaixo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14193430970135)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38158661341591)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38158685744791)

Caso persista, configure no seu AppServer.ini do Rest as seguintes Tag's, abaixo das configurações do ambiente e nos encaminhar os logs para análise:

`[environment]`

**FWLOGMSG\_DEBUG=1**

**FWTRACELOG=1**

**LogProfiler=1**

`[general]`

**Consolelog=1**

**LogHttpFuncs=1**

**LSDebug=2**

Segue documentações sobre essas Tag's: [Chaves para controle de logs](https://tdn.totvs.com/display/public/framework/Chaves+para+controle+de+logs), [LogHttpFuncs](https://tdn.totvs.com/x/MY5vI), [Tag TraceLS](https://tdn.totvs.com/display/LRM/Habilitar+Tag+TraceLS)

*Observação: Limpar o Console.log na pasta AppServer.ini do seu ambiente para recriar um novo arquivo para validação. E encaminhar o Console.log para análise caso o problema persista.*

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
