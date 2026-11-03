---
content_hash: b692bd6b6b15a1a69357cc13ae83a016d2a95501e6daa97370c44e3cc009b795
fetched_at: '2026-06-29T00:10:05.881218+00:00'
page_id: '452719304'
product: rm
source: tdn-rm
title: GPS - Guia de INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/GPS+-+Guia+de+INSS
version: 16
---

falseATENÇÃO:A partir da versão 12.1.2406, esse processo foi descontinuado. A GPS foi substituída pela DCTFWeb.  

* Para a geração do lançamento financeiro da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=727915586)
* Para conferência dos valores da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=717708785)

A Guia da Previdência Social (GPS) é uma obrigação tributária principal devida por todas as pessoas jurídicas e equiparadas, que possuam funcionários.

É utilizada também para o recolhimento devido pelas empresas sobre remunerações a trabalhadores autônomos e profissionais liberais, para a contribuição de sócios ou administradores a título de pró-labore, e para importâncias retidas de terceiros, nos termos estabelecidos pela Lei Orgânica da Previdência Social.   
Através deste processo é possível gerar/imprimir a Guia da Previdência Social (GPS) para o recolhimento das contribuições sociais pagas pela empresa.  
   
**Tela Parâmetros**  
**Quebra de Seção**  
A emissão do identificador na GPS é de acordo com a parametrização da seção da quebra informada, sendo:  
CNPJ ou CPF, quando na seção o parâmetro 'Identificação pelo CNPJ' está marcado, independente de existir CEI na seção;  
   
CEI quando os parâmetros 'Pessoa Física' ou 'Identificação pelo CNPJ' não estão marcados e existe CEI informado na seção;  
   
CEI quando o parâmetro 'Pessoa Física' está marcado e existe CEI informado;  
   
Em Branco quando os parâmetros 'Pessoa Física' ou 'Identificação pelo CNPJ' não estão marcados e não existe parametrização para CEI ou então não existe CEI informado.  
   
   
**Competência**  
Os valores utilizados para o cálculo são extraídos do envelope do funcionário (PFFINANC), verificando sempre a incidência atual dos eventos, independente se a competência é retroativa.  
   
   
**Código de Pagamento**  
Informe o código da GPS para geração da guia.  
   
**Observação:**  
Não preenchendo o campo, é considerado automaticamente o campo código GPS existente em Administração de Pessoal | Seções | aba Dados p/ INSS.  
   
   
**Percentuais para cálculo**  
**Perc. Empresa**  
Informe o percentual de recolhimento de INSS por parte da empresa, desconsiderando os demais percentuais como: Acidente de Trabalho, FAP, Terceiros.  
Para o cálculo de Terceiros é utilizado o percentual informado na seção conforme a quebra.  
Para o cálculo do Acidente de trabalho é utilizado o percentual informado na seção conforme a quebra, multiplicado pelo FAP cadastrado nos Valores Fixos.  
   
**Perc. Autônomos**  
Informe o percentual de recolhimento de INSS a ser calculado sobre os eventos com código de cálculo 046-Honorários.  
   
**Perc. Cooperativa**  
Informe o percentual de recolhimento a ser aplicado no campo 'Valor Cooperativas' na aba 'Valores da Seção'.  
   
**Movimento por Tomador**  
Com o parâmetro marcado a GPS é gerada verificando a distribuição por tomador.   
Sendo necessário selecionar o tipo de prestação de serviço: 'Cessão de Mão de Obra' ou 'Construção Civil', observando as parametrizações do Tomador de Serviço (Parametrizador).  
   
Quando é desmarcado o parâmetro "Movimento por Tomador", é necessário marcar o parâmetro em Parametrizador, pasta Folha Normal/Encargos Sociais/ "Utiliza Controle de Compensação na Guia de INSS" , para habilitar as opções de "código de recolhimento para compensação" na geração da Guia de INSS.   
   
   
**Atenção I:**  
É habilitado quando em Tomador de Serviço (Parametrizador) o parâmetro 'Utiliza Tomador de Serviço' está marcado.  
   
            
**Recolhimento em Atraso**  
São habilitados os campos 'Multa (%)' e 'Juros de Mora (%)', sendo estes percentuais são aplicados sobre o campo 'Líquido' dos 'Valores da Seção'.  
**Controle de Compensação**  
Tem o objetivo em controlar os valores de compensação do mês (Retenção, Compensação e Dedução) que não são utilizados na geração da guia de INSS devido não existir saldo, e guardar os valores para compensação futura, atualizados com juros de 1% mais taxa SELIC.   
   
**Atenção I:**  
É habilitado quando em Encargos Sociais (Parametrizador) o parâmetro 'Utiliza Controle de Compensação na Guia de INSS' esta marcado.  
   
**Atenção II:**  
Quando o parâmetro 'Movimento por Tomador' está marcado, o parâmetro 'Controle de Compensação' não fica habilitado, sendo considerado o código de recolhimento conforme tipo de tomador, ou seja, 150 para Cessão Mão de Obra e 155 para Construção Civil.  
   
Para o recolhimento 150, os valores não compensados são armazenados conforme a seção centralizadora da geração do INSS (matriz e filial), devido à guia de INSS ser gerada por estabelecimento (matriz/filial).  
Para o recolhimento 155, os valores não compensados são armazenados por tomador, devido à guia ser gerada por tomador.  
   
