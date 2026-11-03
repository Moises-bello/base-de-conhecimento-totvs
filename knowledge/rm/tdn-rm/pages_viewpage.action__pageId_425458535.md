---
content_hash: f7f543d540c1398dfa2a852d2acb97e9480946dd5cae3ecdeea52e5c657575d4
fetched_at: '2026-06-29T00:09:30.821460+00:00'
page_id: '425458535'
product: rm
source: tdn-rm
title: Estatísticas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458535
version: 1
---

**Estatísticas**

---

O processo de estatísticas permite levantar dados e informações probabilísticas que facilitam a análise para criação de estratégias relativas aos atendimentos ou às campanhas de marketing.   
Através do processo "Estatísticas" é possível gerar gráficos sobre quantidade e porcentagem de campos selecionados. Os campos podem ser campos da edição do atendimento (com exceção de campos textos livres: solicitação, solução, discussão) e parâmetros (com exceção de parâmetros do tipo Texto).  
O processo está disponível na tela de visão dos atendimentos e nas operações de telemarketing.  
Para atendimentos com o mesmo tipo de atendimento, os parâmetros relacionados, serão apresentados no momento da geração do gráfico para seleção, mas para atendimentos com tipos de atendimento diferenciados somente os campos da edição do atendimento estarão disponíveis. Esta regra também é válida para as campanhas. Os parâmetros serão mostrados com o prefixo PARAMETRO\_.  
No caso da tele-operação, teremos a particularidade de que caso os processos com filtros "Não Atuados" ou "Agendados", apenas os parâmetros serão mostrados (caso existam). Para que mostre campos fixos da tele-operação, será necessário executar o processo com o filtro "Concluído", essa regra é necessária por que apenas com a tele-operação concluída teremos condição de extrair informações, pois os dados estão gravados na tabelas, nos dois casos citados acima a tele-operação ainda não foi gravada.  
Vale ressaltar que para que o processo seja executado, pelo menos um campo deve ser selecionado na elaboração do gráfico, caso contrário uma mensagem de alerta será apresentada e o processo não será concluído.   
O tipo do gráfico e o argumento devem ser setados:  
Tipo: Bar, Point, Pie, Doughnut.  
Argumento: Quantidade, Porcentagem.  
Obs.: Todos os campos podem ser selecionados para geração do gráfico, caso seja necessário. Foi disponibilizado um checkbox para marcação no canto esquerdo da tela.  
Para cada gráfico gerado, um duplo-clique na área do gráfico apresenta uma tela de visão com todos os atendimentos que preencham aquele requisito ou com todas as operações de telemarketing que compõem aquele parâmetro da campanha.  
Os gráficos podem ser exportados em vários formatos (.XLS , .PDF , .RTF , .HTML) ou até mesmo enviado por e-mail informando o destinatário. O remetente será o e-mail do atendente logado.
