---
article_id: 360017811711
category: Materiais - Compras (SIGACOM)
content_hash: 715bf7832244df04e33f9202fdefdb79655c729afd4e40f08a7429b83509be1e
fetched_at: '2026-06-28T22:41:08.757317+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Conteúdo do campo F1_ESPECIE
  pelo Botão Retornar
type: support-article
updated_at: '2022-05-12T21:08:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017811711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Conte%C3%BAdo-do-campo-F1-ESPECIE-pelo-Bot%C3%A3o-Retornar
---

**Dúvida**Quais os conteúdos que sistema poderá preencher no campo F1\_ESPECIE ao utilizar a opção / botão Retornar da rotina do Documento de Entrada - MATA103.  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

**1. I****nicializador padrão do campo F1\_ESPECIE em branco e Sem o PE MT103ESP**Carrega a Espécie do documento de saída (F2\_ESPECIE) no campo Espécie Documento (F1\_ESPECIE).

**Observação:**Se*o campo F2\_ESPECIE estiver em Branco o sistema carregará a Espécie "NF".*

**2. In****icializador padrão do campo F1\_ESPECIE = "NFE" (Exemplo) e Sem o PE MT103ESP**Carrega a Espécie conforme o inicializador padrão do campo F1\_ESPECIE.

**3. Inicializador padrão do campo F1\_ESPECIE em Branco****e Com o PE MT103ESP**Carrega a Espécie conforme o ponto de entrada MT103ESP.

**4. In****icializador padrão do campo F1\_ESPECIE = "NFE" (Exemplo) e Com o PE MT103ESP**

Carrega a Espécie conforme o inicializador padrão do campo F1\_ESPECIE.

***Saiba Mais :***

[Ponto de Entrada - MT103ESP](http://tdn.totvs.com.br/pages/releaseview.action?pageId=6085744)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
