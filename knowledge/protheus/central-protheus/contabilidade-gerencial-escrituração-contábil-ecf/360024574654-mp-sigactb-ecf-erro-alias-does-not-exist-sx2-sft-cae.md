---
article_id: 360024574654
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: e716f18bc5c38e8ee3c13a050fd1ced7877ee9dff616746ae373135a332f5813
fetched_at: '2026-06-28T22:40:48.964227+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'MP - SIGACTB - ECF Erro Alias does not exist SX2 / SFT / CAE '
type: support-article
updated_at: '2021-04-28T22:10:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024574654-MP-SIGACTB-ECF-Erro-Alias-does-not-exist-SX2-SFT-CAE
---

**Dúvida**

Erro log apresentado ao exportar ECF para o TAF

Alias does not exist **SIX**( PREVIOUS ERROR : Alias does not exist: **CAE**) on TABLEINDEX(APLIB200.PRW)

Alias does not exist **SX2** ( PREVIOUS ERROR : Alias does not exist **SFT** ) on CHKFILE(APLIB200.PRW)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038677593/mceclip0.png)

**Ambiente**

Microsiga Protheus  – Contabilidade  – A partir da versão P12  
   
**Solução**  
**1º Passo   :** Verifique se a lib esta atualizada

* PORTUGUES - [https://suporte.totvs.com/portal/p/10098/download?e=754625](https://www.google.com/url?q=https://suporte.totvs.com/portal/p/10098/download?e%3D754625&sa=D&source=hangouts&ust=1560454829683000&usg=AFQjCNFVYkoPr8izNKsOn5SyGPWC34tkwQ)
* INGLES - [https://suporte.totvs.com/portal/p/10098/download?e=754624](https://www.google.com/url?q=https://suporte.totvs.com/portal/p/10098/download?e%3D754624&sa=D&source=hangouts&ust=1560454829683000&usg=AFQjCNFgqXr3YrhgYzk1uta4YTDi5VSXZg)
* ESPANHOL - [https://suporte.totvs.com/portal/p/10098/download?e=754627](https://www.google.com/url?q=https://suporte.totvs.com/portal/p/10098/download?e%3D754627&sa=D&source=hangouts&ust=1560454829683000&usg=AFQjCNEKLemN4xxRvNjJV9GeGqP23yKdVw)

**2º Passo :** Realize a consulta na tabela SX2 e SIX

* Verifique se as tabelas SFT e CAE existem

**3º Passo :** Caso as tabelas existam

* Pare todos os serviços do Protheus;
* Renomeie o arquivo sx2010.cdx
* Inicie apenas um serviço do Protheus (Slave), caso possua balanceamento de carga, este serviço não pode ter a seção [ONSTART] ativa;
* Acesse o Configurador pelo ambiente que esta com a lib atualizada e valide se o erro persiste.

Identificado que este erro ocorre, pois não possui exclusividade de leitura e gravação do índice (SX2.CDX), apresentando o erro. Sendo necessário o acesso exclusivo ao ambiente utilizando a base com a ultima LIB. Cenário entra no processo de ter mais de um RPO com lib's diferentes apontados para o mesmo dicionário de dados(system).
