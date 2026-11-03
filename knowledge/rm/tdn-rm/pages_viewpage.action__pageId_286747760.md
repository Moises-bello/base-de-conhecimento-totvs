---
content_hash: b50df1a18a5dc75c868556847a2b097975c0359b4d269a8a559feea9d0eb3753
fetched_at: '2026-06-29T00:08:41.751173+00:00'
page_id: '286747760'
product: rm
source: tdn-rm
title: RMPAT00001_Exclusão e Importação de Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286747760
version: 5
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.14 Ou superior |
| **Ocorrência:** | Exclusão e Importação de Relatórios |
| **Ambiente:** |  |
| **Passo a passo:** | Os Relatórios padrões do Totvs Gestão Patrimonial são gerados através do Menu Relatórios/Integrações. Se trata dos relatórios de maior utilização dentro do Totvs Gestão Patrimonial. Este relatório reúne informações referentes às movimentações tendo como finalidade o gerenciamento do patrimônio e/ou a prestação de contas à legislação em vigor. Ele ainda permite que as informações sejam filtradas pelo intervalo de [Contas Contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=286516194) ou por [Grupo de Patrimônio](https://tdn.totvs.com/pages/viewpage.action?pageId=244921356), possibilitando maior flexibilidade durante a parametrização.  Acesse o módulo BackOffice | Gestão Patrimonial:  Disponível através do menu | Gestão | Rm Reports.    Crie um Filtro selecionando as opções abaixo:  Menu Descrição | Operador: IS NOT NULL | Adicionar | Salvar | Informe o nome do filtro | TODOS (o o que desejar) | Selecione o filtro | Executar.    Clique na seta ao lado do Ícone Gestão patrimonial para expandir os dados de Coligada Global e Coligadas | Clique na seta de expansão da coligada em questão | Selecione os relatórios e clique em Excluir.    Selecione o Aplicativo do RM Bonum | Processos | Importar Estrutura de Relatório.    Acesse o caminho: C:\totvs\CorporeRM\ObjetosGerenciais\Relatórios | Selecione todos os relatórios (de acordo com a imagem abaixo) | Ok.      **Observação:** Não altere a nome que será apresentado no campo Código do relatório | Clique em Executar.      Caso no processo este “ponto de exclamação  ” apareça é porque os relatórios selecionados já existem na visão. Verifique se todos que estão sendo importados realmente foram excluídos. Caso não tenha, será necessário excluir primeiro e importar novamente.     Após realizar a importação será possível visualizar as estruturas importadas na visão.    Lembrando que o processo de emissão dos relatórios padrões: [Depreciação](https://tdn.totvs.com/pages/viewpage.action?pageId=423937993), [Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=423937991), [Ficha de Imobilizado](https://tdn.totvs.com/pages/viewpage.action?pageId=423938271), [Agrupamento por Contas](https://tdn.totvs.com/pages/viewpage.action?pageId=423937973) e [Ocorrências](https://tdn.totvs.com/pages/viewpage.action?pageId=423937981) deve ocorrer através do menu Relatórios/Integrações. |
| **Observações:** | Vale ressaltar que este processo de importação e válido para todos os relatórios utilizado pelo processo RM Reports. |
