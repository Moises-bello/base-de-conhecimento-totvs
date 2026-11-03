---
article_id: 37570917977623
category: Ativo Fixo - Solicitação Baixa ou Transferência
content_hash: 2d08e808836ea220e44e6250088c33e61c82850c06b380cd89543a037e5f73ab
fetched_at: '2026-06-28T22:41:49.118125+00:00'
product: protheus
section_id: 1500001547622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA126 - Help PVBLOQ
  - Pedido de Venda Bloqueado, transferência interrompida
type: support-article
updated_at: '2026-01-12T10:40:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37570917977623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA126-Help-PVBLOQ-Pedido-de-Venda-Bloqueado-transfer%C3%AAncia-interrompida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37570917970327) Tempo aproximado para leitura: 00**:10 min**

### **Dúvida**

Ao aprovar uma transferência na rotina **ATFA126** (Transferências), o sistema impede a geração do pedido de venda apresentando o **Help: PVBLOQ**. Como proceder?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37570871172887)

### 

### **Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - Todas as versões

### **Solução**

Este incidente ocorre quando o Pedido de Venda, gerado automaticamente no processo de transferência, sofre um bloqueio de estoque ou crédito por regras de negócio do módulo de Faturamento, impedindo a continuidade da rotina no Ativo Fixo.

Para solucionar esta ocorrência, execute os seguintes passos:

1. **Atualização de Dicionário e Pacotes:** Certifique-se de que os pacotes acumulados dos módulos de Ativo Fixo e Faturamento estejam devidamente atualizados em seu ambiente.

   [Expedição Continua Backoffice Protheus - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=587835160#issues-15)

   * *Importante: Aplique pacotes de atualização primeiramente em ambiente de homologação.*
2. **Validação de Saldo:** Avalie se o ativo/produto que está sendo transferido possui saldo disponível e se não está em poder de terceiros.
3. **Configuração de Parâmetro:** Acesse o módulo Configurador (SIGACFG) e ajuste o parâmetro **MV\_VEBLQRG** para **.T.** (True).
4. **Regras de Negócio (FATA100):** Caso existam Regras de Negócio configuradas na rotina **FATA100**, avalie a necessidade de deletar ou ajustar as informações que possam estar incidindo sobre o pedido gerado.
5. **Análise de Tabelas:** Verifique a integridade das tabelas de Pedidos de Venda (**SC5** - Cabeçalho, **SC6** - Itens e **SC9** - Liberação de Pedidos), garantindo que não existam bloqueios manuais ou automáticos.
6. **Teste de Processo:** Após garantir que o pedido de venda não possui restrições, realize novamente o processo de aprovação da transferência na rotina **ATFA126**.

---

Observação: Caso possua dúvida sobre as verificações do módulo de faturamento, deve entrar em contato com o time para auxílio.
