---
article_id: 360018563352
category: Gestão de Transportes (TMS)
content_hash: 426b9b69292737c03f12f61a555ad8f8381d93a3bda7d9b686bc619d301914be
fetched_at: '2026-06-28T22:45:29.443669+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Mudança no horário de verão CT-e, MDF-e
  e CC-e
type: support-article
updated_at: '2021-08-27T12:05:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018563352-Log%C3%ADstica-Linha-Protheus-TMS-Mudan%C3%A7a-no-hor%C3%A1rio-de-ver%C3%A3o-CT-e-MDF-e-e-CC-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min****Dúvida**Qual o procedimento na mudança no horário de verão **CT-e - Conhecimento de Transporte Eletrônico**, **MDF-e - Manifesto Eletrônico de Documentos Fiscais** e **CC-e - Carta de Correção Eletrônica**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Atenção! Não foi realizada nenhuma alteração no **Protheus.**Para ocorrências em relação ao horário de verão é necessário avaliar e ajustar as informações abaixo de acordo com a situação.  
Por meio do **Configurador**, verificar os parâmetros abaixo:

* **MV\_HORARMT****.** Opções de preenchimento:
  + **1 -** Horário do **SmarClient.**
  + **2 -** Horário do **Servidor.**
  + **3**- Fuso horário da filial corrente. Para essa opção avaliar o artigo: [Logística - Linha Protheus - TMS - Configurações referente ao horário de verão quando o parâmetro MV\_HORARMT está igual a 3 - Fuso horário da filial corrente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019758691-MP-TMS0204-Configura%C3%A7%C3%B5es-referente-ao-hor%C3%A1rio-de-ver%C3%A3o-quando-o-par%C3%A2metro-MV-HORARMT-est%C3%A1-igual-a-3-Fuso-hor%C3%A1rio-da-filial-corrente-).
* **MV\_TMSHRVR****:** Define se o cliente encontra-se no período de horário de verão.
* **MV\_TMSHRFL****:** Define Filiais que não aderiram ao horário de verão e/ou possuem diferença de fuso. Ver detalhes no *link:*[Boletim Técnico TFZZMN.](http://tdn.totvs.com/pages/releaseview.action?pageId=44400927)

Após as parametrizações no **Configurador**, acessar no módulo **SIGATMS - Gestão de Transportes** a opção **Miscelânea** - **Cte** **Sefaz**. Dentro da rotina, clicar na opção **Outras Ações** / **Parâmetros** / **Eventos**e ajustar os parâmetros conforme sua região. Segue abaixo exemplo de como proceder:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014335432/mceclip1.png)

Salve as configurações dos parâmetros acima, acesse a tabela **SPED000 - Parâmetros** localizada no banco do **TSS - TOTVS Sped Service**e confira a gravação dos parâmetros abaixo:  
  
**MV\_HRVCTE**: 1 - Está em horário de verão; 2 - Não está em horário de verão;  
**MV\_HRCTE**: 1 - Fernando de Noronha; 2 - Brasília; 3 - Manaus.  
  
Este processo pode ser efetuado também por meio da opção **Atualizações** / **Recebimento**  **Entrada Documentos Clientes** e dentro da rotina clicar em **Outras Ações** / **Cálculo de Frete** / **CTE** / **Parâmetros** / **Eventos**.   
  
Para o **MDF-e** é necessário também acessar no módulo **SIGATMS** a opção **Atualizações / Viagens / Viagens - modelo 2,** e dentro da rotina clicar em **Outras Ações** / **Manutenção** / **Manifesto** / **MDF-E** / **Parâmetros** e ajustar os parâmetros conforme sua região. Segue abaixo exemplo de como proceder:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014339331/mceclip5.png)

No arquivo **appserver.ini**, disponível dentro da estrutura de pastas do **TSS**, a chave **SPED\_HVERAO**. Esta chave define se o local em que o servidor do **TSS** se encontra instalado está em horário de verão.   
  
Os conteúdos válidos são **1 - Sim** ou **2** **- Não.****Exemplo**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014338091/mceclip2.png)

Após efetuar todas as parametrizações citadas acima, é necessário retransmitir o documento, caso esteja com alguma rejeição atrelada ao horário de verão.
