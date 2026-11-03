---
article_id: 360020228691
category: NFe - Nota Fiscal Eletrônica
content_hash: 15d09bf5fd07c4d57435cdad0b951db65c642502a7d60ed00c7e849654bc3410
fetched_at: '2026-06-28T22:40:05.243060+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 694 Rejeição :
  Não informado o grupo de ICMS para a UF de destino'
type: support-article
updated_at: '2025-06-11T12:22:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020228691-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-694-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-grupo-de-ICMS-para-a-UF-de-destino
---

**Dúvida**

Como corrigir a rejeição abaixo:

694 Rejeição : Não informado o grupo de ICMS para a UF de destino

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

 Ao fazer nota de **operação interestadual, para consumidor final e não contribuinte** a Sefaz espera que seja gerado o grupo no XML **ICMSUFDest.**

* **Conforme o exemplo abaixo o grupo deve gerar e deve estar preenchido ao menos pICMSInter e pICMSInterPart :**

<ICMSUFDest>

<vBCUFDest>0</vBCUFDest>

<pFCPUFDest>0</pFCPUFDest>

<pICMSUFDest>0</pICMSUFDest>

<pICMSInter>12.00</pICMSInter> - **conteúdo do campo SD2\_PICM**

<pICMSInterPart>20.0000</pICMSInterPart> - **conforme parâmetro MV\_PPDIFAL**

<vFCPUFDest>0</vFCPUFDest>

<vICMSUFDest>0</vICMSUFDest>

<vICMSUFRemet>0</vICMSUFRemet>

</ICMSUFDest>

1.  Preencher no TES o campo **Calcula ICMS "F4\_ICM" = S - Sim**

![CALCU_ICMS_SIM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495559791895)

2. **Preencher no TES** o campo **Calc.Dif.ICM** (F4\_COMPL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495559802391)

3. Para isso **preencher no TES** o campo **Calc.Difal** (F4\_DIFAL) = SIM

![CALCU_DIF_ICM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495559808535)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar****MV\_PPDIFAL**={{2016,40,60},{2017,60,40},{2018,80,20},{2019,100,0},{2020,100,0},{2021,100,0},{2022,100,0},{2023,100,0},{2024,100,0}}

![MV_PPDIFAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495559816471)

5. Após isso, exclua a nota e gere novamente.

6. Preencher como consumidor final, altere **no pedido de vendas** o campo **C5\_TIPOCLI  "Tipo Cliente"****F  -  Cons. Final**

![CONSUMIDOR_FINAL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495523133719)

7. Após isso, exclua a nota e gere novamente.

8. Caso seja **Contribuinte o destinatário** preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![Ins._Estad..gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495559826967)​

9. Preencha o campo Destaca IE **"A1\_IENCONT"**   em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495523143831)

10. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495523148311)

11. Após isso, exclua a nota e gere novamente.

12. Caso seja I**sento o destinatário** deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

​![inscr_ISENTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495559836439)

13. Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![destaca_IE_em_branco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495523143831)

14. Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![contrib_sim.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495523148311)

15. Após isso, exclua a nota e gere novamente.

***Exceção 6:*** A regra de validação acima não se aplica nas operações com combustíveis (tag:comb) derivados de petróleo: código ANP diferente de:  
820101001, 820101010, 810102001, 810102004, 810102002, 810102003,  
810101002, 810101001, 810101003, 220101003, 220101004, 220101002,  
220101001, 220101005, 220101006, 560101001.

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495523154711)

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

**![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495523154711)**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

**![MV_COMBUST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495523160727)**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**![COMP._COMBUSTIVEL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495559859095)**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS**

**. CDD\_IFCOMP**

Existe a possibilidade do preenchimento automático dos campos da CD6 para isso usar o ponto de entrada MATUCOMP.

Existe a possibilidade do campo CDD\_IFCOMP ser preenchido automaticamente. Para isso é necessário ativar o parâmetro MV\_ATUCOMP e usar o ponto de entrada MATUCOMP, abaixo documentação:   
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=642645988>

***Exceção 7:*** A regra de validação acima não se aplica se informada UF do local de entrega (tag: entrega/UF) igual à UF do emitente (tag: emit/enderEmit/UF).

***Exceção 8:*** A regra de validação acima não se aplica para as operações com  
CFOP de Remessa de Mercadoria (Tabela CFOP, indRemes=1).  
Exceção 9: A regra de validação acima não se aplica para os CFOP:  
- 6.552 - Transferência de bem do ativo imobilizado;  
- 6.922 - Lançamento efetuado a título de simples faturamento decorrente de  
venda p/ entrega futura;  
- 6.929 - Lançamento relativo a Cupom Fiscal.

***Exceção 10:*** Esta regra de validação não se aplica nas operações isentas ***(CST=40-Isenta ou CSOSN=103-Isento), imunes ou não tributadas (CST=41- Não tributada, ou CSOSN=300-Imune, ou CSOSN=400-Não tributada pelo Simples Nacional).***

***Exceção 11:*** A regra de validação acima não se aplica nas ***NF-e complementares (finNFe=2) nem nas de ajuste (finNFe=3).***

***Exceção 12:*** A regra de validação acima não se aplica para emitentes optantes  
pelo Simples Nacional (CRT=1).

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar **MV\_CODREG**

1 - Simples Nacional;

![MV_CODREG.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17495523171479)

* **Saiba mais:**

**O conteúdo das TAGS serão retirados dos campos:**

* Grupo ICMSUFDEST x Campos CD2:

Tag **vBCUFDest** -> **CD2\_BC**

Tag **pFCPUFDest** -> **CD2\_PFCP**

Tag **pICMSUFDest** -> **CD2\_ALIQ**

Tag **pICMSInter** -> **CD2\_ADIF**

Tag **pICMSInterPart** -> **CD2\_PDDES**

Tag **vFCPUFDest** -> **CD2\_VFCP**

Tag **vICMSUFDest** -> **CD2\_VDDES**

Tag **vICMSUFRemet** -> **CD2\_VLTRIB**

* **Validação da Sefaz:**

![694_REJEI__O.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/12263969493527)
