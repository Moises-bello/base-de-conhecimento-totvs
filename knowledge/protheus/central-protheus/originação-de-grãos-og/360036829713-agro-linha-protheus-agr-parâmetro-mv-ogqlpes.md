---
article_id: 360036829713
category: Originação de Grãos (OG)
content_hash: 49fdc9dca36b2ac9dc9b8a1fba02ca3be2b3edf95c9a7367511ec9fae95ced84
fetched_at: '2026-06-28T22:45:42.574301+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetro MV_OGQLPES
type: support-article
updated_at: '2025-05-05T13:28:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036829713-Agro-Linha-Protheus-AGR-Par%C3%A2metro-MV-OGQLPES
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20508406378647)**Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Para que serve o parâmetro **MV\_OGQLPES**?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O parâmetro **MV\_OGQLPES** - **Validar o Parecer da Qualidade** é do tipo caracter e está localizado na rotina **OGA250** - **Romaneio com Pesagem**. Se o parâmetro não existir, o Sistema considera o parâmetro como **.F.** - **False**. Porém, se estiver com o conteúdo **.T.** - **True** indica que irá validar o **Parecer da Qualidade** antes de efetuar a pesagem, bloqueando-a se o parecer não existir.
