---
content_hash: 51852c6e25c432e01671dc5265fd4382c6eee195b7d22cb5dbfeaa303fa0235d
fetched_at: '2026-06-29T00:09:27.317303+00:00'
page_id: '423938499'
product: rm
source: tdn-rm
title: Gerar SPED Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938499
version: 13
---

O processo de geração do SPED Contábil consiste em criar um arquivo digital em um formato específico. Esse arquivo deverá ser submetido a um programa fornecido pela Receita Federal, o PVA (Programa Validador e Assinador).    
O PVA receberá o arquivo gerado pelo RM Saldus e irá realizar as seguintes tarefas:

* Validar Escrituração
* Assinar Escrituração
* Gerenciar Requerimento
* Transmitir Escrituração
* Consultar Situação

Depois de enviada para a receita, a escrituração contábil é armazenada em um banco de dados que irá permitir que os órgãos parceiros do SPED obtenham cópias integrais do arquivo. O titular da escrituração poderá, pela Internet, ter conhecimento de qual órgão teve acesso a sua escrituração. Uma vez transmitido, qualquer pessoa que tiver o arquivo, poderá verificar a autenticidade da escrituração contábil da empresa, visualizar e imprimir a escrituração.

E importante salientar que, apesar de realizar a manutenção no arquivo contábil, o PVA não permite alterações nas informações contábeis.

**Importante** **As empresas que ainda não estão obrigadas a entregar a ECD (Escrituração Contábil Digital), mas que forem auditadas pelo AFRFB (Auditor Fiscal da Receita Federal do Brasil) para entrega da IN 86 em relação aos arquivos contábeis, deverão obedecer ao layout do SPED Contábil. A adoção do layout do SPED Contábil supre a exigência fixada no ADE Cofis 15/2001 para as mesmas informações referentes a períodos anteriores.**

Antes da geração do SPED Contábil, sugerimos que seja executado o Pré – Validador do SPED Contábil para que assim os dados contábeis sejam pré-avaliados e as inconsistências que por ventura forem encontradas possam ser corrigidas antes da geração propriamente dita do arquivo digital, otimizando assim o envio dos dados

---

### Para gerar o SPED Contábil, é necessário o preenchimento de alguns parâmetros, conforme informações a seguir: **Plano Referencial****:** No menu Cadastros | Plano de contas paralelo é possível relacionar as contas do plano de contas contábil do sistema com as contas do plano de contas referencial fornecida pelo governo. Este processo é necessário quando a Sociedade Empresária estiver sujeita à regulamentação, seja do Banco Central ou da SRF. Para isso é necessário identificar a 'Instituição Responsável'. A opção 'Não Aplicável' neste cadastro deverá ser utilizada nos planos de contas paralelo cuja finalidade não seja a geração do SPED Contábil.

No Layout 2.0, o Plano de Contas Referencial da RFB, não poderá mais ser informado na geração do arquivo de Sped Contábil, caso informado o programa validador da Receita Federal apresentará erro. Este plano passa a ser obrigatório apenas para quem utiliza o plano de contas referencial do Banco Central (Cosif).

Para o Layout 3.0 foram disponibilizadas novas entidades responsáveis pela manutenção do Plano de Contas Referencial.

**Indicador do tipo de ECD** (disponível à partir do Layout 3.0) terá como opções:

* ECD de empresa não participante de SCP como sócio ostensivo.
* ECD de empresa participante de SCP como sócio ostensivo.  Quando este for o tipo selecionado, à seguir serão apresentadas para seleção, somente as Filiais parametrizadas como Sócio Ostensivo.
* ECD da SCP.  Quando este for o tipo selecionado, à seguir serão apresentadas para seleção, somente as Filiais que são SCP.

**Filial Matriz:** informe a filial Matriz responsável pela escrituração contábil.

**Tipo de Escrituração:** selecione o tipo de escrituração. Deverá ser "Centralizada" quando a Matriz for a responsável pelas informações das Filiais vinculadas à sua inscrição, e "Descentralizada" quando cada filial for a responsável por sua contabilização.

