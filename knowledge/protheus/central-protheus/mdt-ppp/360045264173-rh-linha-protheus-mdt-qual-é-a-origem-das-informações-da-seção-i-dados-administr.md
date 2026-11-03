---
article_id: 360045264173
category: MDT - PPP
content_hash: 3e6824383a00a8c99847d31e1b516d9c5f4c306d2f938b4c03a49ba31227ca47
fetched_at: '2026-06-28T22:44:22.305098+00:00'
product: protheus
section_id: 360010945654
source: central-protheus
title: RH - Linha Protheus - MDT - Qual é a origem das informações da seção I dados
  administrativo (campos profissiografia 14 ao 14.2) do relatório PPP
type: support-article
updated_at: '2023-12-21T11:45:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045264173-RH-Linha-Protheus-MDT-Qual-%C3%A9-a-origem-das-informa%C3%A7%C3%B5es-da-se%C3%A7%C3%A3o-I-dados-administrativo-campos-profissiografia-14-ao-14-2-do-relat%C3%B3rio-PPP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20008556618519)** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Qual é a origem das informações da seção I dados administrativo (campos **profissiografia**14 ao 14.2) do relatório PPP?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Esta documentação refere-se exclusivamente a versão do PPP impresso no Módulo de Medicina e Segurança do Trabalho, rotina MDTR700, não tendo nenhuma relação com o PPP Eletrônico maiores informações consulte: **[RH - Linha Protheus - MDT - Qual diferença entre o PPP impresso no Módulo Medicina MDTR700 e o PPP da Previdência Social consultado através do APP Meu INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14223826251287)**Veja abaixo a tabela com origem das informação dos campos 14 a 14.2 do relatório PPP.O relatório de Perfil Profissiográfico Previdenciário (rotina mdtr700) é gerado através Caminho sigamdt: atualizações > relatórios > PPP > perfil profissiogr.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Origem** | **Conteúdo** | **Parâmetros (caso exista)** |
| **14** | **PROFISSIOGRAFIA** | Estas informações estão vinculadas a pergunta “**Desc.das Atividad.?**” Da tela de parâmetros para emissão do PPP. Essa pergunta pode ser selecionado para:  Cargo: O programa irá listar as informações do campo “Ds Detalhada” da tabela de Cargos (SQ3).  Tarefa: O programa irá listar as informações descritas na tabela de Tarefas por funcionário (TN5), campo “Descrição”. Porém, se não encontrar para o funcionário para o qual está sendo impresso o PPP, nenhuma tarefa cadastrada, ou o campo descrição estiver em branco, o programa imprimirá a descrição da tabela de Cargos. | | |
| 14.1 | Período | Dados do Cargo ou Tarefa | Este campo é definido pelo período que o funcionário trabalhou em um determinado cargo, ou em determinada tarefa, conforme o parâmetro selecionado. |  |
| 14.2 | Descrição das atividades | Dados do Cargo ou Tarefa | Esta informação é obtida da tabela de cargos (SQ3), com base na tabela de histórico de funções (SR7), ou da tabela de Tarefas por func. (TN5). Condicionada sempre ao parâmetro, conforme já descrito no item 14. |  |

**Saiba Mais**[Artigos PPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050700933)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
