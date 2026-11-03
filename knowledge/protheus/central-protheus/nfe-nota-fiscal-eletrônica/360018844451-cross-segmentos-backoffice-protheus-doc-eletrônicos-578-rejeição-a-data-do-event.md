---
article_id: 360018844451
category: NFe - Nota Fiscal Eletrônica
content_hash: f9836f22304db53bdbdb5ad79abe039c40b68b2c7243c606b6b82fcc420c105d
fetched_at: '2026-06-28T22:40:05.145901+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 578 Rejeição :
  A data do evento não pode ser maior que a data do processamento'
type: support-article
updated_at: '2025-06-18T14:47:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844451-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-578-Rejei%C3%A7%C3%A3o-A-data-do-evento-n%C3%A3o-pode-ser-maior-que-a-data-do-processamento
---

**Dúvida**

Como solucionar a rejeição 578 : A data do evento não pode ser maior que a data do processamento

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução:**

* De acordo com **o Decreto nº 9.772:**

***Fim do horário de Verão***

No término do horário de verão é necessário realizar as configurações novamente dentro da rotina de transmissão para horário de Verão igual a **Não** e o fuso horário de acordo com o **Estado**.

1. Acessar a rotina de transmissão de NFe, CCe, NFC-e, MDFe ou Manifesto: Acesse como Administrador a Rotina de transmissão > ***Outras ações > Parâmetros > Eventos > Horário de Verão = Não (de acordo com a UF da filial).***  
  
  
![HORARIO_DE_VERAO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32896675791511)

2. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar MV\_HVERAO =** .F. (sem)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12633526707863)

3. Acesse o ***appserver.ini do TSS e verifique a chave abaixo:***

SPED\_HVERAO= 2 (horário de verão = NAO).

* ***Exemplo:***  
  [Environment]  
  SPED\_HVERAO=2  
  OBS: Após alterar o ini do TSS o mesmo deverá ser reiniciado.

4. Conferir o conteúdo dos campos ***(F2\_HORA ou F1\_HORA)*** de acordo se está de acordo com o horário da UF filial corrente. Caso esteja incorreto conferir os parâmetros do ERP relacionados no link abaixo:

*[Clique Aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=267794836)*

* **Saiba mais:**

*[Alteração do Parâmetro MV\_HORARMT\_TRKVZW](http://tdn.totvs.com/pages/viewpage.action?pageId=189301887)*

*[Parâmetro MV\_HORANFE - TFJKB0](http://tdn.totvs.com/pages/viewpage.action?pageId=36307649)*

*[MV\_HVERAOI e MV\_HVERAOF - Documentos de Entrada e Saída\_TSBBUX](http://tdn.totvs.com/pages/viewpage.action?pageId=189316246)*