**Situação Especial:** de acordo com a situação, deve ser selecionada uma das opções: Abertura, Cisão, Fusão, Extinção, Incorporação, Transformação, ou Nenhum. Nos casos de extinção, cisão parcial, cisão total, fusão ou incorporação o SPED Contábil deverá ser entregue até o último dia útil do mês subsequente ao do evento.

A opção de "Transformação" será utilizada quando, por exemplo, a empresa passar de Limitada para Sociedade Anônima.

Ainda para o campo Situação Especial, não será possível a utilização da situação de "Abertura" para o Layout 2.0 e posteriores.

**Descentralização:** esse campo só será exibido quando o tipo de escrituração for "Descentralizada".

**Filial Escriturada:** esse campo só será exibido quando o tipo de "Descentralização" for por Filial. Selecione a filial que será escriturada.

**Filtro de Filial:** esse campo só será exibido quando o tipo de escrituração for "Centralizada". Se desejar, selecione a Filial ou Filiais para as quais o arquivo digital para o SPED Contábil será gerado. Vale lembrar que a utilização de Filtro de Filial é de sua inteira responsabilidade, pois somente os dados filtrados serão levados para o arquivo digital.

**Não enviar histórico de alteração de Contas Contábeis para o registro I050** e **Não enviar histórico de alteração de Centros de Custos para o registro I100:** Algumas alterações efetuadas nos cadastros das contas e centros de custos geram um histórico de alteração. Se estas opções forem marcadas serão enviadas somente a situação atual dos registros com suas respectivas datas de inclusão. Se estas opções não forem marcadas, serão enviados para o SPED Contábil todos os Históricos de alterações dos registros existentes na base de dados.

**Forma de Escrituração:** informe a Natureza do Livro, para o qual você deseja gerar o SPED, conforme o Cadastro de Escriturações.

**Demonstrações Contábeis:** Informe aqui o código da estrutura de 'Transferência de Grupos Contábeis' utilizada para a apuração de resultado do período, assim o sistema fará a leitura e indicará automaticamente o(s) Histórico(s) de Fechamento(s) utilizado(s) na estrutura indicada. Se preferir indicar manualmente o(s) código(s) do(s) Histórico(s) de Fechamento(s) utilizado(s) e suas respectivas datas, basta clicar no link correspondente, lembrando que o histórico aqui informado deverá ser o mesmo utilizado no fechamento do período, para zerar as contas de Receitas e Despesas através da Transferência de Grupos Contábeis. Informe também a data do fechamento em que foi utilizado. Cada fechamento deve utilizar histórico distinto. Se, por exemplo, o fechamento for trimestral, pelo menos quatro históricos devem ser informados, um para cada trimestre.

**Indicador do início do período** (disponível a partir do Layout 2.0) terá como opções:

* 0 - Normal (início no primeiro dia do ano)
* 1 - Abertura
* 2 - Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação
* 3 - Início de obrigatoriedade da entrega da ECD no curso do ano calendário

**Indicador de Finalidade da Escrituração** (disponível a partir do Layout 2.0) terá como opções:

* 0 - Original
* 1 - Substituta da escrituração com NIRE
* 2 - Substituta da escrituração sem NIRE
* 3 - Substituta da escrituração com troca de NIRE

**Observações**

* Quando a opção "3 - Substituta da escrituração com troca de NIRE" for selecionada, será apresentado um novo campo NIRE da escrituração que Está sendo Substituída, para que seja informado o novo NIRE.
* Quando as opções 1, 2 ou 3 forem selecionadas será apresentado um novo campo Hash da escrituração substituída para que seja localizado e selecionado o arquivo de Hash.

**Indicador de empresa de grande porte** (disponível no Layout 2.0) terá como opções:

* 0 - Empresa não é de Grande Porte
* 1 - Empresa de grande porte - Ativo Total superior a R$ 240.000.000,00 ou Receita Bruta Anual superior R$300.000.000,00.  **Ou**

**Indicador de entidade sujeita a auditoria independente** (disponível a partir do Layout 3.0) terá como opções:

