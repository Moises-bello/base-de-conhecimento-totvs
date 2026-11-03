---
article_id: 4403121629335
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 6b853f32b2bf039414949157ae870324474576aea67cbd68f934a765ceaeafd6
fetched_at: '2026-06-28T22:40:47.671053+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - Como preencher
  os parâmetros/wizard para geração da ECF??
type: support-article
updated_at: '2023-06-22T11:58:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403121629335-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Como-preencher-os-par%C3%A2metros-wizard-para-gera%C3%A7%C3%A3o-da-ECF
---

**Dúvida** Como preencher os parâmetros/wizard para geração da ECF??  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - TOTVS Contabilidade Gerencial - Todas as versões  
  
**Solução**

Menu Padrão: Atualizações + Escrituração Contábil + Central de Escrituração (CTBS001)

Posicione na opção ECF + botão incluir

**1) Tipo Escrituração?**

1.Com centralização:  
As tabelas de MOVIMENTOS contábil (exemplo CT2, CQ0,CQ1..) podem ser exclusivas ou compartilhadas, porém só será permitido selecionar uma filial por vez.

2. Sem centralização (Descentralizada- Gera o registro 0020)  
Caso as tabelas de movimentos sejam exclusivas por filial (CT2,CQ0,CQ1..) e as tabelas de cadastro compartilhadas (CT1, CTT, CTS) poderá ser selecionado mais de uma filial, com a obrigatoriedade de informar a matriz consolidadora.  
Nesta opção os Demonstrativos (DRE, BP...) e lançamentos serão aglutinados em um único TXT.  
No Registro 0000 irá conter o CNPJ da consolidadora e no Registro 0020 o CNPJ das filiais.

**Importante!**  
Entrega consolidada e plano de contas diferente (tabelas de cadastros)?  
Deverá ser criado no SIGAMAT uma filial consolidadora e processar a rotina CTBA231 –Consolidação configurada (Plano de contas diferente)

Plano de contas iguais (tabela de cadastro) mas não quer gerar o registro 0020?  
Deverá ser criado no SIGAMAT uma filial consolidadora e processar a rotina  
CTBA220- Consolidação Geral.

Documentação:

[Com centralização/ Descentralizada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125892-MP-SIGACTB-ECF-e-ECD-Centraliza%C3%A7%C3%A3o-e-descentralizada)

**2) Indicador Inicio de Período?**  
0- Regular  
1- Abertura  
2- Resultante Cisao/Fusao ou remanescente  
3- Resultado de Mudança de qualificação da Pessoa Jurídica  
4- Início de obrigatoriedade da entrega do curso do ano calendário

**3) Indicador de Situação especial?**  
0- Normal  
1- Extinção  
2- Fusão  
3- Incorporada  
4- Incorporadora  
5- Cisão total  
6- Cisão Parcial  
7- Mudança de qualificação da PJ  
8- Desenquadramento imune/isenta  
9- Inclusão Simples Nacional

Patr. Remanescente de cisão (%)  
Observação: Necessário para o controle de saldos na conta da parte B do LALUR

**4) Retificadora?**  
S- ECF- Retificadora  
N- ECF- Original  
F- ECF- Original com mudança de forma de tributação (Art. 6º-A, § 2º, da Instrução  
Normativa RFB nº 1.422/2013)

Número do recibo Anterior?

**5) Tipo da ECF?**  
0- ECF de empresa não participante como sócio Ostensivo  
1- ECF de empresa participante como sócio ostensivo  
2- ECF da SCP

Identificação da SCP?

**6) Data Situação especial/evento?**

**7) Método de Avaliação de Estoque Final?**  
1- Custo médio Ponderado  
2- Peps  
3- Arbitramento  
4- Custo Especifico  
5- Valor Realizável líquido  
6- Inventário Periódico  
7- Outros  
8- Não há

**Registro 0010: Parâmetros de Tributação**

**Campo 1 -** Texto fixo contendo a identificação do registro (0010).

**Campo 2**- Hashcode da ECF do período imediatamente anterior a ser recuperado. Campo preenchido automaticamente pelo sistema

**Campo 3- 8) Indicador de optante pelo Refis?**  
S- Sim  
N- Não

**9) Indicador de optante pelo Paes?**  
S- Sim  
N- Não  
À partir do leiaute 9, esta pergunta estará desabilitada devido alteração no leiaute.

