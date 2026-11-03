---
content_hash: b2077987350278fb8440c1776d47a76646f93b19aafb04922b58f6c04295f8d0
fetched_at: '2026-06-29T00:05:58.764048+00:00'
page_id: '187828950'
product: rm
source: tdn-rm
title: Envio de relatório por e-mail
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=187828950
version: 21
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework |
| **Processo** | **:** | Fórmula Visual |
| **Subprocesso** | **:** | Utilizando a atividade "Envio de E-mail" |
| **Data da publicação** | **:** | 14/05/2015 |

# Objetivo

A finalidade da atividade de "Envio de E-mail com Arquivo Anexo" como o próprio nome já diz é enviar e-mail com arquivo em anexo através da fórmula visual. 

# Como Funciona

 

DeckPasso 1

Arrastar a atividade "Envio de E-mail" para o “Fluxo de Trabalho Sequencial” em sua fórmula visual.

Passo 2

Após a atividade ter sido adicionada ao fluxo de trabalho é necessário configurar as propriedades da atividade.

Passo 3

Neste exemplo iremos enviar um e-mail com um relatório anexo.

 

**Propriedades**  
 Assunto: Deve ser preenchido com o assunto do e-mail.  
 Destinatários: Lista de e-mails que deseja enviar.  
 Remetente: Quem irá enviar o e-mail. (Usuário/Coligada/ColigadaGlobal)  
 Texto do e-mail: Deve ser preenchido com o corpo do e-mail.

Passo 4

**Anexo**No exemplo abaixo foi utilizado a atividade **"Consulta SQL"**, onde a consulta sql associada à atividade retornará um relatório do banco de dados. Para mais informações sobre esta atividade acesse [Consulta SQL](http://tdn.totvs.com/x/hJi2C).  
 Após adicionar e configurar a atividade **"Consulta SQL"** no fluxo de trabalho é necessário configurar as propriedades **"Anexar Arquivo"** e **"Nome do Arquivo"** da atividade **"Enviar E-mail"**.

A propriedade "Nome do Arquivo" deve conter a extensão que o arquivo receberá ao ser anexado ao e-mail. Conforme no exemplo o arquivo anexo terá a extensão **".pdf".**

Passo 5

Como é a consulta sql que irá me retornar o relatório, é necessário associar à propriedade "Anexar Arquivo" os atributos da atividade "Consulta SQL" criada.  
  
Para realizar a associação, de um duplo clique no ícone  da propriedade "Anexar Arquivo".

Passo 6

Expanda a atividade "Consulta SQL".

 Clique em OK para que o atributo seja inserido na propriedade da atividade.  
 **Obs:** A propriedade Item foi setada como Item["RELATORIO"] pois é este o campo que é retornado da minha consulta sql.

Passo 7

Salve sua fórmula visual.

Passo 8

Na visão de Fórmula Visual selecione o registro desejado e clique em editar.

Passo 9

Na aba Gatilhos selecione o gatilho “Antes da Atualização do Registro (Fim)” e depois clique em “Adicionar Objeto”.

Passo 10

Pesquise pelo objeto que será associado ao gatilho selecionado.

Passo 11

Salve a edição de sua fórmula visual.

Observação

Para que seja possível anexar um relatório ao e-mail é necessário gerar este com a extensão desejada para visualização. Nesse exemplo desejamos anexar esse arquivo no formato de pdf, portanto iremos exportar o arquivo para o formato pdf.

Depois de gerado o relatório você pode conferir o mesmo no banco de dados, utilizando o primeiro select descrito abaixo. O segundo select será o que você utilizará na consulta sql da sua fórmula visual.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha)

|  |  |
| --- | --- |
| Status do Documento: | Em Produção |
| Data: | 14/05/2015 |
| Versão: | 1.0 |
| Versão Anterior: | 1.0 |
| Autores: |  |
