---
article_id: 12500024189335
category: Materiais - Compras (SIGACOM)
content_hash: 47e79459290c1ced967a0a387bd6f3b7f244651e34dcafc004db0e0ae5adf51b
fetched_at: '2026-06-28T22:41:11.557553+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Ao gerar o pedido
  de compras, utilizando moeda 2 (MV_UNIDCOM = 2), o sistema não está gravando os
  dados da C1_PEDIDO  e item da C1_ITEMPED
type: support-article
updated_at: '2023-02-17T19:02:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12500024189335-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Ao-gerar-o-pedido-de-compras-utilizando-moeda-2-MV-UNIDCOM-2-o-sistema-n%C3%A3o-est%C3%A1-gravando-os-dados-da-C1-PEDIDO-e-item-da-C1-ITEMPED
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao gerar o pedido de compras, utilizando moeda 2 (MV\_UNIDCOM = 2), o sistema não está gravando os dados da C1\_PEDIDO e item da C1\_ITEMPED  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**Realizado o ajuste para que o Pedido de Compras e o Pedido de Importação fiquem com o mesmo status (C7\_CONAPRO E W2\_CONAPRO), utilizando o recklock, ao invés do update, assim o registro será atualizado antes do término do processo, atualizando os dados de vínculo do Pedido de Compras e Solicitação de Compras e a informação das unidades de Medida 1 e 2 corretamente para a função de geração do Pedido de Compras.

Além da atualização dos fontes desta correção, será necessário atualizar dicionário via expedição continua.

Para o funcionamento em releases inferiores a 12.1.33 será necessária a atualização manual do dicionário.

Foi criado o parâmetro MV\_EXECCOM, para que seja reativada a utilização do execauto nas rotinas de importação, afetando a performance da integração. (valor default = .F., não utiliza o execauto)

Criação do Parâmetro no Configurador:

![fig1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12499637124503)

![fig2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12499654616215)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
