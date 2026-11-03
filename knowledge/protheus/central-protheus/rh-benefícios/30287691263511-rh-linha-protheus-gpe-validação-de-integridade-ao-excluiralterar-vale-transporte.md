---
article_id: 30287691263511
category: RH - Benefícios
content_hash: 47034bb7e9e312aaf3a2c625873671a7566fe359544851ec607bfa9a0dfc19a7
fetched_at: '2026-06-28T22:44:04.814906+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Validação de integridade ao excluir/alterar Vale
  Transporte
type: support-article
updated_at: '2025-09-12T13:38:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30287691263511-RH-Linha-Protheus-GPE-Valida%C3%A7%C3%A3o-de-integridade-ao-excluir-alterar-Vale-Transporte
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30287691250327) Tempo aproximado para leitura: 00:01:00 min****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2310  
  
**Dúvida**Sistema exibe mensagem de **violação de integridade** entre as tabelas SR0 (Itens de Benefícios) e SM7 (Cadastro de Benefícios) no momento de **exclusão ou alteração** do Vale Transporte.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30287691252375)  
  
  
**Solução:**A validação foi implementada para validar a integridade entre os registros, uma vez que o registro **SM7 (Cadastro de Benefícios)** é pai do registro **SR0 (Itens de Benefícios)**, sendo assim, o registro pai não poderá ser excluído/alterado sem a devida exclusão dos registros filhos.  
  
Para isso, será necessário utilizar a rotina de **Cancelamento de Cálculo (GPEM160)** disponível na rotina  **Miscelânea> Cálculos> Cancelamento de Cálculos** para conseguir realizar a alteração/exclusão.  
  
Se, ao acessar a rotina **Atualização de Vales (GPEA133)**, o Funcionário tiver dados nos quadros conforme exemplo abaixo, significa que foi feito cálculo do benefício e existem dados na tabela SR0, portanto, não seria possível fazer a alteração ou exclusão do benefício.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30506224309655)  
  
**-> Exemplo 1 da nova validação:**- Cálculo de Vale Transporte de Janeiro de 2025 registrado nas tabelas SM7 (Cadastro de Benefícios) e SR0 (Itens de Benefícios)- Funcionário durante o mês de Janeiro decide alterar a opção de Vale Transporte a partir de Fevereiro  
- Roteiro de Vale Transporte **não integrado** à Folha de Pagamento.  
  
Neste caso, **como proceder?  
  
1 -** Realizar a **exclusão do cálculo** do período de **Janeiro/2025** através da rotina de **Cancelamento de Cálculo (GPEM160)  
2 -** Realizar o ajuste dos Meios de Transporte do Funcionário através da rotina **Atualização de Vales (GPEA133)** e processar o cálculo novamente.**-> Exemplo 2 da nova validação:**- Cálculo de Vale Transporte de Janeiro de 2025 registrado nas tabelas SM7 (Cadastro de Benefícios) e SR0 (Itens de Benefícios)  
- Funcionário durante o mês de Janeiro decide suspender o uso de Vale Transporte a partir de Fevereiro  
- Roteiro de Vale Transporte **integrado** à Folha de Pagamento.  
  
Neste caso, **como proceder?  
  
1 -** Será necessário realizar o **Cancelamento da Integração** com a Folha de Pagamento através da rotina **Integrações (GPEM019)  
2 -** Realizar a **exclusão do cálculo** do período de **Janeiro/2025** através da rotina de **Cancelamento de Cálculo (GPEM160)  
3 -** Realizar a exclusão dos dados de Vale Transporte do Funcionário através da rotina **Atualização de Vales (GPEA133).**  
  
  
  
  
**Saiba Mais:**[Documento Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=911836535)  
[RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21372540319383-RH-Linha-Protheus-GPE-Cadastro-e-C%C3%A1lculo-do-Vale-Transporte)
