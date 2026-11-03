---
article_id: 26400351376279
category: MDFe - Manifesto de Carga
content_hash: 3aff3edb16d93869f9824834107e4842e6060b099ce72f0774536ec0d29f2143
fetched_at: '2026-06-28T22:40:08.031246+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE -  Rejeição
  229: IE do emitente não informada MDF-e'
type: support-article
updated_at: '2025-06-10T18:55:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26400351376279-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Rejei%C3%A7%C3%A3o-229-IE-do-emitente-n%C3%A3o-informada-MDF-e
---

**Dúvida**  
Como resolver Rejeição 229: IE do emitente não informada?

**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

Verifique a TAG emit se o conteúdo da TAG CNPJ e IE estão corretos.

A rejeição é um retorno da Sefaz, quando gera a rejeição 229 é necessário consultar a inscrição estadual do emitente.

Acesse o Cadastro Centralizado de Contribuinte (CCC):

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

Em valide se a IE da empresa emissora esta preenchida corretamente acessando o configurador, programa SIGACFG da abertura do smartclient:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26401148514583)

Acesse a opção Ambiente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26401148521751)

Em seguida acesse a opção Empresas > Filial:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26401157450519)

Selecione a Filial em questão e clique em Alterar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26401148530199)

Em seguida valide o preenchimento da Inscrição Estadual e salve:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26401148535319)

Após ajuste, refaça a emissão do documento do zero.

Validação da Sefaz:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26400351323543)
