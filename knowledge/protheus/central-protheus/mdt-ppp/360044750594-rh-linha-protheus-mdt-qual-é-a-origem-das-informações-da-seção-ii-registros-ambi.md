---
article_id: 360044750594
category: MDT - PPP
content_hash: 63ee536230942c1b4c9ecf0112d4ebb06a9ba3fc013cb72401883da806e7581e
fetched_at: '2026-06-28T22:44:22.324705+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Qual é a origem das informações da seção II registros
  ambientais (campos responsável pelos registros 16 ao 16.4) do relatório PPP
type: support-article
updated_at: '2025-03-12T14:18:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044750594-RH-Linha-Protheus-MDT-Qual-%C3%A9-a-origem-das-informa%C3%A7%C3%B5es-da-se%C3%A7%C3%A3o-II-registros-ambientais-campos-respons%C3%A1vel-pelos-registros-16-ao-16-4-do-relat%C3%B3rio-PPP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20008480620823)** Tempo aproximado para leitura: **00:03:00 min****Dúvida**Qual é a origem das informações da seção II registros ambientais (campos **responsável pelos registros**16 ao 16.4) do relatório PPP?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte: **[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)**Veja abaixo a tabela com origem das informação dos campos 16 a 16.4 do relatório PPP.O relatório de Perfil Profissiográfico Previdenciário (rotina MDTR700) é gerado através Caminho SIGAMDT: Atualizações > Relatórios > PPP > Perfil Profissiogr.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Origem** | **Conteúdo** | **Parâmetros (caso exista)** |
| **16** | **RESPONSÁVEIS PELOS REGISTROS AMBIENTAIS** | Estas informações são obtidas da tabela de componentes do SESMT (TMK). O programa irá considerar todos os componentes que estiverem com o campo “Função” selecionado para Engenheiro de Segurança do Trabalho. | | |
| 16.1 | Período | Dados do Sesmt/usuario | Data de início e término da participação do Engenheiro de segurança do trabalho como responsável. |  |
| 16.2 | CPF | Dados do Sesmt/usuario | Esta informação é obtida da rotina do Sesmt/usuar.aten. (TMK), campo CPF. |  |
| 16.3 | Registro Conselho de Classe | Dados do Sesmt/usuario | Esta informação é obtida da rotina do Sesmt/usuar.aten. (TMK), este campo deve ser editado conforme manual de instrução do PPP. XXXXXX-X/XX Sendo: XXXXXX = Numero da registro -X = D – Definitvo ou P – Provisório /XX = UF. |  |
| 16.4 | Nome do profissional | Dados do Sesmt/usuario | Esta informação é obtida da rotina do Sesmt/usuar.aten. (TMK). |  |

**Saiba Mais**[Artigos PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
