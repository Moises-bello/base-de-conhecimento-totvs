---
article_id: 40296207794711
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4af09a0cd1d2228c39b6e7cb09c3595040aad9b5d9ec9a1bb3511c406eb9af99
fetched_at: '2026-06-28T22:38:58.484051+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - É possível realizar
  a transferência de armazéns via MILE?
type: support-article
updated_at: '2026-05-07T12:09:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40296207794711-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-%C3%89-poss%C3%ADvel-realizar-a-transfer%C3%AAncia-de-armaz%C3%A9ns-via-MILE
---

O componente MILE não é recomendado para transferências de armazéns (MATA261) devido a limitações técnicas, pois campos de origem e destino causam duplicidade no dicionário de dados. Para viabilizar a operação via arquivos externos, recomenda-se customização para tratar os dados ou usar diretamente a rotina automática MATA261 via ExecAuto.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40296207789463) Tempo aproximado para leitura: 00**:**01:00 **min**  
  
**Dúvida**  
É possível realizar a transferência de armazéns (MATA261) através do componente MILE (Model Integration Layer Engine)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões

**Solução**

O Migrador MILE tem como objetivo principal a migração de dados, geralmente relacionados a cadastros, sendo mais utilizado em processos de implantação. Não é recomendado para a execução de rotinas operacionais do dia a dia, como transferências de estoque.

Embora o MILE possa ser utilizado em diversas rotinas estruturadas em MVC ou preparadas para execução via MsExecAuto (modelos 1 ou 2), a rotina de transferência **MATA261** apresenta limitações técnicas para essa integração.

Esta rotina possui um modelo de dados onde campos como produto, local, lote e endereço são utilizados simultaneamente para origem e destino. Como o MILE utiliza o dicionário de dados como referência — onde esses campos são únicos — ocorre duplicidade na configuração, impedindo o processamento correto.

**Passos** Para viabilizar a operação a partir da leitura de arquivos externos (como TXT), recomendam-se as seguintes alternativas:

1. **Customização:** Desenvolver um ponto de entrada ou rotina customizada responsável por ler o arquivo, tratar os campos de origem/destino adequadamente e acionar o MsExecAuto da rotina MATA261.
2. **ExecAuto (Paliativo):** Utilizar diretamente a rotina automática de Transferência entre armazéns (MATA261) via programação. [Cross Segmento - Backoffice Linha Protheus - ADVPL - Exemplo execauto MATA261](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022885712-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Exemplo-execauto-MATA261?utm_term=&utm_campaign=TOTVS_CONV_AON_MEIO_NATIVA_ASSINATURA-ELETRONICA-PLANOS-DE-VENDAS&utm_source=adwords&utm_medium=ppc&hsa_acc=5745705588&hsa_cam=23507107132&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23507109535&gbraid=0AAAAADrTa5xnBephWeGow_gXiziVLALye&gclid=Cj0KCQjw8PDPBhCeARIsAOJwmWU4iD8LeJAnySMMl8JJi8HkbdNg_e0IojmYPQg4FBtaBLA97bCK74UaArJmEALw_wcB)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
