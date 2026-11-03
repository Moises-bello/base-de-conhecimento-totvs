---
article_id: 360000590008
category: License Sever Virtual
content_hash: 880da43b6ac8800056e7e3862dfbc2389028f04e4ac5903ab8280830344cf7e5
fetched_at: '2026-06-28T22:42:20.019275+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - Como utilizar arquivo de emergência
type: support-article
updated_at: '2025-08-15T20:23:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000590008-Framework-Linha-Protheus-Como-utilizar-arquivo-de-emerg%C3%AAncia
---

**Dúvida**Como aplicar arquivo de emergência?  
  
**Ambiente**Protheus - LS Virtual  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:1. Acesse o **Portal do Cliente**: <http://suporte.totvs.com>  
2. No **menu**, clique em **Atendimento CST**;  
3. Clique em **Senhas**, **Chave/Arquivo de Emergência;**  
4. Baixe o arquivo **emergency.key** (se estiver como emergency\_XXXXXXXX.key, ou seja, com o número do seu *hardlock*, renomeie e deixe apenas emergency.key);  
**5. Pare o **License Server Virtual**;  
6. Copie o arquivo **emergency.key** para a pasta indicada pela chave StartPath, que se encontra no arquivo appserver.ini da instalação.  
7. Inicie o License Server Virtual**.****

**Ao iniciar o monitor do TOTVS | License Server, uma tela de boas-vindas será exibida. Em seguida, será solicitado o CNPJ.**

Informe o CNPJ existente no arquivo de emergência que deve coincidir com o CNPJ da empresa escolhida pelo usuário.

Documentação completa: [Utilização da chave/arquivo de emergência no LSV](https://tdn.totvs.com/pages/viewpage.action?pageId=977197384)
