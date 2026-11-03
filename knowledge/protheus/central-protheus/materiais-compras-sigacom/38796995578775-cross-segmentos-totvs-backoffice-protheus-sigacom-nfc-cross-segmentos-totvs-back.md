---
article_id: 38796995578775
category: Materiais - Compras (SIGACOM)
content_hash: 8fb6cf9072c01f2aa23d00b9de68feb0cc23fab83466d7d4eb45376ac2c3adc0
fetched_at: '2026-06-28T22:41:10.054100+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Cross Segmentos
  - Totvs Backoffice Protheus - SIGACOM - NFC - HELP "OBRIGAT" ao incluir Novo Participante
  em uma cotação no NFC (PGCA010).
type: support-article
updated_at: '2026-03-04T14:47:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38796995578775-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-HELP-OBRIGAT-ao-incluir-Novo-Participante-em-uma-cota%C3%A7%C3%A3o-no-NFC-PGCA010
---

**Dúvida**  
O que fazer quando ocorre o HELP "OBRIGAT" ao incluir Novo Participante em uma cotação no NFC (PGCA010).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38797040131735)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2210  
  
**Solução**  
Para resolver a ocorrência reportada, por gentileza, efetue todos os passos abaixo.

**1º passo:**Verifique qual o fornecedor que consta na cotação que está incluindo o Novo Participante. **Acesse o cadastro desse fornecedor** e verifique se há caracteres especiais na **Razão Social** ou **Nome Fantasia**. Se houver, **r****emova o caractere especial** identificado (por exemplo, o símbolo **&**), **s****alve as alterações** e **realize um novo teste** no processo de cotação. **Valide** se o problema foi solucionado.

Conforme demonstra na documentação: [Cadastro de fornecedor - Retirada de caracteres especiais](https://tdn.totvs.com/display/public/PROT/DT+Cadastro+de+fornecedor+-+Retirada+de+caracteres+especiais), o time de produto realizou um tratamento para que caracteres especiais sejam removidos da rotina de cadastro de fornecedores. Portanto se trata de um novo comportamento do sistema. As rotinas do NFC não permitirão caracteres especiais.

Se persistir, entre em contato com a Equipe de Suporte Protheus Compras. Na abertura do chamado, por gentileza, encaminhe prints do cadastro do Fornecedor e inspetor de objetos .csv da base.  
  
**2º passo:**Verifique como está o compartilhamento das tabelas SC7, SC8, DHU e DHV na sua base. Conforme recomendação do time de Desenvolvimento é recomendado que as tabelas SC7, SC8, DHU e DHV mantenham o mesmo nível de compartilhamento, uma possibilidade é: o erro está ocorrendo em seu ambiente devido a tabela SC8 estar em modo COMPARTILHADO e as demais tabelas em modo EXCLUSIVO.  
   
A informação referente ao compartilhamento de tabelas consta no tópico 9 da documentação abaixo:

[Novo Fluxo de Compras: Guia de Referência - Gestão de Compras - P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500#NovoFluxodeCompras:GuiadeRefer%C3%AAnciaGest%C3%A3odeComprasP12-01.VIS%C3%83OGERAL)

***Saiba Mais:***

[Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
