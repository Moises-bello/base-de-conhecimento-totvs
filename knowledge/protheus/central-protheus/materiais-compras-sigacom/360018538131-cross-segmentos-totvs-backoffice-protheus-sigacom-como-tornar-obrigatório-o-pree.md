---
article_id: 360018538131
category: Materiais - Compras (SIGACOM)
content_hash: 02c119ccff9dbc3ad1b5d14f1cc84a75da8dc3e0077afb324df0ff4bb2fa1e2c
fetched_at: '2026-06-28T22:41:16.071368+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como tornar obrigatório
  o preenchimento do campo de espécie na inclusão do documento de entrada ?
type: support-article
updated_at: '2024-12-02T12:02:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018538131-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-tornar-obrigat%C3%B3rio-o-preenchimento-do-campo-de-esp%C3%A9cie-na-inclus%C3%A3o-do-documento-de-entrada
---

**Dúvida**Como tornar obrigatório o preenchimento do campo de espécie na inclusão do documento de entrada ?

**Ambiente**Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Solução**Para atender esta necessidade, realize os seguintes passos:  
  
1. Acesse o módulo configurador(SIGACFG);  
2. Acesse o caminho Base de Dados - Dicionário - Base de Dados;  
3. Selecione a opção Parâmetros;  
4. Localize o parâmetro **MV\_ESPOBG** e configure o mesmo como .T.

IMPORTANTE :

Algumas operações realizadas no documento de entrada, não exigem a obrigatoriedade do campo F1\_ESPECIE entre elas processos de beneficiamento, devoluções e outras espécies.

Não podemos em nosso produto padrão colocar o campo como obrigatório, pois, uma grande quantidade de clientes utilizam o processo sem a obrigatoriedade do campo, contudo, estamos cientes da necessidade da informação deste campo em algumas oparações para processos de integração fiscal. Para atender sua necessidade onde todos os documentos lançados devem possuir o campo preenchido

aconselho que verifique junto a um desenvolvedor para a criação de tal validação.

***Saiba Mais:***

[Pontos de entrada do Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-entrada-do-Documento-de-Entrada-MATA103)

[MV\_ESPOBG – Documento de Entrada](http://tdn.totvs.com/pages/viewpage.action?pageId=189316265)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
