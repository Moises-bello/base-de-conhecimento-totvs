---
article_id: 6294473774743
category: TAF - eSocial - Configuração
content_hash: f7d5835869b6bc6ec15a7bf93f5d803fa0b195017277a53d91e611490b40306d
fetched_at: '2026-06-28T22:45:14.422936+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Não Periódicos - Violação de integridade
  ao tentar excluir um registro no TAF
type: support-article
updated_at: '2026-06-26T11:30:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6294473774743-RH-Linha-Protheus-TAF-eSocial-N%C3%A3o-Peri%C3%B3dicos-Viola%C3%A7%C3%A3o-de-integridade-ao-tentar-excluir-um-registro-no-TAF
---

**Dúvida**Ao realizar a exclusão de um registro no TAF, é exibido um alerta com a mensagem de violação de integridade:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6294634774039)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. O evento a ser excluído no TAF, provavelmente está no layout S\_01\_02\_00 e no **sistema TAF** foi alterado para o atual leiaute S\_01\_03\_00;

2. Retorne o parâmetro do TAF,  MV\_TAFVLES para o S\_01\_02\_00 e efetue novamente a exclusão para que o sistema consiga recuperar a versão original e realizar a operação via rotina;

3. Após o processo acima, volte o parâmetro MV\_TAFVLES para o simplificado S\_01\_03\_00.

Abaixo o material para acessar o parâmetro no TAF para realizar a alteração do parâmetro:

[RH - Linha Protheus - TAF - eSocial - Atualização - Como atualizar a versão do layout no TAF E-social?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18585564590999-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%A3o-Como-atualizar-a-vers%C3%A3o-do-layout-no-TAF-E-social#:~:text=Para%20atualizar%20o%20layout%20do,TAF%20%E2%9E%A4%20Par%C3%A2metros.)
