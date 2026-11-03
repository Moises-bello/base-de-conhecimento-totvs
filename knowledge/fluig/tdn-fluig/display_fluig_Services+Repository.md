---
content_hash: b36de11e688f93c79e5e17553b770ef92140558f48bf58d5f8e6f8df7aca9ac4
fetched_at: '2026-06-28T21:35:27.931182+00:00'
page_id: '6066538'
product: fluig
source: tdn-fluig
title: Services Repository
type: documentation
url: https://tdn.totvs.com/display/fluig/Services+Repository
version: 13
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**. 

Na aba Services Repository é possível realizar as configurações de serviços. A tela está dividida apropriadamente em dois grupos: Add Services e Services Available

### Add Services

Permite realizar as configurações de um Web Service para simulação.

| Campo | Descrição |
| --- | --- |
| Service Name | Inserir uma identificação para a configuração do serviço. |
| WSDL URL | Inserir o endereço utilizado na conexão com o web service. |
| Group | Inserir uma identificação para a grupo. |
| Comments | Inserir comentário referente ao serviço. Este comentário será exibido posteriormente na visualização de serviços disponíveis. |
| Use JAXB Binding | Quando utilizada está opção é possível realizar a customização de classes para WSDL através de um arquivo .xml. Este arquivo deve ser colocado no diretório ESB\_INSTALL\wsdl-local onde ESB\_INSTALL é o diretório de instalação do Fluig ESB. Podem ser criadas outras pastas dentro deste diretório porém o caminho seguido do nome do arquivo deve ser referenciado corretamente no campo. |
| Upload | Efetiva a criação do serviço. |

### Services Available

Permite visualizar os serviços disponíveis.

| Campo | Descrição |
| --- | --- |
| Service Name | Exibe o nome do serviço configurado |
| Comments | Exibe os comentários feitos a respeito do serviço configurado |
| Delete | Ao selecionar um serviço da tabela, e pressionar o botão 'Delete' o serviço é excluído. |
