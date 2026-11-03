---
content_hash: 20db31bd8a17fb96ba0201df790166cc937eb0ffbf79d10a3479544d5515b3c9
fetched_at: '2026-06-29T00:09:21.987844+00:00'
page_id: '422545938'
product: rm
source: tdn-rm
title: Bloco 0 - Abertura e Identificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545938
version: 34
---

Este Bloco é composto pelos registros:

.BLOCO0left00000000

**Abertura do Arquivo Digital e Identificação da Pessoa Jurídica**

Este registros é gerado com base nas informações gravadas no anexo [Parâmetros da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=422545950) | Tributação do cadastro de Filiais.

Registro de abertura 0000 - em 2026

* Campo 3:**COD\_VER** - (Código da versão do leiaute) de acordo com o layout 12, Para o ano-calendário 2025 e situações especiais de 2026, o leiaute a ser informado deverá ser = 0012.
* Campo 6:**IND\_SIT\_INI\_PER** - Indicador do Início do Período - foi incluída uma nova opção para este registro:
  + 7 - Retorno às atividades de empresas inativas.
00010001

**Abertura do Bloco 0**

Este é um registro de controle gerado automaticamente pelo processo da rotina que informa se existe ou não movimentação no bloco 0.

00100010

**Parâmetros de Tributação**

Este registro é gerado com base nas informações gravadas no anexo [Parâmetros da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=422545950) | Tributação do cadastro de Filiais. A informação da Forma de Apuração é carregada com base nos períodos de apuração criados para os tributos CSLL e IRPJ incluídos para as filiais. A informação da Forma de Tributação é carregada com base nos eventos tributários incluídos para estes mesmos Tributos. Portando deve-se dar uma atenção especial a estes dois cadastros para que não sejam apresentados erros na validação do arquivo texto da rotina.

Campo 008 - Forma de Tributação no Período (FORMA\_TRIB\_PER)

**Se** o campo referente ao **tipo de Entidade Imune ou Isenta** estiver com a opção **diferente** de **Não se aplica**

Então será gerado em Branco

Senão

**Se** o período de apuração (IRPJ) for **Trimestral**

* Forma de Tributação **Lucro Arbitrado**: "A";
* Forma de Tributação **Lucro Presumido**: "P";
* Forma de Tributação **Lucro Real**: "R".

Senão

**Se** o período de apuração for **Anual** e for encontrado algum período de apuração (IRPJ) Trimestral

Então Será preenchido com "R"

Senão

Será preenchido com "0"

Quando não for encontrado um período de apuração para o trimestre será considerado "0" conforme regras da ECF.

00200020

**Parâmetros Complementares**

Este registro é gerado com base nas informações gravadas no anexo [Parâmetros da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=422545950) | Complementares do cadastro de Filiais.

A partir da versão 010 - (2024) a opção abaixo será gerada com valor Fixo "N"

* Campo 31 - IND\_PR\_TRANSF: Passa a ser gerado de forma Fixa com o Valor **N**

A partir do layout da versão 012 os campos passam a gerar conforme regra abaixo:

* Campo 31: POSSUI\_CEBAS-(Entidades isentas e imunes que possuem CEBAS – Certificado de Entidade Beneficente de Assistência Social)
  + Entidades nas áreas de assistência social, saúde ou educação que atendam aos requisitos de possuírem CEBAS e o possuem, devem indicar SIM neste campo.
* Campo 32: CEBAS- Número CEBAS que a entidade possui.  
    
  Regras:  

  O campo 31 só vai ser gerado com S se o código CEBAS estiver preenchido.
00210021

**Parâmetros Complementares**

Este registro é gerado com base nas informações gravadas no anexo [Parâmetros da ECF](http://tdn.totvs.com/pages/viewpage.action?pageId=422545950) | Mais Informações do cadastro de Filiais.

Os campos que não possuem valor fixo "N", são gerados conforme a opção marcada em:  
*Módulo Fiscal → Cadastros → Filiais → Anexos → Parâmetros da ECF - Escrituração Contábil Fiscal → Aba: Mais Informações*

ExemplocardsLayout 009

A partir da versão 009 - (2023) as opções abaixo serão geradas com valor Fixo "N":

* Campo 5 - IND\_PATVD: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 7 - IND\_REPENEC: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 8 - IND\_REICOMP: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 9 - IND\_RETAERO: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 11 - IND\_RESIDUOS\_SOLIDOS: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 12 - IND\_RECOPA: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 13 - IND\_COPA\_DO\_MUNDO: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 15 - IND\_REPNBL\_REDES: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 16 - IND\_REIF: Passa a ser gerado de forma Fixa com o Valor **N**
Layout 010

A partir da versão 010 - (2024) as opções abaixo serão geradas com valor Fixo "N":

* Campo 8 - IND\_OLEO\_BUNKER: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 9 - IND\_REPORTO: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 10 - IND\_RET\_II: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 11 - IND\_RET\_PMCMV: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 12 - IND\_RET\_EEI: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 13 - IND\_EBAS: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 14 - IND\_REPETRO\_INDUSTRIALIZACAO: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 15 - IND\_REPETRO\_NACIONAL: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 16 - IND\_REPETRO\_PERMANENTE: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 17 - IND\_REPETRO\_TEMPORARIO: Passa a ser gerado de forma Fixa com o Valor **N**
Layout 012

A partir da versão 012 - (2026) as opções abaixo serão geradas com valor Fixo "N":

* Campo 8 - IND\_OLEO\_BUNKER: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 9 - IND\_REPORTO: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 10 - IND\_RET\_II: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 11 - IND\_RET\_PMCMV: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 12 - IND\_RET\_EEI: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 13 - IND\_EBAS: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 14 - IND\_REPETRO\_INDUSTRIALIZACAO: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 15 - IND\_REPETRO\_NACIONAL: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 16 - IND\_REPETRO\_PERMANENTE: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 17 - IND\_REPETRO\_TEMPORARIO: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 18 - IND\_REDATA: Passa a ser gerado de forma Fixa com o Valor **N**

⚠️Para versões anteriores o comportamento seguirá com e geração normal, campo gerado conforme cada opção marcada.

00300030

**Dados Cadastrais**

Este registro é gerado com base nas informações do cadastro da Filial Matriz dos estabelecimentos ou da Filial SCP quando a declaração pertencer a uma Filial do tipo SCP.

00350035

**Identificação das SCP**

Neste registro será gerada uma linha para cada filial do tipo SCP que existir no cadastro de Filais na Coligada corrente.

09300930

**Identificação dos Signatários da ECF**

Para que este registro seja corretamente gerado as informações do anexo da filial -  **Dados Fiscais | Contador** e **Dados Fiscais |  Representante** deverão estar rigorosamente preenchidos. Estes dados são obrigatórios para a validação do arquivo no PVA da ECF.  
  
Se necessário é possível usar os dados da Filial no lugar dos dados do Representante, nos parâmetros da ECF da filial pasta "Complementares" deve ser marcada a opção "Segunda Assinatura - Própria Empresa" e preenchido o "Código de Qualificação do Assinante" desejado.

09900990

**Encerramento do Bloco 0**

Este é um registro de controle gerado automaticamente pelo processo da rotina.
