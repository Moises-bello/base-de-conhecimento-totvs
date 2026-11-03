---
article_id: 17875953917975
category: Materiais - Compras (SIGACOM)
content_hash: 4631f49d9e1e508a2c7ecdac9f47034bd2735ccb4352691860f6891165333088
fetched_at: '2026-06-28T22:41:13.007364+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Help Ao Realizar Nota
  de Devolução de Transferência entre Filiais.
type: support-article
updated_at: '2023-09-28T14:03:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17875953917975-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-Ao-Realizar-Nota-de-Devolu%C3%A7%C3%A3o-de-Transfer%C3%AAncia-entre-Filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17875908475799) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Help Ao Realizar Nota de Devolução de Transferência entre Filiais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17875797635095)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões

**Solução**

O Help não era apresentado no passado e o comportamento foi alterado e passou a ser apresentada a mensagem , segue o retorno da Equipe do Produto abaixo com os esclarecimentos.

"Informamos que o alerta "Campo F4\_TRANFIL (transferencia Filiais) não pode estar com o conteudo 1 = Sim para operações de Devolução, utilize uma TES com conteudo 2 = Não" não é um erro.  
É um alerta recém implementado para não utilizar uma TES de Devolução configurada para uso em Transferências de filiais.  
Este tratamento foi feito devido não haver funcionalidades de automação ou amarrações no processo de Transferencia de Filiais em Devoluções e o uso da TES de devolução configurada para transferência de filiais pode causar efeitos indesejados em grande volume de itens numa nota de entrada.  
Vocês podem alterar a TES de entrada de devolução para F4\_TRANFIL = 2, ou usar uma TES de devolução normal na nota de entrada sem maiores prejuízos.  
No Link <https://tdn.totvs.com/pages/viewpage.action?pageId=784235851>  pode ser visto a origem da implementação que mudou o tratamento da TES."

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
