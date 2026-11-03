---
article_id: 10434835380887
category: MDT - PPRA
content_hash: c53ed60e6080d03f3c44bb31b25872629a1a08c9ab6f47bd380e461098c772ee
fetched_at: '2026-06-28T22:44:27.473805+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT - Quais cadastros são utilizados na impressão da
  Ordem de Serviço do Funcionário MDTR715
type: support-article
updated_at: '2025-09-04T18:44:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10434835380887-RH-Linha-Protheus-MDT-Quais-cadastros-s%C3%A3o-utilizados-na-impress%C3%A3o-da-Ordem-de-Servi%C3%A7o-do-Funcion%C3%A1rio-MDTR715
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372883086615) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais cadastros são utilizados na impressão da Ordem de Serviço do Funcionário MDTR715?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Abaixo listo os campos para a apresentação de informações referentes a **Ordem de Serviço do Funcionário**.

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Data Elaboração | Apresenta a informação do campo **Data Elab**. (*TOB\_DTELAB*) da rotina de Ord. Serviço Func. (*MDTA305*). |
| Última Revisão | Apresenta a informação do campo **Ult. Revisão** (*TOB\_DTREVI*) da rotina de Ord. Serviço Func. *(MDTA305*). |
| Razão Social/Nome | Apresenta a informação do campo *M0\_NOMECOM*. |
| Endereço | Apresenta a informação de acordo com a resposta da pergunta **Endereço?:**   * Cobrança: utiliza o campo *M0\_ENDCOB*; * Entidade: utiliza o campo *M0\_ENDENT*; |
| Cidade | Apresenta a informação de acordo com a resposta da pergunta **Endereço?:**   * Cobrança: utiliza o campo *M0\_CIDCOB*; * Entidade: utiliza o campo *M0\_CIDENT*; |
| CNPJ | Apresenta a informação do campo *M0\_CGC*. |
| CNAE | Apresenta a informação do campo *M0\_CNAE**.* |
| Bairro | presenta a informação de acordo com a resposta da pergunta **Endereço?:**   * Cobrança: utiliza o campo *M0\_BAIRCOB*; * Entidade: utiliza o campo *M0\_BAIREN*T; |
| Nome | Apresenta a informação do campo **Nome** (*RA\_NOME*) da rotina de **Funcionários** (*GPEA010*). |
| Centro de Custo | Apresenta a informação do campo **Centro Custo** (*RA\_CC*) da rotina de **Funcionários** (*GPEA010*). |
| Departamento | Apresenta a informação do campo **Departamento** (*RA\_DEPTO*) da rotina de **Funcionários** (*GPEA010*). |
| Função | Apresenta a informação do campo **Cod. Função** (*RA\_CODFUNC*) da rotina de **Funcionários** (*GPEA010*). |
| CTPS | Apresenta a informação do campo **Cart. Profis**. (*RA\_NUMCP*) da rotina de **Funcionários** (*GPEA010*). |
| Matrícula | Apresenta a informação do campo **Matrícula** (*RA\_MAT*) da rotina de **Funcionários** (*GPEA010*). |
| Data da Admissão | Apresenta a informação do campo **Data Admis**. (*RA\_ADMISSA*) da rotina de **Funcionários** (*GPEA010*). |
| Data Nascimento | Apresenta a informação do campo **Data Nasc**. (*RA\_NASC*) da rotina de **Funcionários** (*GPEA010*). |
| R.G. | Apresenta a informação do campo **R.G.** (*RA\_RG*) da rotina de **Funcionários** (*GPEA010*). |
| Descrição da Função | Ao selecionar na pergunta **Descrição das Atividades?**, o sistema apresenta as descrições de acordo com cada campo:   * **Cargo**: Apresenta a informação contida na rotina de **Cargos** (*GPEA370*) no campo **Ds. Detalhada** (*Q3\_MEMO1*). * **Função**: Apresenta a informação contida na rotina de **Funções** (*GPEA030*) no campo **Requisitos** (*RJ\_MEMOREQ*). * **Tarefa**: Apresenta a informação contida na rotina de **Tarefas** **por func.** (*MDTA090*) no campo **Descrição** (*TN5\_DESCRI*). |
| Agente | Caso a responta da pergunta **Quant. do Agente?** seja igual a **Sim**, a informação impressa será obtida com a junção da pergunta **Buscar Informações?**, apresentando a quantidade do agente de acordo com o risco:   * **Atual**: Apresenta a quantidade de agente encontrado no risco vinculado a função do funcionário; * **Da O.S.**: Apresenta a quantidade de agente encontrado no risco vinculado a função da O.S.. |
| EPIs de Uso Obrigatório | Para a impressão dos EPIs, o sistema faz uma junção de acordo com as duas perguntas: **Descrição das Atividades?** +**Buscar Informações?**   * **Cargo + Atual:** Apresenta a informação dos EPIs relacionados ao Centro de Custo + Risco (da função) do funcionário; * **Cargo + Da O.S**.: Apresenta a informação dos EPIs relacionados ao Centro de Custo + Risco (da função) da O.S.;      * **Função + Atual**: Apresenta a informação dos EPIs relacionados a Função, Centro de Custo + Risco (da função) do funcionário; * **Função + Da O.S**.: Apresenta a informação dos EPIs relacionados a Função, Centro de Custo + Risco (da função) da O.S.;      * **Tarefa + Atual**: Apresenta a informação dos EPIs relacionados ao Centro de Custo + Risco (da função) do funcionário; * Tarefa + Da O.S.: Apresenta a informação dos EPIs relacionados ao Centro de Custo + Risco (da função) da O.S.;     Onde se relaciona o EPI: No **risco**: rotina **Risco x EPI** (*MDTA125*); Na **Função**: rotina **EPI x Função** (*MDTA625*); No **Centro de Custo**: **rotina EPI x C. Custo** (*MDTA725*). |
| Recomendações | Apresenta a informação do campo **Detalhe OS.** (*TOB\_TEXTO*) da rotina de Ord. Serviço Func. (*MDTA305*). |
| Termo de Responsabilidade | presenta a informação do campo **Termo Resp.** (*TOB\_TERMO*) da rotina de Ord. Serviço Func. (*MDTA305*). |
| Aprovação | Apresenta a informação do campo **Responsável** (*TOB\_CODRES*) da rotina de Ord. Serviço Func. (*MDTA305*). |
| Colaborador | Apresenta a informação do campo **Funcionário** (*RA\_NOME*) da rotina de **Funcionários** (*GPEA010*), de acordo com o funcionário destinado a fazer a ordem de serviço. |
| Responsável pela empresa | Apresenta a informação selecionada na pergunta **Responsável Empresa?**. |

**Saiba Mais**  
[Artigos sobre PPRA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945454-MDT-PPRA)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20)  
[ChatBot Carol](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