**Campo 4- [10) Forma de Tributação do Lucro? (FORMA\_TRIB )](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403575196951-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-Tributa%C3%A7%C3%A3o?source=search)**  
1- Lucro Real  
2- Lucro Real/Arbitrado  
3- Lucro Presumido/Real  
4- Lucro Presumido/Real/Arbitrado  
5- Lucro Presumido  
6- Lucro Arbitrado  
7- Lucro Presumido/Arbitrado  
8- Imune de IPRJ  
9- Isento de IPRJ

**Campo 5- [11) Período de apuração do IPRJ e CSLL (FORMA\_APUR)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403566448279-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Per%C3%ADodo-de-apura%C3%A7%C3%A3o-do-IRPJ-e-CSLL-?source=search) ?**  
T- Trimestral  
A- Anual

**Campo 6- [12) Qualificação da Pessoa Jurídica (COD\_QUALIF\_PJ) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415478314519-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Qualifica%C3%A7%C3%A3o-da-Pessoa-Jur%C3%ADdica-?source=search)**  
01- PJ em Geral  
01- PJ componente do Sistema FInar  
03- Sociedades Seguradoras, de Ca

**Campo 7- [13) Forma de trib. no Período (FORMA\_TRIB\_PER)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415486620695-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-trib-no-Per%C3%ADodo-?source=search)**

**Campo 8- [14) Forma de apura. da Estimativa (MES\_BAL\_RED)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415471717655-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-apura-da-Estimativa-?source=search)**

**Campo 9-**[**15) Tipo de escrituração (TIP\_ESC\_PRE)?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415495420183-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Tipo-de-escritura%C3%A7%C3%A3o-?source=search)  
L- Livro Caixa  
C- Contábil

**Campo 10- [16) Tipo de pessoa Jur. Imune ou isenta (TIP\_ENT) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419591453079-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Tipo-de-pessoa-Jur-Imune-ou-isenta?source=search)**  
01- Assistencia Social  
02- Educacional  
03- Sindicato de trabalhadores  
04- Associação civil  
05- Cultural  
06- Entidade Fechada de prêvidencia  
07- Filantrópica  
08- Sindicato  
09- Recreativa  
10- Cientifica  
11- Associação de poupana e empre  
12- Entidade aberta de provência co  
13- FIFA e entidades relacionadas  
14- CIO e entidades relacionadas  
15- Partido Políticos  
99- Outros

**Campo 11- [17) Apuração do IRPJ para imunes ou isentas (FORMA\_APUR\_I) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419600349975-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Apura%C3%A7%C3%A3o-do-IRPJ-para-Imunes-ou-Isentas?source=search)**  
A- Anual  
T- Trimestral  
D- Desobrigada

**Campo 12- 18) Apuração do CSLL para imunes ou isentas?**  
A- Anual  
T- Trismetral  
D- Desobrigada

**19) Optante pela extinção do RTT em 2014?**  
S- Sim  
N- Não

\*desabilitado

**20) Dif. entre contabilidade Societaria e Fcont?**  
S- Sim  
N- Não

\*desabilitado

**Campo 13- 21) Critério de reconhecimento de receitas?**  
1- Regime de Caixa  
2- Regime de Competência

Critério de reconhecimento de receitas para empresas tributadas pelo Lucro Presumido (Art. 215, § 9º, Instrução Normativa RFB nº 1.700/2017)

**Registro 0020: Parâmetros Complementares**

**Campo 1-** Texto fixo contendo a identificação do registro (0020).

**Campo 29- 22) Declaração País a País?**  
S- Sim  
N- Não

Entidade Integrante de Grupo Multinacional: A pessoa jurídica é entidade integrante de grupo multinacional, nos termos da Instrução Normativa RFB nº 1.681/2016?

Caso SIM, Necessário pré-cadastro para geração do **Bloco W**, conforme documentação:

Código Identif. Bloco W? (F3)

[Como cadastrar o bloco W](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006986031-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS410-ECF-Como-gerar-o-bloco-W)

**Campo 30- 23) Derex?**  
S- Sim  
N- Não

Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações.

Campo 2- **24) PJ Sujeita a Alíquota de CSLL?**  
09%  
17%  
20%  
15%

**Campo 3- 25) Quantidade de SCP da PJ?**

**Campo 4- 26) Administradora de Fundos e Clubes de Investimento?**

S- Sim  
N- Não

**Campo 5- 27) Participações em consórcios de Empresas?**  
S- Sim  
N- Não

