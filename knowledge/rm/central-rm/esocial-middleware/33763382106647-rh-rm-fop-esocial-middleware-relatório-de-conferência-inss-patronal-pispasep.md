---
article_id: 33763382106647
category: eSocial - Middleware
content_hash: 250e4d642a25edc803837b930b4216f159bb30cd9f175978eefefbc8161b5aa1
fetched_at: '2026-06-28T22:47:05.510314+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: Relatório de Conferência INSS Patronal
  - PIS/PASEP'
type: support-article
updated_at: '2026-02-02T17:27:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33763382106647-RH-RM-FOP-eSocial-Middleware-Relat%C3%B3rio-de-Confer%C3%AAncia-INSS-Patronal-PIS-PASEP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33763373409687) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como gerar o Relatório de Conferência INSS Patronal para consultar as bases e valores do PIS/PASEP?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - Todas as versões  
  
**Solução**  
Foi implementada no **Relatório de Conferência INSS Patronal** uma nova funcionalidade que permite comparar a **base e o valor do PIS/PASEP** calculados pelo sistema com os dados enviados ao **eSocial no evento S-5011**.

A atualização inclui uma **aba exclusiva para o PIS/PASEP**, pois a base no S-5011 é retornada **por filial**. Após atualização da versão, é necessário executar o **RM.Atualizador.exe** para criação dos novos campos no relatório.  
  
Exemplo   
Relatório de Conferência INSS Patronal campo PIS - FOLHA DE SALARIOS;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33763849448727)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33763938858135)![](https://centraldeatendimento.totvs.com/hc/article_attachments/33764143592855)

**ATENÇÃO:** A base de cálculo do PIS/PASEP (tag <vrBcPisPasep> do S-5011) é retornada por filial, e não por lotação tributária. Diante disso, foi necessário criar uma aba separada no relatório especificamente para o PIS/PASEP.

**Saiba mais:**  
[Relatório de Conferência INSS Patronal](https://tdn.totvs.com/pages/viewpage.action?pageId=714242305)
