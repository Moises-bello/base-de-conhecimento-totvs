---
article_id: 360000091528
category: Gestão de Transportes (TMS)
content_hash: 758bc9996ed6a84e192c081d24484916e9a60bf522286e117da3f3873e352fd0
fetched_at: '2026-06-28T22:45:33.326631+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 746 Tipo de Serviço inválido para
  o tomador informado
type: support-article
updated_at: '2023-08-28T11:36:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000091528-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-746-Tipo-de-Servi%C3%A7o-inv%C3%A1lido-para-o-tomador-informado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17081134547351)**Tempo aproximado para leitura: **00:01:40 min  
  
Ocorrência:**Ao realizar o processo de **Transmissão de CT-e - Conhecimento Eletrônico de Transporte**é apresentado a rejeição **746 - Tipo de Serviço inválido** para o tomador informado.  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**A partir de 01/02/2016 entrou em produção as novas validações referentes a **Nota Técnica 2015/004** da **SEFAZ - Secretaria da Fazenda**, disponíveis para consulta no *site*: [Nota Técnica 2015/004](http://www.cte.fazenda.gov.br/listaConteudo.aspx?tipoConteudo=Y0nErnoZpsg)  
  
Conforme informações desta documentação, a **rejeição 746** ocorre quando o tomador do serviço for emitente de **CT-e** **verificar CNE -** **Cadastro Nacional de Empresas**, e diferente de Remetente ou Destinatário, a rejeição ocorrerá se o tipo de serviço informado for Normal **tpServ=0** **campo** **DTC\_TIPNFC** **= 0** na rotina **TMSA050 - Entrada Documento do Client**e.  
  
**Solução**Nestes casos, para confirmar se o cliente tomador de serviço é credenciado para emissão de CT-e - Conhecimento Eletrônico de Transportes, realize os seguintes passos:

1. Solicite o **CNPJ** do tomador e realize a consulta junto ao **SINTEGRA** **- Sistema Integrado de Informações sobre Operações Interestaduais com Mercadorias e Serviços**;
2. Consulte em **INFORMAÇÕES COMPLEMENTARES** /**Data de Credenciamento como emissor de CT-e**;
3. Visualize as informações conforme imagem abaixo de exemplo da consulta:

![746_IMAGEM.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360000122687)

**Saiba mais**  
Caso as informações mencionadas no **item 2** estejam preenchidas, ou seja, com dados de obrigatoriedade, recomendamos aos clientes que sejam consultados junto a área fiscal da empresa ou junto a **SEFAZ**, para melhor detalhamento quanto as informações desta rejeição, pois trata-se de validação do órgão validador e não do **ERP - Microsiga Protheus**.
