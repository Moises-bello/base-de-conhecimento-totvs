---
content_hash: 87919062b421d0ad83df19f53f0918d0db0766f6d9c5bf5d5efe5dba5b48dcbf
fetched_at: '2026-06-29T00:11:28.685797+00:00'
page_id: '733184530'
product: rm
source: tdn-rm
title: R-4010 – Pagamentos/créditos a beneficiário pessoa física
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=733184530
version: 117
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-4010

## **Conteúdo**

**Conteúdo**

## **01. Introdução**

Neste Evento serão informados os pagamentos e créditos que os contribuintes efetuarem sobre as contratações de serviço sem vínculo empregatício (pessoa física), para o recolhimento do IRRF. Já em relação às informações vinculadas ao IR sobre o trabalho serão entregues pelo eSocial.

## **02. Regras**

### Regras Específicas

* Necessário fazer o Cadastro do Parâmetros de Processos - **EFD REINF**. Para mais informações clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588#1-5)
* É necessário parametrizar o Tributo e a Natureza de Rendimento -  Parâmetros de Processos - **EFD REINF** -Anexo - Filtro de Eventos - Para mais informações clique [aqui](https://tdn.totvs.com/display/LRM/Filtro+de+Eventos)
* **Centralizado**: No cadastro dos [Parâmetros de Processos](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588), pode ser definido se a geração será Centralizada ou Descentralizada.  
  >> Quando estiver habilitado, todos os Lançamentos\Movimentações realizados a uma determinada Pessoa Física\Jurídica, serão gerados em um único arquivo XML a ser transmitido para a EFD-REINF.  
  >> Quando desabilitado, todos os Lançamentos\Movimentações realizados a uma determinada Pessoa Física\Jurídica, serão agrupados em um arquivo XML para cada Filial a ser transmitido para a EFD-REINF.

  Imagem

### Regras Gerais

## **03. Módulo de Origem dos dados**

OrigemOrigem Gestão FinanceiraOrigem Gestão FinanceiraOrigem Gestão FinanceiraOrigemFinleftRetenção PFRetenção PFRetenção PF

**Lançamentos e Rendimentos em que houve retenção do IRRF para Fornecedor Pessoa Física:**

* Lançamentos cujo Cli/For seja pessoa física;
* Lançamentos cujo Estado informado na aba Endereço do Cadastro do Cli/For seja nacional; (Para confirmar se o Estado é nacional acesse o cadastro do Estado vinculado ao Cli\For e verifique se o flag "Nacional" está marcado);
* Baixas e/ou Lançamentos que não tenham\estejam sido Canceladas;
* Lançamentos cujo Tipo de Documento seja “Gerador de IRRF” ou “Gerador de IRRF e INSS”;
* Não será gerado Lançamentos Financeiros “Gerador de IRRF” ou “Gerador de IRRF e INSS”, que no cadastro do cliente/Anexo e-Social - o Campo "Código da Categoria Social" esteja informado;
* Não será gerado Lançamentos Financeiro, com cliente\fornecedor que no Anexo e-Social o  Campo **"Código da Categoria e-Social",** esteja preenchido, mesmo que esteja com **Natureza de Rendimento** preenchida e documento **gerador de IRRF ou Gerador IRRF e INSS.**
* Para que a Rotina da **REINF** busque as informações do Aplicativo Gestão Financeira\RM Fluxus, o usuário deverá escolher esta opção na Tela de Parâmetros de Processo\REINF\Anexos\Filtro de Evento – Campo Origem: igual a Financeiro. Para mais informações clique [aqui](https://tdn.totvs.com/display/LRM/Filtro+de+Eventos)

  Fazendo isto, o aplicativo Gestão Fiscal\RM Liber irá buscar todos os Lançamentos Financeiros cujo Tipo de Documento Gera Imposto de Renda ou que possuem a classificação referente a Contribuições Sociais.
Sem Retenção PFSem Retenção PFSem Retenção PF

**Lançamentos de Rendimentos em que não houve a retenção do IRRF para Fornecedor Pessoa Física:**

* Lançamentos cujo Cli/For seja pessoa física;
* No Cadastro Natureza de Rendimento deverá ser configurado o campo "**Sem IR**";
* O Tipo de Documento utilizado no Lançamento/Movimento deverá ser “Gerador de IRRF” ou “Gerador de IRRF e INSS”;
* Ao incluir Movimento ou Lançamento Financeiro, utilizando uma Natureza de Rendimento com campo "**Sem IR**" configurado, ao gerar a EFD-Reinf apenas o valor bruto será gerado e os valores referentes a retenção não serão gerados mesmo que esteja preenchido no tributo.
Isentos\Outros PFIsentos\Outros PFIsentos\Outros PF

**Lançamentos de Rendimentos Isentos\Outros para Fornecedor Pessoa Física:**

* Lançamentos cujo Cli/For seja pessoa física;
* O Tipo de Documento utilizado no Lançamento/Movimento deverá ser “Gerador de IRRF” ou “Gerador de IRRF e INSS”;
* O grupo será gerado somente quando o campo "Indicador de isenção DIRF" estiver preenchido e seu conteúdo for diferente de "Não se aplica". Este campo pode ser encontrado ao selecionar um Lançamento Financeiro e acessar o menu Anexo| Dados Fiscais.
Origem Gestão FiscalOrigem Gestão FiscalOrigem Gestão Fiscal

**Lançamentos Fiscais**

* Lançamentos cujo Cli/For seja pessoa física;
* O Evento deve agrupar todos os lançamentos do período por cliente/fornecedor e Natureza de Rendimento.
* Lançamentos onde o campo Data Documento esteja dentro da Data informada na capa Evento R-9015 informado na tela de geração da Rotina.
* Lançamentos referentes a Notas Recebidas, ou seja Lançamentos de Entrada, cujo Cliente/Fornecedor seja pessoal física e possua retenção do Tributo. Obrigações Principais | Entrada
* O tributo destacado no Lançamento Fiscal deve conter: base, alíquota, valor e código Natureza de Rendimento preenchidos.
* Os Lançamentos de ajuste não são gerados neste registro.
* Ao incluir Movimento ou Lançamento Financeiro, utilizando uma Natureza de Rendimento com campo "**Sem IR**" configurado, ao gerar a EFD-Reinf apenas o valor bruto será gerado e os valores referentes a retenção não serão gerados mesmo que esteja preenchido no tributo.
Origem Gestão FiscalOrigem Gestão Fiscal - EXTERIOROrigem Gestão Fiscal

**Lançamentos Fiscais de Importação (Exterior)**

**Regras aplicadas para o Evento R-4010**

* Lançamentos cujo Cli/For seja pessoa física e País seja do Exterior;

  Imagem
* Informar a Forma de Tributação do cadastro do Cli\For

  Imagem
* Lançamentos onde o campo Data Documento esteja dentro da Data informada na capa Evento R-9015 informado na tela de geração da Rotina.
* Lançamentos referentes a Notas Recebidas, ou seja Lançamentos de Entrada, cujo Cliente/Fornecedor seja pessoal física e possua retenção do Tributo. Obrigações Principais | Entrada
* O tributo destacado no Lançamento Fiscal deve conter: base, alíquota, valor e código Natureza de Rendimento preenchidos.
* Os Lançamentos de ajuste não são gerados neste registro.

## **04. Exemplo**

xmlExemplo R-4010


{...}
{...}

{...}
]]>ideContri