A pessoa jurídica participante de consórcio constituído nos termos do disposto nos arts. 278 e 279 da Lei nº 6.404, de 15 de dezembro de 1976, deve assinalar este campo. Atenção: Somente deve ser assinalado este campo quando houver receita de pelo menos uma consorciada.

**Campo 6- 28) Operações com o exterior?**  
S- Sim  
N- Não

A pessoa jurídica, inclusive instituição financeira ou companhia seguradora, conforme relacionadas no § 1º do art. 22 da Lei nº 8.212, de 1991, e no inciso II do art. 14 da Lei nº 9.718, de 1998, que realizou exportação/importação de bens, serviços ou direitos ou auferiu receitas financeiras ou incorreu em despesas financeiras em operações efetuadas com pessoa física ou jurídica residente ou domiciliada no exterior, ainda que essas operações não tenham sido realizadas com pessoa vinculada ou com pessoa residente ou domiciliada em país ou dependência com tributação favorecida ou cuja legislação interna oponha sigilo relativo à composição societária de pessoas jurídicas ou a sua titularidade, deve assinalar este campo. Deve também assinalar este campo a pessoa jurídica, inclusive instituição financeira ou companhia seguradora, que realizar as operações acima referidas por intermédio de interposta pessoa.

**Campo 7- 29)Operações com pessoa vinculada/interposta/pais com tributação fa**  
S- Sim  
N- Não

Deve assinalar este campo, a pessoa jurídica, inclusive instituição financeira ou companhia seguradora, conforme relacionadas no § 1º do art. 22 da Lei nº 8.212, de 1991, e no inciso II do art. 14 da Lei nº 9.718, de 1998, que realizou exportação/importação de bens, serviços ou direitos ou auferiu receitas financeiras ou incorreu em despesas financeiras em operações efetuadas com pessoa física ou jurídica residente ou domiciliada no exterior, considerada pela legislação brasileira: a) pessoa vinculada; b) pessoa residente ou domiciliada em países com tributação favorecida ou cuja legislação interna oponha sigilo relativo à composição societária de pessoas jurídicas ou a sua titularidade; e c) a partir de 1º de janeiro de 2009, pessoa residente ou domiciliada no exterior, que goze, nos termos da legislação, de regime fiscal privilegiado (Art. 24-A da Lei nº 9.430, de 1996, instituído pela Lei nº 11.727, de 2008). Deve também assinalar este campo a pessoa jurídica, inclusive instituição financeira ou companhia seguradora, que realizar as operações acima referidas por intermédio de interposta pessoa

**Campo 8- 30) PJ Enquadrada nos artigos 48 ou 49 da instrução normativa RFB n1.312/20**  
S- Sim  
N- Não

**Campo 9- 31)Participações no exterior?**  
S- Sim  
N- Não

**Campo 10- 32) Atividade Rural?**  
S- Sim  
N- Não

**Campo 11- 33) Lucro da exploração?**  
S- Sim  
N- Não

Este campo deve ser assinalado pelas pessoas jurídicas que adotam a forma de tributação pelo lucro real, inclusive se optantes pelo Refis, que gozem de benefícios fiscais calculados com base no lucro da exploração.

**Campo 12- 34) Isenção e redução do imposto para Lucro Presumido?**  
S- Sim  
N- Não

A pessoa jurídica tributada pelo lucro presumido e optante pelo Refis deve assinalar este campo caso usufrua benefícios fiscais relativos a isenção ou redução do imposto de renda.

**Campo 13- 35)FINOR/FINAM/FUNRES?**  
S- Sim  
N- Não

Este campo deve ser assinalado pelas pessoas jurídicas ou grupos de empresas coligadas de que trata o art. 9º da Lei nº 8.167, de 1991, alterado pela Medida Provisória nº 2.199-14, de 24 de agosto de 2001, titulares de empreendimento de setor da economia considerado, em ato do Poder Executivo, prioritário para o desenvolvimento regional, aprovado ou protocolizado até 2 de maio de 2001 nas áreas da Sudam e da Sudene ou do Grupo Executivo para Recuperação Econômica do Estado do Espírito Santo (Geres) (MP nº 2.199-14, de 2001, art. 4º, e MP nº 2.145, de 2 de maio de 2001, art. 50, XX, atuais MP nº 2.156-5, de 2001, art. 32, XVIII, e nº 2.157-5, de 2001, art. 32, IV)

