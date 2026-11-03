---
article_id: 360024854713
category: Gestão de Transportes (TMS)
content_hash: a70d94bc38ec8691d22298f6f98d047dcc6e7f595a35feeae3e59a50d5a36b41
fetched_at: '2026-06-28T22:45:29.500522+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Parametro MV_TMSPNDB - Permite informar
  a ocorrência do tipo Gera Pendência para um Documento Bloqueado
type: support-article
updated_at: '2022-06-20T17:16:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024854713-Log%C3%ADstica-Linha-Protheus-TMS-Parametro-MV-TMSPNDB-Permite-informar-a-ocorr%C3%AAncia-do-tipo-Gera-Pend%C3%AAncia-para-um-Documento-Bloqueado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: 00:01:00 min **Dúvida**Como informar uma ocorrência do tipo **Gera Pendência** para um **Documento Bloqueado**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para atender às situações em que é necessário apontar uma ocorrência do tipo **Gera Pendência** para um documento que possui uma ocorrência do tipo **02 - Bloqueia Documento** - campo **DT2\_TIPOCO**, implementar o parâmetro **MV\_TMSPNDB**.  
  
**Exemplo de uso:** O documento é apreendido pelo posto fiscal e o mesmo não fica com a mercadoria. Enquanto a mercadoria segue para a filial a transportadora fica como fiel depositária sendo responsável pela carga, e então pode ocorrer, por exemplo, uma avaria. Para movimentação do documento, deve-se efetuar a liberação do documento - ocorrência do tipo **03 - Libera Documento**. Caso contrário, o Sistema impede qualquer tipo de movimento a ele relacionado.  
  
Para a devida configuração, no **Configurador** - **SIGACFG** acesse **Ambientes/Cadastros/Parâmetros** **CFGX017**. Crie o Parâmetro a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038096594/mceclip0.png)

**Modo de uso**

1. Configure o parâmetro **MV\_TMSPNDB = .T.**;
2. Em **Gestão de Transportes - SIGATMS**, acesse **Atualizações/Rodoviário Entrega/Viagem**;
3. Crie uma viagem;
4. Efetue o fechamento da viagem e aponte as operações da viagem;
5. No apontamento de ocorrência, selecione um código de ocorrência do tipo **Bloqueia Documento**;
6. Selecione o documento e confirme;

O status do documento fica como **Bloqueado - DT6\_BLQDOC.**

1. Novamente no apontamento de ocorrência, selecione um código de ocorrência do tipo **Gera Pendência**;
2. Selecione o documento e confirme.

O status do documento fica como **Bloqueado - DT6\_BLQDOC.**

1. Em **Gestão de Transportes - SIGATMS**, acesse **Atualizações/Ocorrências/Reg. De Pendências** **- TMSA540**;
2. Selecione a pendência e utilize as opções disponíveis na rotina para gerar o registro de indenização das pendências de seguro;

O status do documento fica como **Bloqueado - DT6\_BLQDOC**, pois não foi registrada o apontamento da ocorrência de **Libera Documento** e sendo assim, não será permitido nenhuma movimentação com o documento.

1. Em **Gestão de Transportes - SIGATMS**, acesse **Atualizações/Ocorrências/Reg. De Ocorrências - TMSA360**;
2. Selecione um código de ocorrência do tipo **Libera Documento**;
3. Selecione o documento e confirme

O documento fica **Desbloqueado - DT6\_BLQDOC**, permitindo a movimentação.