Utiliza um grupo **ideEstab** especifico para este tipo

## **05. Mapeamento de Campos**

1ideEventoideEventoideContriideContriEstabelecimentoEstabelecimento

**Informações de Identificação do Estabelecimento**

| Registro\Campo | Registro Pai | Descrção | Origem dos Dados RM |
| --- | --- | --- | --- |
| ideEstab | evtRetPF | Informações de identificação do estabelecimento. |  |
| tpInscEstab | ideEstab | Preencher com o código correspondente ao tipo de inscrição:   1 - CNPJ; 2 - CPF; 3 - CAEPF. Valores válidos: 1, 2, 3. | Gerando conforme informação do Campo CNPJ da Filial Matriz   Verificar o tamanho do campo CPF (11 carac.) e CNPJ(14 carac.)  GFILIAL.CGC |
| nrInscEstab | ideEstab | Informar o número de inscrição do estabelecimento de acordo com o tipo de inscrição indicado no campo {tpInscEstab}. Validação: A inscrição informada deve ser compatível com o {tpInscEstab}.   Se {tpInscEstab} = [1] e {classTrib} <> [85], deve ser um número de CNPJ pertencente ao contribuinte declarante (mesma raiz de {ideContri/nrInsc}). Se {tpInscEstab} = [2], deve ser igual a {ideContri/nrInsc}. | Gerando conforme informação do Campo CNPJ da Filial correspondente aos lançamentos, agrupado por filial.  GFILIAL.CGC  [Mais Informações](https://tdn.totvs.com/pages/editpage.action?pageId=506387467) |

ideBenefideBenef

**Identificação do Beneficiário**

| Registro\Campo | Registro Pai | Descrição | Origem dados RM |
| --- | --- | --- | --- |
| ideBenef | ideEstab | Identificação do beneficiário |  |
| cpfBenef | ideBenef | Informar o número de inscrição no Cadastro da Pessoa Física - CPF do beneficiário do pagamento.  Validação: Informação obrigatória se houver ao menos um registro {idePgto} cujo campo {paisResidExt} não tenha sido informado.  Em arquivo gerado por declarante pessoa física, não pode ser igual ao CPF do declarante, exceto se {indFciScp} = [2]. Se informado, deve ser um número de inscrição no CPF válido. | Gerado com a informação do Campo CPF\CNPJ do cadastro do Cliente\Fornecedor  FCFO.CGCCFO |
| nmBenef | ideBenef | Nome do beneficiário. Validação: Informação obrigatória e exclusiva se {cpfBenef} não for informado. Regra de validação: REGRA\_NOME\_VALIDO | Gerado com a informação do Campo Nome do cadastro do Cliente\Fornecedor  FCFO.NOME |

idePgtoidePgto

**Informações relativas ao Rendimento Pago/Creditado**

| Registro\Campo | Registro Pai | Descrição | Origem Dados RM |
| --- | --- | --- | --- |
| infoPgto | idePgto | Informações relativas ao rendimento pago/creditado |  |
| natRend | idePgto | Código da natureza do rendimento, conforme Tabela 01.  Validação: Deve ser um código válido, existente na Tabela 01. | Gerado conforme código associado ao Lançamento Fiscal\Lançamento Financeiro O Cadastro deve ser feito no Aplicativo Gestão Fiscal\Cadatro\Mais\Natureza de Rendimento  DNATUREZARENDIMENTO.CODNATRENDIMENTO |
| dtFG | infoPgto | Informar a data do fato gerador, ou, em caso de fato não tributável mas de informação obrigatória conforme legislação vigente, a data do pagamento ou crédito, no formato AAAA-MM-DD. Validação: A data informada deve estar compreendida no período de apuração ao qual se refere o arquivo, conforme informado em (perApur}, no formato AAAA-MM-DD. | Gerado conforme da Data de Apuração do Imposto Parametrizado No RM Fluxus  Data Emissão, Data de Contabilização, Data da Baixa e Data de Vencimento |
| compFP | infoPgto | Informar a competência a que se refere os rendimentos. Validação: Informação permitida apenas se a natureza de rendimento informada em {natRend} for do grupo 10 da Tabela 01 ou se constar "S" na coluna "13°" da mesma tabela. Se informado, não pode ser superior à data atual e deve estar no formato: a) AAAA, se {indDecTerc} = [S]; b) AAAA-MM, nos demais casos. |  |
| indDecTerc | infoPgto | Indicativo de décimo terceiro salário. Só informar se o rendimento for relativo a 13°. Validação: Informação exclusiva para os rendimentos cuja coluna "13°" na Tabela 01 seja igual a [S]. Valores válidos: S. | Não Será Gerado |
| vlrRendBruto | infoPgto | Valor do rendimento bruto, inclusive os rendimentos não tributáveis ou isentos. Validação: Deve ser maior ou igual a {vlrRendTrib}. | Campo retornado no serviço do financeiro Valor Original da Baixa (campo “VALORORIGINAL” da tabela “FLANBAIXA”) ou   Valor Original do Lançamento (campo “VALORORIGINAL” da tabela “FLAN”). |
| vlrRendTrib | infoPgto | Valor do rendimento tributável. Validação: Informação permitida se, para a natureza do rendimento informada em {natRend}, houver "IR" na coluna "Tributo" da Tabela 01 **E** o cadastro da natureza de rendimento possuir IR (parâmetro "Sem IR" desmarcado). | Campo retornado no serviço do financeiro Base de Cálculo do IRRF   Valor Base: campo calculado da seguinte forma: Valor Base do IRRF (campo “VALORBASEIRRF” da tabela “FLAN”) multiplicado pelo campo Valor Original da Baixa (campo VALORORIGINAL” da tabela “FLANBAIXA”) ou Valor Original do Lançamento (campo “VALORORIGINAL” da tabela “FLAN”), divididos por 100. Caso a opção "**Sem IR**" estiver marcada no cadastro da natureza de rendimento informada para este evento (tag **natRend**), a tag "**vlrRendTrb**" **não será gerada**. |
| vlrIR | infoPgto | Valor do imposto de renda retido na fonte. Validação: Informação permitida se, para a natureza do rendimento informada em {natRend}, houver "IR" na coluna "Tributo" da Tabela 01 **E** o cadastro da natureza de rendimento possuir IR (parâmetro "Sem IR" desmarcado). | Campo retornado no serviço do financeiro valor do Tributo na Baixa (campo “VALORIRRF” da tabela “FLANBAIXA”) ou valor do Tributo no Lançamento (campo “VALORIRRF” da tabela “FLAN”). Caso a opção "**Sem IR**" estiver marcada no cadastro da natureza de rendimento informada para este evento (tag **natRend**), a tag "**vlrRendTrb**" **não será gerada**. |
| indRRA | infoPgto | Indicativo de Rendimento Recebido Acumuladamente - RRA, de acordo com o estabelecido na legislação do imposto de renda | Não será gerado |
| indFciScp | infoPgto | Indicativo de Fundo/Clube de Investimento ou Sociedade em Conta de Participação, de acordo com as seguintes opções: 1 - FCI - Fundo ou clube de investimento; 2 - SCP - Sociedade em conta de participação. | Será gerado apenas se a filial do lançamento for **SCP**, com valor fixo igual a 2. |
| nrInscFciScp | infoPgto | Número de inscrição no CNPJ, de acordo com o conteúdo do campo {indFciScp}. | Campo gerado contendo o CNPJ da Filial **SCP**, por isso, será exibido **somente**se a filial do lançamento for **SCP**. |
| percSCP | infoPgto | Percentual que o beneficiário possui na Sociedade em Conta de Participação. Validação: Informação obrigatória e exclusiva se {indFciScp} = [2]. Não pode ser maior que 100. | Gerado somente para lançamentos que possuam o **CPF** do Cliente/Fornecedor cadastrado como sócio da Filial e natureza de rendimento igual a **12001** (Lucro e Dividendo). É necessário o preenchimento do campo DSOCIOECF. PERCAPTOT (% Participação no Capital Total) no cadastro do Sócio.  Para realizar o cadastro do sócio acesse: Cadastros | Filial | Selecione a filial | Anexos | Parâmetros – Escrituração Contábil Fiscal | Edite o Parâmetro | Anexos | Sócio |
| indJud | infoPgto | Indicativo exclusivo de rendimento de natureza diversa de RRA e que seja oriundo de decisão judicial | Não será gerado |
| paisResidExt | infoPgto | Informar o código do país de destino da remessa do pagamento a residente ou domiciliado no exterior, conforme Tabela 07. Este campo não deve ser preenchido se o pagamento for efetuado no Brasil. | Gerado conforme o código de pais associado ao cliente\fornecedor  DPAIS. CODPAIS |