**36) Doações a campanhas eleitorais?**  
S- Sim  
N- Não  
\*Desabilitado a partir do leiaute 7

**Campo 14- 37) Participações permanentes em coligadas ou controladas?**  
S- Sim  
N- Não

A pessoa jurídica domiciliada no Brasil, que teve participações permanentes, no ano calendário, em capital de pessoa jurídica domiciliada no Brasil ou no exterior, considerada, pela legislação brasileira, avaliada pelo método de equivalência patrimonial, deve assinalar este campo.

**38) PJ Efetuou vendas a empresas comercial exportadora com fim especifico de**  
S- Sim  
N- Não  
\*Desabilitado a partir do leiaute 7.

**Campo 15- 39) Recebimentos do exterior ou de não residentes?**  
S- Sim  
N- Não

Deve assinalar este campo, a pessoa jurídica que recebeu, durante o ano-calendário, de pessoas físicas ou jurídicas, residentes ou domiciliadas no exterior ou de não-residentes: - quaisquer valores mediante operações de câmbio de qualquer natureza; - quaisquer valores por intermédio de transferências internacionais em reais (TIR), ou seja, provenientes de conta bancária em reais (R$) titulada por não-residente; - valores iguais ou superiores a R$ 120.000,00 (cento e vinte mil reais), equivalentes a R$ 10.000,00 por mês, por intermédio de cartões de crédito; - quaisquer valores por intermédio de depósitos em contas bancárias mantidas no exterior

**Campo 16- 40)Ativos no exterior?**  
S- Sim  
N- Não

Preenchida por todas as pessoas jurídicas (Sim), salvo quando o valor contábil total dos ativos a declarar, convertido para Reais no final do período abrangido pela ECF, for inferior a R$ 100.000,00 (cem mil reais) (Não).

**41)PJ Comercial exportadora?**  
S- Sim  
N- Não  
\*Desabilitado a partir do leiaute 7.

**Campo 17- 42) Pagamentos ao exterior ou não residentes?**  
S- Sim  
N- Não

Deve assinalar este campo, a pessoa jurídica que tiver pagado, creditado, entregado, empregado ou remetido, durante o ano-calendário, a pessoas físicas ou jurídicas, residentes ou domiciliadas no exterior ou a não-residentes: - quaisquer valores mediante operações de câmbio de qualquer natureza; - quaisquer valores por intermédio de transferências internacionais em reais (TIR), ou seja, pela utilização de reais (R$) para crédito de conta bancária titulada por não-residentes; - valores iguais ou superiores a R$ 120.000,00 (cento e vinte mil reais), equivalentes a R$ 10.000,00 por mês, por intermédio de cartões de crédito; - quaisquer valores mediante a utilização de recursos mantidos no exterior.

**Campo 18- 43) Comércio eletrônico e tecnologia da informação**  
S- Sim  
N- Não

A pessoa jurídica que efetuou durante o ano-calendário vendas de bens (tangíveis ou intangíveis) ou tiver prestado serviços, por meio da Internet, para pessoas físicas e jurídicas, residentes ou domiciliadas no Brasil ou no exterior, deve assinalar este campo. Ao assinalar este campo, são disponibilizados os *registros X400* (Comércio Eletrônico e Tecnologia da Informação) e *X410* (Comércio Eletrônico).

**Campo 19- 44) Royalties Recebidos do Brasil e do Exterior?**  
S- Sim  
N- Não

A pessoa jurídica que tiver recebido, durante o ano-calendário, de pessoas físicas ou jurídicas, residentes ou domiciliadas no Brasil ou no exterior, rendimentos a título de royalties relativos a: exploração econômica dos direitos patrimoniais do autor, de marcas, de patentes e de desenho industrial; exploração de know-how; exploração de franquias e exploração dos direitos relativos à propriedade intelectual referente a cultivares, deve preencher este campo com “Sim”.

**Campo 20- 45) Royalties pagos a beneficiários do Brasil e do Exterior?**  
S- Sim  
N- Não

A pessoa jurídica que tiver efetuado pagamento ou remessa, durante o ano-calendário, a pessoas físicas ou jurídicas, residentes ou domiciliadas no Brasil ou no exterior, a título de royalties relativos a: exploração econômica dos direitos patrimoniais do autor, de marcas, de patentes e de desenho industrial; exploração de know-how; exploração de franquias e exploração dos direitos relativos à propriedade intelectual referente a cultivares, deve preencher este campo com “Sim”.

