---
content_hash: 605b53906438e8af8f75ad565098e82f3a62bc56bd4044b30812aaf827d793e1
fetched_at: '2026-06-29T00:11:16.292316+00:00'
page_id: '66618487'
product: rm
source: tdn-rm
title: RMFIS00006_Importação do layout EFD Contribuições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66618487
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | EFD Contribuições |
| **Subprocesso** | **:** | Importação de Layout |
| **Data da publicação** | **:** | 12/07/2013 |

Este documento tem como objetivo orientá-lo na preparação do ambiente para geração da **EFD PIS/COFINS** e na geração do arquivo para importação no Programa Validador.

1. Acesse o sistema e altere as permissões do Perfil do Usuário para ter acesso aos menus:

+ ***Utilitários | Gerador de Saídas | Categoria do Layout,***
+ ***Utilitários | Gerador de Saídas | Layout***
+ ***Rotinas Legais | Rotinas Federais | EFD PIS/COFINS.***

2. Crie a Categoria para o Layout através do menu ***Utilitários | Gerador de Saídas | Categoria do Layout***. Essa Categoria define a segurança da rotina. Para ter acesso à rotina é preciso que a Categoria esteja associada ao Perfil do usuário.

**Importante!**

   
 Não se esqueça de associar o Perfil à Categoria criada. Caso o Perfil não seja associado, o usuário não conseguirá selecionar o Layout para geração.

6. Faça a importação do layout através do menu ***Utilitários | Gerador  de Saídas***

* + Clique no menu ***"Processos | Importar Layout".***
  + Na tela seguinte, clique no botão **"Adicionar Objetos"** e selecione o arquivo enviado no pacote **"Layout EFD PIS-COFINS.TotvsGen"**
  + Selecione  a opção **"Todas Coligadas"** no quadro  **'Seleção de Coligada'**
  + Selecione o Objeto ***"Layout: Rotinas Legais Federais"*** e, na aba Parâmetros, informe a Categoria **"Rotinas Federais/Legais"**
  + Clique em **"Executar".**

7. Para gerar a rotina acesse o menu "***Rotinas Legais | Rotinas Federais | EFD PIS/COFINS***", selecione o layout importado e informe os dados solicitados na tela de geração.

O arquivo será gravado no diretório apresentado na tela de seleção de layout conforme print acima. Depois de gerado, importe o arquivo no PVA EFD-PIS/COFINS.

**Atenção!**

Não execute a opção de Validação dos dados após a importação. Responda "Não" à pergunta do PVA. Após a importação o arquivo no PVA, edite a Escrituração e execute o processo "Gerar Apurações". Esse processo irá gerar os registros do Bloco M, referente à apuração do PIS e da COFINS. Somente após esse processo, execute a opção de **"Verificar Pendências de Escrituração".**

**Obs.: O layout existente deve ser selecionado e excluído antes de importar o novo layout.**

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/Fis.Geradordesaidas.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
