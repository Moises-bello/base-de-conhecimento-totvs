---
article_id: 4414179017239
category: Evento S-2240
content_hash: e6118ccfca2aa4f95eada9cef7351dfad785b2e54ae0e8fa6ac995d65c9156ec
fetched_at: '2026-06-28T22:45:23.512010+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - Não existem Responsáveis Ambientais para
  o período de exposição do funcionário
type: support-article
updated_at: '2025-02-12T12:05:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414179017239-RH-Linha-Protheus-MDT-eSocial-N%C3%A3o-existem-Respons%C3%A1veis-Ambientais-para-o-per%C3%ADodo-de-exposi%C3%A7%C3%A3o-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24726579949719) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**O que verificar quando gera o relatório de inconsistência com a seguinte mensagem "Não existem Responsáveis Ambientais para o período de exposição do funcionário?"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões   
  
**Solução  
1-** Deve ser cadastrado pelo menos um laudo no sistema que compreenda o período de exposição do funcionário. O responsável pela elaboração do Laudo deve ter a função (**TMK\_INDFUN**) compreendida no parâmetro **MV\_NG2REST**, ter sua data de início (**TMK\_DTINIC**) e fim (**TMK\_DTTERM**) também compreendendo o período de exposição do funcionário e ter o indicativo de responsável ambiental (**TMK\_RESAMB**) igual a "**Sim**".  
Para avaliar esta informação acesse o Módulo Medicina no seguinte caminho: *Atualizações - Laudos - Laudos* (**MDTA210**).  
  
**2-** O CPF do responsável pelos registros ambientais (**TMK\_CIC**) deve ser preenchido.  
Para avaliar esta informação acesse o Módulo Medicina no seguinte caminho: *Atualizações - Sesmt - Sesmt Usuário Aten.* (**MDTA070**).  
  
**3-** O órgão de classe do responsável pelos registros ambientais (**TMK\_ENTCLA**) deve ser preenchido.  
Para avaliar esta informação acesse o Módulo Medicina no seguinte caminho: *Atualizações - Sesmt - Sesmt Usuário Aten.* (**MDTA070**).

**4-** O órgão de classe do responsável pelos registros ambientais (**TMK\_ENTCLA**) deve ser igual a "**CRM**", "**CREA**" ou "**Outros**". Se o conteúdo do campo de órgão de classe do responsável pelos registros ambientais (**TMK\_ENTCLA**) não tiver as expressão "**CRM**" ou "**CREA**" preenchida, será enviada como "**Outros**" automaticamente.  
Para avaliar esta informação acesse o Módulo Medicina no seguinte caminho: *Atualizações - Sesmt - Sesmt Usuário Aten.* (**MDTA070**)  
  
**5-** A descrição do órgão de classe do responsável pelos registros ambientais (**TMK\_ENTCLA**) deve ser preenchido.  
Para avaliar esta informação acesse o Módulo Medicina no seguinte caminho: *Atualizações - Sesmt - Sesmt Usuário Aten.* (**MDTA070**)  
  
**6-** O número do órgão de classe do responsável pelos registros ambientais (**TMK\_NUMENT**) deve ser preenchido.  
Para avaliar esta informação acesse o Módulo Medicina no seguinte caminho: *Atualizações - Sesmt - Sesmt Usuário Aten.* (**MDTA070**)

**7-** A UF do órgão de classe do responsável pelos registros ambientais (**TMK\_UF**) deve ser preenchida.  
Para avaliar esta informação acesse o Módulo Medicina no seguinte caminho: *Atualizações - Sesmt - Sesmt Usuário Aten.* (**MDTA070**)

How To | SIGAMDT - Responsável Ambiental  S-2240 Linha Protheus  
  
  
**Saiba Mais**  
[Como cadastrar responsáveis Ambientais para o período de exposição do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037531594-RH-Linha-Protheus-MDT-eSocial-Como-cadastrar-respons%C3%A1veis-Ambientais-para-o-per%C3%ADodo-de-exposi%C3%A7%C3%A3o-do-funcion%C3%A1rio)  
[Artigo Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051732554-MP-MDT-Pacote-acumulado-SIGAMDT)  
[Eventos SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)
