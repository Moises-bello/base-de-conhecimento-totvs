---
content_hash: dad642ca6fd4082d1c84db16016f2c9f66e667c3c07b0e2e7711946e020f58fc
fetched_at: '2026-06-29T00:06:18.349382+00:00'
page_id: '215483813'
product: rm
source: tdn-rm
title: ORC0001_Importacao_de_Orcamento_via_Arquivo_txt_ou_Excel
type: documentation
url: https://tdn.totvs.com/display/LRM/ORC0001_Importacao_de_Orcamento_via_Arquivo_txt_ou_Excel
version: 157
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e superiores |
| **Ocorrência:** | Descrição do processo de importação de orçamento. Seja o arquivo txt ou Excel |
| **Ambiente:** | Importação de Orçamento |
| **Passo a passo:** | O processo de Importação de Orçamento possibilitará ao usuário a criação de valores orçados automaticamente, ou a atualização de valores já cadastrados.    Antes de realizar a importação, deverá realizar os vínculos obrigatórios para utilização do controle orçamentário, são eles:   * Vínculo do Usuário ao Centro de Custo * Vinculação da Natureza do Orçamento ao Centro de Custo     Este processo pode ser feito via arquivo texto (.txt) e/ou planilhas excel (.xls).  **Caminho Módulo exe:**Menu Utilitários | Importações / Exportações | Importar Orçamento      **Caminho MDI:** Menu Orçamento | Importação de Orçamento        **Abaixo, segue layout a ser seguido para criação dos arquivos de importação:**  **Importante:** A coluna GRUPO ORÇAMENTÁRIO somente deverá ser preenchida se nos parâmetros de Controle Orçamentário a opção de Usa Tabela de Grupo Orçamentário, estiver com os valores **USA** ou **USA OBRIGATORIAMENTE.**    Arquivo Texto:   | **CAMPO** | **TIPO** | **TAMANHO** | **CASAS DECIMAIS** | **POSIÇÃO** | | --- | --- | --- | --- | --- | | Código do Centro de Custo | A | 25 | - | 001 - 025 | | Código da Natureza Orçamentária/Financeira | A | 40 | - | 026 - 065 | | Data | Data | 10 | - | 066 - 075 | | Valor Orçado | N | 20 | 4 | 076 - 095 | | Grupo Orçamentário | A | 40 | - | 096 - 135 |     Planilha Excel:   | **CAMPO** | **TIPO** | | --- | --- | | Código do Centro de Custo | Texto | | Código da Natureza Orçamentária/Financeira | Texto | | Data | Data | | Valor Orçado | Moeda | | Grupo Orçamentário | Texto |     Arquivos de exemplo (Contém um txt e um xls):  250      **Observações**:   1 - Os campos de Código do Centro de Custo, Código da Natureza Orçamentária/Financeira e Grupo Orçamentário devem ter seu tipo como Texto, caso contrário, se na máscara do cadastro estiver com o número 0 à esquerda (exemplo: 001), o excel irá ignorar, podendo assim criar inconsistências e erros ao importar o orçamento.  2 - A primeira linha do arquivo deverá conter o nome das colunas, na seguinte ordem: Código do Centro de Custo, Código da Natureza Orçamentária/Financeira, Data, Valor Orçado e Grupo Orçamentário.  3 - O campo de data deverá seguir o formato DD/MM/AAAA  4 - A importação pode ser feita inclusive para orçamentos que estejam bloqueados.  5 - A importação sempre afetará o valor orçado. Caso este seja zero, e, tente importar um valor negativo, deverá ser gerada uma exceção e a importação não poderá ser concluída.  5.1 - Valores negativos poderão ser importados, desde que este não deixe o valor orçado negativo.  Exemplo:  **Valor Orçado:** R$ 50.000,00 | **Valor a ser importado:** R$ -50.000,00 (Neste caso, o sistema irá realizar a importação, e deixará o campo de valor orçado zerado).  **Valor Orçado:** R$ 30.000,00 | **Valor a ser importado:** R$ -31.000,00 (Neste caso, o sistema irá apresentar erro pois o valor não pode ficar negativo).  Vale lembrar que a medida que as movimentações forem sendo feitas, o valor não será exatamente igual ao que está no Valor Orçado. Nestes casos, aconselhamos que seja verificado o saldo DISPONÍVEL para o item de período a qual está tentando realizar a importação. Tal saldo pode ser visto em Consulta Valores de Orçamento.      Para mais informações sobre o controle orçamentário, segue link:  **Controle Orçamentário** |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |

divs
