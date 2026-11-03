---
article_id: 39542858020247
category: Integrações - Feedz
content_hash: 1f82369247f6acbb32f0ecbaf2c9a01919c8e16fa7e4e2b617479236d05d5311
fetched_at: '2026-06-28T22:46:41.418467+00:00'
product: rm
section_id: 28212337440791
source: central-rm
title: RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Funcionários Ativos
  com o status Demitido na Feedz
type: support-article
updated_at: '2026-04-07T16:16:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39542858020247-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Funcion%C3%A1rios-Ativos-com-o-status-Demitido-na-Feedz
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39542853431063) Tempo aproximado para leitura: **00:02:15 min**  
  
**Dúvida**  
Ao consultar a plataforma Feedz, colaboradores que estão "Ativos" no RM constam com o status "Demitidos" e informações desatualizadas.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2310  
  
  
**Solução**  
Esse comportamento ocorre devido à **sobrescrita no processo de integração** entre o RM e a Feedz. Na Feedz, sempre será considerada a **última informação enviada**.

Para evitar este tipo inconsistência, é necessário configurar **dois agendamentos distintos** para a integração:

* Um agendamento exclusivo para envio de **colaboradores demitidos**
* Outro agendamento exclusivo para envio de **colaboradores ativos**

> ⚠️ **Importante:** O envio deve seguir a seguinte ordem:

1. Primeiro, executar o envio de somente **demitidos**
2. Em seguida, executar o envio de **ativos**

Essa separação é essencial porque, quando um colaborador possui **mais de um vínculo**, o envio simultâneo de registros ativos e demitidos pode gerar inconsistências. Nesse cenário, há o risco de o vínculo ativo ser enviado primeiro e, na sequência, o vínculo demitido sobrescrever as informações, fazendo com que o colaborador apareça como demitido na Feedz, mesmo estando ativo em outro vínculo.  
  
**IMPORTANTE:** Como boa prática, caso o envio de colaboradores seja diário, recomenda-se criar um filtro no agendamento que envie apenas os colaboradores demitidos cuja data de demissão seja igual à data atual. Dessa forma, registros de demissões antigas não serão reenviados, reduzindo inconsistências e ganho de performance.  
  
Caso as informações não sejam atualizadas na Feedz mesmo após o envio exclusivo de colaboradores ativos, é provável que a chapa ativa possua alguma **inconsistência cadastral**. Nessa situação, é necessário realizar as validações conforme orientações das seguintes documentações:  
  
[**RH - RM - FOP - Integração RM Labore x Feedz - Nenhum funcionário atende a seleção**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28206773411095-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-Feedz-Nenhum-funcion%C3%A1rio-atende-a-sele%C3%A7%C3%A3o)

[**RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Erro na integração com a Feedz código XXXX**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29909362246039-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Erro-na-integra%C3%A7%C3%A3o-com-a-Feedz-c%C3%B3digo-XXXX)

**Saiba mais:**

[**RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Como realizar o envio de colaboradores e associação de líderes**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29903246172695-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Como-realizar-o-envio-de-colaboradores-e-associa%C3%A7%C3%A3o-de-l%C3%ADderes)
