---
article_id: 31958025784471
category: Folha Mensal
content_hash: 46193befb2da49f1fe468f0cfa228503e4505bc85049399c8bc1419fabc20f04
fetched_at: '2026-06-28T22:46:58.126625+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Como incluir os novos códigos de cálculo do Empréstimo Consignado
  - Crédito do Trabalhador
type: support-article
updated_at: '2025-07-28T16:33:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31958025784471-RH-RM-FOP-Como-incluir-os-novos-c%C3%B3digos-de-c%C3%A1lculo-do-Empr%C3%A9stimo-Consignado-Cr%C3%A9dito-do-Trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31958025764375) Tempo aproximado para leitura: 00**:02:26 min** **Dúvida**  
Como incluir os novos códigos de cálculo do empréstimo Consignado  - Crédito do Trabalhador ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches: 12.1.2406.287; 12.1.2410.257; 12.1.2502.160; 12.1.2506.104 e superiores

**Solução**Para que os novos códigos de cálculo referentes ao Empréstimo Consignado - Crédito do Trabalhador estejam disponíveis para uso no sistema, é necessário seguir os passos abaixo:

1. Verifique se o ambiente está atualizado com os Patches a seguir (ou versões superiores);

* 12.1.2406.287
* 12.1.2410.257
* 12.1.2502.160
* 12.1.2506.104
* e superiores

2. Realize algum **recálculo** de  envelope na base (pode ser feito para qualquer funcionário).  
Esse procedimento é essencial, pois é durante o recálculo que os novos códigos de cálculo são criados automaticamente na base. Para mais informações sobre recálculo [CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8184130685335-RH-RM-FOP-Recalcular-envelope);

3. Após o recálculo, os eventos devem ser [cadastrados manualmente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412771329815), vinculando cada um ao respectivo código de cálculo criado. No menu **Administração de Pessoal | Eventos**, crie os eventos utilizando os novos códigos de cálculo listados abaixo, conforme especificado na documentação.

* [480 - Desconto Empréstimo Crédito do Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=937704422)
* [481 - Provisão Empréstimo Crédito do Trabalhador Folha](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311697)
* [482 - Remuneração Base Empréstimo Crédito do Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311709)
* [483 - Insuficiência Saldo Empréstimo Crédito Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311723)
* [484 - Provento Provisão Empréstimo Créd.Trab.Folha](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311735)
* [485 - Provisão Crédito Do Trabalhador Férias 1º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707652)
* [486 - Provisão Crédito Do Trabalhador Férias 2º Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707666)
* [487 - Provisão Crédito Trab. Férias 1º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707675)
* [488 - Provisão Crédito Trab. Férias 2º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707680)
* [489 - Adiantamento Provisão Emprést.Crédito](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707701)

**Importante**A parametrização necessária para cada código de cálculo está detalhada nos links indicados acima.  
  
Finalizadas as configurações, o sistema estará pronto para a correta utilização dos novos cálculos relacionados ao Crédito do Trabalhador.  
  
**Saiba mais**

* [RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
* [RH - RM - FOP - Empréstimo consignado Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30965515667607-RH-RM-FOP-Empr%C3%A9stimo-consignado-Cr%C3%A9dito-do-Trabalhador)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