detDeddetDed

**Informações relativas às Deduções do Rendimento Tributável**

| Registro\Campo | Registro Pai | Descrição | Origem de Dados RM |
| --- | --- | --- | --- |
| detDed | infoPgto | Informações relativas às deduções do rendimento tributável |  |
| indTpDeducao | detDed | Indicativo do tipo de dedução: 1 - Previdência oficial;   2 - Previdência privada; 3 - Fundo de aposentadoria programada individual - Fapi; 4 - Fundação de previdência complementar do servidor público - Funpresp;   5 - Pensão alimentícia; 7 - Dependentes. Valores válidos: 1, 2, 3, 4, 5, 7. | Só geramos as opções   1 - Previdência oficial; igual a Dedução de INSS e   7 – Dependentes, igual a Dedução de Dependente  As opções 2, 3, 4, e 5 não geramos |
| vlrDeducao | detDed | Preencher com o valor da dedução do rendimento tributável. Validação: Se {indTpDeducao} = [5, 7] e o grupo {benefPen} vinculado for informado, o valor informado neste campo deve ser a soma do campo {vlrDepen} do grupo {benefPen}. O não preenchimento do grupo {benefPen} indica que o contribuinte declarante não possui as informações detalhadas por dependente/alimentando.   Se {indTpDeducao} = [7], e o grupo {benefPen} não for preenchido, o valor informado neste campo deve ser múltiplo do valor unitário da dedução por dependente definido na legislação e, em caso de diferença, o arquivo será aceito, porém, com alerta ao contribuinte apontando a inconsistência. Deve ser maior que zero. | Campo retornado no serviço do financeiro - Verificar regra da DIRF  valor das Deduções (campo “VALORDEDUCAO” da tabela “FLAN”).  valor das Deduções de Dependentes (campo “VALORDEDUCAODEPENDENTES” da tabela “FLAN”). |
| infoEntid | detDed | Possui informações da entidade de previdência complementar?   S - Sim; N - Não. Validação: Informação obrigatória e exclusiva se {indTpDeducao} = [2, 3, 4]}. Valores válidos: S, N. | Não geramos |
| nrInscPrevComp | detDed | Número de inscrição da entidade de previdência complementar. | Não geramos |
| vlrPatrocFunp | detDed | Valor da contribuição do ente público patrocinador da Fundação de Previdência do Servidor Público (Funpresp). | Não geramos |

