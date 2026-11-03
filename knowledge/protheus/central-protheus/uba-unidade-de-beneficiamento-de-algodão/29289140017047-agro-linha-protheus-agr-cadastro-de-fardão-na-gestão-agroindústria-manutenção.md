---
article_id: 29289140017047
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 0a91b6a8989132b6cafcdcbb2a6fc3b6366067831967d8714d1ffddb32fdc964
fetched_at: '2026-06-28T22:45:35.508996+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - AGR - Cadastro de Fardão na Gestão Agroindústria -
  Manutenção
type: support-article
updated_at: '2025-06-18T13:17:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29289140017047-Agro-Linha-Protheus-AGR-Cadastro-de-Fard%C3%A3o-na-Gest%C3%A3o-Agroind%C3%BAstria-Manuten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29289139992599) Tempo aproximado para leitura: **00:00:40 min** **Dúvida**  
Como funciona uma estrutura **Cadastro de Fardão na Gestão Agroindústria - Manutenção**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12\_1\_27  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Veja na tabela os **Dados Gerais**;

| Produto: | Totvs Agro Beneficiamento |
| --- | --- |

| Linha de Produto: | Microsiga Protheus |
| Segmento: | Agroindústria |
| Módulo: | SIGAAGR |
| Função: | AGRA601- Cadastro de Fardão |
| Ticket: | 9288822 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DAGROINDUSTRIA-7796 |

**2.** **Situação/Requisito:**Ao selecionar a ordem de colheita no cadastro de fardão está validando a ordem de produção e quando há integração com **PIMS** não há a necessidade.  
  
**3.** **Solução:**  
Ajuste na rotina **AGRA601** para validar a existência da ordem de produção apenas se o campo for preenchido. Ajuste na validação do talhão para realizar a **query** com base no banco utilizado na conexão ativa.
