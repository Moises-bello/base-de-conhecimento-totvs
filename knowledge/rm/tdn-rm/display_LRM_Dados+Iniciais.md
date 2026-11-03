---
content_hash: f679077c60016ced060c8ae278539bd0829952e48a3dd287d37c89ba0ae1a583
fetched_at: '2026-06-29T00:12:03.184176+00:00'
page_id: '904593565'
product: rm
source: tdn-rm
title: Dados Iniciais
type: documentation
url: https://tdn.totvs.com/display/LRM/Dados+Iniciais
version: 46
---

LayoutCampos

Os **"Dados Iniciais da Apuração"** no layout do **MIT (Módulo de Inclusão de Tributos)** referem-se às informações fundamentais para a geração do **MIT**. Esses dados são estruturados no formato JSON e incluem detalhes básicos sobre a empresa, sua tributação e o responsável pela apuração.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Campo** | **Nivel** | **Tipo** | **Obrigatório** | **Descrição** | **Origem dos Dados** | **Observações** |
| **DadosIniciais** | 1 | **Object** | **Sim** | **Dados iniciais da apuração.** |  |  |
| SemMovimento | 2 | Boolean | Sim | Indicador de apuração sem movimento, sendo:     **false**: Não;     **true**: Sim. | Gerado automaticamente pelo sistema. Caso exista alguma suspenção e débito sistema preenche com true, caso não exista sistema preenche com false. |  |
| QualificacaoPj | 2 | Number | Sim | Qualificação da pessoa jurídica, sendo:     **1**: PJ em geral;     **2**: Agência de Fomento, Banco ou outra PJ de que trata o § 1° do art. 22 da Lei n° 8.212/1991;     **3**: Cooperativa de Crédito;     **4**: Sociedade Corretora de Seguros;     **5**: Sociedade Seguradora e de Capitalização ou Entidade Aberta de Previdência Complementar com fins lucrativos;     **6**: Entidade Fechada de Previdência Complementar ou Entidade Aberta     de Previdência Complementar sem fins lucrativos;     **7**: Sociedade Cooperativa;     **8**: Sociedade Cooperativa de Produção Agropecuária ou de Consumo;     **9**: Autarquia ou Fundação Pública;     **10**: Empresa Pública, Sociedade de Economia Mista ou PJ de que trata o inc. III do art. 34 da Lei n° 10.833/2003;     **11**: Estado, Distrito Federal, Município ou Órgão Público da Administração Direta;     **12**: Mais de uma qualificação durante o mês. | Gerado conforme o campo informado na Tela de Geração da Rotina |  |
| TributacaoLucro | 2 | Number | Sim | Forma de tributação do lucro, sendo:     **1**: Real Anual;     **2**: Real Trimestral;     **3**: Presumido;     **4**: Arbitrado;     **5**: Imune do IRPJ;     **6**: Isenta do IRPJ;     **7**: Optante pelo Simples Nacional. | Gerado conforme o campo informado na Tela de Geração da Rotina | Deve ser informado se o campo SemMovimento for “false” e se campo QualificacaoPj for diferente de 11. |
| VariacoesMonetarias | 2 | Number | Sim | Critério de reconhecimento das variações monetárias, sendo:     **1**: Regime de Caixa;     **2**: Regime de Competência;     **3**: Regime de Caixa - Elevada oscilação da taxa de câmbio. | Gerado conforme o campo informado na Tela de Geração da Rotina | Deve ser informado se campo SemMovimento for “false”. |
| RegimePisCofins | 2 | Number | Sim | Regime de apuração do PIS/Pasep e/ou da Cofins, sendo:     **1**: Não cumulativa;     **2**: Cumulativa;     **3**: Não cumulativa e Cumulativa;     **4**: Não se aplica. | Gerado conforme o campo informado na Tela de Geração da Rotina | Deve ser informado os campos:  se SemMovimento for "false" e  se QualificacaoPj for [9],  se QualificacaoPj for [4, 8 ou 10] e  se TributacaoLucro for [1, 2 ou 6], ou  se QualificacaoPj for [1 ou 12] e  se TributacaoLucro for [1, 2, 5 ou 6]. |
| **ResponsavelApuracao** | **2** | **Object** | **Sim** | **Dados do responsável pelo preenchimento da apuração.** | **Gerado conforme o Cadastro da Filial – Anexo Dados Fiscais – Sub Pasta Contador** |  |
| CpfResponsavel | 3 | String (11) | Sim. | CPF do responsável | Cadastro da Filial – Anexo Dados Fiscais – Sub Pasta Contador – Campo CPF - "DFILIAL.CPFCONTADOR" | Preencher com 11 dígitos.  Exemplo: "12345678900". |
| **TelResponsavel** | **3** | **Object** | **Não** | **Dados do telefone/celular do responsável.** | **Cadastro da Filial – Anexo Dados Fiscais – Sub Pasta Contador – Campo Telefone** |  |
| Ddd | 4 | String (2) | Sim | DDD do telefone/celular do responsável | Cadastro da Filial – Anexo Dados Fiscais – Sub Pasta Contador – Campo DDD - "DFILIAL.DDDCONTADOR" | Preencher Código DDD com 2 dígitos. Exemplo: “31”. |
| NumTelefone | 4 | String (9) | Sim | Número do telefone/celular do responsável | Cadastro da Filial – Anexo Dados Fiscais – Sub Pasta Contador – Campo Número do Telefone - "DFILIAL.TELCONTADOR" | Preencher Número com 8 ou 9 dígitos. Exemplo: “999999999”. |
| EmailResponsavel | 3 | String (60) | Não | E-mail do responsável | Cadastro da Filial – Anexo Dados Fiscais – Sub Pasta Contador – Campo e-Mail - "DFILIAL.EMAILCONTADOR" |  |
| **RegistroCrc** | **3** | **Object** | **Não** | **Dados do registro profissional do responsável no Conselho Regional de Contabilidade.** | **Cadastro da Filial – Anexo Dados Fiscais – Sub Pasta Contador – Campo Registro CRC** |  |
| UfRegistro | 4 | String (2) | Sim | Sigla da UF do registro profissional | Cadastro da Filial – Anexo Dados Fiscais – Sub Pasta Contador – UF do Código CRC - "DFILIAL.UFCRCCONTADOR" | Sigla do registro provisório ou definitivo originário do responsável, com letras maiúsculas. Exemplo: “MG”. |
| NumRegistro | 4 | String (11) | Sim | Número do registro profissional do responsável. | Cadastro da Filial – Anexo Dados Fiscais – Sub Pasta Contador – Número do registro - "DFILIAL.CRCCONTADOR" | Pode ser incluído sufixo no caso de registro transferido ou secundário, com tamanho de 6 a 11 dígitos. Exemplos: “123456”, “SP123456”, “123456O3”, “123456TMG”, “SP123456O3” e “123456O3TMG”. |

Exemplo

O elemento **SemMovimento** (booleano) indica se a apuração possui ou não movimentação.

* **true**: Sem movimento.
* **false**: Com movimento.

ExemploApuração Sem movimento

É a declaração que deve ser enviada quando não houver fatos geradores a declarar no período de apuração.

jstrueApuração Com movimentação

É a declaração onde a empresa informa os débitos e suspensões apurados no período.

jstrue
