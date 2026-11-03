---
article_id: 360038248513
category: Originação de Grãos (OG)
content_hash: b21b5cd40e4943b71e46c929c57c1343704a363097d7693e1a063cf4a5cc451a
fetched_at: '2026-06-28T22:45:38.867270+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Controle de alçadas no SIGAAGR
type: support-article
updated_at: '2025-06-23T15:54:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038248513-Agro-Linha-Protheus-AGR-Controle-de-al%C3%A7adas-no-SIGAAGR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20297741223063)**Tempo aproximado para leitura: **00:01:20 min**  
**Dúvida**Para que serve a utilização da rotina **ATFA003 - Alçada de Aprovação** no módulo de **Originação de Grãos**?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Essa funcionalidade propicia maior segurança no processo, pois permite definir aprovadores para que determinada operação possa ser continuada ou finalizada.

As rotinas que exigem essa aprovação de um usuário ou grupo de usuários são as que geram alguma operação financeira para pagamento, como multas, comissões ou ajustes financeiros em um contrato.  
Os processos do agronegócio que permitem o envio para aprovação de alçada são:

* **Cancelamento da Fixação**, quando informado um valor para o componente de multa e ele também esteja configurado para aprovação de alçada;
* **Solução das pendências** na rotina **OGA450 - Gestor da Entidade** quando escolhida a geração de **NDC - Nota de Débito** ou **NCC - Nota de Crédito**;
* Geração do **pagamento de comissões**.

**Importante**  
A funcionalidade de aprovação de alçada está disponível apenas quando é utilizada a**Nova Comercialização**.
