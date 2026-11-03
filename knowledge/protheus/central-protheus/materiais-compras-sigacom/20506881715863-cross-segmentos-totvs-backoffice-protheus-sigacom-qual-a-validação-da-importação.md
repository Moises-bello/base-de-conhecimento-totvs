---
article_id: 20506881715863
category: Materiais - Compras (SIGACOM)
content_hash: c2334247a66005201c017833cabcd10da5eb68858efa334e17be2f58dff7904b
fetched_at: '2026-06-28T22:41:24.259895+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual a validação da
  Importação de Documentos XML com mesmo nome - CKO_ARQXML ?
type: support-article
updated_at: '2024-06-12T17:27:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20506881715863-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-a-valida%C3%A7%C3%A3o-da-Importa%C3%A7%C3%A3o-de-Documentos-XML-com-mesmo-nome-CKO-ARQXML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20506881690647) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Qual validação é efetuada no momento da importação de arquivo XML onde o nome de arquivo já existe na tabela CKOCOL com informação no campo CKO\_ARQXML?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução**

Renomeie o novo arquivo XML, antes de iniciar a importação, para que o registro na tabela CKOCOL e/ou arquivo XML na pasta "\Lidos" não seja sobreposto.

**Observações:**

Sistema realizará os seguintes processos:

1)  Quando o conteúdo do campo CKO\_FLAG for **diferente de "1"**:

      a) O registro na tabela CKOCOL **será sobreposto** com as informações do novo arquivo .XML que está sendo importado.

      b) O novo arquivo .XML será movido para a pasta "\Lidos" **sobrepondo o arquivo existente.**

2)  Quando o conteúdo do campo CKO\_FLAG **for igual a "1":**

      a) O registro na tabela CKOCOL **NÃO será sobreposto e nem atualizado** com as informações do novo arquivo .XML que está sendo importado.

      b) O novo arquivo .XML será movido para a pasta "\Lidos" **sobrepondo o arquivo existente.**

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Erros (Códigos)](https://tdn.totvs.com/pages/releaseview.action?pageId=271663193)

[Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