**Atenção III**  
A atualização dos valores é realizada apenas para guias de INSS geradas na competência atual ou na competência anterior.   
Veja mais detalhes sobre Compensação em: Compensação  
   
   
**Utiliza Percentual Redutor (Lei 12.546/2011)**  
Tem o objetivo em atender as normas complementares referente à contribuição previdenciária sobre a receita bruta que prevê a desoneração da folha de pagamento das empresas enquadradas na Lei 12.546/2011.   
   
Antes do cálculo da guia de INSS, é necessário o cadastramento dos valores de Desoneração em Encargos |Guia de INSS | Parâmetros da Guia de INSS Desoneração.  
   
**Por Filial:** Busca os valores cadastrados em Encargos | Guia de INSS | Parâmetros da Guia de INSS Desoneração de acordo com a quebra de CNPJ.  
**Por Empresa:** Busca os valores cadastrados em Encargos |Guia de INSS | Parâmetros da Guia de INSS Desoneração de acordo com a seção informada na guia. Sendo que o percentual definido na Empresa informada, é utilizado para as demais Empresas.  
   
Veja mais detalhes sobre Desoneração em: Desoneração  
   
   
**Tela Opções para Geração**  
   
**Usa Nome da Coligada no Campo Razão Social**  
É considerada a descrição da coligada, ao invés de considerar a descrição da seção informada na quebra de seção.  
   
**Ordenar por seção**  
Para que na geração da guia de INSS a ordenação seja por seção.  
   
**Gerar Valores Detalhado por Funcionário**  
Quando desejar que na finalização do processo, na aba 'Seções' seja apresentada a relação de funcionários considerados na geração da guia de INSS.  
   
Com este parâmetro marcado, na conclusão do processo, é habilitado também o parâmetro 'Detalhar por funcionário' possibilitando a geração da guia de INSS em arquivo texto detalhado por funcionário.  
   
**Imprime Valor Negativo**  
Os valores dos totais por seção são impressos, mesmo sendo negativos.   
Caso o parâmetro esteja desmarcado, o valor relativo ao total por seção é visualizado zerado.  
   
Para empresas que o valor de Dedução, Retenção e Compensação/Reembolso é maior que o valor a pagar da guia é emitido uma mensagem e a guia é gerada com o valor de Terceiros, devido o pagamento de Terceiros ser obrigatório.  
   
Para empresa que não recolhe o valor de Terceiros (filantropia) é emitida a guia com valor negativo quando o valor de deduções é maior que o valor a pagar.  
   
**Atenção:**  
É habilitado quando nos Encargos Sociais (Parametrizador) o parâmetro 'Utiliza Controle de Compensação na Guia de INSS' está desmarcado.  
Quando o parâmetro está marcado os valores não compensados na guia de INSS são guardados na tabela PGPS para compensação na próxima guia. Podendo consultar estes valores em Encargos |Guia de INSS | Consulta Saldo de Compensações.   
Veja mais detalhes sobre Compensação em: Compensação  
   
   
**Código do Relatório**  
São listados todos os relatórios existentes no RM Reports com o tipo de relatório igual 184-Guia da Previdência Social.  
   
**GPS Eletrônica**  
Para atender a Portaria nº 375 do MPAS (Ministério da Previdência e Assistência Social), a guia de INSS é gerada em arquivo, conforme layout do banco em que a empresa firmou convênio para o recolhimento das contribuições previdenciárias em meio eletrônico e por débito em conta.   
   
**Atenção:**  
São listados todos os relatórios existentes no Gerador de Saída que tem a Categoria igual a GPS.  
Atualmente a categoria é criada pelo usuário, e é imprescindível que seja criada com a descrição GPS.  
   
   
**Tela Integrações**  
O processo de integração do TOTVS Folha de Pagamento com o TOTVS Gestão de Estoque, Compras e Faturamento consiste em fazer com que no cálculo da Guia de INSS (GPS), através do TOTVS Folha de Pagamento, possam ser reconhecidos os valores de retenção de INSS efetuados em notas fiscais de tomadores de serviço. Este processamento só é acatado para pessoas jurídicas, para pessoas físicas a integração com o TOTVS Folha de Pagamento se dá através do TOTVS Gestão Financeira.  
**Importa Autônomos TOTVS Gestão Financeira / TOTVS Gestão de Estoque, Compras e Faturamento**  
Os valores são informados de acordo com a data de vencimento do lançamento e o mês de competência do TOTVS Folha de Pagamento.   
Para que seja considerada a data de emissão do lançamento para cálculo da guia de INSS, é necessário marcar o parâmetro 'Considerar data de emissão em vez de data de vencimento' existente em Gestão Financeira (Parametrizador).   
   
**Observação I:**  
Caso a guia de INSS seja gerada com tomador de serviço, a data de emissão ou a data de vencimento considerada para autônomos do TOTVS Gestão Financeira é a mesma da competência da distribuição por tomador.  
   
**Observação II:**  
Somente fica disponível quando o código de quebra da seção é igual ao código de quebra de CNPJ, cadastrado em Máscaras e Quebra (Parametrizador).  
   
**Observação III:**  
Não é necessário existir funcionário do TOTVS Folha de Pagamento alocado na seção ou tomador para que os autônomos do TOTVS Gestão Financeira sejam considerados.  
**Observação IV:**  
São considerados os autônomos que tem os campos 'Tipo de Tomador' e 'Código de Pagamento GPS' preenchidos em Administração de Pessoal | Cliente e Fornecedor | Aba Dados Fiscais.  
   
**Importa Valores de Retenção do TOTVS Gestão de Estoque, Compras e Faturamento**  
Considera o desconto da(s) retenção(ões) do(s) tomador(es) de serviço(s) existente(s) no TOTVS Gestão de Estoque, Compras e Faturamento.  
   
