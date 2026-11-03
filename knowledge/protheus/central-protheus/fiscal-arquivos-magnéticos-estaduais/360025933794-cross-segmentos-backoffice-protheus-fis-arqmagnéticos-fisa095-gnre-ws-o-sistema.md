---
article_id: 360025933794
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: c2fbf47bcd99ff30535c2b83aac35590886d78aabe08c935bbe6c758572f9078
fetched_at: '2026-06-28T22:42:10.901130+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - FISA095 - GNRE
  WS - O SISTEMA APRESENTA A MENSAGEM DE ZERO GNRE(s) TRANSMITIDAS
type: support-article
updated_at: '2022-08-17T20:30:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025933794-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-FISA095-GNRE-WS-O-SISTEMA-APRESENTA-A-MENSAGEM-DE-ZERO-GNRE-s-TRANSMITIDAS
---

**Ocorrência**No módulo de livros fiscais, ao tentar transmitir uma GNRE WS (**FISA095**) o sistema apresenta 0 GNRE(s) transmitidas.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041255413/mceclip1.png)

**Ambiente**Protheus – Livros  – A partir da versão 11.80]  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema está incorreta.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Certifique que o campo código de receita da operação (**F6\_CODREC**) está preenchido, por meio da rotina **MATA960**, caso não esteja, será necessário o preenchimento.  
  
2. Preencha o parâmetro **MV\_UFGNWS** com as UFs que serão transmitidas pela GNRE WS.

Exemplo:

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_UFGNWS |
| **Tipo** | Caractere |
| **Descrição** | UF que contém tratamento para transmissão da GNRE via Web Service. |
| Ex. Conteúdo | AC/AL/AM/AP/BA/CE/DF/GO/MA/MG/MS/MT/PA/PB/PE/PI/PR/RJ/RN/RO/RR/RS/SC/SE/TO |

**Importante**A GNRE será transmitida apenas se a UF estiver configurada neste parâmetro.  
  
3. As GNREs somente serão transmitidas, se a UF da guia da recolhimento estiver disponível, verifique a disponibilidade nos link abaixo:

Ambiente de homologação:  
<http://www.testegnre.pe.gov.br/gnre/portal/GNRE_DisponibilidadeUF.jsp>

Produção:  
<http://www.gnre.pe.gov.br/gnre/portal/GNRE_DisponibilidadeUF.jsp>
