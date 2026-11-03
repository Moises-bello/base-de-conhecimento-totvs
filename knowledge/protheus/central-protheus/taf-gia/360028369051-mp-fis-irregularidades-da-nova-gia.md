---
article_id: 360028369051
category: TAF - GIA
content_hash: ba5428023abd3dce1c23e7ea075bf96502db4cd17351820ac63e29dfe4ad5b65
fetched_at: '2026-06-28T22:41:32.402988+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: MP - FIS - Irregularidades da Nova GIA
type: support-article
updated_at: '2021-04-28T15:22:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028369051-MP-FIS-Irregularidades-da-Nova-GIA
---

**Dúvida**Principais Irregularidades Nova GIA  
  
 **Ambiente**  
Protheus – TAF – A partir da versão 11.80  
  
**Solução**

**Tabela 02 - CR=05**

Na validação do arquivo Nova GIA ocorre o alerta CR=05 - linha 02

Para correção é necessário informar na geração do arquivo : Versão do sistema 0801 e Versão do layout 0210

**Tabela 03 - CR=10**

Na validação do arquivo Nova GIA ocorre o alerta CR=10 - Imposto Inconsistente.

Para correção é necessário verificar a escrituração da nota.

Na validação do arquivo Nova GIA ocorre o alerta Tabela 03 X Tabela 04

Os parâmetros MV\_STUF e MV\_STUFS devem conter todas as UF's com movimentação de entrada/saída para outros Estados, independente se possui IE ou não.

Observar no cadastro de TES o preenchimento do campo:

F4\_CREDST = 2 (quando possui IE e MV\_SUBTRIB preenchido)

F4\_CREDST = 4 (quando não possui IE)

Importante: Para correta geração do SPED FISCAL, informar no parâmetro MV\_STNIEUF as UF's onde possui inscrição estadual.

Para divergência de valores no campo Outros Impostos, consultar o Boletim Nova GIA – Guia de Informação e Apuração do ICMS-SP - P11  
  
**Tabela 06 - CR=20**

Na validação do arquivo Nova GIA ocorre o alerta Tabela 06 - CR=20 Campo - CodSubitem Inconsistente, quando não é informado o código de subitem (segundo campo) na Apuração de ICMS ou foi informado código incorreto, de acordo com a Tabela 13 do Layout da Nova GIA.

Para correção do problema é necessário que seja refeita a Apuração do ICMS e que seja informado os códigos corretos.  
Link para verificação do layout e tabela da GIA:  
http://www.fazenda.sp.gov.br/download/gia0700/pre\_formatado\_ngia\_v0210.pdf

Diferenças entre layout de Apuração de ICMS e layout da Nova GIA  
O layout da Nova GIA não contem as linhas 004 e 009, devido a isso, o sequencial de linhas não confere com o layout da apuração de ICMS.  
Ao incluir a linha 006 na apuração (Outros Créditos) deve ser informado o código 007.XX correspondente a tabela 13 da Nova GIA, pois refere-se a Outros Créditos onde também pode incluir a linha 007 (Estorno de Débitos) que deve trazer o código 008.XX.  
  
**Tabela 07 - CR=25**

Na validação do arquivo Nova GIA ocorre o alerta Tabela 07 - CR=25 quando foi utilizado um código de subitem na apuração de ICMS (00218, 00219, 00704, 00705, 00706, 00707, 00729 ou 00730) que exige a geração do registro CR=25 contendo inscrição estadual e valor da operação. Porém não existe nota fiscal de transferência de Crédito / Débito de ICMS.  
É necessário gerar a nota fiscal de transferência de ICMS e informar o valor na apuração de ICMS. Verificar o valor na aba informações complementares nas linhas 021/022 - transf. crédito/débito.

Configuração de TES - Nota de transferência de ICMS

Credita ICMS (F4\_CREDICM) = Não

Calcula ICMS (F4\_ICM) = Não

Cod. Fiscal (F4\_CF) = Informar CFOP de transferência

L.Fisc. ICMS (F4\_LFICM) = ICMS Zerado

Agrega Valor (F4\_AGREG) = Não

Txt Padrão (F4\_TEXTO) = Transferência

TRF. Deb/Crd (F4\_TRFICM) = SIM

Fórmula (F4\_FORMULA) = Criar uma fórmula: “Transferência de saldo (credor/devedor) conforme art. 98 do RICMS” (utilizar aspas duplas)

**Lançamento da Nota / Apuração**  
Produto = Criar um produto “Transferência de Saldo de ICMS”

Quantidade = 1

Valor unitário e valor total = Valor do ICMS

TES = Informar a TES de transferência

Acessar a rotina de Apuração do ICMS e incluir manualmente em "Outros Créditos" ou “Outros Débitos” o valor do ICMS Transferido.

**Tabela 08 - CR=30**

Na validação do arquivo Nova GIA ocorre o alerta Tabela 08 - CR=30, quando não é informado o código de município aceito pelo validador da nova GIA.

Para gerar corretamente as informações referentes à DIPAM-B, informe no Cadastro de Fornecedor/ Cliente, o código do Município de acordo com a tabela 15

da Nova GIA, nos campos:   
A1\_NOVAGIA: Indicado no parâmetro MV\_CODMUN

A2\_NOVAGIA: Indicado no parâmetro MV\_MUNA2

Informar no parâmetro MV\_CODDP o do código Município que está localizada a empresa.

**Utilização de SIGATMS e Coleta**  
O sistema buscará o código do Município dos campos: DUE\_GIASP ou DUL\_GIASP

**Tabela 18 - CR=31**

Na validação do arquivo Nova GIA ocorre o alerta Tabela 18 - CR=31, quando não é informado o número do registro de exportação.

Para gerar corretamente as informações, configurar o parâmetro MV\_RE e informar no campo D2\_RE o número do registro de exportação.

Para o preenchimento do campo D2\_RE, seguem sugestões de Ponto de Entrada: M468SD2, MTA920IT, MSD2460, MT920IT

Utilização de SIGAEEC  
É necessário o preenchimento do campo EEC\_DTEMBA com a data de embarque. A data informada neste campo será considerada para a geração do arquivo.

O sistema buscará o registro de exportação do campo E9\_RE