**Observação I:**  
Fica disponível quando o parâmetro 'Movimento por tomador' está marcado e o código de quebra da seção é igual ao código de quebra de CNPJ, cadastrado em Máscaras e Quebra (Parametrizador).  
   
**Observação II:**  
Quando o valor de retenção é maior que o valor da guia de INSS, é apresentada uma mensagem.  
   
**Observação III:**  
A empresa cedente de mão de obra ou empreiteira de mão de obra pode efetuar a compensação do valor consignado como retenção na nota fiscal, fatura ou recibo, com a contribuição a ser recolhida (campo 6 da GPS), não podendo absorver contribuições destinadas a Terceiros (campo 9 da GPS), as quais devem ser recolhidas integralmente, não se aplicando a este caso as disposições do art. 89 da Lei no 8.212/1991.  
   
**Observação IV:**  
O mês da data de emissão do movimento no TOTVS Gestão de Estoque, Compras e Faturamento (nota fiscal) deve ser compatível com a competência do TOTVS Folha de Pagamento.  
   
**Observação V:**  
O tipo do movimento gerado no TOTVS Gestão de Estoque, Compras e Faturamento deve ser do tipo a receber.  
**Observação VI:**  
O valor considerado no campo 'Retenções' da guia de INSS é o valor informado ou calculado no campo 'Valor' da aba Tributos, do movimento gerado no TOTVS Gestão de Estoque, Compras e Faturamento.   
   
**Observação VII:**  
Deve existir funcionário do TOTVS Folha de Pagamento alocado no tomador que tem lançamento no TOTVS Gestão de Estoque, Compras e Faturamento e devem ser considerados no cálculo da guia.  
   
**Observação VIII:**  
A filial informada no lançamento do TOTVS Gestão de Estoque, Compras e Faturamento deve ser a mesma utilizada no TOTVS Folha de Pagamento, podendo existir inclusive mais de um lançamento no TOTVS Gestão de Estoque, Compras e Faturamento, do mesmo tomador, para filiais diferentes, porém a filial deve estar sendo utilizada em um dos funcionários do TOTVS Folha de Pagamento.   
Caso o lançamento do TOTVS Gestão de Estoque, Compras e Faturamento tenha sido gerado para a filial 2 e no TOTVS Folha de Pagamento existir funcionário com distribuição para o mesmo tomador, porém em filial diferente, este lançamento do TOTVS Gestão de Estoque, Compras e Faturamento não é considerado.  
   
   
**Importa Arquivos de Autônomos**  
Importar autônomos de outro sistema, para serem considerados no cálculo da guia de INSS.  
Na importação são atualizados os campos 'Autônomos não cad.', 'INSS Aut. (M.P 83)' e 'Terceiros', e o campo 'Empresa' é calculado conforme percentual informado no campo 'Perc. Autônomos'.  
   
**Observação I:**  
O arquivo somente é importado, quando existe funcionário do TOTVS Folha de Pagamento na mesma filial do arquivo.  
   
   
**Arquivo**  
Preencher com a localização e nome do arquivo de autônomos a ser importado.  
   
**Layout do arquivo de importação**

|  |  |  |  |
| --- | --- | --- | --- |
| **Ordem** | **Descrição** | **Formato** | **Obrigatório** |
| 1 | Código da Coligada | Alfa Numérico | Sim |
| 2 | Código da Filial | Alfa Numérico | Sim |
| 3 | Sequencial | Inteiro | Sim |
| 4 | Nome do Autônomo | Alfa Numérico | Sim |
| 5 | Valor da Base de INSS | Valor | Sim |
| 6 | INSS descontado | Valor | Sim |
| 7 | Total Terceiros | Valor | Sim |
| 8 | Código da Coligada do Fornecedor/Tomador | Alfa Numérico | Não |
| 9 | Código do Fornecedor/Tomador | Alfa Numérico | Não |

   
**Observação I:**  
Quando o campo 8- Código da Coligada do Fornecedor/Tomador é preenchido, o campo 9- Código do Fornecedor/Tomador é obrigatório.  
   
**Observação II:**  
No formato 'Valor' são consideradas duas casas decimais e a separação é por ponto (.).  
   
**Observação III:**

Os campos do arquivo devem ser separados por ponto e vírgula  e não deve existir ponto e vírgula  ao final da linha a não ser que o último campo esteja vazio.

   
**Observação IV:**  
O arquivo de importação de autônomos precisa ter 9 colunas, independente se há valor nessas colunas ou não.  
   
   
**Tela Geração da Guia de INSS**  
Selecione as coligadas para a geração da guia de INSS - GPS.  
   
<span style="color: #333333"><strong>Usar Parâmetros Específicos</strong></span> Esta parametrização tem prioridade sobre a anterior, podendo ser especificada por coligada.  
<span style="color: #333333">Para a coligada que não tem o parâmetro marcado, são considerados os parâmetros preenchidos anteriormente.</span>  
   
**Retificação**  
Quando há pagamento de complemento de INSS retificando um valor pago a menor em meses anteriores, inclusive referente ao 13º salário.  
   
**Competência de Origem**  
Informe o Mês, Ano e Período em que os eventos criados para retificação foram lançados.  
   
**Eventos para Retificação**  
**Folha**  
Selecione o(s) evento(s) que deve(m) ser informado(s) na guia de INSS para recolhimento da retificação.  
São visualizados os eventos com os códigos de cálculos:  
188 - INSS Retificação SEFIP  
189 - Retificação SEFIP  
   
