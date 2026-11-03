---
article_id: 360045266833
category: MDT - PPP
content_hash: 94b6b52c8a91fb15046f8eab899935f72a2808d27a4946fec707f71596eee84d
fetched_at: '2026-06-28T22:44:22.331709+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Qual é a origem das informações da seção III responsáveis
  pelas informações (campos responsável pelos registros 17 ao 18.2) do relatório PPP
type: support-article
updated_at: '2025-03-03T12:30:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045266833-RH-Linha-Protheus-MDT-Qual-%C3%A9-a-origem-das-informa%C3%A7%C3%B5es-da-se%C3%A7%C3%A3o-III-respons%C3%A1veis-pelas-informa%C3%A7%C3%B5es-campos-respons%C3%A1vel-pelos-registros-17-ao-18-2-do-relat%C3%B3rio-PPP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20008425030935)** Tempo aproximado para leitura: **00:04:00 min****Dúvida**Qual é a origem das informações da seção III resultados de monitoração biológica (campos **responsável pelos registros** 17 ao 18.2) do relatório PPP?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte: **[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)**Veja abaixo a tabela com origem das informação dos campos 17 a 18.2 do relatório PPP.O relatório de Perfil Profissiográfico Previdenciário (rotina MDTR700) é gerado através Caminho SIGAMDT: Atualizações > Relatórios > PPP > Perfil Profissiogr.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Origem** | **Conteúdo** | | |
| **17** | **DATA DE EMISSÃO DO PPP** |  | Data em que o PPP é impresso e assinado pelos responsáveis, no formato DD/MM/AAAA. | | |
| **18** | **REPRESENTANTE LEGAL DA EMPRESA** |  | Informações sobre o Representante Legal da empresa. Somente deve ser preenchido os casos de PPP em meio físico (papel). Estas informações são obtidas da rotina de componentes do Sesmt/usuar.aten. (TMK) campo "**Monit.Biolog**". E os componentes que estiverem com o campo “**Função**” selecionado para Médico do Trabalho. | | |
| 18.1 | CPF do Representante Legal | Dados do Sesmt/usuário | CPF do representante legal da empresa, com onze caracteres numéricos, no formato: xxx.xxx.xxx-xx. Esta informação é obtida da rotina do Sesmt/usuar.aten. (TMK), verificar o campo CPF. | | |
| 18.2 | Nome do Representante Legal | Dados do Sesmt/usuário | Esta informação é obtida da rotina do Sesmt/usuar.aten. (TMK), campo Nome. | | |
|  | **CARIMBO DA EMPRESA E ASSINATURA DO REPRESENTANTE LEGAL** |  | Carimbo da empresa e assinatura, física ou eletrônica, do Representante Legal. | | |
|  | **OBSERVAÇÕES** |  | Devem ser incluídas neste campo informações necessárias à análise do PPP, bem como facilitadoras do requerimento do benefício.  Pode ser incluída através da rotina Termo de Responsabilidade (MDTA235) Atualizações > Cadastros Básicos > Termo Resp. | | |

**Saiba Mais**[Artigos PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
