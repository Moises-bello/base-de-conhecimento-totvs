---
article_id: 4460815111063
category: ADVPL - Classe e Função
content_hash: 9c8ee7d474e4ec7d9fd252c659d25513c9b8835eb69bb505745877bb8d1482cc
fetched_at: '2026-06-28T22:40:14.107523+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Autenticar usuario
  no Active directory
type: support-article
updated_at: '2022-02-21T17:01:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4460815111063-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Autenticar-usuario-no-Active-directory
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:55 min****Dúvida**Como autenticar uma conta de usuário de um domínio baseado no ***Active Directory*** do **Microsoft Windows** no **Protheus**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**A função **ADUserValid**,  possibilita fazer a autenticação de uma conta de usuário de um domínio baseado no ***Active Directory*** do **Microsoft Windows**.  
  
**Sintaxe:**

```
ADUserValid ( < cDomainName >, < cUserName >, < cPassword > ) --> lValid
```

**Importante:**

```
Esta função suporta apenas o Active Directory, não possui suporte ao Active Directory Federation Services.  
Para uso de outros IDP (Identity provider) é necessário o Identity.  
Abaixo mais detalhes sobre estes serviços:  
O Active Directory ou AD é uma implementação da Microsoft de serviço de diretório no protocolo LDAP que armazena informações sobre objetos em rede de computadores e disponibiliza essas informações a usuários e administradores desta rede.  
O Active Directory Federation Services ou ADFS é um provedor de identidade (IDP) fornecido pela Microsoft que funciona como um intermediário a um serviço ou domínio externo e permite a consulta e uso das credenciais existentes do Active Directory.
```

**Saiba mais**  
[ADUserValid](https://tdn.totvs.com/display/tec/ADUserValid)
