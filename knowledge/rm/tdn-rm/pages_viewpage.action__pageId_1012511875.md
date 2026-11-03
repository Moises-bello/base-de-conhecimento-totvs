---
content_hash: 488dd5dd52e51c227328f228ab2eaba7c11ddeb02ef8fc160aa9ef09c69a4829
fetched_at: '2026-06-29T00:05:47.379304+00:00'
page_id: '1012511875'
product: rm
source: tdn-rm
title: Destinatário do Serviço ("Dest. Serviço")
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1012511875
version: 8
---

# Conteúdo

2Conteúdonone

# 1. Visão Geral

Essa aba tem como objetivo atender algumas especificações da Reforma Tributária de Consumo (RTC) para emissão do documento eletrônico Nota Fiscal de Serviço (NFS-e).

Os campos na aba ficarão visíveis **somente se** o tipo de movimento estiver configurado para os tributos **ISS** e/ou **IBS.**

# 2. Destinatário

Ela se refere aos dados do destinatário do serviço para atender as regras fiscais e de negócio definidas nos produtos TOTVS Educacional, TOTS Gestão Fiscal, e TOTVS Gestão Estoque Compras e Faturamento.

Disponível a partir das versões 12.1.2502 (12.1.2502.231, 12.1.2506.180, 12.1.2510.113 e 12.1.2602).

 

Observações:

* Os campos **NIF e motivo de não informação do NIF** devem ser exibidos e preenchidos somente para destinatários do exterior (os quais tem no cadastro no estado o campo "Nacional" desmarcado").
* Caso o NIF não seja informado, o motivo de não informação deve ser automaticamente preenchido com:  
  “0 - Não informada na nota de origem”.  
  Para destinatários nacionais (Brasil), NIF e motivo de não informação não são exigidos.

No processo de **“Cópia de movimento a partir de outro movimento”**, os dados do destinatário (NIF, motivo de não informação, CNPJ/CPF, e-mail) são copiados integralmente para o novo movimento.

# 3. Dados Imóvel

As informações de dados do imóvel se referem ao imóvel onde a prestação de serviços ocorreu, desde que não seja uma obra (novo empreendimento).

VisãoDescrição dos campos

|  |  |
| --- | --- |
| **Campos** | **Descrições dos Campos** |
| Inscrição Imobiliária | Inscrição imobiliária fiscal    (código fornecido pela prefeitura para a  identificação da obra ou para fins de recolhimento  do IPTU) |
| Cadastro Imobiliário Brasileiro | Código do Cadastro Imobiliário Brasileiro |
| CEP | Código de Endereçamento Postal numérico do  endereço nacional do imóvel |
| Logradouro | Tipo e nome do logradouro do endereço do imóvel |
| Número | Número no logradouro do endereço do imóvel |
| Complemento | Complemento do endereço do imóvel |
| Bairro | Bairro do endereço do imóvel |
| Estado | Estado do endereço do imóvel |
| Município | Município do endereço do imóvel |
| CEP alfanumérico Exterior | Código de Endereçamento Postal alfanumérico do  endereço do imóvel no exterior |
| Cidade Exterior | Nome da cidade no exterior, local do imóvel |
| Estado, província ou região da cidade Exterior | Estado, província ou região da cidade no exterior,  local do imóvel |
