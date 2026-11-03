---
article_id: 6735231841175
category: MDT - eSocial
content_hash: af82f6ecbe33d04f278259589689b040e79a1f459fa22a15fe9534e322e4d7c3
fetched_at: '2026-06-28T22:44:29.312261+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - Como ter controle sobre quais categorias de funcionários
  não terão os eventos de SST comunicados ao SIGATAF/Middleware.
type: support-article
updated_at: '2025-08-05T17:20:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6735231841175-RH-Linha-Protheus-MDT-Como-ter-controle-sobre-quais-categorias-de-funcion%C3%A1rios-n%C3%A3o-ter%C3%A3o-os-eventos-de-SST-comunicados-ao-SIGATAF-Middleware
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20283266478103) Tempo aproximado para leitura: **00:03:00 min**  
 **Dúvida**Como ter controle sobre quais categorias de funcionários não terão os eventos de SST comunicados ao SIGATAF/*Middleware*?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Foi criado do parâmetro **MV\_NG2NENV** para definir quais categorias de funcionários do eSocial **NÃO** serão integrados com o SIGATAF/Middleware, ou seja, os funcionários que tiverem suas categorias (RA\_CATEFD) inseridas no parâmetro MV\_NG2NENV não serão comunicados.  
É importante frisar que o sistema irá realizar essa validação em todos os envios dos eventos de SST (S-2210, S-2220 e S-2240) e não apenas na carga inicial do evento S-2240, como por exemplo: o evento S-2210 também não será comunicado caso a categoria do funcionário (RA\_CATEFD) que sofreu o acidente estiver contida no parâmetro MV\_NG2NENV.  
  
Detalhes sobre criação do parâmetro, consulte: [Controle de Envio dos Eventos de SST - Parâmetro MV\_NG2NENV](https://tdn.totvs.com/pages/releaseview.action?pageId=628360803)  
  
**Saiba Mais**[MDT -](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial) [eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico?page=1#articles)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
