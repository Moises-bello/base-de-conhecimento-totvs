---
content_hash: 4356e03c8ab41c874b8007eb8fb9c2a6644e231c375a90c403f15df8b4258127
fetched_at: '2026-06-29T00:09:22.558452+00:00'
page_id: '422546002'
product: rm
source: tdn-rm
title: Geração e Consulta Arquivo TXT/XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546002
version: 6
---

## **01. Em que consiste o processo**

Este processo é aplicável à Prefeituras que não recebem os RPS por webservice. Ele consiste em gerar as informações do RPS em um arquivo texto ou XML que será posteriormente importado para o portal da Prefeitura. Em seguida, a Prefeitura fornecerá um arquivo de retorno que deverá ser importado no RM.

A parametrização para o envio de uma NFS-e em TXT/XML permanece a mesma do processo pelo webservice.

O processo identifica o método de envio pela Classificação do Município do endereço da filial emissora. A única exceção é quanto ao certificado digital que este processo não utiliza.

## **02. Como executar**

### Geração do RPS no RM

1. Crie o movimento de RPS normalmente.
2. Acesse a visão das NFS-e nos Processos clique em Enviar. Informe os parâmetros e execute o envio.
3. Concluído o envio o registro da NFS-e será criado com o status Geração do Arquivo TXT/XML Pendente.
4. Selecione o registro e nos Processos clique em "Gerar Arquivo TXT/XML".
   1. Se o processo for bem-sucedido a NFS-e terá seu status alterado para "Aguardando Geração do Arquivo TXT".
   2. Se o parâmetro Tipo FTP estiver configurado como WebService o status é alterado para "Geração do Arquivo TXT/XML Pendente" e o passo 5 pode ser ignorado.
5. Aguarde o processamento do arquivo, selecione novamente o registro e em Processos clique em "Consulta Geração do Arquivo TXT".
6. Se processo for bem-sucedido a NFS-e terá seu status alterado para Pendente. Se o arquivo ainda não tiver sido gerado, aguarde e execute o processo novamente. Se for apresentado algum erro analise o log e corrija-o e repita todo o processo de envio até a geração do arquivo.

### Envio do RPS para a Prefeitura

1. Após executar o processo de Consulta de Geração do Arquivo TXT com sucesso o arquivo poderá ser enviado para a Prefeitura.
2. Acesse o diretório ARQGER\FTP do TSS.
   1. Dentro deste diretório será criado (automaticamente) um subdiretório com o código do munícipio da filial emitente.
   2. Um exemplo da localização do diretório ARQGER\FTP: C:\totvssped\ftp\arqger\3505708. Onde 3505708 é referente ao código IBGE para o município de Barueri. Os arquivos são gravados no seguinte formato : nfse\_000000000000000.txt.
3. Acesse o site da Prefeitura e faça a importação do arquivo gerado.
4. Aguarde o processamento do arquivo pela Prefeitura e faça o download do retorno e grave-o no diretório ARQIMP\FTP (C:\totvssped\ftp\arqimp\3505708)  do TSS.
5. Se o site da Prefeitura acusar inconsistência no RPS enviado e rejeitar a NFS-e consulte Rejeitar NFS-e TXT/XML para saber como proceder.  
   ***Atenção!* A geração de NFS-e por arquivo TXT/XML não existe no processo integrado pelo TOTVS Colaboração 2.0.**
