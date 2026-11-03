---
content_hash: a51853dea7370029b627c27234cb28674c9b10a0a85863422631e948e4679c5c
fetched_at: '2026-06-29T00:09:22.213796+00:00'
page_id: '422545987'
product: rm
source: tdn-rm
title: Bloco X- Informações Econômicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545987
version: 20
---

BLOCOXleftX390X390

**Registro X390 -** **Origem e Aplicação de Recursos - Imunes ou Isentas**  
O processamento desse registro na ECF será feita através da Ferramenta de [Demonstrações Contábeis](https://tdn.totvs.com/pages/viewpage.action?pageId=423938730), no Totvs Gestão Contábil.  
Está disponível na área de Download e no diretório de instalação totvs\CorporeRM\ObjetosGerenciais\Layout o template (CTBLAY0011 - Estrutura do Registro X390 da ECF.XML) para importação e parametrização.  
Após a parametrização da Demonstração Contábil, a mesma deverá ser informada no cadastro da Filial, na parametrização da ECF, aba "[Outras Informações](https://tdn.totvs.com/pages/viewpage.action?pageId=422546058)", campo "Registro X390: Origem e Aplicação de Recursos (Imunes e Isentas)"    
Esse registro é de preenchimento obrigatório por todas as empresas imunes e isentas e solicita as seguintes informações:

* Contribuições de Associados ou Sindicalizados (R$).
* Receita da Venda de Bens ou da Prestação de Serviços (R$).
* Rendimentos de Aplicações Financeiras de Renda Fixa (R$).
* Ganhos Líquidos Auferidos no Mercado de Renda Variável (R$).
* Doações e Subvenções (R$).
* Outros Recursos (R$).
* Ordenados, Gratificações e Outros Pagamentos, Inclusive Encargos Sociais (R$).
* IR Retido sobre Rendimentos de Aplicações Financeiras de Renda Fixa (R$).
* IR Retido ou Pago sobre Ganhos Líquidos Auferidos no Mercado de Renda Variável (R$).
* Impostos, Taxas e Contribuições (R$).
* Despesas de Manutenção (R$).
* Outras Despesas (R$).
X450X450Regras de geraçãoRegras de geração

**Pagamentos ou Remessas a Título de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior**

As informações serão providas pelo TOTVS Gestão Financeira. Portanto, para geração deste registro, é preciso possuir integração do Gestão Fiscal com o Gestão Financeira.

Regra específica do **Registro X450:**

* Este será gerado se o campo “***Pagamentos ou Remessas a Título de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior***” estiver marcado (Aba Complementares).
* Serão selecionados todos os lançamentos financeiros a **pagar** que estiverem com o campo**Classificação do Pagamento ou Recebimento** preenchido.

Regras comuns:

* Serão considerados os lançamentos de todas as Filiais, exceto as SCP’s.
* Na ECF da SCP, serão considerados os lançamentos apenas daquela Filial.
* Será gerado um registro para cada país movimentado durante o período da escrituração.
* Os Lançamentos Financeiros selecionados devem ser **Baixados**.

**Lançamentos Financeiros**.

Deve-se classificar todos os lançamentos financeiros quanto ao tipo da operação. Um campo foi criado na pasta “**Integração Fiscal**” do Lançamento Financeiro.

Classificação do Pagamento ou Recebimento

Ele também está disponível no Processo de **Alteração Global** (*Contas a Pagar/Receber -> Lançamentos -> Processos -> Manutenção de Lançamentos -> Alteração Global*)**.**

Alteração Global

**Escrituração Contábil Fiscal**

Para que os registros X430 e X450 sejam gerados na rotina, é necessário habilitar os campos “**Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior**” e “**Pagamentos ou Remessas a Título de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior**”, respectivamente, em Anexos | Parâmetros da ECF, no Cadastro da Filial.

Parâmetros ECF - Rendimentos

Assim como o campo "**Classificação do País**", na aba Identificação, deve ser informado.

Parâmetros ECF - Classificação de PaísEstrutura do registrov112025

Layout do Registro Após o ano de 2025 - Layout 0011

| Nº | CAMPO | DESCRIÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "X450" | Valor Fixo |
| 02 | PAIS | Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e no programa da ECF no diretório Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas). | País conforme parametrização da Classificação do País nos parâmetros da ECF |

2024

Layout de Registro antes do Ano 2024 - Layout 0010

