---
article_id: 4403469935255
category: NFe - Nota Fiscal Eletrônica
content_hash: 19fb4a444130bfbda08233ba5e30814cc2e339d1f619b56f3f8a63ee8d43a5ae
fetched_at: '2026-06-28T22:40:03.220053+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  446 Rejeição:
  Informado CEST inexistente'
type: support-article
updated_at: '2025-06-25T12:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403469935255-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-446-Rejei%C3%A7%C3%A3o-Informado-CEST-inexistente
---

**Dúvida**Como solucionar a rejeição abaixo ?

446 Rejeição: Informado CEST inexistente

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Nota Técnica, **2020.005**, trouxe  **novas TAGS e alterações de regras de validação para a versão 4.0, Nota Fiscal Eletrônica (NF-e), modelo 55.**

* **Nota técnica** disponível no link abaixo:

[Nota Técnica 2020.005 - v.1.10 - Publicada em 22/12/2020](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=kPdOuLsAd34=)

Se informado CEST, CEST inexistente (vide tabela de apoio publicada no  
Portal da NF-e). **Observação:** **Regra desabilitada,** aguardando publicação da tabela de códigos  
CEST válidos

* Caso a UF do seu estado valide a **Rejeição, realize o processo abaixo:**

1. Preencher no cadastro de produto o **CEST "B1\_CEST" na aba outros, um CEST válido:  
  
  
![cest.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11646130517655)​**  
2- Após isso, **exclua a nota e gere novamente.**

* **Importante:**

Para saber os códigos de CEST **validos pela sua UF entre em contato junto a Sefaz.**

* **Impressão no Danfe:**

O CEST é gerado **apenas no XML.**

Não existe até o momento um layout da Sefaz para que seja apresentada a informação do CEST, ou seja, não foi criado um novo campo no Danfe, e não há nenhuma informação na nota técnica sobre a obrigatoriedade de mensagem.

Caso seja uma solicitação da Sefaz do seu estado, poderá utilizar um padrão para gerar a mensagem em informações complementares, como exemplo **C5\_MENNOTA.**

* **Validação da Sefaz:**

![446_rejeicao.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4403469719447)
