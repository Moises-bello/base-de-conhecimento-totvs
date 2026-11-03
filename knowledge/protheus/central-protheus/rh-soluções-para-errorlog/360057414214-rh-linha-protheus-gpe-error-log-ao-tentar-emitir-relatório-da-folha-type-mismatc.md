---
article_id: 360057414214
category: RH - Soluções para error.log
content_hash: d34281091c452fc3111a509dcd1194f98cc52b98474d8487428ad0cdd408c8ec
fetched_at: '2026-06-28T22:44:08.903965+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Error log ao tentar emitir Relatório da Folha -
  type mismatch on compare on GPER040(GPER040.PRX)
type: support-article
updated_at: '2022-11-08T14:54:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057414214-RH-Linha-Protheus-GPE-Error-log-ao-tentar-emitir-Relat%C3%B3rio-da-Folha-type-mismatch-on-compare-on-GPER040-GPER040-PRX
---

**Ocorrência**  
Ao tentar realizar a geração do Relatório da Folha de Pagamento Não Personalizável, através da rotina **GPER040**, é apresentado o seguinte ***error log**: **type mismatch on compare on GPER040(GPER040.PRX)***  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - à partir da versão 12.1.27  
  
**Causa**Este erro ocorre devido à incorreta configuração do Grupo de Perguntas **GPER040**  
  
**Solução**Para solucionar esta ocorrência realize o processo conforme descrito abaixo:  
  
**1.** Acesse o Módulo de **Configurador**;  
**2.** Acesse a rotina de **Base de Dados/Dicionário/Base de Dados**;  
**3.** Procure e verifique o Grupo de Perguntas **GPER040**, que deve estar conforme demonstrado no print abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/HngiEdkniChnl4sPJxyKk3S3u/?name=inline-877783605.png)  
  
Obs.: Abra a imagem apresentada em outra aba, para avaliar todos os itens.  
Obs 2.: Os itens do Grupo de Perguntas devem respeitar a Ordem e Tipo apresentadas no *print*.  
  
**Saiba mais:**  
[Pacote Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
