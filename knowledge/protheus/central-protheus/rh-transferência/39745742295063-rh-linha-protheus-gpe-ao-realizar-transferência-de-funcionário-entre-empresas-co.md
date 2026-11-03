---
article_id: 39745742295063
category: RH - Transferência
content_hash: 1246fbc7fd5b6086e498e70589fdc9845051f5ebe13e25945004c20cfadaa966
fetched_at: '2026-06-28T22:43:23.283215+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao realizar transferência de funcionário entre
  empresas com CNPJs diferentes ocorre erro Não foi possível gerar o XML para o evento:
  S-2200 / S-2240'
type: support-article
updated_at: '2026-04-14T19:24:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39745742295063-RH-Linha-Protheus-GPE-Ao-realizar-transfer%C3%AAncia-de-funcion%C3%A1rio-entre-empresas-com-CNPJs-diferentes-ocorre-erro-N%C3%A3o-foi-poss%C3%ADvel-gerar-o-XML-para-o-evento-S-2200-S-2240
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39745742254231) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Ao realizar transferência de funcionário entre empresas com CNPJs diferentes ocorre erro Não foi possível gerar o XML para o evento: S-2200 / S-2240.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39745742259607)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Conforme orientação do módulo SIGATAF, foi implementado um processo em thread paralela para execução da transferência. Nesse processo, é realizado o login correto na empresa e filial de destino, garantindo o contexto adequado para a operação. Após isso, é chamada a função TafPrepInt() do SIGATAF para a geração dos eventos no ambiente de destino, assegurando a busca correta do evento S-2200 antes da geração do S-2240.

Para correção realize a atualização do ambiente com o pacote de correção conforme release do ambiente:

12.1.2310:<https://r.totvs.io/p/1243919> **(****SOMENTE COM GARANTIA ESTENDIDA****)**;   
12.1.2410:<https://r.totvs.io/p/1243917>;   
12.1.2510:<https://r.totvs.io/p/1243918>;

**Saiba Mais**  
[Documentação Técnica](https://tdn.totvs.com/pages/releaseview.action?pageId=1054118663)  
[RH - Transferência](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781974-RH-Transfer%C3%AAncia)
