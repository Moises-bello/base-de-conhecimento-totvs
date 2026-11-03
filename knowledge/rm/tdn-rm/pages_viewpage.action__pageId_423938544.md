---
content_hash: 19e133a6ffadc249462e180bfbc42a3ad0718caa39a1161cd505edca748bc9bd
fetched_at: '2026-06-29T00:09:27.559863+00:00'
page_id: '423938544'
product: rm
source: tdn-rm
title: Relatório Balancete
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938544
version: 23
---

Pré-Requisitos

O Balancete é um relatório contábil oficial exigido pela Legislação. Ele reflete a contabilidade de uma empresa ou organização num determinado período. Para emiti-lo no TOTVS Gestão Contábil, siga as orientações abaixo:

Acesse o menu "Relatórios" e em seguida a opção Balancete. Será aberta uma janela de processo para configuração do Relatório. As informações escolhidas ao emitir este relatório serão gravadas pelo sistema nas preferencias do mesmo. Assim ao entrar novamente no relatório você visualizará as últimas opções escolhidas.

O relatório Balancete é totalmente parametrizado, ou seja, dependendo da opção marcada, pode ser criado mais etapas ou novos campos nas mesmas, por esse motivo veja cada etapa e opções que a mesma possibilita.

O processo para emissão do relatório é divido nas seguintes etapas:

Exportação com Smart ViewExportação com Smart View

Novo Tipo de Saída adicionado.

Configurar Recurso Smart View

Segue documentação: 

Parâmetros Contemplados

**1 -** Intervalo de Datas e se as informações serão buscadas do histórico:

**2 -** Filtro de Coligada\Filial\Departamento:

**3 -** Tipo de Balancete FIXO como **Contábil**:

**4 -** Opções de Imprimir\Filtrar:

**5 -** Filtro de Lotes:

**6 -** Filtros de Conta Contábil \ Centro de Custo \ Histórico:

**7 -** Tipo de Valor (Moeda):

**8 -** Imprimir Valores e Milhares e Não imprimir os centavos:

---

Após selecionado o tipo Smart View, deverá preencher o Lookup para informar o Recurso do Smart View

**Validação** com relação ao Tipo do Razão informado.

Após gerar, é necessário clicar em **"Enviar"** na tela do Smart View pois o usuário pode ter parametrizado outros filtros no relatório.

**Exibição do Relatório:**

**Geração do relatório via agendamento/JOB:**

O usuário ainda possui a opção de agendar a geração do relatório para acessá-lo posteriormente no caso de, por exemplo, existirem muitas contas e/ou transações a processar.

Neste caso o relatório é gerado como um job e armazenado em um arquivo interno. Para visualizá-lo o usuário deve acessar o log de processamento do job (relativo ao processamento/geração do relatório) onde neste log estará disponível a opção para visualização.

Para esta opção, [agendamento e processamento como um job](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005088792-Framework-Linha-RM-Frame-Como-agendar-a-execu%C3%A7%C3%A3o-de-um-processo), ao final das etapas de opções do relatório será apresentado as opções de agendamento. O usuário deve escolher a que mais lhe convém e acionar a execução (clicar em "Executar").

 

Ao fazê-lo o sistema enviará o processo/relatório para a fila de execução e apresentará uma mensagem com o identificador do job (JobID) e instruções para acessar o log e visualizar o relatório depois de pronto.

 

Acessando o Gerenciamento de jobs, o registro/log de execução de nosso relatório em questão e enfim visualizando o relatório.

   

Veja Também

* [Boletim Técnico Relatório Balancete](http://tdn.totvs.com/display/rm/CTB_BT_Balancete_CTB000148)
