---
article_id: 360021559532
category: Financeiro - Contas a Pagar - Dirf
content_hash: fd00ffbcec358cf800bb21eedc6781ea55a239c62ae730e8898ac90146734aea
fetched_at: '2026-06-28T22:38:10.683421+00:00'
product: protheus
section_id: 1500001550482
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN  - FINA401 - Como gerar
  os dados do Financeiro para a DIRF
type: support-article
updated_at: '2026-02-20T11:06:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021559532-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA401-Como-gerar-os-dados-do-Financeiro-para-a-DIRF
---

**Dúvida**  
Como gerar DIRF no módulo Financeiro?  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – FINA401 -  Todas as versões  
  
**Solução**  
Pela rotina **Nota de Entrada**(MATA103).  
  
**Configurações:**   
Por meio do parâmetro **MV\_VISDIRF** é habilitada na aba **Impostos** da rotina **Documento de Entrada** (MATA103),   
a opção para gerar a DIRF e informar o código de retenção:  
- **MV\_VISDIRF** = 1 - Habilitado \*  
- **MV\_VISDIRF** = 2 (Default) - Desabilitado

No cadastro de Fornecedor o campo CGC/CPF (**A2\_CGC**) tem que estar preenchido com o CNPJ do Fornecedor.

1 - No **Lançamento da Nota** (MATA103) lançar as notas e informar as Opções:  
- Na aba **Duplicatas**:  
- Selecione a **Condição de Pagamento** e **Natureza**(com configuração da retenção);  
- Na aba **Impostos**:  
- Selecione => **Gerar DIRF**;  
- Insira o código respectivo da retenção (Ver com Setor Fiscal da Empresa)

2 - No módulo **Financeiro**, selecione **Miscelânea** -> **Arquivos** -> **Gerar Dados Para a DIRF** (FINA401)

**Parâmetro Importante:**  
- **Tipo de Fornecedor**:  
\* Gerar para Pessoa Física;  
\* Gerar para Pessoa Jurídica;

**Sugestão:**   
Se ambos as situações tiverem informações:   
Gerar o primeiro arquivo , Pessoa Física como "Sim", e o segundo  
para Pessoa Jurídica, como "Não"  
Se somente Pessoa Física ou Pessoa Jurídica apresentarem informações, selecione "Sim";   
  
A mensagem **Atenção**, informa que será gerado:  
- Selecione "Sim": Excluirá o conteúdo das tabelas e gerar outro arquivo do período;  
- Selecione "Não": Incluirá o novo conteúdo nas tabelas.

![Mensagem_Atencao.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360018566492)

Caso não seja emitido o relatório, verifique se há conteúdos (informações de impostos) nos títulos.  
  
Verifique o relatório que será gerado, o mesmo estará no diretório:  
- ...\system\dirf

**Tabelas envolvidas**:  
- **SRL** - DIRF / Informe de rendimentos;   
- **SR4** - Itens DIRF/Informe rendimentos

**Importante:**  
A DIRF é gerada pelo módulo **Gestão de Pessoal - GPE**, porém o módulo **Financeiro** possui informações pertinentes para as notas fiscais (Através da rotina **FINA401 - Gera dados para DIRF**), e estas são gravadas nas tabelas SR4 e SRL no módulo **GPE**, para compor o arquivo.

**Saiba mais:**

DIRF - [Geração de Dados para DIRF (FINA401)](https://tdn.totvs.com/pages/releaseview.action?pageId=224126168)

DIRF - Declaração do Imposto de Renda Retido na Fonte  
[DIRF - Declaração do Imposto de Renda Retido na Fonte | Protheus](http://tdn.totvs.com/pages/releaseview.action?pageId=329035626)

Perguntas sobre Geração de dados para DIRF  
[DIRF - Declaração do Imposto de Renda Retido](http://tdn.totvs.com/pages/releaseview.action?pageId=329035626)

Para efetuar uma DIRF Complementar, segue documentação de Repasse de Imposto de Renda Pessoa Jurídica  
[Repasse de Imposto de Renda Pessoa Jurídica](http://tdn.totvs.com/pages/releaseview.action?pageId=284861092)