* 0 - Empresa não é entidade sujeita a auditoria independente
* 1 - Empresa é entidade sujeita a auditoria independente - Ativo Total superior a R$ 240.000.000,00 ou Receita Bruta Anual superior R$300.000.000,00.

**DMPL / DLPA** (disponível a partir do Layout 2.0) **[**Estrutura da Demonstração**](http://tdn.totvs.com/x/qcpEGQ)**: Neste campo o usuário deverá selecionar uma estrutura de DMLP ou DLPA já criada anteriormente através do menu de Demonstração Contábil. Esta informação irá compor os registros J200, J210 e J215 do SPED.

Conforme a necessidade de envio, podem ser selecionadas as opções de Enviar somente Fatos Contábeis que tenha valor processado bem como Mostrar código do Fato Contábil juntamente com a descrição (registro J200).

**Parametrização da DRE / Balanço Patrimonial:** Nesta etapa pode-se definir como as informações serão enviadas para os respectivos registros além de se poder escolher mandar estas informações utilizando o modelo criado pela própria rotina do SPED Contábil ou um modelo próprio, que neste caso deverá ser criando previamente no menu Relatórios/Demonstração de Resultados. Nesta etapa deve ser definido também o Grau de Aglutinação. Para maiores informações sobre as Contas de Aglutinação [clique aqui](http://tdn.totvs.com/x/hMpEGQ).

J150: O registro J150 será gerado seguindo a ordem que foi definida nos fatos contábeis na [Estrutura](https://tdn.totvs.com/pages/viewpage.action?pageId=423938729) da Demonstração. Caso necessário, esta ordem pode ser alterada.  
A ordem do registro só será afetada caso neste passo da geração do SPED seja informada uma estrutura de demonstração, caso contrário, a ordem dos registros J150 não será alterada.

OBS: Quando escolhido pelo usuário gerar a DRE através da ferramenta de demonstrações contábeis, foi adicionado o flag 'Mostra fato Contábil com Valor zerado na geração do registro J150' que possibilita que o usuário gere fato com saldos igual a zero na ECD.

**Seleção de arquivos facultativos** Nesta etapa podem-se informar quais registros facultativos devem ser enviados para o arquivo do SPED Contábil. Estes registros (opcionais) variam de acordo com a Forma de Escrituração utilizada.

**J800 - Outras Informações** Nesta etapa, se desejar, selecione arquivos que contenham informações adicionais que julgue necessárias constar nos livros a serem entregues, tais como Pareceres, Demonstrações, Relatórios, etc. Estes arquivos devem ter a extensão .RTF

**J801 - Termo de Verificação para Fins de Substituição da ECD** Quando a escrituração contábil for substituta este registro deverá ser preenchido. O conteúdo do termo de verificação é de responsabilidade da empresa e a orientação do mesmo esta disponível no Manual de Orientações da ECD**.**Lembrando que o arquivo deverá ser salvo em extensão .RTF.

**Signatários:**O signatário marcado como responsável no  utilizada, será apresentado pré selecionado para uma melhor usabilidade (pode ser trocado caso seja necessário).

---

### **Baixar Arquivo Gerado**

Após a execução do processo, o arquivo digital será salvo na máquina em um caminho fixo. Caso seja desejado, o arquivo poderá ser salvo em um caminho específico, indicado por você. Para isto clique no botão "Baixar Arquivo" e informe os dados.

Para otimizar a utilização da memória evitando travamento na execução do processo de geração do SPED, o sistema utiliza o recurso de **Upload** dos arquivos manipulados, tais como arquivo com modelo próprio para o Razão Auxiliar e Arquivos Adicionais-J800, levando-os parcialmente para o servidor de aplicação liberando a memória. Ao mandar Copiar o arquivo gerado o sistema utiliza o recurso de **Download** para baixar o arquivo do servidor para o local indicado.

**Observações**

* O Conselho Federal de Contabilidade (CFC) publicou no Diário Oficial da União (DOU), a revisão dos itens 8 e 11 do Comunicado Técnico Geral (CTG) 2001, que estabelece o detalhamento dos procedimentos a serem observados na escrituração contábil de forma digital. Os principais pontos são a alteração na transmissão do plano de contas para o Sistema Público de Escrituração Digital (Sped) e a ratificação de que o Livro Diário só precisará ser autenticado em registro público ou entidade competente quando legislação específica exigir. O CTG 2001 também determina que o plano de contas transmitido para o Sped junto com os Livros Diários e Auxiliares, e com os documentos da Escrituração Contábil Digital, contenha apenas contas que tenham saldo ou sido movimentadas no período.

Ou seja, somente deverão ser geradas informações para as contas contábeis que tenham saldo  ou tenham sido movimentadas no período da geração.

Para isso, será aplicada a regra detalhada acima, porém se mesmo assim usuário desejar enviar as informações das contas contábeis que um dia tiveram movimentação o sistema disponibilizara um parâmetro que poderá ser marcado para que isto ocorra durante a geração.

Em: Parâmetros >> TOTVS Gestão Contábil >> Rotinas Legais >> SPED Contábil

Opção: Enviar para o SPED Contábil / ECF Contas Contábeis que não tenha saldo ou  movimentação no período da geração ?

Registros impactados:

I015: Identificação das Contas da Escrituração Resumida a que se Refere a Escrituração Auxiliar.

I050: Plano de Contas.

I155: Detalhe dos Saldos Periódicos.

I250: Partidas do Lançamento.

I310: Detalhes do Balancete Diário.

I355: Detalhes dos Saldos das Contas de Resultado Antes do Encerramento.

* Todas as vezes que esta rotina fiscal for executada será verificado se o período indicado para a respectiva geração é igual ao período em que a ferramenta de Diagnóstico de Rastreabilidade dos Lançamentos Contábeis foi executada. Caso seja diferente, será sugerido que a ferramenta de "Diagnóstico" seja executada para o mesmo período de geração da rotina fiscal minimizando, assim, possíveis problemas na validação do arquivo gerado por esta rotina.
* Ao final do processo serão gerados LOG´s com informações relevantes sobre os dados levados para os registros do arquivo digital assim como LOG's de execução, indicando todas as ações realizadas para a geração do SPED e o tempo gasto em cada uma. Favor avaliar o conteúdo da pasta Logs.
* Após a geração e validação do arquivo do SPED Contábil pelo PVA da ECD, é importante que antes de realizar a Transmissão da Escrituração Contábil, os relatórios (DRE, Balanço Patrimonial, DMPL/DLPA e outros) apresentados no validador sejam conferidos com os relatórios gerados pelo TOTVS Gestão Contábil.
* Após a conferência, o arquivo deverá ser assinado digitalmente pelo empresário ou representante legal da sociedade empresária e pelo contabilista responsável pela escrituração.
* Depois de transmitida, a escrituração contábil é armazenada em um banco de dados que irá permitir que os órgãos parceiros do SPED obtenham cópias integrais do arquivo. O titular da escrituração poderá, pela Internet, ter conhecimento de qual órgão teve acesso a sua escrituração.
* Uma vez transmitida, qualquer pessoa que tiver o arquivo, poderá verificar a autenticidade da escrituração contábil da empresa, visualizar e imprimir a escrituração.
* Para obter mais informações sobre os procedimentos, obrigatoriedade, prazos, entre outras informações, o Ministério da Fazenda mantem à disposição de todos um resumo com as Perguntas mais Frequentes conforme o link abaixo.

OBS.: Caso o usuário precise gerar registro I355 com contas sem valores(zeradas), basta marcar o parâmetro de sistema "Enviar para o SPED Contábil/ECF Contas Contábeis que não tenha saldo ou movimentação no período da geração?", presente na etapa de Rotinas Legais.

Recursos Adicionais

* [Perguntas Frequentes - Receita Federal](http://www1.receita.fazenda.gov.br/faq/sped-contabil.htm)
Veja também


* Demonstração Contábil - Estrutura
