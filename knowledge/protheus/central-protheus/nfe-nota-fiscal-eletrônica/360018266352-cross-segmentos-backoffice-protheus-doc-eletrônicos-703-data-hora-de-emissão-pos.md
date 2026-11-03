---
article_id: 360018266352
category: NFe - Nota Fiscal Eletrônica
content_hash: f41df79ad07a4a536c23fd13f9e566ce58e050e52d9bb45f9bc9002f78e079ac
fetched_at: '2026-06-28T22:40:05.253424+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 703 - Data-Hora
  de Emissão posterior ao horário  de recebimento
type: support-article
updated_at: '2025-08-12T00:47:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018266352-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-703-Data-Hora-de-Emiss%C3%A3o-posterior-ao-hor%C3%A1rio-de-recebimento
---

**Dúvida**Como resolver a rejeição:

703 - Data-Hora de Emissão posterior ao horário de recebimento?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução:**

* De acordo com **o Decreto nº 9.772:**

***Fim do horário de Verão***

Neste caso será necessário  verificar o ***horário da estação local e do servidor*** de acordo com o site <http://pcdsh01.on.br/>

* **Importante:**

No término do horário de verão é necessário realizar as configurações novamente dentro da rotina de transmissão para horário de Verão igual a **Não** e o fuso horário de acordo com o **Estado**.

Desabilite o parâmetro no **Protheus** de horário de verão e parâmetro do Ini do **TSS**.

* Conferir o conteúdo dos campos ***(F2\_HORA ou F1\_HORA)*** de acordo se está de acordo com o horário da UF filial corrente. Caso esteja incorreto conferir os parâmetros do ERP relacionados no link abaixo:

*[Clique Aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=267794836)*

* Na rotina de transmissão de NFe, CCe, NFC-e, MDFe ou Manifesto: Acesse como Administrador a Rotina de transmissão > ***Outras ações > Parâmetros > Eventos > Horário de Verão = Não (de acordo com a UF da filial).***  
    
    
  ![HORARIO_DE_VERAO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/34112473492887)

* Acessar no **configurador: MV\_HVERAO :**

MV\_HVERAO (X6\_VAR)  
Tipo Lógico (X6\_TIPO)  
Define se o local físico do servidor está em Horário de Verão que o ERP está instalado.  
Valor Padrão .F.(sem) ou .T.(com)

* Acesse o ***appserver.ini do TSS e verifique a chave abaixo:***

SPED\_HVERAO=1(horário de verão = SIM) ou = 2 (horário de verão = NAO).

* ***Exemplo:***  
  [Environment]  
  SPED\_HVERAO=2  
  OBS: Após alterar o ini do TSS o mesmo deverá ser reiniciado.

* **Saiba mais:**

*[Alteração do Parâmetro MV\_HORARMT\_TRKVZW](http://tdn.totvs.com/pages/viewpage.action?pageId=189301887)*

*[Parâmetro MV\_HORANFE - TFJKB0](http://tdn.totvs.com/pages/viewpage.action?pageId=36307649)*

*[MV\_HVERAOI e MV\_HVERAOF - Documentos de Entrada e Saída\_TSBBUX](http://tdn.totvs.com/pages/viewpage.action?pageId=189316246)*
