---
content_hash: aacb03aa646336ea6b0eafb82924c022a5584bdb855b525d31de75e0c44f35da
fetched_at: '2026-06-29T00:09:22.193152+00:00'
page_id: '422545984'
product: rm
source: tdn-rm
title: Bloco Y - Informações Gerais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545984
version: 28
---

Este Bloco é composto pelos registros:

BLOCOYleftY520Y520

**Pagamentos/Recebimentos do Exterior ou de não Residentes -** **Não gerado pelo sistema.**

Deve ser gerado pelas pessoas jurídicas que receberam, pagaram, creditaram, entregara,, empregaram ou remeteram, durante o ano-calendário, de pessoas físicas ou jurídicas, residentes ou domiciliados no exterior ou de não-residentes:

* Quaisquer valores mediante operações de câmbio de qualquer natureza;
* Quaisquer valores por intermédio de transferências internacionais em reais (TIR), ou seja, provenientes de conta bancária em reais  (R$) titulada por não-residente;
* Quaisquer valores por intermédio de depósitos em contas bancárias mantidas no exterior;
* Valores iguais ou superiores a R$120.000,00, equivalentes a R$10.000,00 por mês, por intermédio de cartões de crédito;

* Valores em moeda nacional ou estrangeira, cheques ou chegues de viagem, convertidos em reais (R$) na data de cada operação, iguais ou superiores a R$120.000,00, equivalentes a R$10.000,00 por mês. Deverão ser incluídos nesta linha os recebimentos que tenham sido objeto de Declaração de Porte de Valores (e-DVP), instituída pela [IN SRF nº 619, de 2006](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=15555).
Y540Y540

**Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica - Descontinuado a partir da versão 0007**

Este registro deve ser gerado por todas as pessoas jurídicas, para discriminação da receita de vendas dos estabelecimentos por atividade econômica, quando for o caso. Para maiores informações veja o [detalhamento das regras de geração deste registro](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546105).

