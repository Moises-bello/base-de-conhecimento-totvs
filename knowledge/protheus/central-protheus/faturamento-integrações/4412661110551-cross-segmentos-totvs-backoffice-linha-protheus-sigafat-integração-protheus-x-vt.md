---
article_id: 4412661110551
category: Faturamento - Integrações
content_hash: e94798b7e25dde426097b97c7290737b70193a30dd0e49e012437a209c73336f
fetched_at: '2026-06-28T22:38:26.546178+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Integração
  Protheus x Vtex no Cadastro de Clientes
type: support-article
updated_at: '2022-08-02T20:11:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412661110551-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Integra%C3%A7%C3%A3o-Protheus-x-Vtex-no-Cadastro-de-Clientes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como funciona a integração Protheus x Vtex no Cadastro de Clientes?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - A partir da versão 12  
  
**Solução**As compras via e-commerce do Vtex possuem uma integração com a rotina de Cadastro de Clientes (CRMA980, antigo MATA030) do Protheus, assim, ao realizar uma compra pelo site, é **incluído um cadastro para o cliente da compra na tabela de Clientes do Protheus (SA1).**Avaliando pela tabela de “De/Para” (XXF), o sistema irá verificar se o cliente já existe na tabela de cadastro (SA1), **caso ele já exista**, o sistema irá editar o cadastro já existente com as informações enviadas no arquivo Json, **caso não exista**, o sistema irá cadastrar um novo cliente.  
  
A partir do release **12.1.33** do Protheus, foi criado o parâmetro **([MV\_INTVTX](https://tdn.totvs.com/x/-JCjJ))**, ao **habilitar** o parâmetro **(.T.)**, o sistema verifica o “**InternalId**” na tabela de “De/Para” (**XXF**) e irá verificar se o cliente já existe na tabela de cadastro de cliente (SA1), **caso ele já exista,** o sistema irá editar o cadastro já existente com as informações enviadas no arquivo Json, **caso o endereço principal seja diferente** **será criada** **uma nova loja para o mesmo cliente.**  
  
Clientes em releases anteriores à 12.1.33 necessitam utilizar o ponto de entrada:

* **[MTI030NOM - permite a inclusão de campos customizados no array](https://tdn.totvs.com/x/SAvMCg)**

Para que o sistema possa realizar o cadastro de dois ou mais clientes com o mesmo código de CPF/CNPJ, porém com endereço diferente, é necessário configurar os parâmetros “**MV\_VALCPF**” e “**MV\_VALCNPJ**” como 1.  
  
**Saiba mais**: **[Integração Cadastro de Clientes (MATA030) x E-commerce (Vtex) via EAI](https://tdn.totvs.com/x/5VmmJg)**
