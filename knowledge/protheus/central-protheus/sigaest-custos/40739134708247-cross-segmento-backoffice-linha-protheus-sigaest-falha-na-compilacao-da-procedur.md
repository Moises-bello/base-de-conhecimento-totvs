---
article_id: 40739134708247
category: SIGAEST - CUSTOS
content_hash: 6b388de1abcd927ca125f57d2e26f4c0dbae9cbb3f5d2c865db1c3c0613269e0
fetched_at: '2026-06-28T22:39:00.929934+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Falha na compilacao
  da procedure 19 - DKN_FILIAL
type: support-article
updated_at: '2026-05-26T13:35:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40739134708247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Falha-na-compilacao-da-procedure-19-DKN-FILIAL
---

O erro na atualização da procedure 19 ocorre por desatualização do dicionário de dados relacionado aos impostos IBS e CBS, que fazem utilização da tabela DKN para o processo de nota de debito para apontamento de perdas sob produções ou por exemplo extravios de mercadoria. Para corrigir, é necessário aplicar a atualização do dicionário via pacote acumulado Backoffice usando o UPDDISTR, garantindo a criação correta da tabela DKN e seus campos antes de recompilar a procedure.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40739144722199) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar efetuar a atualização da procedure 19, ocorre o seguinte erro: "Falha na compilação da procedure [MAT042\_19\_01] - Erro: Campo(s) DKN\_FILIAL não localizado(s) no dicionário de dados." Como corrigir?

![ERROPROCEDURE19DKN.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40739280033047 "CLIQUE PARA VISUALIZAR A IMAGEM COMPLETA")

![ERROPROCEDURE19DKN.png Ampliada](https://centraldeatendimento.totvs.com/hc/article_attachments/40739280033047)

Para corrigir o problema apresentado, é necessário aplicar a atualização do dicionário de dados contida no pacote acumulado do Backoffice via [**UPDDISTR**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152-MP-FIS-Como-Processar-o-UPDDISTR-para-atualiza%C3%A7%C3%A3o-de-dicion%C3%A1rios?utm_term=&utm_campaign=TOTVS_CONV_AON_MEIO_NATIVA_ASSINATURA-ELETRONICA-PLANOS-DE-VENDAS&utm_source=adwords&utm_medium=ppc&hsa_acc=5745705588&hsa_cam=23507107132&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23507109535&gbraid=0AAAAADrTa5xnBephWeGow_gXiziVLALye&gclid=Cj0KCQjw8PDPBhCeARIsAOJwmWUO-27LnYv1bYIqX9c32kBKk9rS1exTR5YclfTx_W0IZ6DvqiteqcAaAgwsEALw_wcB).

Dessa forma, serão criados os registros de atualização do dicionário necessários para a criação da tabela DKN.

**Passos**

1. Acesse o portal do cliente e realize o [download](https://tdn.totvs.com/x/2hgdHw) do pacote acumulado Backoffice correspondente à sua release.
2. Aplique a atualização do dicionário de dados no ambiente de acordo arquivos contidos na pasta **SDF** do pacote backoffice (via [**UPDDISTR**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152-MP-FIS-Como-Processar-o-UPDDISTR-para-atualiza%C3%A7%C3%A3o-de-dicion%C3%A1rios?utm_term=&utm_campaign=TOTVS_CONV_AON_MEIO_NATIVA_ASSINATURA-ELETRONICA-PLANOS-DE-VENDAS&utm_source=adwords&utm_medium=ppc&hsa_acc=5745705588&hsa_cam=23507107132&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23507109535&gbraid=0AAAAADrTa5xnBephWeGow_gXiziVLALye&gclid=Cj0KCQjw8PDPBhCeARIsAOJwmWUO-27LnYv1bYIqX9c32kBKk9rS1exTR5YclfTx_W0IZ6DvqiteqcAaAgwsEALw_wcB)).
3. Certifique-se de que a tabela **DKN** e seus respectivos campos foram criados corretamente após finalização do [**UPDDISTR**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152-MP-FIS-Como-Processar-o-UPDDISTR-para-atualiza%C3%A7%C3%A3o-de-dicion%C3%A1rios?utm_term=&utm_campaign=TOTVS_CONV_AON_MEIO_NATIVA_ASSINATURA-ELETRONICA-PLANOS-DE-VENDAS&utm_source=adwords&utm_medium=ppc&hsa_acc=5745705588&hsa_cam=23507107132&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23507109535&gbraid=0AAAAADrTa5xnBephWeGow_gXiziVLALye&gclid=Cj0KCQjw8PDPBhCeARIsAOJwmWUO-27LnYv1bYIqX9c32kBKk9rS1exTR5YclfTx_W0IZ6DvqiteqcAaAgwsEALw_wcB).

   ![TABELADKN.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40739289778711)
4. Execute novamente a rotina de atualização/compilação da procedure 19.

**Saiba Mais**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o calculo do IBS e CBS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33661274329367-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-calculo-do-IBS-e-CBS)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Nota de Débito do tipo 7 Perda em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/40653605488663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Nota-de-D%C3%A9bito-do-tipo-7-Perda-em-Estoque)