**Campo 21- 46) Rendimentos relativos a serviços, juros e dividendos recebidos do Brasil**  
S- Sim  
N- Não

A pessoa jurídica que tiver recebido, durante o ano-calendário, de pessoas físicas ou jurídicas, residentes ou domiciliadas no Brasil ou no exterior, rendimentos relativos a: serviços de assistência técnica, científica, administrativa e semelhantes que impliquem transferência de tecnologia; serviços técnicos e de assistência que não impliquem transferência de tecnologia; juros sobre capital próprio, bem como juros decorrentes de contratos de mútuo entre empresas ligadas e juros decorrentes de contratos de financiamento; dividendos decorrentes de participações em outras empresas, deve preencher este campo com “Sim”

**Campo 22- 47) Pagamentos ou Remessas a Título de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior.**  
S- Sim  
N- Não

A pessoa jurídica que tiver pagado ou remetido, durante o ano-calendário, a pessoas físicas ou jurídicas, residentes ou domiciliadas no Brasil ou no exterior, valores relativos a: serviços de assistência técnica, científica, administrativa e semelhantes que impliquem transferência de tecnologia; serviços técnicos e de assistência que não impliquem transferência de tecnologia; juros sobre capital próprio, bem como juros decorrentes de contratos de mútuo entre empresas ligadas e juros decorrentes de contratos de financiamento; dividendos decorrentes de participações em outras empresas, deve preencher este campo com “Sim”.

**Campo 23- 48) Inovação Tecnológica e Desenvolvimento Tecnológico**

S- Sim  
N- Não

A pessoa jurídica beneficiária de incentivos fiscais relativos às atividades de pesquisa tecnológica e desenvolvimento de inovação tecnológica de que tratam os arts. 17 a 26 da Lei nº 11.196, de 21 de novembro de 2005, ou a pessoa jurídica executora dos programas de desenvolvimento tecnológico industrial ou agropecuário (PDTI/PDTA) de que trata a Lei nº 8.661, de 1993, aprovados até 31 de dezembro de 2005, que não tenha migrado para o regime estabelecido nos arts. 17 a 26 da Lei nº 11.196, de 2005, deve preencher este campo com “Sim”.

**Campo 24-** **49) Capacitação de Informática e Inclusão Digital:**

S – Sim

N – Não

A pessoa jurídica que tiver investido em atividades de pesquisa e desenvolvimento em tecnologia da informação no âmbito dos programas de capacitação e competitividade dos setores de informática e automação e tecnologias da informação de que trata a Lei nº 8.248, de 23 de outubro de 1991, a Lei nº 10.176, de 11 de janeiro de 2001, e a Lei nº 11.077, de 30 de dezembro de 2004, regulamentadas pelo Decreto nº 5.906, de 26 de setembro de 2006, ou tiver efetuado venda a varejo nos termos dos arts. 28 a 30 da Lei nº 11.196, de 2005, que dispõem sobre o programa de inclusão digital, deve preencher este campo com “Sim”. 

**Campo 25-** **50) Pessoa habilitada?**

 S – Sim

N – Não

