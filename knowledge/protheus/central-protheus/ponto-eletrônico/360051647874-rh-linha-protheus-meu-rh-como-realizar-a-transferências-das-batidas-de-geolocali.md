---
article_id: 360051647874
category: PONTO ELETRÔNICO
content_hash: 962306c7425a8c51ecc5dfd5c22066ecb1b380703a612763a33c7fee8644a7d3
fetched_at: '2026-06-28T22:44:36.749468+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como realizar a transferências das batidas de
  geolocalização de um funcionário ao transferi-lo
type: support-article
updated_at: '2026-06-22T18:20:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051647874-RH-Linha-Protheus-MEU-RH-Como-realizar-a-transfer%C3%AAncias-das-batidas-de-geolocaliza%C3%A7%C3%A3o-de-um-funcion%C3%A1rio-ao-transferi-lo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19283400737687) Tempo aproximado para leitura: 00:02:00 min****Dúvida**Como transferir as marcações do MEU RH junto com a transferência do funcionário ?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**A transferência de funcionários demandará o preenchimento do parâmetro **MV\_ARQTRAN** conforme o exemplo abaixo:  
  
**MV\_ARQTRAN** = **SP8SPCRFERFBSP5SPISPBSPESPKRF0RFFSP2RH3RH4RS3**Para modificar o parâmetro, acesse o **Configurador do Protheus - SIGACFG** e na rotina **Ambiente > Cadastros > Parâmetros**, localize o **MV\_ARQTRAN**, alterando com o conteúdo sugerido acima.  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/19283400739735)  
  
Após o preenchimento do parâmetro** conforme o exemplo, **execute a rotina de transferência** para levar as informações de batidas realizadas no MEU RH.  
  
Acesse o artigo abaixo para mais informações sobre o **MV\_ARQTRAN**  
[**MP - PON - Funcionamento do parâmetro MV\_ARQTRAN**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013366292-MP-PON-Funcionamento-do-par%C3%A2metro-MV-ARQTRAN)  
  
**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
[**MP - MEU RH - Como Atualizar os arquivos do Portal Meu RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
**[MP - GPE - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)****Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
