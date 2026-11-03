---
content_hash: 354f7ddc51a1aac0e81215677a176ac77bf854d6b6bbc5af9e09c542100a7862
fetched_at: '2026-06-29T00:09:16.726071+00:00'
page_id: '421385541'
product: rm
source: tdn-rm
title: Relatórios de Composições de Custo Horário Planilhas .NET 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385541
version: 80
---

**Relatórios de Composições de Custo Horário Planilhas .NET** 
Migração do relatório de composições de custo horário utilizando a Planilha.NET.
  As opções de filtro "Equipamentos" e "Mão de obra", serão usadas para filtrar os registros do respectivo Grupo DNER;   Após selecionar os insumos(seleção obrigatória) e clicar  no botão "Gerar", será enviado diretamente para impressora relatórios (um relatório para cada insumo selecionado) contendo informações recuperadas através do recálculo de uma planilha. Essa planilha será recuperada da tabela "GPlan - cadastro de planilhas do RM" através do campo "IdPlan" recuperado da tabela "MIsm.IdPlan". Para efetuar o cálculo dessas planilhas de "Custo horário", algumas informações do cadastro de insumos e dos parâmetros gerais são enviadas para essas planilhas substituindo as constantes presentes nessas planilhas do Solum, entre elas:   a)      Dados recuperados da tabela MIsm:   Constante = "CISM " | Valor = Parametro.CODISM; Constante = "DISM " | Valor = Parametro.DESCISM; Constante = "QTDEISM" | Valor = \[Somatório da quantidade recuperada da tabela MABCIsm.Quantidade (filtrada por coligada, id projeto, insumo)\] Constante = "CLI1" | Valor = MIsm.CLIVREVALOR1; Constante = "CLI2" | Valor = MIsm.CLIVREVALOR2; Constante = "CLI3" | Valor = MIsm.CLIVREVALOR3; Constante = "CLI4" | Valor = MIsm.CLIVREVALOR4; Constante = "CLI5" | Valor = MIsm. CLIVREVALOR5; Constante = "CLI6" | Valor = MIsm.CLIVREVALOR6; Constante = "CLI7" | Valor = MIsm.CLIVREVALOR7; Constante = "CLI8" | Valor = MIsm.CLIVREVALOR8; Constante = "CLI9" | Valor = MIsm.CLIVREVALOR9; Constante = "CLI10" | Valor = MIsm. CLIVREVALOR15; Constante = "CLI11" | Valor = MIsm.CLIVREVALOR16; Constante = "CLI12" | Valor = MIsm.CLIVREVALOR17; Constante = "CLI13" | Valor = MIsm.CLIVREVALOR18; Constante = "CLI14" | Valor = MIsm.CLIVREVALOR19; Constante = "CLI15" | Valor = MIsm. CLIVREVALOR20; Constante = "CLI16" | Valor = MIsm.CLIVREVALOR21; Constante = "CLI17" | Valor = MIsm.CLIVREVALOR22; Constante = "CLI18" | Valor = MIsm.CLIVREVALOR23; Constante = "CLI19" | Valor = MIsm.CLIVREVALOR24; Constante = "CLI20" | Valor = MIsm. CLIVREVALOR25;   b)      Dados recuperados da tabela de parâmetros (MParametro):   Constante = "CLP1" | Valor = Parametro.CLIVREVALOR1PAR; Constante = "CLP2" | Valor = Parametro.CLIVREVALOR2PAR; Constante = "CLP3" | Valor = Parametro.CLIVREVALOR3PAR; Constante = "CLP4" | Valor = Parametro.CLIVREVALOR4PAR; Constante = "CLP5" | Valor = Parametro.CLIVREVALOR5PAR; Constante = "CLP6" | Valor = Parametro.CLIVREVALOR6PAR; Constante = "CLP7" | Valor = Parametro.CLIVREVALOR7PAR; Constante = "CLP8" | Valor = Parametro.CLIVREVALOR8PAR; Constante = "CLP9" | Valor = Parametro.CLIVREVALOR9PAR; Constante = "CLP10" | Valor = Parametro.CLIVREVALOR10PAR; Constante = "CLP11" | Valor = Parametro.CLIVREVALOR11PAR; Constante = "CLP12" | Valor = Parametro.CLIVREVALOR12PAR; Constante = "CLP13" | Valor = Parametro.CLIVREVALOR13PAR; Constante = "CLP14" | Valor = Parametro.CLIVREVALOR14PAR; Constante = "CLP15" | Valor = Parametro.CLIVREVALOR15PAR; Constante = "CLP16" | Valor = Parametro.CLIVREVALOR16PAR; Constante = "CLP17" | Valor = Parametro.CLIVREVALOR17PAR; Constante = "CLP18" | Valor = Parametro.CLIVREVALOR18PAR; Constante = "CLP19" | Valor = Parametro.CLIVREVALOR19PAR; Constante = "CLP20" | Valor = Parametro.CLIVREVALOR20PAR;   Restrições   As planilhas do RM Solum cadastradas atualmente na ferramenta de planilhas Delphi deverão ser convertidas para a nova ferramenta de planilhas da RM utilizando o executável MigradorPlan.exe.
 ]]>

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Nome Amigável do Link 1 Nome Amigável do Link 2

|  |  |
| --- | --- |
|  | Como Fazer |

---

Nome Amigável do Link 1 Nome Amigável do Link 2

|  |  |
| --- | --- |
|  | Recursos Adicionais |

---

Nome Amigável do Link 1 Nome Amigável do Link 2

|  |  |
| --- | --- |
|  | Veja Também |

---

Nome Amigável do Link 1 Nome Amigável do Link 2
