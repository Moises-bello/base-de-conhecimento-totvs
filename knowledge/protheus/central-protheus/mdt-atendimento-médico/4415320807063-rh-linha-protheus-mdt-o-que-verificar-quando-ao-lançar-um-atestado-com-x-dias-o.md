---
article_id: 4415320807063
category: MDT - Atendimento Médico
content_hash: dc88b7bfd05da660a0e5938a0948e2cd0b1b2d7994a3efb2a199db18200cc4be
fetched_at: '2026-06-28T22:44:21.408325+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - O que verificar quando ao lançar um atestado com
  X dias o sistema considerar dias a menor
type: support-article
updated_at: '2025-03-03T18:10:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415320807063-RH-Linha-Protheus-MDT-O-que-verificar-quando-ao-lan%C3%A7ar-um-atestado-com-X-dias-o-sistema-considerar-dias-a-menor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372604016919) Tempo aproximado para leitura: **00:02:00min** **Dúvida**O que verificar quando ao lançar um atestado com X dias o sistema considerar dias a menor na rotina MDTA685?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Verifique o conteúdo do parâmetro **MV\_NG2TUAT**, pois ele pode interferir na contagem dos dias.  
  
**MV\_NG2TUAT** =Considera na impressão do atestado:  
**1**=Tempo de trabalho perdido conforme o turno   
**2**=Tempo total entre o inicio e o fim do atestado.  
  
Para acessar o parâmetro  acesse o Configurador no caminho: *Ambiente - Cadastro - Parâmetro.*Localize e edite conforme sua necessidade.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415306019735)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico) **[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)**
