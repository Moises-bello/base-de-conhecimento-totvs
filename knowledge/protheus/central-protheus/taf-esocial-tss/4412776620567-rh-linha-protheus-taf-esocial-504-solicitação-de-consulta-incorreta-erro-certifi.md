---
article_id: 4412776620567
category: TAF - eSocial -TSS
content_hash: fe16e86ae5d55b838e67db71d964d9b4a108afb4c6f1806feaa7fed47235a6c1
fetched_at: '2026-06-28T22:45:21.899995+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - 504 - Solicitação de consulta incorreta
  - Erro: Certificado'
type: support-article
updated_at: '2026-06-23T11:26:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412776620567-RH-Linha-Protheus-TAF-eSocial-504-Solicita%C3%A7%C3%A3o-de-consulta-incorreta-Erro-Certificado
---

**Dúvida**Como corrigir o erro 504 - Solicitação de consulta incorreta - Erro: Certificado no TSS ao transmitir os eventos para o e-Social?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial  - Todas as versões

**Solução**1 - Este problema ocorre quando existem dois serviços do TSS apontando para o mesmo banco de dados e consequentemente gera o erro de transmissão para o e-Social;

2 - Uma das soluções é criar um novo banco de dados e apontar um dos serviço para o novo banco de dados conforme material de apoio:  
[TAF - CONFIGURAÇÃO - Criando e/ou testando conexões com o DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034395574-TAF-CONFIGURA%C3%87%C3%83O-Criando-e-ou-testando-conex%C3%B5es-com-o-DBAccess)

3 - Outra alternativa é deixar um único serviço ativo para enviar os dados ao e-Social apontando o IP e Porta do serviço que desejar deixar ativo e neste caso configurar o Certificado Digital apontando para o novo serviço ativado:  
[TAF - Configuração - Como configurar o Certificado Digital no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001814402-TAF-Configura%C3%A7%C3%A3o-Como-configurar-o-Certificado-Digital-no-TAF)
