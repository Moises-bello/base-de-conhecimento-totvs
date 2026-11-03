---
article_id: 7898129522967
category: Meu RH - Pagamento
content_hash: 0b9cad4abd2ece688f29ced7e09d00651b73fef2e488e9a3fe4e2d9cddfb3dfc
fetched_at: '2026-06-28T22:47:33.874629+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: RH - RM - Meu RH - Evento não aparece no envelope de pagamento do Meu RH
type: support-article
updated_at: '2026-02-27T18:38:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7898129522967-RH-RM-Meu-RH-Evento-n%C3%A3o-aparece-no-envelope-de-pagamento-do-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22519061889303) Tempo aproximado para leitura: **00:02:27 min**  
  
**Dúvida**  
Um determinado evento é apresentado no envelope do funcionário ao conferir via **RM,** porém o mesmo evento não aparece no Envelope do **Meu RH**, como proceder?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – Todas as versões  
  
**Solução**  
Quando um determinado evento aparece no envelope via **RM** porém não aparece no envelope via **Meu RH**, conforme exemplo abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7923192810391)  
  
Para solução deverá acessar Folha de Pagamento / Configurações / Parametrizador / RM Portal / Edite o Quiosque / Demonstrativo de pagamento e **desmarque** o parâmetro **"Usar Chaves Ativas para filtrar eventos do envelope"**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7922554992279)  
  
Após salvar a alteração, poderá acessar o Envelope de Pagamento via **Meu RH**, onde o evento será apresentado normalmente.  
  
**Importante**  
Não é necessário marcar este parâmetro para utilização do **Meu RH**, o mesmo foi criado para ocultar eventos do tipo Base de Calculo no **Portal RH (legado)**, porém para o **Meu RH**, os eventos do tipo Base de Cálculo já são **ocultos por padrão**.
