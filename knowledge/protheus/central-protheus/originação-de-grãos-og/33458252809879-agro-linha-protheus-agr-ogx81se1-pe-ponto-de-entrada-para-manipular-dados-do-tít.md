---
article_id: 33458252809879
category: Originação de Grãos (OG)
content_hash: 055001295539b5ea859d0f13c6b503061c58dd17e2ed73ab7794f219ec2601e8
fetched_at: '2026-06-28T22:45:41.123491+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - OGX81SE1 PE Ponto de Entrada para Manipular dados
  do Título à Receber - DCO/PEPRO
type: support-article
updated_at: '2025-07-14T18:58:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33458252809879-Agro-Linha-Protheus-AGR-OGX81SE1-PE-Ponto-de-Entrada-para-Manipular-dados-do-T%C3%ADtulo-%C3%A0-Receber-DCO-PEPRO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33458252778903) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como funciona um **Ponto de Entrada para** **Manipular dados na geração de produção à Pagar - Registro de Negócios**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA810 | DCO PEPRO | |
| **Ponto de entrada:** | OGX81SE1 |
| **País(es):** | Todos |
| **Pacote:** | 12.1.23 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao gerar os títulos a receber do DCO PEPRO |
| **Programa Fonte:** | OGX81SE1 |
| **Função:** | Permitir manipular dados do Título a Receber. |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **OGX81SE1** | Variedade | Envia como parâmetro array dos dados do título e o código do produto do Aviso PEPRO. | Não | |

**Exemplo:**

**Função de usuário OGX81SE1()**  
**Local aFina040 := aClone(PARAMIXB[1])**  
**Local cCodPro := PARAMIXB[2]**  
  
**aAdd( aFina040, {"E1\_SEUCAMPO" , '' , Nil } )**  
  
**Retorna aFina040**
