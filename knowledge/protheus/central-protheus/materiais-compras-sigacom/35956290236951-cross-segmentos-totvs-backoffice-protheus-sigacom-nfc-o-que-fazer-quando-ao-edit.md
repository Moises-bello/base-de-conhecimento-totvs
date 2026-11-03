---
article_id: 35956290236951
category: Materiais - Compras (SIGACOM)
content_hash: 3d3ceb05636b5bf5461c16056930052bd74ecaf02abc1d0af75dcf6b1c855e25
fetched_at: '2026-06-28T22:41:21.864648+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - O que fazer quando
  ao Editar Cotação no NFC os itens não aparecerem?
type: support-article
updated_at: '2025-12-30T16:21:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35956290236951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-O-que-fazer-quando-ao-Editar-Cota%C3%A7%C3%A3o-no-NFC-os-itens-n%C3%A3o-aparecerem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35956261091735) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
 O que fazer quando ao Editar a Proposta da Cotação manualmente no NFC os itens não aparecerem? A linha do item vem toda vazia sem nenhuma informação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35956290230423)  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
Para resolver a ocorrência reportada, por gentileza, efetue todos os passos abaixo.

**1º passo:** Realize teste em ambiente de Homologação com as atualizações a seguir:

- [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)

- LIB Atual -[Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)

- Smartclient - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112221) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168455)

Observação.: Aplicar após backups e validar primeiro em ambiente teste.

**2º passo:** Verifique qual o fornecedor que consta na Proposta que está editando. **Acesse o cadastro desse fornecedor** e verifique se há caracteres especiais na **Razão Social** ou **Nome Fantasia**. Se houver, **r****emova o caractere especial** identificado (por exemplo, o símbolo **&**), **s****alve as alterações** e **realize um novo teste** no processo de cotação. **Valide** se o problema foi solucionado.

Conforme demonstra na documentação: [Cadastro de fornecedor - Retirada de caracteres especiais](https://tdn.totvs.com/display/public/PROT/DT+Cadastro+de+fornecedor+-+Retirada+de+caracteres+especiais), o time de produto realizou um tratamento para que caracteres especiais sejam removidos da rotina de cadastro de fornecedores. Portanto se trata de um novo comportamento do sistema. As rotinas do NFC não permitirão caracteres especiais.

Se persistir, entre em contato com a Equipe de Suporte Protheus Compras. Na abertura do chamado, por gentileza, encaminhe prints do cadastro do Fornecedor e inspetor de objetos .csv da base.

**3º passo:** Verifique como está o compartilhamento das tabelas SC7, SC8, DHU e DHV na sua base. Conforme recomendação do time de Desenvolvimento é recomendado que as tabelas SC7, SC8, DHU e DHV mantenham o mesmo nível de compartilhamento, uma possibilidade é: o erro está ocorrendo em seu ambiente devido a tabela SC8 estar em modo COMPARTILHADO e as demais tabelas em modo EXCLUSIVO.  
   
A informação referente ao compartilhamento de tabelas consta no tópico 9 da documentação abaixo:  
   
[Novo Fluxo de Compras: Guia de Referência - Gestão de Compras - P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500#NovoFluxodeCompras:GuiadeRefer%C3%AAnciaGest%C3%A3odeComprasP12-01.VIS%C3%83OGERAL)

***Saiba Mais:***

[Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