A pessoa jurídica habilitada no Regime Especial de Tributação para a Plataforma de Exportação de Serviços de Tecnologia da Informação (Repes) ou no Regime Especial de Aquisição de Bens de Capital para Empresas Exportadoras (Recap) instituídos pela Lei nº 11.196, de 2005, regulamentados pelos Decretos nº 5.712, de 2 de março de 2006, e nº 5.649, de 29 de dezembro de 2005, respectivamente, deve assinalar este campo. Também deve assinalar este campo a pessoa jurídica executora de projeto aprovado no âmbito do Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Semicondutores (Padis) ou do Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Equipamentos para TV Digital (PATVD), instituídos pela Lei nº 11.484, de 2007. Este campo deve também ser assinalado pela pessoa jurídica habilitada ou co-habilitada no Regime Especial de Incentivos e Desenvolvimento da Infraestrutura (Reidi), instituído pela Lei nº 11.488, de 15 de junho de 2007, e regulamentado pelo Decreto nº 6.144, de 3 de julho de 2007, com alterações introduzidas pelo Decreto nº 6.167, de 24 de julho de 2007. Habilitada ou co-habilitada no Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura da Indústria Petrolífera das Regiões Norte, Nordeste e Centro-Oeste (Repenec), instituído pela Lei nº 12.249, de 2010, regulamentado pelo Decreto nº 7.320, de 28 de setembro de 2010. Habilitada no Regime Especial de Incentivo a Computadores para Uso Educacional (REICOMP), instituído pela Lei nº 12.715, de 17 de setembro de 2012. Habilitada no Regime Especial para a Indústria Aeronáutica Brasileira (Retaero), instituído pela Lei nº 12.249, de 2010 Detentora de projeto de exibição cinematográfica aprovado no âmbito do Regime Especial de Tributação para Desenvolvimento da Atividade de Exibição Cinematográfica (Recine), instituído Lei nº 12.599, de 23 de março de 2012. Os estabelecimentos industriais que adquirirem resíduos sólidos utilizados como matérias-primas ou produtos intermediários na fabricação de seus produtos, de acordo com o art. 5º da Lei nº 12.375, de 30 de dezembro de 2010, devem assinalar este campo. Habilitada ou co-habilitada no Regime Especial de Tributação para construção, ampliação, reforma ou modernização de estádios de futebol (Recopa), instituído pela Lei nº 12.350, de 20 de dezembro de 2010. Habilitada para fins dos benefícios fiscais previstos na Lei nº 12.350, de 20 de dezembro de 2010, relativos à realização, no Brasil, da Copa das Confederações FIFA 2013 e da Copa do Mundo FIFA 2014. Habilitada no Regime Especial Tributário para a Indústria de Defesa (Retid), instituído pela Lei nº 12.598, de 22 de março de 2012. Habilitada no Regime Especial de Tributação do Programa Nacional de Banda Larga para Implantação de Redes de Telecomunicações (REPNBL-Redes), instituído pela Lei nº 12.715, de 17 de setembro de 2012, regulamentado pelo Decreto nº 7.921, de 15 de fevereiro de 2013. Habilitada ou cohabilitada no Regime Especial de Incentivo ao Desenvolvimento da Infraestrutura da Indústria de Fertilizantes (REIF), instituído pela Lei nº 12.794, de 02 de abril de 2013, arts. 5º a 11. Habilitada para fins de fruição dos benefícios fiscais, relativos à realização, no Brasil, dos Jogos Olímpicos de 2016 e dos Jogos Paraolímpicos de 2016, de que trata a Lei nº 12.780, de 2013.

**Campo 26- 51) Pólo Industrial de Manaus e Amazônia Ocidental:**

S – Sim

N – Não

A pessoa jurídica que estiver localizada na área de atuação da Superintendência da Zona Franca de Manaus (Suframa) que seja beneficiária dos incentivos de que trata o Decreto-lei nº 288, de 28 de fevereiro de 1967, e alterações posteriores; a Lei nº 8.387, de 30 de dezembro de 1991, e alterações posteriores; ou o Decreto-lei nº 356, de 15 de agosto de 1968, e alterações posteriores (Amazônia Ocidental), deve preencher este campo com “Sim”. 

**Campo 27- 52) Zonas de Processamento de Exportação:**

S – Sim

N – Não

A pessoa jurídica autorizada a operar em Zonas de Processamento de Exportação, voltadas para a produção de bens a serem comercializados no exterior, de acordo com o estabelecido pela Lei nº 11.508, de 20 de julho de 2007 e pela Lei nº 11.732, de 30 de junho de 2008, deve preencher este campo com “Sim”. 

**Campo 28- 53) Áreas de Livre Comércio:**

S – Sim

N – Não

A pessoa jurídica autorizada a operar nas Áreas de Livre Comércio de Boa Vista, Bonfim, Tabatinga, Macapá e Santana, Brasiléia, Cruzeiro do Sul ou Guajará-Mirim, beneficiária dos incentivos de que tratam a Lei nº 8.256, de 25 de novembro de 1991, a Lei nº 11.732, de 30 de junho de 2008, a Lei nº 7.965, de 22 de dezembro de 1989, a Lei nº 8.387, de 30 de dezembro de 1991, o Decreto nº 517, de 8 de maio de 1992, a Lei nº 8.857, de 8 de março de 1994, e a Lei nº 8.210, de 19 de julho de 1991, e alterações posteriores, deve preencher este campo com “Sim”. 

**54) Código identif. Registro 0021?**

**55) Cod. Identif. Bloco V- Derex? (F3)**

Ao informar SIM (**campos 30**) necessário pré- cadastro, para geração do **Bloco V**, conforme Documentação a seguir:

[Como gerar o Bloco V- Derex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004953631-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS450-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-do-bloco-V-DEREX-)