| Nº | CAMPO | DESCRIÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "X450" |  |
| 02 | PAIS | Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e no programa da ECF no diretório Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas). | País conforme parametrização da Classificação do País nos parâmetros da ECF |
| 03 | VL\_SERV\_ASSIST | Valor dos Serviços de Assistência Técnica, Científica, Administrativa e Assemelhados com Transferência de Tecnologia: Pagamentos ou as remessas efetuados a título de serviços de assistência técnica, científica, administrativa e assemelhados referentes aos contratos que, em conformidade com a Lei nº 9.279, de 14 maio de 1996 | Valor Baixado conforme Classificação do Pagamento ou Recebimento |
| 04 | VL\_SERV\_SEM\_ASSIST | Valor dos Serviços Técnicos e de Assistência sem Transferência de Tecnologia Prestados no Brasil: Valores pagos a título de serviços técnicos e de assistência, prestados no Brasil, referentes aos contratos dispensados de averbação no Instituto Nacional de Propriedade Industrial (INPI) por não constituírem transferência de tecnologia, | Valor Baixado conforme Classificação do Pagamento ou Recebimento |
| 05 | VL\_SERV\_SEM\_ASSIST\_EXT | Valor dos Serviços Técnicos e de Assistência sem Transferência de Tecnologia Prestados no Exterior: Valores pagos a título de serviços técnicos e de assistência, prestados no Brasil, referentes aos contratos dispensados de averbação no Instituto Nacional de Propriedade Industrial (INPI) por não constituírem transferência de tecnologia | Valor Baixado conforme Classificação do Pagamento ou Recebimento |
| 06 | VL\_JURO\_PF | Valor dos Juros sobre o Capital Próprio Pagos a Pessoa Física: Valor pago ou remetido à pessoa física residente ou domiciliada no Brasil ou no exterior a título de remuneração dos recursos investidos na pessoa jurídica declarante, de que trata o art. 9º da Lei nº 9.249, de 26 de dezembro de 1995. | Valor Baixado conforme Classificação do Pagamento ou Recebimento |
| 07 | VL\_JURO\_PJ | Valor dos Juros sobre o Capital Próprio Pagos a Pessoa Jurídica: Valor pago ou remetido pela pessoa jurídica a outra pessoa jurídica domiciliada no Brasil ou no exterior a título de remuneração dos recursos investidos na pessoa jurídica declarante, de que trata o art. 9º da Lei nº 9.249, de 26 de dezembro de 1995 | Valor Baixado conforme Classificação do Pagamento ou Recebimento |
| 08 | VL\_DEMAIS\_JUROS | Valor dos Demais Juros: Valor pago ou remetido a título de juros decorrentes da remuneração de empréstimos tomados pela pessoa jurídica no Brasil ou no exterior por meio de contratos de financiamento e de mútuo registrados ou não no Banco Central do Brasil. | Valor Baixado conforme Classificação do Pagamento ou Recebimento |
| 09 | VL\_DIVID\_PF | Dividendos Pagos a Pessoa Física: Valor dos lucros ou dividendos pagos ou remetidos pela pessoa jurídica à pessoa física residente ou domiciliada no Brasil ou no exterior em decorrência de participação societária avaliada pelo método da equivalência patrimonial ou pelo custo de aquisição. | Valor Baixado conforme Classificação do Pagamento ou Recebimento |
| 10 | VL\_DIVID\_PJ | Dividendos Pagos a Pessoa Jurídica: Valor dos lucros ou dividendos pagos ou remetidos pela pessoa jurídica a outra pessoa jurídica domiciliada no Brasil ou no exterior em decorrência de participação societária avaliada pelo método da equivalência patrimonial ou pelo custo de aquisição. | Valor Baixado conforme Classificação do Pagamento ou Recebimento |

X451X451

**REGISTRO X451: PAGAMENTOS OU REMESSAS A TÍTULO DE SERVIÇOS, JUROS E DIVIDENDOS A BENEFICIÁRIOS DO BRASIL E DO EXTERIOR – DEMAIS**  
**INFORMAÇÕES**

Este Registro é filho do X450 e considera as mesmas consistências para ser gerado.

Este registro será gerado depois do ano de 2024, à partir da versão 11 do layout da ECF.

| Nº | CAMPO | DESCRIÇÃO | ORIGEM DA INFORMAÇÃO |
| --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "X451" | Valor Fixo |
| 02 | Código | Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e no programa da ECF no diretório Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas). | Gerado Conforme o Código da Tabela Dinâmica - X451, de acordo com opção selecionada na Classificação de Pagamento ou Recebimento do lançamento financeiro |
| 03 | Descrição | Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e no programa da ECF no diretório Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas). | Gerado Conforme o Código da Tabela Dinâmica - X451 , de acordo com opção selecionada na Classificação de Pagamento ou Recebimento do lançamento financeiro. |
| 04 | Valor | Valor |  |

São gerados os seguintes códigos e descrições nos campos 02 e 03:

**1.** Valor dos Serviços de Assistência Técnica, Científica, Administrativa e Assemelhados com Transferência de Tecnologia  
**2.** Valor dos Serviços Técnicos e de Assistência sem Transferência de Tecnologia Prestados no Brasil  
**3.** Valor dos Serviços Técnicos e de Assistência sem Transferência de Tecnologia Prestados no Exterior  
**4.** Valor dos Juros sobre o Capital Próprio Pagos a Pessoa Física- considera a opção 'Valor dos Juros sobre o Capital Próprio', cujo Cli/For do lançamento seja Pessoa Física.  
**5.** Valor dos Juros sobre o Capital Próprio Pagos a Pessoa Jurídica - considera a opção 'Valor dos Juros sobre o Capital Próprio', cujo Cli/For do lançamento seja Pessoa Jurídica.  
**6.** Valor dos Demais Juros   
**7.** Dividendos Pagos a Pessoa Física - considera a opção 'Dividendos', cujo Cli/For do lançamento seja Pessoa Física.  
**8.** Dividendos Pagos a Pessoa Jurídica - considera a opção 'Dividendos', cujo Cli/For do lançamento seja Pessoa Jurídica.

Observação:

Estes códigos **não são gerados**:

9. Despesas - Produtos e Serviços Brasileiros

10. Despesas - Promoção do Brasil no Exterior

11. Despesas - Comissões Pagas

12. Despesas - Cargas no exterior

13. Despesas - Cobertura de Risco de Variação

14. Despesas - Juros – Financiamento de Exportações

15. Despesas - Juros – Financiamento de Exportações

16. Despesas – Comissões – Financiamento de Exportações
