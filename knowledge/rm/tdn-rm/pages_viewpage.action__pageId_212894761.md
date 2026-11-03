---
content_hash: 0425c6f2eb88c9d27a24e0af67c0770e1c3f52a6538c78795d9d454ae1576051
fetched_at: '2026-06-29T00:06:16.280386+00:00'
page_id: '212894761'
product: rm
source: tdn-rm
title: DT_Utilitário_de_Assinatura_Digital_em_Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212894761
version: 2
---

# Utilitário de Assinatura Digital em Lote

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Utilitários |
| **Rotina:** | |  | | --- | | **Rotina** | | Utilitários do RM Saúde |  |  | | --- | | **Rotina(s) envolvida(s)** | | Utilitário de Assinatura Digital em Lote | |
| **Requisito (ISSUE):** | [PCREQ-4505](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-4505 "PCREQ-4505") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle/MSSQL |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

   Implementada funcionalidade que possiblita aos usuários assinarem digitalmente todos os arquivos contidos em seu nome no sistema e que ainda não possuam a certificação digital.

## Procedimento para Implantação

 Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema(executáveis, dlls e arquivos de configuração):  
   Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

   O Patch 12.1.8 [BIBLIOTECA RM e TOTVS RM PORTAL] e 12.1.8.1 [TOTVS Gestão Hospitalar], disponíveis na Central de Download do Portal do Cliente.

   Para acesso siga as instruções abaixo:  
   1. Acesse a Central de Download em [www.totvs.com/suporte](http://www.totvs.com/suporte).   
   2. Faça o login, com seu E-mail e Senha.

   3. Na barra de menu superior, clique em DOWNLOAD.

   4. No boxe Central de Downloads aplique os filtros conforme campos abaixo:  
   a. Linha: RM  
   b. Versão: RM 12.1.8  
   c. Tipo: Patch

   Pronto! Todos os instaladores correspondentes do filtro aplicado no passo 4 serão disponibilizados para download.

   Para iniciar o download do arquivo, clique na figura com uma seta para baixo localizada na primeira coluna da grid. Escolha o método mais apropriado de download e salve o arquivo na pasta desejada.  
   Importante: Caso algum produto não tenha sido exibido no filtro acima, entende-se que não houve demanda de atualização para essa versão.

   Dica: Para facilitar na busca do arquivo, utiliza-se o campo "Filtro" da grid de download, digitando o nome do arquivo ou parte do mesmo para pesquisa/download.

```
Procedimento para Configuração
```

```
CONFIGURAÇÃO DE PARÂMETROS
```

```
      
```

```
Parâmetros Gerais:
```

1. ```
   No Menu "Opções / Parâmetros / Parâmetros Gerais", aba "Prontuário Eletrônico", Sub Aba " Assinatura Digital",  os "CheckBox" "utiliza Certificação Digital no PEP" e "Filtra Certificados Pelo CPF do prestador". Preencher também a URL do WebService para assinatura.
   ```
2. ```
   Na aba "Geral", marcar o CheckBox "Gravar Arquivos no Banco de Dados e informar o caminho da pasta, que sistema utilizará para manipulação do arquivo:
   ```

   ```
   Parâmetros da Assinatura Digital:
   ```

    1. Acesse o menu "Opções \ Parâmetros \ Parâmetros da Assinatura Digital" e preencha os relatórios cujos documentos serão assinados.

**Acesso à Funcionalidade de Assinatura em Lote:**

1. Acesse o menu "Cadastros / Segurança / Perfis", selecione o perfil desejado e dê permissão para o menu "Assistente de Assinatura em Lote".

## Procedimento para Utilização

1. Acesse o sistema com o usuário médico que realizará a assinatura dos documentos. No cadastro de prestadores, o prestador deve estar relacionado com o usuário do sistema.
2. O CPF deve ser igual ao que está informado no certificado digital. Esta configuração é necessária para que o componente da "E-val" ache o certificado relacionado ao usuário que está utilizando o sistemae

    3. Execute o assistente em "Utilitários / Utilitários do RM Saúde / Assistente de Assinatura em Lote".

    4. O assistente exibirá a quantidade de documentos que serão assinados. É necessário aguardar que os primeiros 20 documentos sejam assinados, pois neste momento o sistema solicitará a senha do certificado digital.

    5. Após a finalização da execução, uma mensagem será exibida, caso não ocorra nenhum problema. Caso ocorram erros, serão listados pelo sistema.

    6. Para verificar os documentos que foram assinados, acesse o PEP e localize um atendimento realizado pelo médico logado. Acesse o atendimento e selecione a página de evolução médica, anamnese ou prescrição médica. A imagem de um cadeado amarelo será exibida para os itens que já estiverem assinados.

    7. Todas as telas possuem um botão com o ícone de uma lupa para aumento. Clique neste botão e um log será exibido para a verificação da assinatura do documento.

    8. Ao clicar no botão "Verificar", o sistema acessa o endereço do WebService que faz a validação do documento assinado. O botão visualiza, exibirá o documento assinado.

divs
