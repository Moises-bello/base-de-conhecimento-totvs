---
article_id: 8208338101655
category: Encargos
content_hash: 614fd7b87466172560fc061f51fe2660dcde31a910fbec81978b2239b5b761d1
fetched_at: '2026-06-28T22:46:52.477024+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração da Guia de INSS
type: support-article
updated_at: '2024-06-20T20:46:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8208338101655-RH-RM-FOP-Gera%C3%A7%C3%A3o-da-Guia-de-INSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16341995180439) Tempo aproximado para leitura: **00:13:55 min****Dúvida**Como gerar a GPS no RM?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Através do processo abaixo é possível gerar/imprimir a Guia da Previdência Social (GPS) para o recolhimento das contribuições sociais pagas pela empresa.  
A geração da GPS ocorre na aba **Encargos |  Guia de INSS**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769386844567)  
  
**Tela Parâmetros  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769426852119)**

**Quebra de Seção**  
A emissão do identificador na GPS é de acordo com a parametrização da seção da quebra informada, sendo:

* CNPJ ou CPF, quando na seção o parâmetro **Identificação pelo CNPJ** está marcado, independente de existir CEI na seção;
* CEI quando os parâmetros **Pessoa Física** ou **Identificação pelo CNPJ** não estão marcados e existe CEI informado na seção;
* CEI quando o parâmetro **Pessoa Física** está marcado e existe CEI informado;
* Em Branco quando os parâmetros **Pessoa Física** ou **Identificação pelo CNPJ** não estão marcados e não existe parametrização para CEI ou então não existe CEI informado.

**Competência**  
Os valores utilizados para o cálculo são extraídos do envelope do funcionário (PFFINANC), verificando sempre a incidência atual dos eventos, independente se a competência é retroativa.  
   
**Código de Pagamento**  
Informe o código da GPS para geração da guia.  
   
**Importante**  
Não preenchendo o campo, é considerado automaticamente o campo código GPS existente em **Administração de Pessoal | Seções | aba Dados p/ INSS**.  
   
**Percentuais para cálculo**  
**Perc. Empresa**  
Informe o percentual de recolhimento de INSS por parte da empresa, desconsiderando os demais percentuais como: Acidente de Trabalho, FAP, Terceiros.  
Para o cálculo de Terceiros é utilizado o percentual informado na seção conforme a quebra.  
Para o cálculo do Acidente de trabalho é utilizado o percentual informado na seção conforme a quebra, multiplicado pelo FAP cadastrado nos Valores Fixos.  
   
**Perc. Autônomos**  
Informe o percentual de recolhimento de INSS a ser calculado sobre os eventos com código de cálculo 046-Honorários.  
   
**Perc. Cooperativa**  
Informe o percentual de recolhimento a ser aplicado no campo **Valor Cooperativas** na aba **Valores da Seção**.  
   
**Movimento por Tomador**  
Com o parâmetro marcado a GPS é gerada verificando a distribuição por tomador.  
Sendo necessário selecionar o tipo de prestação de serviço: **Cessão de Mão de Obras** ou **Construção Civil**, observando as parametrizações do Tomador de Serviço (Parametrizador).  
Quando é desmarcado o parâmetro **Movimento por Tomador**, é necessário marcar o parâmetro em **Parametrizador |** **Folha Normal | Encargos Sociais | Utiliza Controle de Compensação na Guia de INSS**, para habilitar as opções de **código de recolhimento para compensação** na geração da Guia de INSS.   
  
**Recolhimento em Atraso**  
São habilitados os campos **Multa (%)** e **Juros de Mora (%)**, sendo estes percentuais são aplicados sobre o campo **Líquido** dos **Valores da Seção**.  
  
**Controle de Compensação**  
Tem o objetivo em controlar os valores de compensação do mês (Retenção, Compensação e Dedução) que não são utilizados na geração da guia de INSS devido não existir saldo, e guardar os valores para compensação futura, atualizados com juros de 1% mais taxa SELIC.  
   