**Atenção:**  
Deve criar um evento para cada competência em que se refere à retificação.  
   
**13º Salário**  
Selecione o(s) evento(s) que deve(m) ser informado(s) na guia de INSS para recolhimento da retificação.  
São visualizados os eventos com os códigos de cálculos:  
190 - Retificação SEFIP - 13º Salário  
191 - INSS Retificação SEFIP - 13º Salário  
   
**Atenção:**  
Deve criar um evento para cada competência em que se refere à retificação.  
   
**Observação:**  
Quando houver valor de salário maternidade a retificar, deve incluir este valor manualmente, após o cálculo da guia, na aba 'Valores da Seção'.  
   
**GUIA de INSS / Lançamento Financeiro**   
   
**-Gerar Lançamentos Financeiros**  
Selecionar o tipo de lançamento financeiro da guia de INSS, já parametrizado em Encargos | Financeiro | Cadastros Financeiros | Parâmetros.  
São visualizados os lançamentos com o tipo:   
4 - INSS a pagar  
11 - INSS 13º a pagar  
   
   
**-Gerar Lanctos por centro de custo**  
Este parâmetro somente ficará visível se no parametrizador Folha normal/Calculo/"Utiliza Calculo Por Centro de Custo"  estiver MARCADO.  
   Através deste parâmetro, caso o TOTVS Folha de Pagamento esteja integrado com o TOTVS Gestão Financeira ou com BackOffice Protheus, será feito o rateio do lançamento financeiro por centro de custo ,buscando o do rateio fixo do cadastro do  funcionário. Caso contrário o rateio será feito por centro de custo buscando o rateio do Fornecedor informado na parametrização do Lançamento.  
   
   
**-Gerar lanctos rateados pelo Centro de custo da seção do funcionário**   
 Este parâmetro somente ficará visível se no parametrizador Folha normal/Calculo/"Utiliza Calculo Por Centro de Custo"  estiver DESMARCADO.  
 Através deste parâmetro será feito o rateio do lançamento financeiro por centro de custo ,buscando ao invés do rateio fixo do funcionário o centro de custo cadastrado na seção do funcionário aba Dados Contábeis.  
   
**Observação 1 :**  
Quando a seção do funcionário não tiver cadastrado o centro de custo o sistema emitira uma mensagem informando que a seção está sem Centro de custo   
          **Exemplo:** Os lançamentos financeiros não foram gerados devido o seguintes motivos :  
             A seção COM\_DEP Comercial não possui centro de custo cadastrado .   
   
**Tabelas Opcionais**  
Estas tabelas são visualizadas quando habilitadas no TOTVS Gestão Financeira.  
   
**Usa Parametrização**  
Opção em selecionar o Código/Descrição de cada item das Tabelas Opcionais no momento da geração da guia ou utilizar as definições parametrizadas no lançamento selecionado.  
   
   
**Eventos não Considerados**  
   
Com o inicio do *eSocial* esta aba não será mais utilizada para desconsiderar eventos no calculo GPS.   
Agora, para desconsiderar o evento da base de INSS(parte empresa, terceiros e acidente de trabalho ), deverá marcar o parâmetro "Incidência exclusiva do segurado "no cadastro de evento, pasta incidências.  
   
**Tela Valores**  
   
**Seções**  
**Seção Funcionários**  
São listados todos os funcionários considerados na guia de INSS, inclusive os autônomos.  
   
**Seção Autônomos**  
São listados todos os autônomos importados do TOTVS Gestão Financeira ou de outros sistemas.   
   
**Gerar Guia de INSS**  
A guia de INSS é emitida, conforme relatório informado na **Tela Opções para Geração**, e  
gerada em arquivo conforme parametrização.  
   
**Observação:**  
Quando o valor da Retenção e/ou Dedução e/ou Compensação é maior que o valor a pagar, é emitida uma mensagem de alerta e a guia é processada apenas com o valor de Terceiros, devido ser obrigatório o recolhimento deste valor, e para empresa que não recolhe o valor de Terceiros (filantropia), a guia é emitida com o valor negativo, caso o parâmetro 'Imprime Valores Negativos' esteja marcado.  
Quando nos Encargos Sociais (Parametrizador) o parâmetro 'Utiliza Controle de Compensação na Guia de INSS' está marcado, os valores não compensados na guia de INSS são guardados na tabela PGPS para compensação na próxima guia, para isso é necessário executar [Atualizar Saldo de Comp. E Ret.]. Podendo consultar estes valores em Encargos | Guia de INSS | Consulta Saldo de Compensações.   
Veja mais detalhes sobre Compensação em: [<span style="color: #0000ee"><span style="text-decoration: underline; ">Compensação</span></span>](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719300 "GPS - Compensação")  
   
   
**Gerar Arquivo Texto**  
Na geração da guia de INSS é criado o arquivo GRPS.TXT no caminho informado.  
Este arquivo contem as mesmas informações apresentadas em **Tela Valores das Seção**, conforme a quebra informada na seção, sendo a primeira quebra sempre é a coligada.  
   
**Detalhar por Funcionário**  
O arquivo GRPS.TXT passa a ser detalhado por funcionário, dentro da quebra informada na seção, sendo a primeira quebra sempre é a coligada.  
   
**Atenção:**  
É habilitado quando os parâmetros: 'Gerar Arquivo Texto' e 'Gera valores detalhado por funcionário' (**Tela Opções para Geração)** estão marcados.  
   
   
**Gerar Log de Cálculo**  
Na geração da guia de INSS é gerado o arquivo LOG\_GRPS.txt no caminho informado.  
   
