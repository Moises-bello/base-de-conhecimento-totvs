---
content_hash: f7252d5658b445f58b27a0643de36fa90e9e4842dc993fc17774c6e7abe34854
fetched_at: '2026-06-29T00:09:35.874089+00:00'
page_id: '425459406'
product: rm
source: tdn-rm
title: Linha RM x TOTVS By You ECM (GED) - Processo Sincronizar Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459406
version: 3
---

**Processo Sincronizar Usuários**

---

A integração entre o Corpore RM e o GED – TOTVS By You ECM possibilita realizar a partir de qualquer visão o upload de arquivos do Corpore para o ECM.

Para o usuário que realizou o upload acessar o arquivo dentro do ECM é necessário que o mesmo seja cadastrado no ECM. Este cadastro pode ser realizado através do processo "Sincronizar usuários do ECM com o GED", que exporta o usuário selecionado no Corpore RM para o ECM.

O usuário exportado será cadastrado no GED no Grupo de Usuário definido nos parâmetros da integração.  A senha que o usuário utiliza no RM não é sincronizada. O usuário é exportado com uma senha padrão.

Esta senha padrão deve ser alterada pelo supervisor do ECM, que também deve definir as configurações de segurança para o usuário, bem como os ajustes necessários no cadastro do mesmo. Somente após a alteração da senha o usuário exportado conseguirá acessar o ECM.

As permissões de acesso do usuário a um documento enviado ao ECM irão depender se o documento está em uma pasta visível ao grupo de usuário. Sendo assim, os usuários exportados ao ECM que fazem parte do mesmo grupo poderão visualizar todos os documentos postados na pasta referente aquele grupo.

É possível selecionar mais de um usuário ao mesmo tempo, sendo que apenas os usuários ativos podem ser sincronizados. Caso sejam selecionados usuários inativos, ao realizar a sincronização esses usuários serão ignorados pelo processo, não aparecendo na visão do mesmo.

Para realizar a sincronização de usuários, o supervisor do sistema deve configurar adequadamente as permissões de acesso a esta função. Apenas usuários que tenham acesso conseguirão realizar a exportação de usuários

O processo está disponível em:

Serviços Globais | Segurança | Usuários | Processos | Sincroniza usuários do Corpore RM com o GED.

Para utilizar o serviço é necessário que a integração Corpore RM x GED (TOTVS By You ECM), nos parâmetros do TOTVS Business Connect esteja configurada.
