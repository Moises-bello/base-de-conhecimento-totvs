---
article_id: 20884034668567
category: NFe - Nota Fiscal Eletrônica
content_hash: a7c10853b1d77e83a0513f41fadf222c5a6c7334738582c72af59df0ac859d6c
fetched_at: '2026-06-28T22:40:00.084427+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como incluir logo
  no Danfe gerado pelo Protheus?
type: support-article
updated_at: '2025-12-26T16:41:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20884034668567-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-incluir-logo-no-Danfe-gerado-pelo-Protheus
---

**Dúvida**

Como incluir logo no Danfe gerado pelo Protheus?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Devem configurar o parametro MV\_LOGOD conforme as opções abaixo:

Quando MV\_LOGOD=S

As dimensões da imagem devem ser 90 x 90 | Formato: BMP de 256 cores

A imagem deve estar na pasta \System e seguir a seguinte regra de nomenclatura: DANFE + Código da Empresa + Código da Filial+.bmp como o exemplo abaixo:

DANFE010101.bmp (caso o servidor seja linux a extensão deve ser maiúscula)

**\*Caso seja utilizada apenas uma imagem para todas as filiais: DANFE + Código da Empresa.bmp como o exemplo abaixo:**

DANFE01.bmp (caso o servidor seja linux a extensão deve ser maiúscula)

Quando MV\_LOGOD=N

As dimensões da imagem devem ser 90 x 90 | Formato: BMP de 256 cores

A imagem deve estar na pasta \System e seguir a seguinte regra de nomenclatura: LGRL+Código da Empresa+Filial.bmp como o exemplo abaixo:

LGRL010101.bmp (caso o servidor seja linux a extensão deve ser maiúscula)

**\*Caso seja utilizada apenas uma imagem para todas as filiais: LGRL+Código da Empresa.bmp como o exemplo abaixo:**

LGRL99.bmp (caso o servidor seja linux a extensão deve ser maiúscula)

OBS.: No diretório SIGAADV ou SYSTEM existe o arquivo LGRL99.BMP que pode ser utilizado como exemplo para dimensionamento do arquivo.

**Pontos de atenção:**

- Caso o ambiente esteja no servidor do T-Cloud da TOTVS toda a nomeclatura e extensão deve ser minúscula.

- É importante que o arquivo modelo LGRL99.BMP seja **renomeado ou deletado** ao inserir o novo arquivo do logo que deve ser configurado.
