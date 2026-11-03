---
content_hash: 3a1c7b43bd66d3a37eeff1295179aa768cd693ca7c47a280ae9b7e1bf7c8f353
fetched_at: '2026-06-29T00:11:11.467063+00:00'
page_id: '64652705'
product: rm
source: tdn-rm
title: RMFIS00020_SPED Fiscal - Comparação do Livro CIAP com Bloco G
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=64652705
version: 13
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:** 11.52.x |
| **Processo** | **:** | Crédito ICMS sobre Ativo Permanente |
| **Subprocesso** | **:** | Comparação do Livro CIAP com Bloco G do Sped Fiscal |
| **Data da publicação** | **:** | 17/03/2014 |

**Introdução:**

Para as empresas que controlam o crédito do ICMS sobre bens adquiridos para o ativo permanente – **CIAP**, o sistema **TOTVS** de **Gestão** **Fiscal** oferece o controle automático, para isto é necessário realizar a parametrização abaixo:

* [Controle CIAP](https://tdn.totvs.com/pages/viewpage.action?pageId=307839761)

Caso o cliente esteja obrigado a entregar o Sped Fiscal, estas informações do Ativo Permanente são geradas no Bloco G:

**“BLOCO G – CONTROLE DO CRÉDITO DE ICMS DO ATIVO PERMANENTE CIAP”**

Antes de realizar a conferencia dos valores é necessário cadastrar alguns campos complementares no RM LIBER e/ou RM BONUN, para isto siga as instruções da FAQ abaixo:

* "Editar"

**Procedimentos:**

Para realizar a conferência das informações que são geradas no Livro do **CIAP** e no Bloco G do **Sped** **Fiscal** o cliente deve seguir o seguinte procedimento:

**Lançamento de entrada do BEM:**

No **TOTVS** **Gestão** **Fiscal** deve ser dada a entrada da Nota de compra de ativo com **CFOP** (Tipo de ICMS) compatível com a operação, no nosso caso estamos utilizando os seguintes dados:

• **CFOP**: 1.551.01

• **Código do Bem**: 01.01.229

• **Numero do Lançamento**: 111111

• **Data de inicio do Credito**: 01/01/2012

• **Valor do ICMS**: R$500,00

**Importante:**

 Veja que no Lançamento de entrada o valor do ICMS deve ser informado dentro da aba “Valores ICMS” dentro do ITEM. É com este valor que o sistema vai fazer o cálculo do CIAP para apropriação do Crédito.

Depois de realizada a entrada do BEM pelo lançamento de entrada e o cálculo do CIAP tiver sido feito podemos visualizar o relatório:

Gerando o SPED FISCAL para este mês 01/2012 temos o seguinte **bloco G:**

Referente ao Tipo de movimentação (campo complementar), o sistema faz uma regra para que seja gerado da seguinte forma:

As opções abaixo devem ser definidas / preenchidas no item do lançamento, na pasta Bens para o correto funcionamento da rotina.

**Tipo de movimentação do bem ou componente:**

**MC = Imobilização oriunda do Ativo Circulante;**  
**AT = Alienação ou Transferência;**  
**PE = Perecimento, Extravio ou Deterioração;**  
**OT = Outras Saídas do Imobilizado.**

As opções abaixo serão geradas de forma automática pela rotina do SPED :

**IM** = Imobilização de bem individual; (Entradas de bens no período de apuração que não possuem Bem Principal - Cadastro de bem campo "agregado" não preenchido)  
**IA** = Imobilização em Andamento - Componente; (Entrada de bens no período de apuração que possuem Bem Principal - Cadastro de bem campo "agregado" preenchido)  
**SI** = Saldo inicial de bens imobilizados  
**BA** = Baixa do Saldo de ICMS - Fim do período de apropriação

Regras :  
**SI** : Para os bens que entraram em período de apuração anterior ao período apuração do SPED e que não estão no período de baixa.

**BA**: Informar os bens baixados pelo fim do período de apropriação no ICMS no período apuração. Para esses bens, além do tipo de movimentação “BA” deve ser gerado, também, um registro com o tipo de  
movimentação “SI”. No BA, os campos “NUM\_PARC”, “VL\_PARC\_PASS” e “VL\_PARC\_APROP” não devem ser informados.

**Outras Informações:**

Caso o BEM, durante o seu período de crédito, tenha sido Vendido, transferido, extraviado ou etc, deve ser feito a Saída do BEM através do lançamento de saída com o BEM vinculado dentro do  
ITEM.

No teste acima foi feito a saída no mês 03/2012 com um tipo de movimentação **OT = Outras Saídas do Imobilizado.**

**• CFOP: 5.551.01**  
**• Código do Bem: 01.01.229**  
**• Numero do Lançamento: 666666**  
**• Data de inicio do Credito: 01/03/2012**  
**• Valor do ICMS: R$500,00**

Foi feito o cálculo do CIAP e depois gerado o relatório, onde será apresentado a saída deste bem com o valor do ICMS informado na aba **“Valores ICMS”:**

**• No relatório:**

**• No Sped Fiscal de 03/2012:**

**Duvidas frequente:**

**Pergunta: Porque o sistema tem que gerar dois registros G125?**

**Resposta**: Esta geração é uma regra do próprio SPED, veja o entendimento abaixo constante no Guia Pratico:

**Pergunta: Se o BEM não for sido vendido, transferido, extraviado ou etc , e a sua apropriação for realizada 100% dentro do sistema (gerado as 48 parcelas) como deve ser gerado a ultima parcela?**

**Resposta:** São gerados dois registros G125 da seguinte forma:

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.RegistrosSpedFiscal.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
