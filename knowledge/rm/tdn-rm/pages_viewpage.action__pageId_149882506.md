---
content_hash: 43d1b11b4876a633fb107114fc92057a2845a6793e7d4e61fcb2fe082ad3dfba
fetched_at: '2026-06-29T00:05:56.409747+00:00'
page_id: '149882506'
product: rm
source: tdn-rm
title: Como Fazer - Parametrização do Relatório do Espelho do Cartão.Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149882506
version: 1
---

|  |
| --- |
| **Produto:** *TOTVS Gestão de Automação de Ponto***Versão:***11.4 X ou superior* |
| **Processo:** *Relatório do Espelho do Cartão de Ponto* |
| **Subprocesso:** **Parametrização e configuração no gerador de relatórios (RM Reports)** |
| *****Introdução***** |
| Existe no TOTVS Automação de Ponto, o módulo para parametrização para impressão do “Relatório do Espelho do Cartão de Ponto”.  Este módulo permite parametrizar a emissão do relatório em conformidade com as necessidades do cliente.  Esta parametrização será feita no wizard “Relatório do Espelho do Cartão de Ponto” e, se houver necessidade, no gerador de relatórios através do RM Reports com a flexibilidade de renomear campos, ocultar campos, adicionar novos, criar fórmulas, criar consultas.  O processo de alteração no Gerador de Relatórios depende de parametrizações específicas do produto TOTVS Reports e aqui se tem as orientações para defini-las. |

