---
article_id: 360035443974
category: RH - Contabilização
content_hash: afd3b6241d9b9f6a318dd5e295e8b6fd986211371114ac5d0129fabc65c438bf
fetched_at: '2026-06-28T22:43:45.933180+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização de filiais por usuários diferentes
  através do parâmetro MV_MULTSRZ (GPEM110)
type: support-article
updated_at: '2025-07-30T14:59:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035443974-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-de-filiais-por-usu%C3%A1rios-diferentes-atrav%C3%A9s-do-par%C3%A2metro-MV-MULTSRZ-GPEM110
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**É possível contabilizar filiais de um mesmo grupo de empresas por usuários diferentes?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Para atender essa necessidade foi criado o parâmetro MV\_MULTSRZ para possibilitar a contabilização de filiais de um mesmo grupo de empresas por usuários diferentes.  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047015833/mceclip0.png)**  
  
No processo de contabilização usual, é criada a tabela SRZ padrão conforme nomenclatura definida no dicionário de dados do Protheus, e o acesso a essa tabela é realizado de modo exclusivo, ou seja, não permite o seu uso simultâneo por mais de um usuário.  
  
Com a definição da contabilização por usuário através do parâmetro MV\_MULTSRZ, a tabela SRZ será criada com outra nomenclatura e em **memória**(ou seja, não estará acessível via banco de dados) durante toda a sua operação sem a gravação de novos registros na tabela SRZ, composta por: "SRZ" + Cód. Grupo + Id. Usuário. Dessa forma, com cada usuário possuindo sua própria tabela, a contabilização poderá ser realizada simultaneamente por usuários diferentes acessando o mesmo grupo de empresas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407919358487/mceclip0.png)

**CONFIGURAÇÃO DE PARÂMETROS:**

**1.**No Configurador (SIGACFG), acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Configure o parâmetro, conforme instruções a seguir:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046154674/mceclip2.png)
