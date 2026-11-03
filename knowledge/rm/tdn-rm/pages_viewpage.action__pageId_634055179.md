---
content_hash: 9eee0aea49896661ab92625db1b1013041cdc946d16777f4fbc3dd82dbf332cf
fetched_at: '2026-06-29T00:11:06.388358+00:00'
page_id: '634055179'
product: rm
source: tdn-rm
title: Autenticação com TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=634055179
version: 18
---

## 

## **Conteúdo**



## **01. Visão GeralVisaoGeral**

        A partir do release **12.1.33**, o **TSS** implementa a funcionalidade de utilização de **Token de Autenticação** baseado em credenciais, contemplando a **LGPD (Lei Geral de Proteção de Dados).**Para o fluxo de autenticação, serão utilizadas as credenciais (**client\_id** e **client\_secret**) geradas pelo TSS. Essas credenciais **deverão ser informadas no ERP** para que sejam utilizadas na **requisição de solicitação do Token** de autenticação da empresa.

        Esse Token de autenticação, **será inserido no cabeçalho de todas as requisições** enviadas para do RM para o TSS, para que seja realizada a autenticação segura no consumo do serviço.

        A partir da versão 12.1.33 ao instalar o TSS essa configuração fica ativada automaticamente. Porém o cliente pode desabilitá-la se desejar.

## **02.****Segurança****Seguranca**

         Por padrão, a validade do token de **autenticação será de 1 (uma) hora** mas pode ser parametrizável. Quanto maior a validade menor será sua segurança. A validade do **token de refresh será 24 horas**, esse não é configurável. 

## **03.****Client ID e Client Secret****ClientIDeClientSecret**

Para a comunicação com o TSS foi criado campos para salvar as informações do client\_id e client\_secret do TSS. O Token pode ser cadastrado por Filial do TSS. 

Regras de Preenchimento CLIENT\_ID e CLIENT\_SECRET

1. Esses campos deverão ser preenchidos juntos, não será possível prosseguir com as alterações em tela caso apenas uma delas estiver preenchida;
2. Caso a versão do TSS seja **menor** que 12.1.33 estes campos **não** deverão ser preenchidos. Se forem preenchidos, será emitida uma mensagem de erro em tela;
3. Caso a versão do TSS seja **maior ou igual** a 12.1.33 este campo poderá ou não ser preenchido, dependendo da configuração do TSS:
   1. Caso o TSS esteja parametrizado para realizar a Autenticação via Token, os campos de credenciais deverão ser preenchidos. Se não tiverem sido preenchidos ou as credenciais estiverem inválidas, será emitida uma mensagem de erro em tela;
   2. Caso o TSS esteja parametrizado para **não** utilizar a Autenticação via Token, estas informações das credenciais não deverão ser preenchidas.

## **04.****Processos que utilizam integração com TSS****Processos**

0Nota Fiscal Eletrônica (NF-e)Quando a NFS-e esta pendente o processo esta consultando uma autorização

Os processos de NF-e ficam localizados no sistema Gestão de Estoque, Compras e Faturamento em Vendas | Documentos Eletrônicos | Nota Fiscal Eletrônica (NF-e)

* Enviar
* Consultar Autorização
* Consultar Autorização Automática (Job)
* Inutilizar
* Consultar Inutilização
* Alterar Modalidade de Operação
* Monitor SEFAZ
* Envio de Eventos
* Consulta de Eventos
Nota Fiscal de Consumidor Eletrônica (NFC-e)

Os processos de NFC-e ficam localizados no sistema Gestão de Estoque, Compras e Faturamento em Vendas | Documentos Eletrônicos | Nota Fiscal Eletrônica (NFC-e)

* Enviar
* Consultar Autorização
* Consultar Autorização Automática (Job)
* Inutilizar
* Consultar Inutilização
* Alterar Modalidade de Operação
* Monitor SEFAZ
* Envio de Eventos
* Consulta de Eventos
Nota Fiscal de Serviço Eletrônica (NFS-e)

Os processos de NFS-e ficam localizados no sistema Gestão de Estoque, Compras e Faturamento em Vendas | Documentos Eletrônicos | Nota Fiscal de Serviço Eletrônica (NFS-e)

* Enviar NFS-e
* Gerar Arquivo TXT/XML
* Consultar Geração do Arquivo TXT
* Consultar Autorização/Cancelamento
* Consultar Autorização pelo número do RPS
* Consultar Autorização/Cancelamento Automático (Job)
* Cancelar NFS-e
* Substituir NFS-e
Nota Fiscal de Comunicação Eletrônica (NFCom)Quando a NFS-e esta pendente o processo esta consultando uma autorização

Os processos de [NFCom](https://tdn.totvs.com/pages/viewpage.action?pageId=880058547) ficam localizados no sistema Gestão de Estoque, Compras e Faturamento em Vendas | Documentos Eletrônicos | Nota Fiscal de Comunicação Eletrônica (NFCom)

* Gerar
* Reprocessar
* Transmitir
* Consultar Autorização
* Eventos
* Consulta de Eventos
EFD-Reinf

Os processos da REINF ficam localizados no sistema Gestão Fiscal em Obrigações Acessórias| SPED | EFD - Reinf.

* Transmitir Evento
* Consultar Evento

## **05. Configurações do TSSConfiguracoesTSS**

As configurações do TSS referente a autenticação estão disponíveis no documento: <https://tdn.totvs.com/x/1RhcIw>

## **06.****Parâmetro RM -****Conexão ao TSSParametroRM**

       Informando os parâmetros **Client ID TSS e Client Secret TSS**no RM.

       **IMPORTANTE**: O Parâmetro deve ser informado no caminho correspondente aos processos que a empresa utiliza.

0NF-e/NFC-e/NFS-e/NFCom

**Caminho para NF-e/NFC-e/NFS-e/NFCom:** BackOffice | Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais | Parâmetros por Filial | Conexão NF-e

Observação: O Client ID e Client Secret deve ser gerado no TSS (Passo 5) e informado nos parâmetros do RM.

EFD-Reinf

**Caminho para REINF:**BackOffice | Gestão Fiscal | Ambiente | Parâmetros | TOTVS Gestão Fiscal | TOTVS Gestão Fiscal | Integração | TSS | Parâmetros por Filial | Gerais

Observação: O Client ID e Client Secret deve ser gerado no TSS (Passo 5) e informado nos parâmetros do RM.
