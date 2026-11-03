---
content_hash: 4325155eccb6f2dafe68a282837fbe11798676e163dcdd4b0301e1b0009f34c1
fetched_at: '2026-06-29T00:10:26.103161+00:00'
page_id: '512429100'
product: rm
source: tdn-rm
title: Conversão Cliente/Fornecedor para Global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=512429100
version: 17
---

Disponibilizado no sistema o processo de conversão de Cli/For para Global (coligada zero). Este processo é recomendado para os usuários que já utilizam ou irão utilizar os cadastros de Cliente/Fornecedor globais, e aqueles que fazem integração com o Protheus pelo módulo TOTVS Construção e Projetos e TOTVS Gestão de Estoque, Compras e Faturamento com SigaMNT.

Para disponibilizar o processo, deve ser habilitada a permissão no perfil de usuário, em:

- Serviços Globais | Perfis | (selecionar o perfil) | Editar | Aba: Acesso a Menus | [07] Utilitários | [07.04] Outros | [07.04.03] Mais ... | [07.04.03.06] Conversão Cliente\Fornecedor para Global.

Liberado no perfil de usuário, basta acessar TOTVS Gestão Financeira | Utilitários | Outros | Mais... | Conversão Cliente/Fornecedor para Global.

ConversãoInterface do Processo

Na interface do processo, o sistema disponibiliza três campos que serão utilizados no processamento do conversor:

* Coligada base para conversão: indica a coligada que será utilizada como principal no processo de conversão.
* Campos disponíveis para conversão: determinam a regra para identificação dos clientes/fornecedores “idênticos” nas diversas coligadas. Deve ser indicado pelo menos um campo.
* Quantidade de registros a serem convertidos: Ao marcar essa opção é possível definir a quantidade de registros que serão processados pelo conversor.

Execução do Processo

1. Processo na coligada base:  Ao executar o processo na coligada base, o sistema realiza a cópia dos registros dessa coligada para a coligada global (0). Após a cópia, os registros originados da coligada base serão excluídos, iniciando a verificação nas demais coligadas.
2. Cópia das demais coligadas: Nas demais coligadas, os cadastros de Cliente/Fornecedor que tenham os valores correspondentes nos “campos disponíveis para conversão” com os cadastros processados para coligada 0, serão vinculados e estes Cli/For serão excluídos.

**Importante**:

* Este processo após executado não poderá ser desfeito;
* O processo deverá ser executado para cada coligada, caso tenha registros não convertidos, por não encontrar correspondente na coligada base informada;
* O cliente/fornecedor que estiver vinculado a algum parâmetro no RM será substituído no parâmetro automaticamente.
* É indicado, em casos que não haja integração com Protheus, o uso do Código do Cli/For + CPF/CNPJ como chave para processamento do conversor.
* **ATENÇÃO:** dependendo do número de clientes/fornecedores a serem convertidos e do volume da base de dados no que diz respeito às tabelas atualizadas na conversão, este processo pode ser demorado e consumir recursos do banco de dados (volume alto de acesso ao banco de dados). Em cenário como este recomendamos a execução em períodos de baixo acesso ao banco de dados e também utilizar a conversão parcial de registros usando a opção de informar a quantidade na tela.

**Integração com Protheus**

Para base de dados que tenha integração com Protheus e que usa a mensagem de cliente/fornecedor (CUSTOMERVENDOR) após a migração dos registros para global será necessário refazer a carga inicial no Protheus para que seja restabelecido o vínculo entre os cadastros. Segue alguns pontos relevantes a serem observados:

* Os registros de "De-Para" devem ter a coligada e/ou código atualizados como Global.
* Na tela de conversão será exibido aviso para não converter a base caso exista alguma integração com mensagem de cliente/fornecedor (CUSTOMERVENDOR) ativa  no Protheus  
  para cadastro não global.

 Informações Complementares

[FIN - Cliente / Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=421388786)
