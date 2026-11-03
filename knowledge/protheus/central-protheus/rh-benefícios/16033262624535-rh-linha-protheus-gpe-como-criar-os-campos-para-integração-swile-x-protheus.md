---
article_id: 16033262624535
category: RH - Benefícios
content_hash: 5085d7f3407f38c34de146d4f8d67471fa191dcf8015474772b173f9abe01ba3
fetched_at: '2026-06-28T22:44:03.746006+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar os campos para integração Swile X Protheus
type: support-article
updated_at: '2025-09-12T13:53:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16033262624535-RH-Linha-Protheus-GPE-Como-criar-os-campos-para-integra%C3%A7%C3%A3o-Swile-X-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16033286088983) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como criar os campos para integração Swile X Protheus?  
  
**Ambiente**

TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.33

**Solução**Para criar os campos e tabelas responsáveis pela integração Swile x Protheus, siga os passos abaixo:

**1.** Baixe o pacote de expedição continua modulo RH [no link](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA) e **atualize o ambiente.**

**2. Atualize o dicionário**, executando o [UPDDISTR.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152-MP-FIS-Como-Processar-o-UPDDISTR-para-atualiza%C3%A7%C3%A3o-de-dicion%C3%A1rios)

**3.** Inclua as rotinas **GPEM940** e **GPEM940A** no menu do **SIGAGPE**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16032803579799)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16032806655511)

**4.** Configure os parâmetros **MV\_APISWI1**, **MV\_APISWI2** e **MV\_APISWI3** via configurador;

**MV\_APISWI1 = https://prod.veedigital.com.br/FinancialBackend/rest**

**MV\_APISWI2 = Usuário**

**MV\_APISWI3** **= Senha  
![](https://i.imgur.com/B4nqmjQ.png)**

**05**. Acesse as rotinas **VT/VR/VA** e a aba e campo **Swile serão criados**.

**- Cadastro Vale Refeição** ![](https://i.imgur.com/ciEwz2N.png)

**- Cadastro Vale Alimentação****![](https://i.imgur.com/osAS7Py.png)**

**- Meio de transporte**![](https://i.imgur.com/xnD6dge.png)

**Observação:** Os dados de usuário e senha são disponibilizados pela Swile.

**Saiba Mais**[RH - Linha Protheus - GPE - Como incluir a rotina GPEM940 no menu - Integração Protheus e Swile](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15829745409815-RH-Linha-Protheus-GPE-Como-incluir-a-rotina-GPEM940-no-menu-Integra%C3%A7%C3%A3o-Protheus-e-Swile?source=search)  
[RH - Linha Protheus - GPE - Como incluir a rotina Consulta GPEM940A no menu - Integração Protheus e Swile](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15969592963479-RH-Linha-Protheus-GPE-Como-incluir-a-rotina-Consulta-GPEM940A-no-menu-Integra%C3%A7%C3%A3o-Protheus-e-Swile?source=search)  
[DT Integração com a Swile - Linha Microsiga Protheus - TDN (totvs.com)](https://tdn.totvs.com/pages/releaseview.action?pageId=707370134)