**Observação:**  
Na geração da guia do INSS quando o movimento for por tomador e estiver marcado a opção construção Civil, será apresentado no log da guia os campos CEI e CNPJ, para identificação dos registros de cada tomador.  
   
   
**Atualizar Saldo de Comp. e Ret.**  
Guarda os valores de compensação a serem descontados automaticamente na próxima guia de INSS.  
Sempre que executado, os valores são armazenados na tabela PGPS, podendo consultar e alterar estes valores em Encargos | Guia de INSS | Consulta Saldo de Compensações.  
   
**Atenção I:**  
É habilitado quando nos parâmetros Encargos Sociais (Parametrizador) o parâmetro 'Utiliza Controle de Compensação na Guia de INSS' está marcado.  
Veja mais detalhes sobre Compensação em: [<span style="color: #0000ee"><span style="text-decoration: underline; ">Compensação</span></span>](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719300 "GPS - Compensação")  
   
**Atenção II:**  
Sempre que executar esta opção, os valores armazenados anteriormente referente à competência da geração da guia de INSS são deletados e os novos valores são armazenados.  
   
**Atenção III:**  
São armazenados os valores a serem compensados somente quando a competência da geração da guia de INSS é igual ou anterior à competência do folha.  
   
   
**Valores da Seção**  
   
**Quantidade**  
É o total de funcionários considerados para o cálculo da guia de INSS. Essa quantidade pode ser diferente da quantidade total de funcionários processados exibidos no log, pois alguns funcionários podem não ser considerados para o cálculo da Guia por motivos diversos.  
   
**Base de INSS**  
É soma da base de INSS de todos os funcionários, sendo que, quando a base de INSS do funcionário é negativa, é considerado zero para este funcionário.

**Observação:** 

Nesta Base de INSS também é considerado o evento com incidência exclusiva do empregador marcado no cadastro de eventos.

**Autônomos**  
São apresentados os valores encontrados no envelope de pagamento referente aos códigos de cálculos 46-HONORARIOS, independente se o evento incide ou não INSS.  
   
