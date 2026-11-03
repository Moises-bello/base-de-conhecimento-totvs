---
article_id: 6847169590935
category: Evento S-2240
content_hash: beaf846cd3c995df844f13dc0a6fdf147ab113c7efd7ef078836c7c3cb206c8a
fetched_at: '2026-06-28T22:45:23.601629+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Condições em que os EPI's não
  serão enviados ao SIGATAF
type: support-article
updated_at: '2025-03-03T18:13:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6847169590935-RH-Linha-Protheus-MDT-eSocial-S-2240-Condi%C3%A7%C3%B5es-em-que-os-EPI-s-n%C3%A3o-ser%C3%A3o-enviados-ao-SIGATAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372706392087)**Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Condições em que os EPI's **não** **serão enviados** ao SIGATAF.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**

Ao realizar a entrega de um EPI a algum funcionário no SIGAMDT com a integração com o eSocial (MV\_NG2ESOC) habilitada, o sistema tentará enviar o EPI ao SIGATAF/Middleware no evento S-2240. Porém existem casos em que o EPI pode não ser integrado ao SIGATAF/Middleware, entre eles: caso o funcionário para que o EPI tenha sido entregue não esteja exposto a nenhum risco ou caso o EPI que foi entregue ao funcionário não esteja vinculado a um risco a que o funcionário está exposto.  
  
**Funcionário que recebeu o EPI não exposto a nenhum risco:**

Caso o funcionário que recebeu o EPI através das rotinas de Funcionário x EPI (MDTA695) ou EPI x Funcionário (MDTA630) não esteja exposto a nenhum risco, nenhum EPI entregue à ele será integrado ao SIGATAF/Middleware. Como o sistema verifica a tabela de Riscos x EPI (TNX) para saber quais EPI's enviar para o funcionário no evento S-2240, o sistema não encontrará nenhum risco a que o funcionário esteja exposto e por esse motivo também não encontrará nenhum EPI.  
  
**EPI entregue ao funcionário não vinculado a nenhum risco a que o funcionário está exposto:**

Caso o EPI entregue ao funcionário através das rotinas de Funcionário x EPI (MDTA695) ou EPI x Funcionário (MDTA630) não esteja vinculado a nenhum risco a que o funcionário está exposto, não será enviado ao SIGATAF/Middleware. Como o sistema verifica a tabela de Riscos x EPI (TNX) para saber quais EPI's enviar para o funcionário no evento S-2240, o sistema não encontrará o EPI entregue ao funcionário relacionado a nenhum risco a que ele esteja exposto.  
  
**EPI entregue ao funcionário realizando a troca por outro EPI de mesmo C.A.:**

Sempre que houver a troca de um EPI ou uma nova entrega (que não seja a primeira) de um EPI por outro motivo, e, que esse EPI possua o mesmo **Certificado de Aprovação (C.A.)** do EPI que já entregou, ou seja, já existe um **Evento S-2240**anterior com o mesmo EPI, não será gerado outro envio do evento, pois, não existe informação para ser alterada no **S-2240**.  
  
**Importante!**

É importante lembrar que existe o parâmetro MV\_NG2VLAU que é utilizado na integração com o eSocial e que define se apenas riscos vinculados a um laudo PPRA serão considerados no envio ao SIGATAF/Middleware. Caso em alguma das situações citadas acima, os riscos a que o funcionário está exposto não esteja vinculado a um laudo PPRA, o sistema não considerará no envio ao eSocial. Por exemplo, caso o parâmetro MV\_NG2VLAU esteja com o conteúdo igual a "1" (sem aspas) e o funcionário não esteja exposto a nenhum risco vinculado a um laudo PPRA ou o EPI entregue ao funcionário não esteja relacionado a nenhum risco vinculado a um laudo PPRA, o sistema não irá considerar no envio ao SIGATAF/Middleware. Por isso, deve-se tomar cuidado com a configuração desse parâmetro.  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