Observação

Este grupo será gerado apenas uma vez no agrupamento de mais de um lançamento financeiro para o mesmo cli/for para evitar duplicidade na geração do XML.

rendIsentorendIsento

**Rendimentos Isentos ou Não Tributáveis**

| Registro\Campos | Registro Pai | Descrição | Origem de Dados RM |
| --- | --- | --- | --- |
| rendIsento | infoPgto | Rendimentos isentos ou não tributáveis | O grupo será gerado somente quando o campo "Indicador de isenção DIRF" estiver preenchido e seu conteúdo for diferente de "Não se aplica". Este campo pode ser encontrado ao selecionar um Lançamento Financeiro e acessar o menu Anexo| Dados Fiscais. |
| tpIsencao | rendIsento | Tipo de Isenção: 1 - Parcela isenta 65 anos;   2 - Diária de viagem;  3 - Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho;  4 - Abono pecuniário;  5 - Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore, alugueis e serviços prestados;  6 - Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço;  7 - Complementação de aposentadoria, correspondente às contribuições efetuadas no período de 01/01/1989 a 31/12/1995;  8 - Ajuda de custo;  9 - Rendimentos pagos sem retenção do IR na fonte - Lei 10.833/2003;  12 - Lucros e dividendos distribuídos nos termos do § 3º do art. 6º-A da Lei nº 15.270/2025;  99 - Outros (especificar). Validação: Vide regras na Tabela 01 - Regras para utilização dos tipos de isenção, na coluna "Rendimentos isentos". | Origem RM Fluxus:  Ao selecionar um Lançamento Financeiro e acessar o menu Anexo| Dados Fiscais| é encontrada a Opção ”Indicador de isenção DIRF”   * **Não se Aplica** Grupo rendIsento não será gerado. * **Diária de Viagem** Tipo isenção gerado com 2 - Diária de Viagem  * **Ajuda de Custo** Tipo isenção gerado com 8 - Ajuda de Custo  * **Isenção de Lucros e Dividendos** Tipo isenção gerado com 12 - Isenção de Lucros e Dividendos  * **Bolsa de Estudo Recebida por Médico Residente** Tipo Isenção Gerado com 99 - Outros * **Outros** Tipo Isenção Gerado com 99 - Outros |
| vlrIsento | rendIsento | Valor da parcela isenta. Se {tpIsencao} = [1], o valor informado neste campo deve ser igual ou menor que o valor oficial definido para a parcela isenta adicional sobre rendimentos de aposentadoria ou pensão para maiores de 65 anos. Validação: Deve ser maior que zero. Não pode ser maior que {vlrRendBruto}. Se {tpIsencao} = [1] e o valor informado neste campo for diferente do valor unitário oficial da parcela isenta para maiores de 65 anos, gerar alerta para o contribuinte sobre possível inconsistência da informação prestada. | Campo retornado no serviço do financeiro - Verificar regra da DIRF  Controlado pelo Fluxus, o valor será resultante da fórmula: “(VALORORIGINAL – VALORBASEIRRF)”. Ambos campos do lançamento financeiro.  Para o mesmo tributo, controlado pelo Liber, o valor será resultante da fórmula: “(VALORCONT – BASETRB)”  Se nos Dados Fiscais do lançamento o campo "Indicador de Isenção" estiver preenchido com valor diferente de "Não se aplica" e o VALORORIGINAL seja igual ao VALORBASEIRRF, então a tag vlrIsento passa a ser preenchida com o VALORORIGINAL do lançamento. |
| descRendimento | rendIsento | Descrição do rendimento isento/não tributável. Validação: Informação obrigatória e exclusiva se {tpIsencao} = [99]), obedecendo às regras: a) Deve conter ao menos 5 caracteres alfabéticos; b) Não é permitida a repetição consecutiva de caracteres especiais. | Como a informação é obrigatória e exclusiva para o tipo de isenção de código 99 é gerado apenas se a tag: tpIsencao for 99 - Outros, com o texto fixo: Rendimentos Isentos Outros. Demais opções a tag não é gerada. |
| dtLaudo | rendIsento | Data da moléstia grave atribuída pelo laudo. Validação: Informação exclusiva se {tpIsencao} = [6]. Se informada, a data deve ser anterior ou igual ao período de apuração ao qual se refere o arquivo. Não pode ser anterior ao ano de 1900. | Não geramos |

Informações Não Geradas

infoComplContri - Informações complementares do contribuinte.

ideDep - Identificação dos dependentes do beneficiário identificado em {ideBenef}.

benefPen - Informação dos dependentes e beneficiários da pensão alimentícia.

dedSusp - Detalhamento das deduções com exigibilidade suspensa.

infoRRA - Informações complementares relativos a Rendimentos Recebidos Acumuladamente - RRA.

despProcJud - Detalhamento das despesas com processo judicial.

ideAdv - Identificação do advogado.

infoProcJud - Informações complementares - Demais rendimentos decorrentes de decisão judicial.

despProcJud - Detalhamento das despesas com processo judicial.

ideAdv - Identificação do advogado.

ideOpSaude - Identificação da operadora do plano privado coletivo empresarial de assistência à saúde.

infoReemb - Informação de reembolso do titular do plano de saúde coletivo empresarial.

infoDependPl  - Informações de dependente do plano de saúde coletivo empresarial.

infoReembDep - Informação de reembolso do dependente do plano de saúde coletivo empresarial.
