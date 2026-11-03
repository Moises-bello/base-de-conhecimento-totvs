---
article_id: 360000837688
category: Ferramentas
content_hash: 83550ef99126d5b6bab02357642a2b914439206d3349ad3aef18ed1fe525a0c6
fetched_at: '2026-06-28T22:42:18.046891+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - Mensagem de erro TopConnect - Excedeu Licenças
type: support-article
updated_at: '2024-05-09T11:13:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000837688-Framework-Linha-Protheus-Mensagem-de-erro-TopConnect-Excedeu-Licen%C3%A7as
---

**Dúvida**O que fazer quando aparecer a mensagem TopConnect: Excedeu Licenças?  
 **Ambiente**Protheus - Todo o sistema - Todas as versões  
  
**Solução**Se aparecer no sistema a mensagem **TopConnect: Excedeu Licenças**, primeiro verifique se não estão realmente sendo utilizadas todas as licenças de DBAccess que você tem no **Servidor de Licenças**. Caso não esteja, existe um problema com o **consumo de licenças** do DBAccess. Neste caso, seguem as verificações que devem ser feitas:

1. Abra o **DBAccess Monitor** e verifique, na aba **Informações**, para quantos usuários está registrado (ou para quantos Processadores). Se estiver registrado para 2 usuários, o DBAccess não pegou licenças no **LSVirtual**;
2. Abra a aba Configurações/**Gerais**, e confirme se o Servidor de Licenças está apontado para o **IP** e **Porta** corretos do LSVirtual. Caso esteja incorreto, corrija, clique em **Salvar**, e reinicie o DBAccess;
3. Se o DBAccess estiver apontando corretamente para o LSVirtual, abra o **Monitor de Licenças** do LSVirtual, e verifique, na tela principal, se estão listadas as licenças de DBAccess. Se não estiverem, acesse o Portal do Cliente / **Gestão de Licenças**, aba **Licenças**, clique sobre a licença DBAccess, e distribua a mesma para o Totvs ID que você está utilizando no LSVirtual. Após distribuir, clique em **Salvar**, e então, no Monitor de Licenças do LSVirtual, clique no **ícone em forma de antena**, espere sincronizar, e então clique para atualizar a tela. Após aparecerem as licenças DBAccess, reinicie o **DBAccess**.
