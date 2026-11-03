---
article_id: 24236507381271
category: MDFe - Manifesto de Carga
content_hash: 28c10d1e9d592c40801705327e8d76b35e9d561e0f8101077cd96c3542a8e758
fetched_at: '2026-06-28T22:40:08.325408+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - Rejeição
  686 - Existe MDF-e não encerrado há mais de 30 dias para o emitente
type: support-article
updated_at: '2025-06-10T19:14:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24236507381271-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-Rejei%C3%A7%C3%A3o-686-Existe-MDF-e-n%C3%A3o-encerrado-h%C3%A1-mais-de-30-dias-para-o-emitente
---

**Dúvida**Como proceder com Rejeição 686 - Existe MDF-e não encerrado há mais de 30 dias para o emitente ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**Para corrigir a rejeição em questão, é necessário providenciar o **encerramento do MDF-e** que está pendente em sua base.

**Para identificar** quais os MDF-es não encerrados, é necessário acessar a rotina SPEDMDFE - Outras ações - Gerenciar MDFe, na tela seguinte aparecerá todos os MDFe e a situação de cada um, verifiquei qual o MDFe que a Sefaz esta acusando como não encerrado e faça o encerramento do MDFe.

**Para encerrar** o MDFe basta marcar o MDFe desejado e depois clicar em Outras Ações e clicar em Encerrar, na sequencia deve clicar em outras ações - monitorar e informar a serie e numero do MDFe que deseja monitorar.

**Obs:** Verifique o conteúdo do parâmetro **MV\_CANCEXT**, ele verifica o numero de dias que o TSS vai verificar nas tabelas para mandar o envio do evento para a Sefaz.