**Desenvolvimento/Procedimento**

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Ordena por Nome | SubFuncionário -   CabeçalhodoDetalhe12 - Ordenação - Coleção | Ordena por Seção e Chapa |
| Ordena por seção e chapa | SubFuncionário - CabeçalhodoDetalhe12   - Ordenação - Coleção | Ordena por Seção e Chapa |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime discriminação de abonos | SubFuncionário - Abono - Detalhe 17   - Visível = Sim | Visível = Não |
| Imprime código e planilha de abono | SubFuncionário - Abono - Detalhe 17   - Visível = Sim | Visível = Não |

                

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime totais de horas | Inicio | Filtro | Disponível sem filtro |
| Imprime totais de extras nas faixas | Inicio | Filtro | Disponível sem filtro |
| Não imprime totais zerados | Inicio | Filtro | Disponível sem filtro |
| Imprime somente exceções | Inicio | Filtro | Disponível sem filtro |
| Totais Extras | Inicio | Filtro | Disponível sem filtro |
| Totais Afastamentos | Inicio | Filtro | Disponível sem filtro |
| Totais Faltas | Inicio | Filtro | Disponível sem filtro |
| Totais DSR | Inicio | Filtro | Disponível sem filtro |
| Totais Atrasos | Inicio | Filtro | Disponível sem filtro |
| Totais Saldo Banco Horas | Inicio | Filtro | Disponível sem filtro |
| Totais Adic Noturno | Inicio | Filtro | Disponível sem filtro |
| Totais Horas Base | Inicio | Filtro | Disponível sem filtro |
| Totais Abonos | Inicio | Filtro | Disponível sem filtro |
| Totais Horas Trabalhadas | Inicio | Filtro | Disponível sem filtro |
| Totais Nona Hora | Inicio | Filtro | Disponível sem filtro |
| Exceções Extras Executadas | Inicio | Filtro | Disponível sem filtro |
| Exceções Extras Autorizadas | Inicio | Filtro | Disponível sem filtro |
| Exceções Atrasos | Inicio | Filtro | Disponível sem filtro |
| Exceções Faltas | Inicio | Filtro | Disponível sem filtro |
| Exceções Abonos | Inicio | Filtro | Disponível sem filtro |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime eventos da movimentação | SubFuncionário -   EventosMovimentoPeríodo - Visível = Sim | Visível = Sim |

                             

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime eventos calculados por   fórmulas | SubFuncionário - EventosCalculados   - Visível = Sim | Visível = Sim |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime eventos de refeição | SubFuncionário - EventoRefeicao -   Visível = sim | Visível = Sim |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime Horário em cada dia | SubFuncionário - Batidas -   HorárioPlanejadoData - Visível = sim | Visível = Não |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime Descrição do Horário | SubFuncionário - Horário - Visível = sim | Visível = Sim |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime Histórico do Horário | SubFuncionário - QuadroHorário -   Visível = sim | Visível = Sim |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Um funcionário por página | SubFuncionário - RodapédoDetalhe3 -   Quebra de Página | Depois da Seção |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime local para assinatura | SubFuncionário - RodapédoDetalhe3 -   Campo a campo - Visível = verdadeiro | Visível = verdadeiro |
| Imprime assinatura da chefia | SubFuncionário - RodapédoDetalhe3 -   Campo a campo - Visível = verdadeiro | Visível = verdadeiro |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime Colunas selecionadas | SubFuncionário - Batidas - Detalhe   15 - Seta na coluna | Conforme cada coluna |
| Colunas Extras executadas | SubFuncionário - Batidas - Detalhe   15 - Seta na coluna - Ligação de Dados | Extras executadas |
| Colunas Extras autorizadas | SubFuncionário - Batidas - Detalhe   15 - Seta na coluna - Ligação de Dados | xxxx |
| Colunas Atrasos | SubFuncionário - Batidas - Detalhe   15 - Seta na coluna - Ligação de Dados | Atrasos |
| Colunas Faltas | SubFuncionário - Batidas - Detalhe   15 - Seta na coluna - Ligação de Dados | Faltas |
| Colunas Abonos | SubFuncionário - Batidas - Detalhe   15 - Seta na coluna - Ligação de Dados | Abonos |
| Colunas Horas Trabalhadas | SubFuncionário - Batidas - Detalhe   15 - Seta na coluna - Ligação de Dados | xxxx |
| Colunas Adicional Noturno | SubFuncionário - Batidas - Detalhe   15 - Seta na coluna - Ligação de Dados | Adicional Noturno |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime Período de Férias | SubFuncionário - PeríodoFérias -   Visivel = sim | Visível = Não |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime Informações do dia ponte | SubFuncionário - DiaPonte - Visível   = sim | Visível = Não |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime apenas cargo do funcionário | SubFuncionário - CabeçalhodoDetalhe12   - Selecionar campo - Visível = verdadeiro | Visível = verdadeiro |
| Imprime apenas função do   funcionário | SubFuncionário -   CabeçalhodoDetalhe12 - Selecionar campo - Visível = verdadeiro | Visível = verdadeiro |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime descrição do atraso | Relatório do Espelho do Cartão de   Ponto - Passo 2 - Preencher ou não | Em branco |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime espelho de acordo com a Jornada | Alterado para Imprime espelho de   acordo com a Jornada | Desmarcado |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Mensagem | Exibição | Janelas | Ferramentas |   Controles padrões arrastar texto para inserir | Sem mensagem |
| Imprime observação abaixo | Exibição | Janelas | Ferramentas |   Controles padrões arrastar texto para inserir | Sem observação |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime Campo Complementar | SubFuncionário -   CamposComplementares - Visivel = Sim | Visível = Não |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Imprime Logomarca | Somente retirar caso não queira a   impressão da logomarca ou trocar a imagem | Imagem do cadastro de coligadas. |

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Gerador de Relatório** | **Default/Padrão para o Relatório   Oficial** |
| Totais – Totais de batidas | Montando filtros de acordo com o   que deve ser totalizado | Sem filtro |

- Na tela de filtros, inserir o filtro desejado:

- Como exemplo, foi montado um filtro para retornar os totais que contenham a descrição “D.S.R”:

- Feito isso, gerar o relatório de espelho:

**Informações Adicionais**

O relatório a ser gerado deve ser importado em TOTVS Reports para ser selecionado no processo de gerar o espelho do relatório.

O Relatório do Espelho do Cartão de Ponto poderá ser personalizado sempre que for necessário, mas para isto será preciso importar o relatório oficial, exportar para um diretório local e depois importar novamente. Isto deve ser feito para manter a integridade do relatório original, oficial da TOTVS.

Defaults do relatório oficial da TOTVS estão descritos em cada item relacionado acima.

**Dicas para criação dos filtros**

**-** **Códigos ocorrência:**

- **Códigos de cálculos:**
