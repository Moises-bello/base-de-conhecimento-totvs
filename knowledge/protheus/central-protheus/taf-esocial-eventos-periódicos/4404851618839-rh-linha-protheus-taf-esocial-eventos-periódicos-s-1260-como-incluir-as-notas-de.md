---
article_id: 4404851618839
category: TAF - eSocial - Eventos Periódicos
content_hash: ef7aa44b64323267f1fafeb1308d78ca510c3e43ff7e9d6780c18e0b2a760a09
fetched_at: '2026-06-28T22:45:19.077367+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1260 - Como incluir
  as notas de Comercialização da Produção Rural Pessoa Física no TAF
type: support-article
updated_at: '2024-05-24T11:20:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404851618839-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1260-Como-incluir-as-notas-de-Comercializa%C3%A7%C3%A3o-da-Produ%C3%A7%C3%A3o-Rural-Pessoa-F%C3%ADsica-no-TAF
---

**Dúvida**Como incluir as notas de Comercialização da Produção Rural Pessoa Física no TAF, **evento S-1260** do eSocial.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Periódicos - Todas as versões  
  
**Solução**

Para **incluir** as notas de Comercialização da Produção Rural Pessoa Física no TAF, evento **S-1260 (TAFA414)**, siga os passos abaixo:

1. É necessário rodar o **Extrator Fisca**l (EXTFISXTAF);

*\*\*Este primeiro passo é utilizado para CLIENTES COM MÓDULOS DO PROTHEUS.*

*\*\*CLIENTES SEGREGADOS, precisam realizar a IMPORTAÇÂO do documento fiscal (pela rotina TAFA500), ou efetuar  inclusão MANUAL, direto na rotina TAFA414 (S-1260).*

[TAF - INTEGRAÇÃO - Como importar arquivos XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027012291)

2. No menu principal TAF, selecione as opções: "Atualizações" > "Eventos Esocial" > "Periódicos" > "Com.  Rural. Pf"

3. Selecione o botão "Incluir";

4. Com a rotina aberta, preencha os seguintes campos: **"Per. Apuração "** e **" Id. Estab"**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404850983959)

5. Em seguida,  selecione o botão **"Outras Ações"** e em seguida a opção **"Buscar Docs Fiscais"**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404842957335)

6 – Confira as notas que serão alimentadas pela rotina:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404851306647)

7. Selecione o botão **"Confirmar"** para salvar o evento S-1260;

**Saiba mais:**

Consulte as documentações do TDN para o evento S-1260:

<https://tdn.totvs.com/pages/releaseview.action?pageId=272712628>

<https://tdn.totvs.com/pages/releaseview.action?pageId=676591852>

Consulte o Manual de Orientação do eSocial:

<https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-0-final-publicada-revisada.pdf>