* [Registro Y540 - Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica](http://tdn.totvs.com/pages/viewpage.action?pageId=422546105)
Y550Y550

**Vendas a Comercial Exportadora com Fim Específico de Exportação - Descontinuado a partir da versão 0007**

Este registro dever ser gerado pelas pessoas jurídicas que efetuaram vendas a empresas comerciais exportadoras com o fim específico de exportação no ano-calendário a que se refere a ECF.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Campo da Base** | **Observações** |
| 01 | REG | Texto fixo contendo "Y550" |  | Regra de Geração do Registro |
| 02 | CNPJ\_EXP | CNPJ da Comercial Exportadora | FCFO.CGCCFO |  |
| 03 | COD\_NCM | Código NCM, conforme tabela do Sped. | TPRODUTO.NUMEROCCF |  |
| 04 | VL\_VENDA | Valor da venda | DITEM.VALORMERC - DITEM.DESCONTOITEM + DITEM.VALORDESPESA + DITEM.VALORSEGURO + DITEM.VLRFRETE | Calcular o valor líquido do item:(Valor da mercadoria - desconto + despesa + seguro + frete) |

* [Registro Y550 - Vendas a Comercial Exportadora com Fim Específico de Exportação](http://tdn.totvs.com/pages/viewpage.action?pageId=422546106)
Y560Y560

**Detalhamento das Exportações da Comercial Exportadora - Descontinuado a partir da versão 0007**

Este registro deve ser gerado pela empresa comercial exportadora que, no ano-calendário a que se refere a ECF, comprou produtos com o fim específico de exportação ou exportou produtos adquiridos com esta finalidade.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Campo da Base** | **Observações** |
| 01 | REG | Texto fixo contendo "Y560" |  | [Regra de geração do registro.](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546107) |
| 02 | CNPJ | CNPJ do produtor/vendedor | FCFO.CGCCFO | Buscar o CNPJ do Cli/For associado à nota fiscal de compra da mercadoria. |
| 03 | COD\_NCM | Código NCM, conforme tabela do Sped. | TPRODUTO.NUMEROCCF |  |
| 04 | VL\_COMPRA | Valor da compra | Serão calculados os valores baseando se na Tabela DITEM. Vide Regra de Geração | Calcular o valor líquido do item na nota fiscal de compra referenciada:(Valor da mercadoria - desconto + despesa + seguro + frete) |
| 05 | VL\_EXP | Valor da exportação | Serão calculados os valores baseando se na Tabela DITEM. Vide Regra de Geração | Quantidade exportada informada nas Referências \* valor líquido do item calculado anteriormente. |

* [Registro Y560 - Detalhamento das Exportações da Comercial Exportadora](http://tdn.totvs.com/pages/viewpage.action?pageId=422546107)
Y570Y570

**Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte**

Este registro deve ser gerado quando houver retenção de IRRF e CSLL durante o período abrangido pela ECF incidentes sobre as receitas que compõe a base de cálculo do tributo devido.  
- Inserido log dos lançamentos fiscais que foram selecionados para geração do registro.   
- Na seleção dos lançamentos fiscais para geração do registro Y570 será filtrado somente o Cli/For “Pessoa Jurídica”.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Campo da Base** | **Observações** |
| 01 | REG | Texto fixo contendo "Y570" |  | Regra de Geração do Registro |
| 02 | CNPJ\_FON | CNPJ da fonta pagadora | FCFO.CGCCFO |  |
| 03 | NOM\_EMP | Nome empresarial | FCFO.NOME |  |
| 04 | IND\_ORG\_PUB | Indicador de órgão público: S - Sim N - Não | FCFO.ORGAOPUBLICO |  |
| 05 | COD\_REC | Código da receita, conforme " Tabela de Códigos de Retenção na Fonte" publicada pela RFB | DTRIBUTO.CODRECEITA |  |
| 06 | VL\_REND | Rendimento bruto/receita | DTRBLAF.BASETRB ou FTRBLAN.BASEDECALCULO |  |
| 07 | IR\_RET | IR retido na fonte | DTRBLAF.VALORTRB ou FTRBLAN.BASEDECALCULO |  |
| 08 | CSLL\_RET | CSLL retida na fonte | DTRBLAF.VALORTRB ou FTRBLAN.BASEDECALCULO |  |

**O registro pode ser gerado a partir com as seguintes origens:**

1 -  Origem Fiscal

2 - Origem Nucleus x Fluxus

3 - Aplicação financeira

Para mais detalhes acesse o link abaixo:

* [Registro Y570 - Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte](http://tdn.totvs.com/display/LRM/Registro+Y570+-+Demonstrativo+do+Imposto+de+Renda+e+CSLL+Retidos+na+Fonte)
Y600Y600

**Identificação e Remuneração de Sócios, Titulares, Dirigentes e Conselheiros**

Este registro deve ser preenchido pela pessoa jurídica com dados dos 999 (novecentos e noventa e nove) maiores sócios ou dos titulares no período de apuração, inclusive os sócios ou titulares que tenham saído da sociedade no período de apuração e não fazem parte do quadro societário na data final do período apuração.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Campo da Base** | **Observações** |
| 01 | REG | Texto fixo contendo "Y600" |  | Regra de Geração do Registro |
| 02 | DT\_ALT\_SOC | Data da Alteração no Quadro Societário | DSOCIOECF.DTALTSOC |  |
| 03 | DT\_FIM\_SOC | Data da Saída do Quadro Societário | DSOCIOECF.DTALIENACAO |  |
| 04 | PAIS | País de Residência ou Domicílio da Pessoa Física ou Jurídica | DSOCIOECF.IDPAIS |  |
| 05 | IND\_QUALIF | Indicador de Qualificação do Sócio, Titular, Dirigente ou Conselheiro: PF - Pessoa Física PJ - Pessoa Jurídica FI – Fundo de Investimento | DSOCIOECF.INDQUALIFSOCIO |  |
| 06 | CPF\_CNPJ | CPF ou CNPJ do Sócio, Titular, Dirigente ou Conselheiro | DSOCIOECF.CPFCNPJ |  |
| 07 | NOM\_EMP | Nome empresarial do Sócio, Titular, Dirigente ou Conselheiro | DSOCIOECF.NOME |  |
| 08 | QUALIF | Qualificação do Sócio, Titular, Dirigente ou Conselheiro | DSOCIOECF.QUALIF |  |
| 09 | PERC\_CAP\_TOT | Percentual Relativo à Participação d a Pessoa Física o u Jurídica, Sócio, Titular, Conselheiro ou Dirigente, no Capital Total | DSOCIOECF.PERCAPTOT |  |
| 10 | PERC\_CAP\_VOT | Percentual Relativo à Participação d a Pessoa Física o u Jurídica, Sócio, Titular, Conselheiro ou Dirigente, no Capital Votante | DSOCIOECF.PERCAPVOT |  |
| 11 | CPF\_REP\_LEG | CPF do Representante Legal | DSOCIOECF.CPFREPRESENTANTE |  |
| 12 | QUALIF\_REP\_LEG | Qualificação do Representante Legal | DSOCIOECF.QUALIFREPRELEGAL |  |
| 13 | VL\_REM\_TRAB | Remuneração do Trabalho | DSOCIOECF.VLREMTRAB |  |
| 14 | VL\_LUC\_DIV | Lucros/Dividendos | DSOCIOECF.VLLUCDIV |  |
| 15 | VL\_JUR\_CAP | Juros Sobre o Capital Próprio | DSOCIOECF.VLJURCAP |  |
| 16 | VL\_DEM\_REND | Demais Rendimentos | DSOCIOECF.VLDEMREND |  |
| 17 | VL\_IR\_RET | IR Retido n a Fonte | DSOCIOECF.VLIRRET |  |

Y640Y640

**Participações em Consórcios de Empresas**

Será gerado com base nas informações da tabela "DPARTICICONSORCIOSEMPRESASECF". O campo chave do registro será o CNPJ, portanto os dados serão agrupados por esse campo.  
Para que o registro Y640 seja gerado, é necessário que o anexo "Participações em Consórcios de Empresas" (anexo "Parâmetros ECF" da Filial) esteja preenchido.

Y650Y650

**Participantes do Consórcio**

Será gerado com base nas informações da tabela "DPARTICIPANTESCONSORCIOSECF". O campo chave do registro será o CNPJ, portanto os dados serão agrupados por esse campo.

Y671Y671

**Outras Informações (Lucro Real) - Descontinuado a partir da versão 0007**

O processamento desse registro na ECF será feita através da Ferramenta de [Demonstrações Contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=423938730), no Totvs Gestão Contábil.   
Está disponível na área de Download e no diretório de instalação totvs\CorporeRM\ObjetosGerenciais\Layout o template ( CTBLAY0012 - Estrutura do Registro Y671 da ECF.XML) para importação e parametrização.  
Após a parametrização da Demonstração Contábil, a mesma deverá ser informada no cadastro da Filial, na parametrização da ECF, aba "Outras Informações", campo "Registro Y671:Outras Informações (Lucro Real)".   
Esse registro é de preenchimento obrigatório por todas as pessoas jurídicas que apuraram o imposto de renda com base no lucro real e solicita as seguintes informações:

* Aquisição de máquinas, aparelhos, instrumentos e equipamentos novos (R$).
* Doação aos fundos dos direitos da criança e do adolescente (R$).
* Doação aos fundos nacional, estaduais e municipais do idoso (R$).
* Aquisições para o ativo imobilizado (R$).
* Baixas do ativo imobilizado (R$).
* Bens sujeitos ao incentivo de que trata a Lei no 11.051/2004, no início do período (R$).
* Bens sujeitos ao incentivo de que trata a Lei no 11.051/2004, no fim do período (R$).
* Saldo de créditos de CSLL sobre depreciação no início do período (R$).
* Valor das operações de câmbio com isenção de IOF.
* Valor total da folha de pagamento sujeita à alíquota reduzida de que trata a Lei no 11.774/2008 (R$).
* Alíquota reduzida de que trata a Lei no 11.774/2008 (%). *Este campo deve ser parametrizado com origem do valor: Valor Fixo. Se for o caso, deve ser informada a alíquota, com os decimais separados por vírgula (,) sem o sinal de percentual (%). Se não for o caso, deixar o campo sem parametrização.*
* Alteração de capital na forma dos art. 22 e 23 da Lei no 9.249/1995 (Sim/Não). *Esta linha devem receber "1" (Não) ou "2" (Sim), origem do valor: Valor Fixo*
* Opção pela escrituração, no ativo, da base de cálculo negativa da CSLL (Sim/Não) *Esta linha devem receber "1" (Não) ou "2" (Sim), origem do valor: Valor Fixo*
Y672Y672

**Outras Informações (Lucro Presumido ou Lucro Arbitrado)**

O processamento desse registro na ECF será feita através da Ferramenta de [Demonstrações Contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=423938730), no Totvs Gestão Contábil. Está disponível nas área de Download e no diretório de instalação totvs\CorporeRM\ObjetosGerenciais\Layout o template ( CTBLAY0013 - Estrutura do Registro Y672 da ECF.XML) para importação e parametrização.  
Após a parametrização da Demonstração Contábil, a mesma deverá ser informada no cadastro da Filial, na parametrização da ECF, aba "Outras Informações", campo "Registro Y672:Outras Informações (Lucro Presumido)".   Esse registro é de preenchimento obrigatório por todas as Pessoas Jurídicas que apuraram o imposto de renda com base no Lucro presumido ou Arbitrado e solicita as seguintes informações:

* Capital registrado no ano imediatamente anterior (R$)
* Capital registrado no ano da escrituração (R$)
* Estoques no ano imediatamente anterior (R$)
* Estoques no ano da escrituração (R$)
* Caixa no ano imediatamente anterior (R$)
* Caixa no ano da escrituração (R$)
* Aplicações financeiras no ano imediatamente anterior (R$)
* Aplicações financeiras no ano da escrituração (R$)
* Conta a receber no ano imediatamente anterior (R$)
* Conta a receber no ano da escrituração (R$)
* Conta a pagar no ano imediatamente anterior (R$)
* Conta a pagar no ano da escrituração (R$)
* Compras de mercadorias no ano da escrituração (R$)
* Compras do ativo, exceto ativo circulante e ativo não circulante realizável a longo prazo, no ano da escrituração (R$)
* Receitas e rendimentos não tributáveis ou tributados exclusivamente na fonte no ano da escrituração (R$)
* Total do ativo no ano da escrituração (R$)
* Folha de pagamento sujeita à alíquota reduzida de que trata a Lei no 11.774/2008 (R$)
* Alíquota reduzida de que trata a Lei no 11.774/2008 (%) *Este campo deve ser parametrizado com origem do valor: Valor Fixo. Se for o caso, deve ser informada a alíquota, com os decimais separados por vírgula (,) sem o sinal de percentual (%). Se não for o caso, deixar o campo sem parametrização.*
* Regime de apuração das receitas (Não se aplica/Caixa/Competência) *Este campo deve ser parametrizado com origem do valor: Valor Fixo. Sendo, "0" – Não se aplica, "1" – Caixa ou "2" – Competência*
* Método de avaliação de estoques (Custo Médio Ponderado/PEPS/Arbitramento) *Este campo deve ser parametrizado com origem do valor: Valor Fixo. Sendo, "1" – Custo Médio Ponderado, "2" – PEPS ou "3" – Arbitramento*
Y730Y730

**Identificação de donatários/destinatários de deduções do IRPJ/CSLL.**

A geração deste registro é baseada nas informações cadastradas em . O sistema exportará apenas os registros cuja **Data da Dedução** esteja compreendida entre as datas inicial e final informadas nos parâmetros de geração da ECF.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Campo da Base** | **Observações** |
| 01 | REG | Texto fixo contendo "Y730" | - |  |
| 02 | DEDUCAO | Tipo da dedução, conforme tabela do Sped (Disponibilizada no programa da ECF no diretório Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas/ SPEDECF\_DEDUCOES\_IRPJ\_CSLL). | DDEDUCOES.CODDEDUCAO |  |
| 03 | TIPO | Tipo da doação, conforme tabela do Sped (Disponibilizada no programa da ECF no diretório Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas/ SPEDECF\_TIPO\_DOACAO). | DDEDUCOES.TIPODEDUCAO |  |
| 04 | DATA | Data que a doação foi efetuada | DDEDUCOES.DATADEDUCAO |  |
| 05 | TIPO\_DESTINATARIO | Identificação se o destinatário da dedução é pessoa física ou jurídica. | Caso DDEDUCOES.CPFCNPJDESTINATARIO tenha 11 dígitos = "PF", 14 dígitos = "PJ" |  |
| 06 | DESTINATARIO | Identificação do destinatário. Deve ser informado um CNPJ (14 dígitos) ou CNP (11 dígitos) | DDEDUCOES.CPFCNPJDESTINATARIO |  |
| 07 | VALOR | Valor utilizado na dedução do IRPJ/CSLL. | DDEDUCOES.VALORDEDUCAO |  |
| 08 | OBSERVACAO | Texto livre a ser utilizado pelo contribuinte, podendo citar: • Artigo e lei que refere a dedução; • Número do processo judicial e/ou Tribunal que originou eventual processo. | DDEDUCOES.OBSERVACAO |  |

Registros Não GeradosRegistros Não Gerados

Os registros Y580, Y590, Y611, Y612, Y620, Y630, Y640, Y650, Y660, Y665, Y680, Y681, Y682, Y690 e Y800 atualmente não são gerados pelo sistema.
