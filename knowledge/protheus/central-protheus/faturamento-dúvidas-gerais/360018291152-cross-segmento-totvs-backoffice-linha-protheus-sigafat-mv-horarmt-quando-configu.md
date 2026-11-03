---
article_id: 360018291152
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 5293ffad546c90c5cfa25500791835c96470635a25a6bb2805611d73775a3005
fetched_at: '2026-06-28T22:38:28.606473+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - MV_HORARMT quando
  configurado como 3, não gera o horário correto.
type: support-article
updated_at: '2023-03-20T19:47:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018291152-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-MV-HORARMT-quando-configurado-como-3-n%C3%A3o-gera-o-hor%C3%A1rio-correto
---

**Ocorrência**

O sistema não está obedecendo as regra setadas no parâmetro **MV\_HORARMT**. Temos uma filial com a diferença de menos uma hora em relação a matriz e mesmo configurando este parâmetro para opção 3=Fuso horário da filial corrente; o sistema está pegando a hora errada impedindo a transmissão da nota. Como devemos proceder para corrigir este problema; pois não estamos conseguindo emitir as notas dessa filial?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

O problema ocorria em razão dos parâmetros **MV\_HVERAOI** e **MV\_HVERAOF** não terem sido criados com a tipagem correta e não haver o parâmetro **MV\_HORARMT** criado exclusivo para a filial em questão.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Valide se os parâmetros  **MV\_HVERAOI** e **MV\_HVERAOF** estão com a tipagem correta, "**DATA**", caso não esteja seguir o boletim técnico do TDN para ajustar:

[MV\_HVERAOI e MV\_HVERAOF - Documentos de Entrada e Saída](https://tdn.totvs.com/pages/releaseview.action?pageId=189316246)

2. Valide se a tabela de parâmetros é exclusiva por filial, sendo exclusiva, o parâmetro **MV\_HORARMT** deverá ter um para cada filial, caso não haja, crie conforme a documentação existente no tdn:

**[MV\_HORARMT - Documento de Entrada e Saida](https://tdn.totvs.com/display/public/PROT/MV_HORARMT+-+Documento+de+Entrada+e+Saida)**

Sendo a tabela de parâmetros compartilhada, deverá existir apenas um parâmetro **MV\_HORARMT** com o campo filial vazio.

3. Após esses procedimentos, efetue novamente a geração do documento para que gere o **F2\_EMISSAO** e **F2\_HORA** correto, e assim , efetue o processo de transmissão da NF-e.