**Utiliza Percentual Redutor (Lei 12.546/2011)**  
Tem o objetivo em atender as normas complementares referente à contribuição previdenciária sobre a receita bruta que prevê a desoneração da folha de pagamento das empresas enquadradas na Lei 12.546/2011.  
Antes do cálculo da guia de INSS, é necessário o cadastramento dos valores de Desoneração em Encargos |Guia de INSS | Parâmetros da Guia de INSS Desoneração.  
   
**Por Filial:** Busca os valores cadastrados em Encargos | Guia de INSS | Parâmetros da Guia de INSS Desoneração de acordo com a quebra de CNPJ.  
**Por Empresa:** Busca os valores cadastrados em Encargos |Guia de INSS | Parâmetros da Guia de INSS Desoneração de acordo com a seção informada na guia. Sendo que o percentual definido na Empresa informada, é utilizado para as demais Empresas.  
   
**Tela Opções para Geração**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769428479511)  
   
**Usa Nome da Coligada no Campo Razão Social**  
É considerada a descrição da coligada, ao invés de considerar a descrição da seção informada na quebra de seção.  
   
**Ordenar por seção**  
Para que na geração da guia de INSS a ordenação seja por seção.  
   
**Gerar Valores Detalhado por Funcionário**  
Quando desejar que na finalização do processo, na aba **Seções** seja apresentada a relação de funcionários considerados na geração da guia de INSS.  
Com este parâmetro marcado, na conclusão do processo, é habilitado também o parâmetro **Detalhar por funcionário** possibilitando a geração da guia de INSS em arquivo texto detalhado por funcionário.  
   
**Imprime Valor Negativo**  
Os valores dos totais por seção são impressos, mesmo sendo negativos.  
Caso o parâmetro esteja desmarcado, o valor relativo ao total por seção é visualizado zerado.  
Para empresas que o valor de Dedução, Retenção e Compensação/Reembolso é maior que o valor a pagar da guia é emitido uma mensagem e a guia é gerada com o valor de Terceiros, devido o pagamento de Terceiros ser obrigatório.  
Para empresa que não recolhe o valor de Terceiros (filantropia) é emitida a guia com valor negativo quando o valor de deduções é maior que o valor a pagar.  
   
**Código do Relatório**  
São listados todos os relatórios existentes no RM Reports com o tipo de relatório igual 184-Guia da Previdência Social.  
   
**GPS Eletrônica**  
Para atender a Portaria nº 375 do MPAS (Ministério da Previdência e Assistência Social), a guia de INSS é gerada em arquivo, conforme layout do banco em que a empresa firmou convênio para o recolhimento das contribuições previdenciárias em meio eletrônico e por débito em conta.  
  
**Tela Integrações**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769471994903)  
  
O processo de integração do TOTVS Folha de Pagamento com o TOTVS Gestão de Estoque, Compras e Faturamento consiste em fazer com que no cálculo da Guia de INSS (GPS), através do TOTVS Folha de Pagamento, possam ser reconhecidos os valores de retenção de INSS efetuados em notas fiscais de tomadores de serviço. Este processamento só é acatado para pessoas jurídicas, para pessoas físicas a integração com o TOTVS Folha de Pagamento se dá através do TOTVS Gestão Financeira.  
**Importa Autônomos TOTVS Gestão Financeira / TOTVS Gestão de Estoque, Compras e Faturamento**  
Os valores são informados de acordo com a data de vencimento do lançamento e o mês de competência do TOTVS Folha de Pagamento.  
Para que seja considerada a data de emissão do lançamento para cálculo da guia de INSS, é necessário marcar o parâmetro **Considerar data de emissão em vez de data de vencimento** existente em Gestão Financeira (Parametrizador).   
  
**Importa Valores de Retenção do TOTVS Gestão de Estoque, Compras e Faturamento**  
Considera o desconto da(s) retenção(ões) do(s) tomador(es) de serviço(s) existente(s) no TOTVS Gestão de Estoque, Compras e Faturamento.  
   
**Importa Arquivos de Autônomos**  
Importar autônomos de outro sistema, para serem considerados no cálculo da guia de INSS.  
Na importação são atualizados os campos **Autônomos não cad.**, **INSS Aut. (M.P 83)** e **Terceiros**, e o campo **Empresa** é calculado conforme percentual informado no campo **Perc. Autônomos**.  
O arquivo somente é importado, quando existe funcionário do TOTVS Folha de Pagamento na mesma filial do arquivo.  
   
