---
content_hash: d83f632b18d6fffb44db80f35c1f3509f17e24397d9485db4e4506d2a4a3475c
fetched_at: '2026-06-29T00:10:50.659220+00:00'
page_id: '562474384'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Cobrança - Envio de SMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=562474384
version: 14
---

# 

Atenção

Para utilizar esta funcionalidade é necessário contratar um plano de serviço de SMS. Para maiores informações, acesse .

SMSUtilizando Mashups |

# Processo de Envio de SMS via Mashups.

Importante teste incialmente no Mashups para verificar se o Serviço de SMS encontra-se ativo e configurado corretamente com usuário / senha por exemplo.

-- Teste no Mashups com Usuário / Senha configurados no RM :**<http://mashups.totvs.com.br/TotvsSOAWebClient/WebClient.LoginScreen.aspx>**

Logando no Mashups com Uusario Mashups e senha do Usuário Mashups.

TOTVS - Envio de SMS

Informando o Usuario e Senha do Serviço SMS -  Informado nos **Parâmetros Gerais do RM.**

**SMS enviado com sucesso para o Celular do Cliente.**

Configuração RM para uso de SMS |

# Configurações no RM para uso do SMS.

No tipo de ação Envio de SMS deve ser definido o texto padrão que será enviado referente a cobrança.

* Efetuar a parametrização de Usuário / Senha ( mashups ) Serviço de Envio de SMS no RM.

**Parâmetros Globais**

Informar **Usuario / Senha** do usuario que possui credenciais para **envio de SMS.**

* Configurar Servidor de Mashups no cadastro da Coligada RM

Cadastro de Coligada | Processos | Mashups | Gerenciar

Clicar para inserir servidor Mashups.

**Servidor** : [mashup.totvs.com.br](http://mashup.totvs.com.br)

**Usuário** : Usuário de acesso ao Servidor Mashups

**Senha** : Senha do Usuário do Servidor Mashups

Envio de SMS no RM.

# Processo de envio de SMS no RM.

* Configurar o Processo de Ação de Cobrança de SMS no RM primeiramente.

Cobrança | Ações de Cobrança.

Incluídos os Mnemônicos para envio do SMS

CLIENTE: [CLI]  
PRIMEIRO NOME DO CLIENTE [PRINOMCLI]  
CLIENTE DO CONTRATO: [CONT]  
VALOR DO LANÇAMENTO: [VLR]  
VENCIMENTO: [VCTO]  
CODIGO DE BARRA: [BARR]  
NOME DO EMPREENDIMENTO: [NOM]

Configuração necessária para envio do SMS para o Cliente.

Selecionar a Ação Cadastrada | Gerar Ação Manual de Cobrança

Selecionar a Parcela para Ação da Cobrança.

## OBS : Verificar o cadastro do Cliente / Fornecedor se tem Telefone cadastrado.

FCFO.TELEX - SMS busca o Numero de Telefone - Tem que estar preenchido corretamente com DDD mais Número de Telefone.

Depois de conferir dados do Cliente , selecionar a Parcela - **EXECUTAR**

SMS enviado para o Celular do Cliente.
