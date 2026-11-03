---
article_id: 360052555953
category: RH - Definições de Cálculo
content_hash: 2d191e9c4bfbc4437973e624e3f1f982efe514010c6a880825a49d5c9294ab92
fetched_at: '2026-06-28T22:43:22.283016+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo já efetuado para este roteiro
type: support-article
updated_at: '2025-10-02T17:35:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052555953-RH-Linha-Protheus-GPE-C%C3%A1lculo-j%C3%A1-efetuado-para-este-roteiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32838976120855)**Tempo aproximado para leitura: **00:01:30 min  
  
Ocorrência**Ao realizar alteração da data de pagamento de qualquer roteiro de cálculo na rotina de períodos gera a mensagem:  **Cálculo já efetuado para este roteiro!** **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**  
A mensagem ocorre pois existe cálculo já efetuado para o roteiro.  
  
**Solução**Ao realizar alteração da data de pagamento de qualquer roteiro de cálculo gera a mensagem:  **Cálculo já efetuado para este roteiro!****Para evitar inconsistência na geração do evento S1210 do eEsocial, realize o cancelamento para alteração da data de Pagamento.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32838958953623)

A mensagem foi incluída porque, ao alterar a data de pagamento no cadastro de períodos após o cálculo já ter sido realizado, ocorre divergência entre essa data e a registrada nos movimentos (SRD/SRC). Essa diferença compromete a integridade das informações e **impacta diretamente na geração do S-1210.**

Alterar a data de pagamento após o cálculo é considerado um erro de processo, pois o campo é destinado ao roteiro e não ao controle individual por trabalhador.

Caso seja necessário alterar a data do roteiro, será preciso cancelar todos os tipos de cálculo já realizados para esse roteiro. Após o cancelamento, os campos **Data de Referência De** e **Data de Referência Até** devem ser deixados em branco.

**->** Segue exemplo de preenchimento dos parâmetros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32838976127639)

**->** Selecione o Tipo de Cancelamento, lembrando que a rotina só permite efetuar um tipo de cancelamento por vez, pois não existe a opção de selecionar todos os tipos. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32838976128279)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32838976128791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32838976129431)

**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como efetuar o cadastro de período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052262653-RH-Linha-Protheus-GPE-Como-efetuar-o-cadastro-de-per%C3%ADodo)  
[RH - Linha Protheus - GPE - Como Criar Períodos Automaticamente pela Rotina Geração Período Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010729592-RH-Linha-Protheus-GPE-Como-Criar-Per%C3%ADodos-Automaticamente-pela-Rotina-Gera%C3%A7%C3%A3o-Per%C3%ADodo-Padr%C3%A3o)  
[RH - Linha Protheus - GPE - Como criar processo e período de cálculo diferente do padrão já existente no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045247114-RH-Linha-Protheus-GPE-Como-criar-processo-e-per%C3%ADodo-de-c%C3%A1lculo-diferente-do-padr%C3%A3o-j%C3%A1-existente-no-sistema)  
[RH - Linha Protheus - GPE - Tabelas utilizadas para o Cadastro de Período GPEA400](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8426220799511-RH-Linha-Protheus-GPE-Tabelas-utilizadas-para-o-Cadastro-de-Per%C3%ADodo-GPEA400)
