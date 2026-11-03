---
content_hash: 06d59a743e92f6d4a2efe3416a3ca6fdc74deb8a042f01917e9777967ef20a39
fetched_at: '2026-06-29T00:08:52.344079+00:00'
page_id: '338382208'
product: rm
source: tdn-rm
title: Como proceder em casos onde o Gerenciador de Integração permanece em branco
  após executar o processamento de jobs com sucesso?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338382208
version: 9
---

## IMPORTANTE! **Situação específica para ambientes com base Oracle**

**1º Passo**

Verifique se o campo "Código Filial" localizado em "Configurações > Parametrizador > eSocial > Integração com TAF", está igual ao localizado em "Atualizações > Empresas > Complemento Cadastral".

**2º Passo**

Se os campos supracitados estiverem iguais, realize o procedimento contido no vídeo abaixo

**3º Passo**

Caso a situação ainda persista, siga o passo a passo abaixo :

1- Efetue o download <https://suporte.totvs.com/portal/p/10098/download#detail/657291> caso o o ODBC seja de 32 bits.   
ou Efetue o download <https://suporte.totvs.com/portal/p/10098/download#detail/657292> caso o o ODBC seja de 64 bits.

2- Acesse "[diretório]\TOTVS\TAF\bin\smartclient" e execute o SmartClient.exe. Em "Programa Inicial" selecione "APSDU" : 

3- Efetue o Login conforme dados abaixo:

Usuário: admin  
Senha: (vazio)

4- Ao acessar a APSDU, será exibida a tela abaixo. Selecione arquivo>>Abrir:   
  
  
  
  
5- Selecione em seguida a opção "TopConnect (TOPCONN)" em "Driver" e clique em 'Ok': 

6- Clique em "OK" novamente na próxima tela: 

7- Procure as tabelas "TAFST1" e "TAFST2" e clique em OK  
  
  
Obs.:A tabela TAFST2 guarda todos os registros que foram integrados do RM para o TAF antes de serem processados.

8 - **Faça um backup das tabelas TAFST1 e TAFST2** para posterior restauração. Poderá ser utilizada a função "Copiar para (Ctrl+Y)" dentro do menu "Utilitário".

 **Processo necessário para uso posterior**

9 - Posteriormente, clique em "Utilitarios > Drop Table" para apagar as informações destas tabelas.

 

Obs.: As tabelas TAFST1 e TAFST2 são tabelas dinâmicas. Ao acessar o TAF elas serão recriadas (o conteúdo das tabelas não é recriado).

10 - Após recriar as tabelas, restaure as informações através do menu "Utilitário > Append From (Ctrl+A)"

11- Pare todos os serviços do TAF e do TSS e, por questões de segurança, faça o backup do diretório: "[diretório]\TOTVS\TAF\TafDbAccess". Copie os arquivos contidos no ZIP baixados no item 1 e cole no seguinte diretório "[diretório]\TOTVS\TAF\TafDbAccess".   
  
  
12- Reinicie todos os serviços

13- Após tais procedimentos, gentilezar entrar em contato com o Atendimento Técnico
