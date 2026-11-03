---
article_id: 40821231566231
category: Automação Fiscal
content_hash: 94ce691d54314a2951a9bf43cba901fccae827fa262a3027b3915cf59a2eb8f1
fetched_at: '2026-06-28T22:36:34.927501+00:00'
product: protheus
section_id: 1500001533341
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Automação Fiscal - Arq. Magnéticos
  - ''Importação SmartSchedule habilitada, não é possível executar a extração fiscal
  manualmente."
type: support-article
updated_at: '2026-05-29T14:18:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40821231566231-Cross-Segmentos-Backoffice-Protheus-Automa%C3%A7%C3%A3o-Fiscal-Arq-Magn%C3%A9ticos-Importa%C3%A7%C3%A3o-SmartSchedule-habilitada-n%C3%A3o-%C3%A9-poss%C3%ADvel-executar-a-extra%C3%A7%C3%A3o-fiscal-manualmente
---

**Ocorrência**  
Ao utilizar o extrator fiscal é apresentada a mensagem '''Importação SmartSchedule habilitada, não é possível executar a extração fiscal manualmente."

![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40821295894423)

**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - A partir da versão **12.1.2410**

**Causa**  
O incidente ocorre devido à versão desatualizada do fonte TAFA613, ou à ativação da integração via Smart Schedule na sua Wizard do TAF.

**Solução**  
Para a utilização do extrator fiscal, é necessário que o fonte TAFA613 esteja atualizado, com a versão igual ou superior ao pacote de correção mencionado a seguir;

* 12.1.2310:<https://r.totvs.io/p/1240175> ;
* 12.1.2410:<https://r.totvs.io/p/1240176> ;
* 12.1.2510:<https://r.totvs.io/p/1240177> ;

Verifique se o parâmetro MV\_TAFISCH está configurado com o valor "0". Caso esteja ativo, significa que a configuração para utilização da integração via Smart Schedule foi realizada. Nesse modelo de integração ativo, não será possível utilizar o extrator fiscal.
