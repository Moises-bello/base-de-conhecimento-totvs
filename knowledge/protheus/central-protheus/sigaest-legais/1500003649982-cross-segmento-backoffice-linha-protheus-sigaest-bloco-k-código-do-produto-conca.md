---
article_id: 1500003649982
category: SIGAEST - LEGAIS
content_hash: 9217f3baef4625d12c369b108cbd1a6eabf738db0073ba998c3c5daeaf912419
fetched_at: '2026-06-28T22:38:51.603409+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Bloco K - Código do
  Produto concatenado com o Código da Filial
type: support-article
updated_at: '2022-08-24T19:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003649982-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-C%C3%B3digo-do-Produto-concatenado-com-o-C%C3%B3digo-da-Filial
---

**Dúvida**Ao gerar o SPED Fiscal, verifico que no Bloco K o código do produto está concatenando com o código da filial. Como ajustar para não ficarem concatenados?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**Para que o código do produto não venha concatenado ao código da Filial no SPED, basta configurar o parâmetro MV\_COFLSPD = .F.

Quando este parâmetro não existe os códigos são concatenados por padrão

Para criar o parâmetro MV\_COFLSPD, crie conforme abaixo:

**Nome da Variável:** MV\_COFLSPD

**Tipo:** Logico

**Conteúdo:** .F.

**Descrição:** Informe .F. para não concatenar o código da filial nos códigos dos registros do SPED Fiscal e SPED Contribuições

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)
