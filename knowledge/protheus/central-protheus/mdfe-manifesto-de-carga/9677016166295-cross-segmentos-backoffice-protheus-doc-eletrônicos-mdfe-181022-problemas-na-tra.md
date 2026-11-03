---
article_id: 9677016166295
category: MDFe - Manifesto de Carga
content_hash: 8ae6979e0f811a4a1d20ef30aa2c457d64a271162ad1e14888c9fb3ed1aec722
fetched_at: '2026-06-28T22:40:08.228283+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFe - 18/10/22
  Problemas na transmissão do MDFe, "Aguardar processamento do lote" ou "Contigencia
  autorizada".
type: support-article
updated_at: '2022-10-21T14:13:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9677016166295-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFe-18-10-22-Problemas-na-transmiss%C3%A3o-do-MDFe-Aguardar-processamento-do-lote-ou-Contigencia-autorizada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como resolver o incidente abaixo?  
Ao transmitir e monitorar o MDFe fica em constante "Aguardar processamento do lote" ou "Contingencia autorizada", e não evolui.  
Erro no console do TSS: **THREAD ERROR ([12428], IPC\_CONT, THIS) 19/10/2022 09:09:44**  
**invalid property \_DHRECBTO on TSSMDFERECEPCAO(TSSPROCMDFE.PRW) 04/01/2022 16:45:47 line : 685**

**Ambiente**Cross Segmentos - TSS - a partir da versão 12

**Solução**

Prezado Cliente,

Foi identificado um problema na transmissão do MDF-e, apresentando as mensagens "Aguardar processamento do lote" ou "Contingencia autorizada", e não evolui.

O problema ocorreu devido a uma alteração no retorno da Sefaz, sem aviso prévio, que deixou de retornar uma tag obrigatória, onde para os manifestos que retornam alguma rejeição sofrem esse impacto.

Para contornarmos o problema, inicialmente foi disponibilizado um pacote emergencial e posteriormente o pacote oficial homologado.  
O pacote homologado foi expedido, conforme links a seguir:

- Link do pacote oficial release 12.1.33: <https://suporte.totvs.com/portal/p/10098/download?e=1085125>  
- Link do pacote oficial release 12.1.2210: <https://suporte.totvs.com/portal/p/10098/download?e=1085126>  
\*Caso tenha alguma dificuldade no download, copie o link e cole em uma nova aba ou utilize em outro navegador.  
  
- O patch deve ser aplicado no rpo do TSS, de acordo com a release em seu ambiente de TSS. Exemplo 12.1.33 ou posterior.  
- Segue orientações sobre como aplicar patch no TSS: [Cross Segmentos - TOTVS Backoffice - Doc. Eletrônicos - Como configurar e aplicar o pacote de atualização do TSS via VSCODE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062284573-Cross-Segmentos-TOTVS-Backoffice-Linha-RM-Doc-Eletr%C3%B4nicos-Como-configurar-e-aplicar-o-pacote-de-atualiza%C3%A7%C3%A3o-do-TSS-via-VSCODE?source=search)

Após a atualização, os manifestos que estavam pendentes devem ter o retorno atualizado no monitoramento, sendo necessário corrigir as rejeições retornadas pela Sefaz para fazer uma nova transmissão.
