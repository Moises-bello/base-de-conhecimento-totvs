---
content_hash: 57623ca8537111de4691f3b95181d0da019136ca479ad83ab53768cf798e41d9
fetched_at: '2026-06-29T00:10:59.111326+00:00'
page_id: '611307804'
product: rm
source: tdn-rm
title: Assinatura Eletrônica - Aditivos Contratuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611307804
version: 5
---

---

Após habilitar a utilização de Assinatura Eletrônica para os Aditivos de Contratuais em, aba **Projeto | TOTVS Construção Obras e Projetos | Projetos (ou atalho F6) | Contratos | Assinatura Eletrônica;**

Ao acessar a Funcionalidade de Aditivos de Contratuais em, aba **Controle | Contrato | Anexo Aditivos de Contratuais,**no Menu do Anexo é exibido um ícone referente a Funcionalidade da Assinatura Eletrônica: 

Ao selecionar um Aditivo e clicar no ícone da Assinatura, o sistema irá direcionar para a tela de login do Portal do Totvs Assinatura Eletrônica, onde se deve inserir os dados de e-mail e senha. Nesta mesma tela é possível alterar uma senha que tenha "esquecido" e/ou realizar um novo cadastro.

Validade do Login

**Atenção:**

Por questões de segurança, e para garantir a confiabilidade dos documentos enviados, o login tem validade de **12 horas**. Ou seja, passado esse tempo, o sistema irá solicitar um novo Login para a próxima utilização da Assinatura Eletrônica.

 Após efetuar o login, o sistema irá apresentar a tela de Edição do Aditivo, com o Anexo de **Integração TOTVS Assinatura Eletrônica** aberto.

Ao inserir um novo registro Deve-se informar na aba **Identificação**o**Nome do documento**, e Buscar nos **Arquivos** o Documento que será submetido a Assinatura, para isto basta clicar na Opção Selecionar o Arquivo ou selecionar um relatório criado ou importado no RM Reports, sendo que essa opção somente estará disponível se o parâmetro "Relatório Default" tiver sido informado. Veja:

Anda nesta tela, na aba **Destinatários** deve-se inserir os e-mails dos usuários que deverão receber o Documento para Assinatura no TOTVS Assinatura Eletrônica. O TCOP não irá permitir a inclusão do documento caso não tenha definido os destinatários.

**Importante:**Os contatos do Cliente/Fornecedor serão automaticamente exibidos nesse cadastro para definição de Assinantes e Validadores.

Podemos também fazer uma pesquisa por Cliente/Fornecedor. Somente Clientes / Fornecedores que possuem E-mail aparecerão nesta listagem. Sendo assim, basta selecionar o Cliente /Fornecedor e adicioná-lo à lista de Destinatários.

Ao selecionar os Destinatários, deve-se informar na tela se os mesmos são **Assinante**ou **Validador,**onde o Assinante irá autenticar o Documento com a sua Assinatura via Portal e o Validador vai testemunhar a Assinatura.

Ao Salvar os registros será habilitado a opção de **Visualizar Arquivo**para fins de conferência do Arquivo que foi enviado para Assinatura, e então o status do Documento se mantém como **Pendente** até que o mesmo seja Assinado.

Se o parâmetro de projeto **Bloquear Processos dependentes da Assinatura,**para os Aditivos Contratuais, estiver marcado, as seguintes rotinas serão validadas em suas execuções:

* Se o documento não estiver assinado não será permitido executar:
  + Não utiliza Status de Contrato:
    - Medição do item do Aditivo / Consumo de objeto do Aditivo;
  + Utiliza Status de Contrato:
    - Alteração do Status do Aditivo. Os Status considerados são: Em Andamento, Cancelado, Paralisado e Concluído;
* Se o documento estiver assinado não será permitido executar:
  + Associação de itens ao Aditivo / Associação de objetos ao Aditivo;
  + Alteração no Aditivo;

| **Importante:**   * **A partir da versão 12.1.32, para que a real situação dos documentos possa ser consultada corretamente, é necessário configurar em "Aba Ambiente | Parâmetros | Parâmetros Globais | Aba Integração com TOTVS Sign", o Usuário de serviço e sua senha, onde esse usuário deverá estar cadastrado no portal do TOTVS Assinatura e deverá ter as devidas permissões de consulta que serão definidas no momento da implantação da ferramenta.** |
| --- |

[Voltar](https://tdn.totvs.com.br/pages/viewpage.action?pageId=611021102)