**Tela Geração da Guia de INSS**  
Selecione as coligadas para a geração da guia de INSS - GPS.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769474942871)   
**Retificação  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769528162199)**  
Quando há pagamento de complemento de INSS retificando um valor pago a menor em meses anteriores, inclusive referente ao 13º salário.  
   
**Competência de Origem**  
Informe o Mês, Ano e Período em que os eventos criados para retificação foram lançados.  
   
**Eventos para Retificação**  
**Folha**  
Selecione o(s) evento(s) que deve(m) ser informado(s) na guia de INSS para recolhimento da retificação.  
São visualizados os eventos com os códigos de cálculos:  
188 - INSS Retificação SEFIP  
189 - Retificação SEFIP  
   
Deve criar um evento para cada competência em que se refere à retificação.  
   
**13º Salário**  
Selecione o(s) evento(s) que deve(m) ser informado(s) na guia de INSS para recolhimento da retificação.  
São visualizados os eventos com os códigos de cálculos:  
190 - Retificação SEFIP - 13º Salário  
191 - INSS Retificação SEFIP - 13º Salário  
Deve criar um evento para cada competência em que se refere à retificação.  
   
**Importante**  
Quando houver valor de salário maternidade a retificar, deve incluir este valor manualmente, após o cálculo da guia, na aba **Valores da Seção**.  
   
**GUIA de INSS / Lançamento Financeiro**   
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769529533975) **Gerar Lançamentos Financeiros**  
Selecionar o tipo de lançamento financeiro da guia de INSS, já parametrizado em Encargos | Financeiro | Cadastros Financeiros | Parâmetros.  
São visualizados os lançamentos com o tipo:   
4 - INSS a pagar  
11 - INSS 13º a pagar  
   
**Gerar Lanctos por centro de custo**  
Este parâmetro somente ficará visível se no **Parametrizador | Folha normal | Calculo | Utiliza Calculo Por Centro de Custo**  estiver marcado.  
Através deste parâmetro, caso o TOTVS Folha de Pagamento esteja integrado com o TOTVS Gestão Financeira ou com BackOffice Protheus, será feito o rateio do lançamento financeiro por centro de custo, buscando o do rateio fixo do cadastro do  funcionário. Caso contrário o rateio será feito por centro de custo buscando o rateio do Fornecedor informado na parametrização do Lançamento.  
 **Gerar lanctos rateados pelo Centro de custo da seção do funcionário**   
 Este parâmetro somente ficará visível se no **Parametrizador | Folha normal | Calculo | Utiliza Calculo Por Centro de Custo** estiver desmarcado.  
 Através deste parâmetro será feito o rateio do lançamento financeiro por centro de custo ,buscando ao invés do rateio fixo do funcionário o centro de custo cadastrado na seção do funcionário aba Dados Contábeis.  
   
**Tabelas Opcionais**  
Estas tabelas são visualizadas quando habilitadas no TOTVS Gestão Financeira.  
   
**Usa Parametrização**  
Opção em selecionar o Código/Descrição de cada item das Tabelas Opcionais no momento da geração da guia ou utilizar as definições parametrizadas no lançamento selecionado.  
   
**Eventos não Considerados**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8769544675607)  
  
Com o inicio do *eSocial* esta aba não será mais utilizada para desconsiderar eventos no calculo GPS.   
Agora, para desconsiderar o evento da base de INSS(parte empresa, terceiros e acidente de trabalho ), deverá marcar o parâmetro **Incidência exclusiva do segurado** no cadastro de evento, pasta incidências.  
   
**Saiba mais**Veja as documentações completas sobre a geração da GPS abaixo:  
[GPS - Guia de INSS](https://tdn.totvs.com/display/public/LRM/GPS+-+Guia+de+INSS)  
[GPS - Compensação](https://tdn.totvs.com/pages/viewpage.action?pageId=452719300)  
[GPS - Desoneração](https://tdn.totvs.com/pages/releaseview.action?pageId=452719205)  
[COMO FAZER - Desoneração Guia de INSS](https://tdn.totvs.com/pages/releaseview.action?pageId=118883664)
