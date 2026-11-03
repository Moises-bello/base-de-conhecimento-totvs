---
article_id: 360020718912
category: NFe - Nota Fiscal Eletrônica
content_hash: 47db327ed69cb2b8e6e08b10e2c3e3b3d8237f167d0a440b6427356b38128956
fetched_at: '2026-06-28T22:40:03.170005+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  238 Rejeição :
  Cabecalho - Versao do arquivo XML superior a Versao vigente (Desacordo de CT-e)'
type: support-article
updated_at: '2025-06-11T12:29:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020718912-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-238-Rejei%C3%A7%C3%A3o-Cabecalho-Versao-do-arquivo-XML-superior-a-Versao-vigente-Desacordo-de-CT-e
---

**Dúvida**

Como corrigir a Rejeição 238 - Cabeçalho - Versão do arquivo XML superior a Versão vigente (Desacordo de CT-e)

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS

**Solução**

Significa que para essa entidade não foi realizada a configuração do parâmetro MV\_VERCTE para 4.00.

Para alterar a versão do evento de desacordo do CTE devem acessar a rotina de documentos de entrada Outras ações > Ev. Desacordo > Parâmetros:

  
![](https://totvssuporte.zendesk.com/attachments/token/qCyjzUlfbbprRiCpd5Jy2Dgvf/?name=image.png)

É importante que alterem como o exemplo da imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21224966013207)

**(FAVOR REFAZER ATÉ CLICAR NO BOTÃO "OK" PARA RECONFIGURAR O TSS)**

Além da configuração da rotina de documento de entrada devem confirmar as configurações da versão do CTE na rotina de faturamento como abaixo:

Acesse a rotina de **Faturamento > Atualizações > Nf-e e Nfs-e > Nf-e Sefaz.**

Dentro da rotina **Parâmetros > Nfe/CTE** etc. Verifique se os parâmetros estão corretos, conforme o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21224958114711)

Após informar os parâmetros nas duas rotinas, confirme clicando em + Salvar como grupo administrador e clique em "OK" para confirmar.

Obs: Caso não esteja disponível a versão 4.00 para o CT-e, será necessário atualizar a rotina SPEDNFE aplicando o patch abaixo de acordo com sua versão do Protheus (Deve ser aplicado no RPO do Protheus):

**Protheus 12.1.2210:** [Clique aqui para download.](https://suporte.totvs.com/portal/p/10098/download#detail/1081419)

**Protheus 12.1.2310:** [Clique aqui para download.](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)

**Protheus 12.1.2410:** [Clique aqui para download.](https://suporte.totvs.com/portal/p/10098/download?e=1171486)