Com a Medida Provisória Nº 83 de 12/12/2002 e a conversão desta, na Lei nº 10.666 de 08 de maio de 2003 fica extinta a partir de 01 de abril de 2003, a escala transitória de salários-base, utilizada para fins de enquadramento e fixação do salário de contribuição dos contribuintes individual e facultativo filiados ao Regime Geral de Previdência Social, estabelecida pela Lei nº 9.876, de novembro de 1999. Para o contribuinte individual (autônomo ou empresário) que prestar serviço a uma ou mais empresas terá, descontado de sua remuneração, o valor referente a 11%, o qual empresa ficará responsável pelo recolhimento, juntamente com as contribuições a seu cargo, até o dia dois do mês seguinte ao da competência.  
As empresas (inclusive empregador rural pessoa jurídica, microempresas e empresas optantes pelo SIMPLES) e cooperativas são obrigadas a arrecadar a contribuição previdenciária do Contribuinte Individual a seu serviço, mediante desconto da remuneração paga, devida ou creditada a este segurado. A contribuição, em razão da dedução prevista, corresponde a 11% (onze por cento) do total da remuneração paga, devida ou creditada, a qualquer título, no decorrer do mês, ao segurado contribuinte individual, observando o limite máximo do salário de contribuição.  
Dados extraídos do site da previdência: [<span style="color: #0000ee"><a href="http://www.previdencia.gov.br/conteudoDinamico.php?id=450" class="external-link" rel="nofollow">http://www.previdencia.gov.br/conteudoDinamico.php?id=450+</a></span>](http://www.previdencia.gov.br/conteudoDinamico.php?id=450)  
   
**Autônomos não Cad.**  
Armazena a base de INSS do autônomo importado por outro sistema ou pelo TOTVS Gestão Financeira ou digitado pelo usuário.  
   
**INSS Aut. (M.P 83)**  
Destinado à informação do INSS descontado do autônomo não cadastrado no sistema, ou seja, importado por outro sistema ou pelo TOTVS Gestão Financeira ou digitado pelo usuário.  
   
**Terceiros**  
É o percentual informado na seção da quebra aplicado sobre o campo Base de INSS.  
Soma-se também o valor importado.  
   
**Acidente Trabalho**  
É o percentual informado no campo 'Percentual Acidente Trabalho' da seção conforme quebra informada, aplicado sobre o campo Base de INSS, considerando:  
   
**Aposentadoria Especial:** verifica o campo 'Código da Ocorrência' em Administração de Pessoal | Funcionários | aba FGTS / SEFIP e os percentuais de acréscimo informados Administração de Pessoal | Seções | aba Dados p/ INSS   
   
**FAP:** verifica o valor fixo FAP vigente e multiplica pelo 'Percentual Acidente Trabalho'.  
   
**Exemplo:**   
Valor Fixo FAP = 0,98%  
Percentual Acidente Trabalho = 2%  
Acréscimo Aposentadoria Especial 15 anos = 12%  
Funcionário com aposentadoria especial de 15 anos e remuneração de R$1.000,00.  
Funcionário sem aposentadoria especial e remuneração de R$600,00.  
   
O cálculo para encontrar o percentual do Acidente Trabalho e aplicar sobre a remuneração de R$1.000,00 é: (2 (Acidente Trabalho) \* 0,98 (FAP)) + 12 (acréscimo) = 13,96%  
   
O cálculo para encontrar o percentual do Acidente Trabalho e aplicar sobre a remuneração de R$600,00 é: (2 (Acidente Trabalho) \* 0,98 (FAP)) = 1,96%  
   
O valor do Acidente de Trabalho é: (1.000,00 \* 13,96%) + (600,00 \* 1,96%) = R$151,36  
   
Veja mais detalhes sobre o FAP em: [<span style="color: #0000ee"><span style="text-decoration: underline; ">FAP</span></span>]  
   
   
**Segurados**  
É o valor das contribuições de INSS descontadas dos funcionários.  
   
**Empresa**  
É a soma dos percentuais informados nos parâmetros: 'Perc. Empresa', 'Perc. Autônomos' e 'Perc. Cooperativa' aplicado sobre a soma dos campos: 'Base de INSS', 'Autônomos', 'Autônomos não Cad.' e 'Valor Cooperativas'.  
   
**Compensações/Reembolsos**  
Compensação é a previsão legal que permite aos contribuintes deduzirem em Guia da Previdência Social, valores pagos ou recolhidos indevidamente.  
   
Após a geração da guia, havendo compensação/reembolso, deve informar neste campo a importância a ser compensada.  
   
É considerado automaticamente os valores cadastros em Encargos | Parâmetros INSS/FGTS | aba Valores I | Campo Compensação.  
   
A compensação pode ser efetuada em tantos recolhimentos de competências subsequentes quantos forem necessários.  
Quando utilizar o controle de compensação, este campo é atualizado automaticamente pelo sistema, conforme preenchimento da tabela PGPS visualizada em Encargos | Guia de INSS | Consulta Saldo de Compensações.  
   
**Observação:**   
É emitida uma mensagem de alerta informando que o valor da compensação está acima do limite legal determinado.  
   
**Atenção:**  
O limite de 30% para compensação foi extinto pela Medida Provisória 449/2008, que revogou o §3º do artigo 89 da Lei 8.212/91.   
[<span style="color: #800080"><a href="http://www.coad.com.br/home/noticias-detalhe/19724/compensacao-contribuicao-previdenciaria-nao-tem-limite-de-30" class="external-link" rel="nofollow">http://www.coad.com.br/home/noticias-detalhe/19724/compensacao-contribuicao-previdenciaria-nao-tem-limite-de-30+</a></span>](http://www.coad.com.br/home/noticias-detalhe/19724/compensacao-contribuicao-previdenciaria-nao-tem-limite-de-30)  
   
   
   
**Multa / Juros**  
É o resultado da aplicação dos percentuais informados nos campos do parâmetro 'Recolhimento em Atraso' sobre o campo Líquido.  
   
   
**Sal. Matern. não Deduz**  
Atualmente este campo não é mais utilizado pelo sistema.  
   
Quando este campo foi criado, era para atender a legislação trabalhista relativa ao salário maternidade que previa um valor máximo de desconto na GRPS (Guia de Recolhimento da Previdência Social).  
Este valor era cadastrado em Administração de Pessoal | Cálculos | Valores Fixos com a finalidade 'Limite para desconto de Salário Maternidade em GRP'. O valor deste campo era a diferença entre o total do salário maternidade pago para a funcionária e o limite de desconto para o salário maternidade.  
   
   
**Deduções**  
Alguns benefícios são pagos pela empresa e posteriormente deduzidos em guia de recolhimento quando do pagamento de suas contribuições sociais. Sendo os benefícios: Salário Família e Salário Maternidade.  
   
Salário Família  
Benefício previdenciário pago diretamente pela empresa, aos segurados empregados que possuam filhos ou a eles equiparados de 0 a 14 anos ou inválidos.  
São considerados os eventos do tipo proventos e com os códigos de cálculos:   
5-Salário Família  
55-Salário Família Retroativo  
65-Dif. Salário Família  
149-Salário Família nas Férias  
   
   
Salário Maternidade  
O pagamento é feito pela empresa e posteriormente deduzido em GPS quando da quitação das contribuições previdenciárias.  
São considerados os eventos do tipo provento e com os códigos de cálculos:   
17- Salário Maternidade  
178- Salário Maternidade Retroativo  
   
Salário Maternidade sobre o 13º Salário  
Conforme legislação atual, o valor de Licença Maternidade é pago pela empresa, artigo 2º da Lei 10.710 de 05/08/2003.  
   
No mês de rescisão ou rescisão complementar, a funcionária que durante o ano corrente teve dias de afastamento por licença maternidade, o valor do 13º Salário pago que contemplam o período de afastamento, é deduzido na guia de INSS. Sendo assim, no momento do cálculo da rescisão ou rescisão complementar, é lançado automaticamente o evento com código cálculo 324-13º Salário Rescisão Licença Maternidade ou 325- Diferença 13º Salário Rescisão Licença Maternidade.  
Estes eventos são do tipo base de cálculo.  
   
Para informar a dedução quanto ao pagamento da 2ª Parcela de 13º Salário, no momento do lançamento do 13º salário, é lançando também o evento com código de cálculo 322-2ª Parcela 13º Salário Licença Maternidade, ou na diferença de 13º salário é lançado o evento com código de cálculo 323-Diferença de 13º Salário Licença Maternidade, estes eventos são considerados automaticamente no momento da geração da guia de INSS de 13º salário.  
   
   
**Exemplo:**  
A funcionária esteve afastada por licença maternidade até o dia 20/01/2013, sendo que, em 01/03/2013 foi demitida.   
A empresa é responsável pelo pagamento de 13º salário, referente aos dias de afastamento. Sendo o cálculo:  
(Salário+médias+adicionais) / 12 avos / 30 \* número de dias de afastamento no ano corrente  
   
Para que este valor seja demonstrado na Folha Analítica, é necessário criar a fórmula com a soma destes eventos e informá-la na Folha Analítica. O valor desta fórmula é impresso junto com as bases.  
   
**Valores Cooperativas**  
As cooperativas de trabalho estão sujeitas à retenção em decorrência de contrato de prestação de serviços com pessoas jurídicas. Lei nº 9.876/99  
A empresa contratante deve a seu cargo, contribuir com 15% sobre o valor bruto da nota fiscal, fatura ou recibo emitida pela cooperativa, relativamente aos serviços prestados por cooperados.  
   
Sobre o valor informado neste campo é lançado o percentual informado no campo 'Perc. Cooperativa' na **Tela Parâmetros** e o valor encontrado é lançado no campo 'Empresa'.  
   
**Atenção:**  
É considerado automaticamente os valores cadastros em Encargos | Parâmetros INSS/FGTS | aba Valores II | Campo Valor - Cooperativas.  
   
   
**Valores Anteriores**  
Valores de contribuições (acidente trabalho, segurados ou empresa) de meses onde não foi possível o recolhimento.  
Os valores informados não são guardados automaticamente, é utilizado apenas na informação do mês em que for inserido (campo 6 da GPS), e o valor não altera o 'Líquido', apenas o 'Total'.  
   
Havendo valores informados em Encargos | Parâmetros INSS/FGTS | aba Valores I | Campo Valor INSS Folha Pagto, estes valores são buscados automaticamente para este campo.  
   
   
**Retenções**  
Informar o valor descontado de Retenção para tomadores de serviços.   
Quando o parâmetro 'Importa Valores de Retenção do TOTVS Gestão de Estoque, Compras e Faturamento' em **Tela Integrações** está marcado, este campo é preenchido automaticamente.   
Havendo valores informados em Encargos | Parâmetros INSS/FGTS | aba Parâmetros Tomadores de Serviço | Campo Valor da Renteção (Lei 9711/98), estes valores são utilizados automaticamente na geração da guia de INSS.  
   
**Observação I:**  
Quando o valor de retenção é maior que o valor da guia de INSS, é apresentada uma mensagem.  
   
**Observação II:**  
A empresa cedente de mão de obra ou empreiteira de mão de obra pode efetuar a compensação do valor consignado como retenção na nota fiscal, fatura ou recibo, com a contribuição a ser recolhida (campo 6 da GPS), não podendo absorver contribuições destinadas a Terceiros (campo 9 da GPS), as quais devem ser recolhidas integralmente, não se aplicando a este caso as disposições do art. 89 da Lei no 8.212/1991.  
   
**Observação III:**  
O mês da data de emissão do movimento no TOTVS Gestão de Estoque, Compras e Faturamento (nota fiscal) deve ser compatível com a competência do TOTVS Folha de Pagamento.  
   
**Observação IV:**  
O tipo do movimento gerado no TOTVS Gestão de Estoque, Compras e Faturamento deve ser do tipo a receber.  
**Observação V:**  
O valor considerado no campo 'Retenções' da guia de INSS é o valor informado ou calculado no campo 'Valor' da aba Tributos, do movimento gerado no TOTVS Gestão de Estoque, Compras e Faturamento.   
   
**Observação VI:**  
Deve existir funcionário do TOTVS Folha de Pagamento alocado no tomador que tem lançamento no TOTVS Gestão de Estoque, Compras e Faturamento e devem ser considerados na geração da guia.  
   
**Observação VII:**  
A filial informada no lançamento do TOTVS Gestão de Estoque, Compras e Faturamento deve ser a mesma utilizada no TOTVS Folha de Pagamento, podendo existir inclusive mais de um lançamento no TOTVS Gestão de Estoque, Compras e Faturamento, do mesmo tomador, para filiais diferentes, porém a filial deve estar sendo utilizada em um dos funcionários do TOTVS Folha de Pagamento.   
Caso o lançamento do TOTVS Gestão de Estoque, Compras e Faturamento tenha sido gerado para a filial 2 e no TOTVS Folha de Pagamento existir funcionário com distribuição para o mesmo tomador, porém em filial diferente, este lançamento do TOTVS Gestão de Estoque, Compras e Faturamento não é considerado.  
   
**Observação VIII:**  
São verificados valores por filial.  
Quando o tomador default é 'Cessão de Mão de Obra', o valor da retenção na filial é o valor TOTAL da retenção cadastrada no TOTVS Gestão de Estoque, Compras e Faturamento para aquela Filial, mesmo quando o movimento estiver distribuído por tomador no TOTVS Folha de Pagamento.  
Quando o tomador default é 'Construção Civil', o valor da retenção no tomador é o valor TOTAL da retenção cadastrada no TOTVS Gestão de Estoque, Compras e Faturamento para aquele Tomador, caso não exista distribuição no TOTVS Folha de Pagamento para algum tomador do TOTVS Gestão de Estoque, Compras e Faturamento, este valor não é importado.

**Aposentadoria Especial**  
A partir da competência abril/99, há o acréscimo da alíquota de contribuição destinada ao financiamento da aposentadoria especial prevista nos artigos 57 e 58 da Lei n° 8.213/91, concedida em razão de maior incidência de incapacidade laborativa decorrente de riscos ambientais do trabalho, conforme a atividade exercida pelo segurado a serviço da empresa permita a concessão de aposentadoria especial após 15, 20 ou 25 anos de contribuição, conforme a tabela progressiva abaixo:  
 

|  |  |  |  |
| --- | --- | --- | --- |
| **APOSENTADORIA ESPECIAL** | **01/04/1999 a 31/08/1999** | **De 01/09/1999 a 29/02/2000** | **A partir de 01/03/2000** |
| 15 anos | 4% | 8% | 12% |
| 20 anos | 3% | 6% | 9% |
| 25 anos | 2% | 4% | 6% |

Os percentuais incidem exclusivamente sobre o total das remunerações pagas ou creditadas, no decorrer do mês, aos segurados empregados e trabalhadores avulsos sujeitos a condições especiais (MP nº 1.729, de 02/12/98, DOU de 03/12/98 e Orientação Normativa nº 12, de 18/03/99, DOU de 23/03/99, do INSS).   
O acréscimo incide exclusivamente sobre o total das remunerações pagas ou creditadas, no decorrer do mês, aos segurados empregados e trabalhadores avulsos sujeitos a condições especiais.  
   
**Observação:**  
Quando existe funcionário com aposentadoria especial, o percentual acima é acrescido ao SAT da empresa.  
   
**Exemplo:**   
Competência = Março/2013  
Valor Fixo FAP = 0,98%  
Percentual Acidente Trabalho (SAT) = 2%  
Remuneração Segurados com Aposentadoria 20 anos = R$500,00  
Remuneração Segurados com Aposentadoria 15 anos = R$300,00  
Remuneração Segurados sem Aposentadoria Especial = R$200,00  
**Total remuneração                                      R$1.000,00**  
   
1.000,00 \* 1,96% (2% SAT \* 0,98% FAP) = R$19,60  
500,00 \* 9% (percentual de acréscimo 20 anos) = R$45,00  
300,00 \* 12% (percentual de acréscimo 15anos) = R$36,00  
Valor total R$100,60  
   
   
**Base INSS % 15 anos**  
É visualizado o total da remuneração dos funcionários com aposentadoria especial de 15 anos, conforme o preenchimento do campo 'Ocorrência' em Administração de Pessoal | Funcionários |FGTS/SEFIP, tipo:   
2-Exp. a ag. nocivo (apos. aos 15 anos de serviço) 1 vínculo  
6-Exp. a ag. nocivo (apos. aos 15 anos de serviço) + de 1 vínc.  
   
**Base INSS % 20 anos**  
É visualizado o total da remuneração dos funcionários com aposentadoria especial de 20 anos, conforme o preenchimento do campo 'Ocorrência' em Administração de Pessoal | Funcionários |FGTS/SEFIP, tipo:   
3- Exp. a ag. nocivo (apos. aos 20 anos de serviço) 1 vínculo  
7- Exp. a ag. nocivo (apos. aos 20 anos de serviço) + de 1 vínc.   
   
**Base INSS % 25 anos**  
É visualizado o total da remuneração dos funcionários com aposentadoria especial de 25 anos, conforme o preenchimento do campo 'Ocorrência' em Administração de Pessoal | Funcionários |FGTS/SEFIP, tipo:   
4- Exp. a ag. nocivo (apos. aos 25 anos de serviço) 1 vínculo  
8- Exp. a ag. nocivo (apos. aos 25 anos de serviço) + de 1 vínc.  
   
**Func. não Expostos**  
É visualizado o total da remuneração dos funcionários que não tem exposição a agente nocivo, ou seja, não tem aposentadoria especial, conforme o preenchimento do campo 'Ocorrência' em Administração de Pessoal | Funcionários |FGTS/SEFIP, tipo:  
0-Nunca exposto a agentes nocivos  
1-Não exposição a agente nocivo - 1 vínculo (já esteve exposto)  
5-Não exposição a agente nocivo + de 1 vínculo  
   
Os campos **'Informação 1 da GPS'** e **'Informação 2 da GPS'** não são utilizados na impressão da GPS.  
   
   
**Líquido**  
Fica negativo quando a retenção e/ou compensação é maior que os campos 'Acidente Trabalho', 'Empresa' e 'Segurados' e a empresa não recolhe Terceiros, e o parâmetro 'Imprime Valor Negativo' está marcado e nos Encargos Sociais (Parametrizador) o parâmetro 'Utiliza Controle de Compensação na Guia de INSS' está desmarcado.  
   
O valor deste campo tem o seguinte cálculo:  
(Terceiros + Acidente Trabalho + Segurados + Empresas + INSS Aut. (M.P 83) ) – (Compensação/Reembolso + Deduções)  
   
   
**Total**  
É o valor total impresso na GPS.  
O valor deste campo tem o seguinte cálculo: campo Líquido + Valores Anteriores + Juros + Multa  
   
   
**Recalcular Valores**  
Tem o objetivo em, após qualquer alteração de valores realizados na tela, recalcular os campos correspondentes à alteração.  
**Exemplo:**  
É digitado na tela o valor de R$100,00 no campo 'Valores Cooperativas', ao clicar em Recalcular Valores, o campo 'Empresa' tem seu valor alterado somando o percentual calculado sobre os R$100,00.  
   
   
**Campo 6 da GPS**   
São os campos: (Acidente Trabalho + Segurados + Empresas + INSS Aut. + Valores Anteriores) - (Compensação/Reembolso + Deduções)  
 

|  |  |
| --- | --- |
|  | Informações Complementares |

Compensação  
FAP  
Desoneração
