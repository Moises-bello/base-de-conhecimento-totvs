---
content_hash: e403b7298e23ee130dcd7bfe530c7b7df58c91c726954b8b9785b9c4f8aebd40
fetched_at: '2026-06-29T00:10:59.101698+00:00'
page_id: '611307773'
product: rm
source: tdn-rm
title: Assinatura Eletrônica - Cadastro de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611307773
version: 7
---

---

Após habilitar a utilização de Assinatura Eletrônica para o cadastro de Contrato em, aba **Projeto | TOTVS Construção Obras e Projetos | Projetos (ou atalho F6) | Contratos | Assinatura Eletrônica;**

Ao acessar o cadastro de Contratos em, aba **Controle | Contrato,**na barra de ferramentas da visão é exibido um ícone referente a Funcionalidade da Assinatura Eletrônica: 

Ao selecionar um Contrato e clicar no ícone da Assinatura, o sistema irá direcionar para a tela de login do Portal do Totvs Assinatura Eletrônica, onde se deve inserir os dados de e-mail e senha. Nesta mesma tela é possível alterar uma senha que tenha "esquecido" e/ou realizar um novo cadastro.

Validade do Login

**Atenção:**

Por questões de segurança, e para garantir a confiabilidade dos documentos enviados, o login tem validade de **12 horas**. Ou seja, passado esse tempo, o sistema irá solicitar um novo Login para a próxima utilização da Assinatura Eletrônica.

Após efetuar o login, o sistema irá abrir o anexo de **Integração TOTVS Assinatura Eletrônica**.

Ao inserir um novo registro Deve-se informar na aba **Identificação**o**Nome do documento**, e Buscar nos **Arquivos** o Documento que será submetido a Assinatura, para isto basta clicar na Opção Selecionar o Arquivo ou selecionar um relatório criado ou importado no RM Reports, sendo que essa opção somente estará disponível se o parâmetro "Relatório Default" tiver sido informado. Veja:

Ainda nesta tela, na aba **Destinatários** deve-se inserir os e-mails dos usuários que deverão receber o Documento para Assinatura no TOTVS Assinatura Eletrônica. O TCOP não irá permitir a inclusão do documento caso não tenha definido os destinatários.

**Importante:**Os contatos do Cliente/Fornecedor serão automaticamente exibidos nesse cadastro para definição de Assinantes e Validadores.

Podemos também fazer uma pesquisa por Cliente/Fornecedor. Somente Clientes / Fornecedores que possuem E-mail aparecerão nesta listagem. Sendo assim, basta selecionar o Cliente /Fornecedor e adicioná-lo à lista de Destinatários. 

Ao selecionar os Destinatários, deve-se informar na tela se os mesmos são **Assinante**ou **Validador,**

Se o parâmetro de projeto **Bloquear processos dependentes de Assinatura**, relacionado com o cadastro de Contrato estiver marcado, as seguintes rotinas serão validadas em suas execuções:

* Se o documento não estiver assinado não será permitido executar:
  + Faturamento Direto
  + Medição de itens / Consumo de objetos
  + Alteração de Status do Contrato
* Se o documento estiver assinado não será permitido executar:

+ Alteração do Cliente/Fornecedor
+ Associação de itens e objetos

| **Importante:**   * **A partir da versão 12.1.32, para que a real situação dos documentos possa ser consultada corretamente, é necessário configurar em "Aba Ambiente | Parâmetros | Parâmetros Globais | Aba Integração com TOTVS Sign", o Usuário de serviço e sua senha, onde esse usuário deverá estar cadastrado no portal do TOTVS Assinatura e deverá ter as devidas permissões de consulta que serão definidas no momento da implantação da ferramenta.** |
| --- |

[Voltar](https://tdn.totvs.com.br/pages/viewpage.action?pageId=611021102)
