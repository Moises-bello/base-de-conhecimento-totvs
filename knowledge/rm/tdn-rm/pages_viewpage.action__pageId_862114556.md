---
content_hash: f628f3df56f14a7a9d40929548da7e81219ac39c7a3394fd14a2107607399948
fetched_at: '2026-06-29T00:11:55.550045+00:00'
page_id: '862114556'
product: rm
source: tdn-rm
title: Leiaute S-1.3 e Nota Técnica 01/2024
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862114556
version: 92
---

false

**A partir das Releases:**

# Objetivo:

Adequamos o TOTVS Folha de Pagamento para atender à **nova versão S-1.3 do eSocial**, conforme publicado na [Portaria Conjunta RFB/MPS/MTE nº 13, de 25/06/2024](https://www.totvs.com/blog/fiscal-clientes/esocial-normativo-sobre-o-leiautes-s-1-3/). Essa atualização é crucial, pois conclui os ajustes necessários para a substituição da DIRF. Além disso, o Manual de Orientação do eSocial – MOS foi atualizado para a versão S-1.3.

Adicionalmente, no dia 04/09/2024, foi publicada no portal do eSocial a Nota Técnica S-1.3 nº 01/2024, que traz as alterações necessárias para essa versão do leiaute. Mais informações estão disponíveis [aqui](https://www.totvs.com/blog/fiscal-clientes/esocial-ajuste-no-leiaute-versao-1-3/).

**Cronograma de Implantação ambiente eSocial:**

* + **Ambiente de produção restrita:** 07/10/2024
  + **Ambiente de produção:** 02/12/2024

ATENÇÃO!

O período de convivência entre os leiautes **S-1.2** e **S-1.3** será de **02/12/2024 a 02/02/2025**. Entretanto, é importante destacar que, a partir do **período de apuração 01/2025**, os eventos **S-1210 (S-5002)** e **S-2501** deverão ser enviados **exclusivamente** na versão **S-1.3**, conforme informado no [link](https://www.gov.br/esocial/pt-br/noticias/publicacao-da-versao-s-1-3-dos-leiautes-do-esocial-e-da-nota-tecnica-no-04-2024-revisada).

É de **extrema importância** que os clientes **realizem a migração com antecedência**, evitando problemas de última hora e garantindo uma transição tranquila. 

Exemplo Pagamento de Folha

**REGIME COMPETÊNCIA**

ENVELOPE                     PAGAMENTO              EVENTOS                                                    PRAZO ENVIO       LEIAUTE

12/2024                          30/12/2024                **S-1200** / **S-1210** *(perApur 2024-12)*         15/01/2025            S-1.2 ou S-1.3

01/2025                          30/01/2025                **S-1200** / **S-1210** *(**perApur 2025-01**)*        15/02/2025            **S-1.3**  
  
  
**REGIME CAIXA**

ENVELOPE                     PAGAMENTO              EVENTOS                                                    PRAZO ENVIO       LEIAUTE

11/2024                          05/12/2024                **S-1200** *(perApur 2024-11)*                         15/12/2024            S-1.2 ou S-1.3

11/2024                          05/12/2024                **S-1210** *(perApur 2025-12)*                         15/01/2025            S-1.2 ou S-1.3

12/2024                          05/01/2025                **S-1200** *(perApur 2024-12)*                         15/01/2025            S-1.2 ou S-1.3

12/2024                          05/01/2025                **S-1210** *(**perApur 2025-01**)*                       15/02/2025            **S-1.3**

01/2025                          05/02/2025                **S-1200** *(**perApur 2025-01**)*                        15/02/2025            **S-1.3**

01/2025                          05/02/2025                **S-1210** *(**perApur 2025-02**)*                       15/03/2025            **S-1.3**

Exemplo Pagamento de Rescisão

**PAGAMENTO RESCISÃO MESMO MÊS**

LANÇAMENTO              PAGAMENTO               EVENTOS                                                    PRAZO ENVIO                                   LEIAUTE

12/2024                          XX/12/2024                **S-2299/S-2399**                          10 dias a contar data do desligamento            S-1.2 ou S-1.3

12/2024                          XX/12/2024               **S-1210** *(perApur 2024-12)*                        15/01/2025                                        S-1.2 ou S-1.3

12/2024                          XX/01/2025                 **S-2299/S-2399**                          10 dias a contar data do desligamento            S-1.2 ou S-1.3

12/2024                          XX/01/2025                **S-1210** *(perApur 2025-01)*                          15/02/2025                                        S-1.3

01/2025                          XX/01/2025                **S-2299/S-2399** 10 dias a contar data do desligamento            S-1.2 ou S-1.3

01/2025                          XX/01/2025                **S-1210** *(perApur 2025-01)*                          15/02/2025                                        S-1.3 

Lembrete:

**S-1200** considera as verbas lançadas na **competência** relacionada ao período de apuração a ser gerado.   
**S-1210** considera as verbas cuja **data de pagamento** está compreendida dentro do período de apuração a ser gerado, independentemente da competência que se encontra.

---

11ParametrizaçãoParametrização

1) Criado o parâmetro da Nota Técnica (**S-1.3**) em Configurações | Parametrizador | Folha de Pagamento | eSocial | Configurações Gerais conforme demonstrado abaixo.

**ATENÇÃO**: A mudança para a versão do Leiaute **S-1.3 NT 01/2024** é **irreversível**, não sendo possível voltar para o leiaute **S-1.2 NT 04/2024** após alteração.

2) Após a liberação da versão será necessário executar os scripts de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

1Alterações Folha de PagamentoAlterações Folha de Pagamento

**Índice :**  
Objetivo:none

---

##### **1) Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF - incluídos os códigos:**

* 702 Bolsa médico residente - remuneração mensal.
* 703 Bolsa médico residente - 13º salário.
* 704 Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função.

##### **2) S-1000 - Alteração da descrição conforme abaixo:**

| De | Para |
| --- | --- |
| indTribFolhaPisCofins | indTribFolhaPisPasep |

##### **3) S-1010 - Criado novos campos para informar as incidências de PIS/PASEP no cadastro de eventos nas abas provento e desconto.**

Provento:

Desconto:

* Ao preencher este campo no cadastro de evento, será gerado gatilho do evento S-1010 e no XML a tag <codIncPisPasep> será de preenchimento obrigatório:

**ATENÇÃO**:

1. Só será gerado o tag <codIncPisPasep> quando o campo de "indicador de tributação sobre folha - PIS e PASEP" estiver marcado no cadastro do empregador.
2. Se o parâmetro não for preenchido no cadastro do evento, a *Tag* <*codIncPisPasep*> não será gerada no XML do S-1010. Conforme diretriz do leiaute do eSocial, quando a tag não é informada, o governo assumirá automaticamente o valor "***00 - Não é base de cálculo do PIS/PASEP***".

##### **4) S-1010 - Criado o novo grupo <ideProcessoPisPasep> para informar a suspensão da incidência de PIS/PASEP.**

Ao informar o código de incidência PIS/PASEP (91 ou 92) será necessário informar em Eventos | Anexos | Processo de Suspensão de incidência o tipo de tributo PIS/PASEP.

Caso não seja preenchido ao gerar o XML  será apresentado o log de erro abaixo:

   XML

##### **5)  Alterado a validação do campo {vlrDespAdvogados} nos eventos abaixo:**

* S-1200 - Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social
* S-1202 - Remuneração de Servidor vinculado ao Regime Próprio de Previd. Social
* S-1207 - Benefícios - Entes Públicos
* S-2299 - Desligamento
* S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término

| De | Para |
| --- | --- |
| Campo {vlrDespAdvogados}  Preencher com o valor total das despesas com advogado(s).  Validação: Permitir somente valores maiores que zero. | Campo {vlrDespAdvogados}  Preencher com o valor total das despesas com advogado(s). Validação: Se o grupo ideAdv for preenchido, o valor informado neste campo deve ser a soma do(s) campo(s) vlrAdv do grupo ideAdv. Deve ser maior ou igual a 0 (zero). O não preenchimento do grupo ideAdv indica que o contribuinte declarante não possui as informações detalhadas por advogado. |

##### **6) S-1210 - Criado o novo campo <vlrDedPC13> no grupo <previdCompl> para informar o valor de dedução do décimo terceiro relativa a previdência complementar.**

Para a impressão da tag <vlrDedPC13**>**, foi criado o campo **"Décimo Terceiro"** no menu eSocial | Previdência Complementar | Cadastro Previdência Complementar. Esse campo tem o objetivo de identificar os eventos relacionados ao décimo terceiro no cadastro, permitindo a correta vinculação dos dados da previdência complementar.

Para mais informações, acesse o link [Previdência Complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=791847949).

##### **7) S-1210 - Alterado validação e ocorrência do campo <vlrDedPC>, conforme abaixo:**

| De | Para |
| --- | --- |
| Campo{vlrDedPC}  Valor da dedução mensal relativa a previdência complementar. **Validação:** Deve ser maior que 0 (zero). | Campo{vlrDedPC}  Valor da dedução mensal relativa a previdência complementar  **Validação:** Preenchimento obrigatório se {vlrDedPC13} não for preenchido. Deve ser maior que 0 (zero). |

##### **8) S-1210 - Criado o novo grupo <infoProcRet> para informar processos relacionados a não retenção de tributos :**

Para gerar o grupo**<infoProcRet>** é necessário ir emEventos | Anexos | Processo de Suspensão de incidência e preencher o cadastro de processo conforme abaixo:

  XML S-1210:

##### **9)** **S-1210 - Alterada a validação do campo {vlrSaudeDep}****, conforme abaixo:**

| De | Para |
| --- | --- |
| Campo {vlrSaudeDep}  Valor relativo a dedução do rendimento tributável correspondente a pagamento a plano de saúde do dependente. **Validação:** Deve ser maior ou igual a 0 (zero). Se for igual a 0 (zero), deve haver informações de reembolso do dependente no grupo [infoReembDep](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3#1210_ideBenef_infoIRComplem_infoReembMed_infoReembDep). | Campo {vlrSaudeDep}  Valor relativo a dedução do rendimento tributável correspondente a pagamento a plano de saúde do dependente. **Validação:** Deve ser maior que 0 (zero). |

##### **10) S-1299  - Alteração na tag <naoValid> passando a aceitar valores "Sim" e "Não".**

| De | Para |
| --- | --- |
| Indicativo de não validação das regras de fechamento, para que os grandes contribuintes possam reduzir o tempo de processamento do evento. O preenchimento deste campo implica a não execução da REGRA\_VALIDA\_FECHAMENTO\_FOPAG. **Valores válidos:** **S** - Sim Validação: Não informar se procEmi for diferente de [1]. | Indicativo de não validação das regras de fechamento, para que os grandes contribuintes possam reduzir o tempo de processamento do evento. O não preenchimento deste campo ou seu preenchimento com [S] implica a não execução da REGRA\_VALIDA\_FECHAMENTO\_FOPAG. Para executá-la, informar [N]. **Valores válidos:** **S** - Sim **N** - Não |

 **XML:**

Parâmetro Marcado:

 Parâmetro Desmarcado:

##### **11) Empréstimo eConsignado**

##### **11.1 -** Criado grupo <descFolha> - informações sobre operação de crédito consignado com garantia de FGTS, nos eventos abaixo:

* S-1200 - Remuneração de Trabalhador vinculado ao Regime Geral de Previd. Social
* S-1202 - Remuneração de Servidor vinculado ao Regime Próprio de Previd. Social
* S-1207 - Benefícios - Entes Públicos
* S-2299 - Desligamento
* S-2399 - Trabalhador Sem Vínculo de Emprego/Estatutário - Término

O grupo será preenchido automaticamente sempre que o evento lançado e vinculado ao cadastro de empréstimo tiver a rubrica **9253 - Empréstimos ECONSIGNADO - Desconto**.

As informações necessárias serão extraídas diretamente do cadastro de empréstimos, acessível no menu: Administração de Pessoal | Funcionários | Anexos | Folha de Pagamento | Empréstimos.

**XML**

Mais informações acesse:

##### **11.2** Alteração no tamanho e validação do campo nrDoc no grupo <descFolha>

| De | Para |
| --- | --- |
| Campo nrDoc – Alterados tamanho e validação | Campo nrDoc – Alteração do tamanho e validação para permitir número de documentos com 8 algarismos. |

##### **11) Retificadora S-1210**

A partir de **Janeiro de 2026**, será possível incluir o grupo ***perAnt*** no evento **S-1210** (Pagamentos de Rendimentos do Trabalho) para realizar a retificação das Informações Complementares de IRRF referentes ao ano anterior. Esse novo recurso permitirá que o cliente faça ajustes retroativos de maneira mais eficiente, possibilitando retificações anuais a partir de janeiro de cada ano.

É importante destacar que, embora essa opção esteja disponível, o ideal é que os usuários **realizem as correções mensalmente**, evitando acúmulos de ajustes em Janeiro. A retificadora do S-1210 em Janeiro será apenas uma ferramenta adicional para garantir flexibilidade, devendo ser considerada como uma opção de **extrema exceção**.

A Folha de Pagamento está em processo de implementação desta funcionalidade. Sua liberação ocorrerá **ao longo do ano de 2025**, sendo **notificada no [TOTVS Informa](https://informa.totvs.com/rh/)**.

3Alterações Processo TrabalhistaAlterações Processo Trabalhista

Para verificar as mudanças do S-1.3 para os eventos de Processo Trabalhista, acesse a aba "**Como Funciona | Leiaute S-1.3**" da página abaixo:

* [Processo Trabalhista - Cadastros dos eventos S-2500 e S-2501](https://tdn.totvs.com/display/public/LRM/Processo+Trabalhista+-+Cadastros+dos+eventos+S-2500+e+S-2501)

*Veja também:*  
[DT - Processo Trabalhista - leiaute 1.3 - Banco de Dados - Evento S-2500](https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+Banco+de+Dados+-+Evento+S-2500)  
[DT - Processo Trabalhista - leiaute 1.3 - Banco de Dados - Evento S-2501](https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+Banco+de+Dados+-+Evento+S-2501)  
[DT - Processo Trabalhista - leiaute 1.3 - Banco de Dados - Evento S-2555](https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+Banco+de+Dados+-+Evento+S-2555)  
[DT - Processo Trabalhista - leiaute 1.3 - API - Evento S-2500](https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+API+-+Evento+S-2500)  
[DT - Processo Trabalhista - leiaute 1.3 - API - Evento S-2501](https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+API+-+Evento+S-2501)   
[DT - Processo Trabalhista - leiaute 1.3 - API - Evento S-2555](https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+API+-+Evento+S-2555)
