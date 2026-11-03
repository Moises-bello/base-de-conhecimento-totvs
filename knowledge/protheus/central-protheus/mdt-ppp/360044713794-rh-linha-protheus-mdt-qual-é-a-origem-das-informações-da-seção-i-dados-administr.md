---
article_id: 360044713794
category: MDT - PPP
content_hash: c4bc47c575d4862bf005b793b88facb9ebda3c935dd9b5e9b7db53c50bbf4931
fetched_at: '2026-06-28T22:44:22.292231+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Qual é a origem das informações da seção I dados
  administrativo (campos CAT 12 ao 12.2) do relatório PPP
type: support-article
updated_at: '2023-12-26T13:42:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044713794-RH-Linha-Protheus-MDT-Qual-%C3%A9-a-origem-das-informa%C3%A7%C3%B5es-da-se%C3%A7%C3%A3o-I-dados-administrativo-campos-CAT-12-ao-12-2-do-relat%C3%B3rio-PPP
---

**Dúvida**Qual é a origem das informações da seção I dados administrativo (campos **CAT**12 ao 12.2) do relatório PPP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte: **[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)**Veja abaixo a tabela com origem das informação dos campos 12 a 12.2 do relatório PPP.O relatório de Perfil Profissiográfico Previdenciário (rotina mdtr700) é gerado através Caminho sigamdt: atualizações > relatórios > PPP > perfil profissiogr.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Origem** | **Conteúdo** | **Parâmetros (caso exista)** |
| **12** | **CAT REGISTRADA** | | | |
| 12.1 | Data do Registro | Dados do Acidente de Trabalhado | Acidentes (TNC) só serão considerados aqueles acidentes cujo os campos “Recibo” e “Data Emissão” estiverem preenchidos. |  |
| 12.2 | Número da CAT | Dados do Acidente de Trabalhado | Acidentes (TNC) só serão considerados aqueles acidentes cujo os campos “Recibo” e “Data Emissão” estiverem preenchidos. |  |

**Saiba Mais**[Como gerar o PPP (Perfil Profissiográfico Previdenciário) no modulo Medicina (sigamdt), e de onde vem as informações apresentadas no relatório](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Central de artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho)
