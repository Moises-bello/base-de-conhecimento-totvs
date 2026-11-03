---
content_hash: bf32902fb2c495ae471821799008b7d6f264875b27d33103988df797c624a954
fetched_at: '2026-06-29T00:09:22.051997+00:00'
page_id: '422545954'
product: rm
source: tdn-rm
title: Bloco 1 (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545954
version: 14
---

## Complemento da Escrituração — Controle de Saldos de Créditos e de Retenções, Operações Extemporâneas e Outras Informações

Neste bloco são escrituradas as informações dos controles de créditos do contribuinte, controle do saldo das retenções na fonte, as informações extemporâneas, bem como as contribuições devidas pela empresa da atividade imobiliária pelo RET.

1lefttrue1Registro 1001

**Registro 1001 — Abertura do bloco 1**  
Este registro informa se houve movimentação no bloco M.

2Registro 10114Registro 1101

**Registro 1101 — Apuração de Crédito Extemporâneo — Documentos e Operações de Períodos Anteriores – PIS/PASEP**

3Registro 1100

**Registro 1100 — Controle de Créditos Fiscais — PIS/PASEP**

5Registro 1300

**Registro 1300 — Controle dos Valores Retidos na Fonte — PIS/PASEP**

6Registro 1500

**Registro 1500 — Controle de Créditos Fiscais — COFINS**  
Estes registros são gerados com base nas informações dos créditos fiscais apurados no período da escrituração e em períodos anteriores.  
Os saldos existentes antes da implantação do processo da EFD devem ser incluídos manualmente. A partir da implantação os valores dos créditos normais  podem ser gerados pela execução do processo.  
O cadastro dos Créditos Fiscais pode ser acessado no menu Cadastros | Tabelas Auxiliares | Obrigações Federais | Apuração PIS/COFINS — Controle e Créditos Fiscais de Tributos.  
Informações detalhadas a respeito da geração destas informações em: Controle de Créditos Fiscais.

7Registro 1501

**Registro 1501 — Apuração de Crédito Extemporâneo — Documentos e Operações de Períodos Anteriores — COFINS**  
Estes registros são gerados com base nas informações dos créditos fiscais extemporâneos apurados em períodos anteriores.  
Os saldos existentes antes da implantação do processo da EFD devem ser incluídos manualmente. A partir da implantação os valores dos créditos extemporâneos  podem ser gerados pela execução do processo.  
O cadastro dos Créditos Fiscais pode ser acessado no menu Cadastros | Tabelas Auxiliares | Obrigações Federais | Apuração PIS/COFINS — Controle e Créditos Fiscais de Tributos.   
Informações detalhadas a respeito da geração destas informações em: Controle de Créditos Fiscais.

8Registro 1700

**Registro 1700 — Controle dos Valores Retidos na Fonte — COFINS**  
Estes registros são gerados com base nas retenções feitas nos lançamentos financeiros a receber que foram baixados no TOTVS Gestão Financeira no período da escrituração e as compensações feitas com estas retenções. Informações detalhadas a respeito da geração destas informações em: Controle de Créditos Fiscais

99Registro 1800

**REGISTRO 1800: INCORPORAÇÃO IMOBILIÁRIA – RET**

Este registro deve ser preenchido pela pessoa jurídica que executa empreendimentos objeto de incorporação imobiliária e que apuram contribuição social com base em Regimes Especiais de Tributação – RET.

Devem ser escriturados registros específicos para cada incorporação imobiliária, bem para cada Regime Especial estabelecido na legislação tributária, sujeitos ao pagamento mensal unificado a alíquotas diversas.

A receita da incorporação sujeita a tributação pelo RET não deve ser computada nos demais registros da escrituração, relativos a suas outras atividades empresariais, inclusive incorporações não optantes pelo RET.

**Regras**

* No cadastro da Filial marque a opção **“Apura pelo Regime Especial de Tributação”**, acesse o menu | Cadastros | Filial | Selecione a Filial | Anexos | Dados Fiscais | Aba Tributos;
* Período de Apuração do Tributo RET, esse Período de Apuração será fonte para geração dos **campos 07 e 08 do Registro** e deverá estar encerrado. Caso tenha valor apurado é necessário a guia gerada.
* É consistido para o período que exista informações de incorporações imobiliárias, ou seja, será emitido erro caso exista período encerrado para o tributo e não exista informações de incorporações.
* As guias para pagamento do RET devem ser inseridas na Gestão Fiscal e integradas com o sistema Financeiro quando houver integração. Isso é necessário para a geração do campo 08.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Origem dos Dados** |
| 01 | REG | Texto fixo contendo "1800" | Fixo 1800 |
| 02 | INC\_IMOB | Empreendimento objeto de Incorporação Imobiliária, optante pelo RET. |  |
| 03 | REC\_RECEB\_RET | Receitas recebidas pela incorporadora na venda das unidades imobiliárias que compõem a incorporação. | Gerado conforme informações fornecidas pelo Módulo Totvs Incorporação através de serviço. |
| 04 | REC\_FIN\_RET | Receitas Financeiras e Variações Monetárias decorrentes das vendas submetidas ao RET. | Gerado conforme informações fornecidas pelo Módulo Totvs Incorporação através de serviço. |
| 05 | BC\_RET | Base de Cálculo do Recolhimento Unificado | Calculado **REC\_RECEB\_RET** + **REC\_FIN\_RET** |
| 06 | ALIQ\_RET | Alíquota do Recolhimento Unificado. | Alíquota informada no Cadastro do Tributo do tipo RET |
| 07 | VL\_REC\_UNI | Valor do Recolhimento Unificado. | Receberá o Valor Principal da guia DARF para o Tributo do Tipo RET  Informado no Período de Apuração – Guia Darf |
| 08 | DT\_REC\_UNI | Data do recolhimento unificado | Se a Coligada tiver integração com o sistema Financeiro, rastrear a Data de Baixa da Guia. Se não, receber a Data de Vencimento do Período de Apuração. |
| 09 | COD\_REC | Código da Receita | Receberá o Código de Receita informado no Cadastro do Tributo |

9Registro 1900false

**Informações gerais:**

Registro 1900: Consolidação dos Documentos Emitidos no Período por Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido–Regime de Caixa ou de Competência

Registro para a pessoa jurídica sujeita à tributação com base no lucro presumido, que procedeu à escrituração de suas receitas de forma consolidada, pelo regime de caixa (registro “F500” ou “F510”) ou de competência (registro “F550” ou “F560”).

Observações sobre a geração do registro

* é gerado de forma agrupada considerando CFOP e CST (a partir do layout com data de 30/11/2021, disponível no [TOTVS Compartilhamento](https://tdn.totvs.com/pages/viewpage.action?pageId=348297816));
2true1Regime de caixa ou de competência

**Registro 1900 — Consolidação dos documentos emitidos no período por pessoa jurídica submetida ao regime de tributação com base no lucro presumido — Regime de caixa ou de competência**  
Neste registros serão informadas, por estabelecimento, os valores totais consolidados representativos das receitas emitidas, de acordo com cada modelo/tipo de documento, de natureza fiscal (notas fiscais) ou não (contratos, recibos, etc.) independente de sua realização (recebimento) ou não.  
Serão selecionados todos os [Lançamentos Financeiros](http://tdn.totvs.com.br/pages/viewpage.action?pageId=435104976) a receber emitidos no mês informado na tela de geração da rotina (baixados ou não) e que estejam associados ao processo criado para a geração do F500. Não serão selecionados lançamentos cancelados.

21900 Gerado com base nos movimentos 

**1900 Gerado com base nos movimentos de Pedido/Medição do TOTVS Gestão de Estoque, Compras e Faturamento**  
É necessário que o cliente/fornecedor das movimentações seja órgão público. Nos parâmetros do tipo de movimento de Pedido, etapa 54 — Financeiro — Faturamento do TOTVS Gestão de Estoque, Faturamento e Compras deve ser habilitada a opção "Fatura o Movimento" e também seleciono um "Tipo de Documento Duplicata Default". No momento da geração da rotina deve ser preenchido o campo "Tipo de Movimento (Pedido/Medição) a ser considerado registro 1900.

***Observação**:* O Tipo de Movimento informado deve estar no formato 2.1.XX e caso haja mais de um Tipo de Movimento que ser considerado, deve ser separados por ponto e vírgula, exemplo: 2.1.XX;2.2.XX.  
O pedido/medição gravado no registro 1900, conforme processo descrito acima, será faturado dando origem a outro movimento. A venda gerada e integrada ao TOTVS gestão Financeira, será informado na rotina EFD Contribuições no registro F500 e para isto o lançamento financeiro deve estar parametrizado pelo tipo de documento na parametrização normal (opções ⇒ parâmetros ⇒ processos) Regime de Caixa no TOTVS Gestão Fiscal.
