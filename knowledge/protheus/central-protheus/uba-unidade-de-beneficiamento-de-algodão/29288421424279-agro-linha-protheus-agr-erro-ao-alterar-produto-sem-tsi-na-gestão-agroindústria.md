---
article_id: 29288421424279
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 7e60a1a909ce652499e2e331c8ac4a8e584426b10c97c1aa6551976b19358c34
fetched_at: '2026-06-28T22:45:35.523842+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - AGR - Erro ao alterar produto sem TSI na Gestão Agroindústria
  - Manutenção
type: support-article
updated_at: '2025-06-18T13:12:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29288421424279-Agro-Linha-Protheus-AGR-Erro-ao-alterar-produto-sem-TSI-na-Gest%C3%A3o-Agroind%C3%BAstria-Manuten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29288421405079) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**  
**Erro ao alterar produto sem TSI na Gestão Agroindústria - Manutenção**. Como solucionar essa dúvida?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Veja na tabela os **Dados Gerais**;

|  |
| --- |
|  |
| Produto: | Totvs Agro Beneficiamento |

|  |  |
| --- | --- |
| Linha de Produto: | Linha Protheus |
| Segmento: | Agroindústria |
| Módulo: | Gestão de Agronegócio |
| Função: | AGRA840 - Lote de Sementes |
| Ticket: | 9820741 |
| Requisito/Story/Issue (informe o requisito relacionado) : | DAGROINDUSTRIA-8199 |
|  |  |

  

**2.** **Situação/Requisito:**  
Ao tentar alterar um registro que não possui **TSI** está sendo apresentado a mensagem **"Lote de sementes possui TSI. Alteração não permitida"**;  
  
**3.** **Solução:**Realizado os ajustes na rotina de **Lote de Sementes** alterando o índice;

**4.** Abra o **Configurador** - **(SIGACFG)** para criação de novo índice;

**5.** Crie o novo índice na tabela **NP9**;

**6.** Busque pela tabela **NP9** e editá-la.

![TSI.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29288425882007)

**7.** Ir em **"Índices"** e incluir um novo;

![TSI1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29288425883543)

Chave: **NP9\_FILIAL+NP9\_LOTE+NP9\_CODSAF+NP9\_PROD+NP9\_TRATO**

Descrição: **Lote+Cod.Safra+Produto+Tratado?**
