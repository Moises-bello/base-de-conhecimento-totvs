---
content_hash: be90c4820fe1d4129388f2592995d6c5b336b6c0ee3ffe536ef9df81c6501d30
fetched_at: '2026-06-29T00:09:22.746702+00:00'
page_id: '422546022'
product: rm
source: tdn-rm
title: NFs-e Formato TXT 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546022
version: 41
---

# Conteúdo

Conteúdo

# 1. Envio da NFS-e ao TSS

Após criar os movimentos no módulo de faturamento, deve-se executar o processo "Enviar NFS-e", disponível na seção de Notas Fiscais Eletrônicas Municipais.

Esse processo irá gerar as NFS-e correspondentes aos movimentos filtrados e enviá-las ao TSS. As notas transmitidas serão identificadas pelo status "Geração de Arquivo TXT Pendente" na seção de Notas Fiscais Eletrônicas Municipais.

Fluxo de integração com o TSS

falseEnviar NFS-e TXT TSSfalseautohiddentrue6209

# 2. Geração do arquivo TXT no formato da Prefeitura

Após enviar as NFS-e ao TSS, é possível selecionar os registros das NFS-e que foram enviadas e executar o processo "Gerar Arquivo TXT".

Após a geração do arquivo, caso seja bem-sucedida, a nota terá seu status alterado para "Pendente". Esse processo possibilita que as notas previamente enviadas ao TSS sejam convertidas em arquivo TXT no formato exigido pela Prefeitura.

Fluxo de integração com o TSS

trueGerar arquivo NFS-e TXT TSSfalseautotoptrue6201

# 3. Importação das NFS-e no ambiente da Prefeitura

Como a prefeitura não oferece interação direta via WebServices, após a geração dos arquivos TXT, estes devem ser importados manualmente no website da prefeitura.

Após a importação bem-sucedida dos arquivos, a prefeitura gerará arquivos de retorno que devem ser importados de volta no ERP.

# 4. Importação dos arquivos de Retorno da Prefeitura para o ERP

Após obter os arquivos de retorno do website da prefeitura, o usuário deverá selecionar os registros de NFS-e pendentes e executar o processo "Consultar Autorização/Cancelamento".

Durante esse processo, o sistema solicitará ao usuário que informe o nome do arquivo de retorno gerado pela prefeitura ou assuma o nome padrão (Retorno.txt).

As notas que forem autorizadas pela prefeitura terão seu status alterado para "Autorizada".

As notas que forem rejeitadas pela prefeitura terão seu status alterado para "Rejeitada" e poderão ser corrigidas e reenviadas para uma nova validação.

Fluxo de integração com o TSS

trueConsultar NFS-e TXT TSSfalseautotoptrue6201

# 5. Cancelamento da NFS-e em TXT

Para que a NFS-e seja cancelada, ela deve estar com o status "Autorizada".

Para solicitar o cancelamento, o usuário deve executar o processo "Cancelar NFS-e", disponível na seção de Notas Fiscais Eletrônicas Municipais.

Após a conclusão bem-sucedida do processo de cancelamento, a NFS-e terá seu status alterado para "Geração de Arquivo TXT Pendente".

Posteriormente, o usuário deverá executar novamente o processo "Gerar Arquivo TXT" para que o TSS gere um novo arquivo contendo os dados do cancelamento. Esse novo arquivo deverá ser importado no website da prefeitura.

Fluxo de integração com o TSS

trueCancelar NFS-e TXT TSSfalseautotoptrue6201

# 6. Importação dos arquivos de Retorno da Prefeitura para o ERP (Cancelamento)

Após obter os arquivos de retorno do website da prefeitura, deve-se selecionar os registros de NFS-e pendentes e executar o processo "Consultar Autorização/Cancelamento".

Durante este processo, será solicitado que o usuário informe o nome do arquivo de retorno gerado pela prefeitura ou assuma o nome padrão (Retorno.txt).

As notas cujo cancelamento seja aceito pela prefeitura terão seu status alterado para "Cancelado".

As notas que forem rejeitadas pela prefeitura terão seu status alterado para "Autorizada".

O Fluxo de integração com o TSS é o mesmo da consulta da NFS-e (item 4)

# 7. Configuração da Integração com o TSS

O TSS pode ser configurado pelo parâmetro **Tipo FTP** que informa qual método de transferência de arquivo será usado.

Configuração Tipo FTP

Quando a opção Web Service é selecionada, ao enviar a NFS-e o seu status passa para "Geração do Arquivo TXT/XML Pendente" não sendo necessário executar o processo "Gerar Arquivo TXT".

Para mais detalhes da integração com o TSS:
