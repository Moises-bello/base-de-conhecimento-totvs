---
article_id: 5397675981719
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 4107709b061feaa10421b17b695fd53c0ce68fd6df900866b2b37130b1ac1f19
fetched_at: '2026-06-28T22:42:05.081287+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como gerar o Bloco I com Integração Contábil ?
type: support-article
updated_at: '2022-08-31T12:36:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5397675981719-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-gerar-o-Bloco-I-com-Integra%C3%A7%C3%A3o-Cont%C3%A1bil
---

**Dúvida**Como gerar  **Bloco I com integração contábil  EFD CONTRIBUÇÕES**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  - Todas as versões  
  
**Solução:**

**Passo 1.**  Efetue/ Realize a configuração do parâmetro **MV\_INTBLCI = 4**No configurador **(SIGACFG)** acesse: **Ambiente/ Cadastros/ Parâmetros** e verifique o parâmetro a seguir:  
  
**MV\_INTBLCI = 4****Descrição:**

Opção 4: O sistema utilizará somente os dados da contabilidade, não realizando integrações com nenhum outro modulo.

**Passo 2.** Efetue a importação dos códigos de receita para a **tabela 7.1.3**  e para as Deduções os códigos da **tabela 7.1.4.**

Para realizar importação basta acessar a rotina **Importação Códigos EFD**no menu lateral da Apuração da **EFD Contribuições**, e depois selecionar as opções **3-Rec Inst.Fin.** para importar o arquivo com códigos de receita da **tabela 7.1.3**, e/ou opção **4-Ded. Inst.Fin** para importar o arquivo com códigos de deduções da **tabela 7.1.4**.  
  
Segue o exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5397175052695/mceclip0.png)

**Obs:**  O arquivo dos códigos de receitas devem ser renomeados no formato padrão (**TABELA713GRZZZ.TXT/ TABELA714GRZZZ.TXT)**  ZZZ corresponde ao grupo da tabela.  
  
Exemplo: **TABELA713GR100.TXT**, do grupo 200 **TABELA713GR200.TXT**.  
  
**Passo 3.** Efetue um lançamento contábil no **Módulo 34** (**Contabilidade Gerencial**)

**Passo 4.** Cadastre a **Visão Gerencial** para amarrar a conta contábil informada no lançamento contábil afim de levar os valores no momento da integração

**Atenção:**

Não existe parâmetro para informar a **visão gerencial** na **Rotina FISA009** ou **FISA001**, as informações são levadas  de maneira automática quando é realizada a **integração contábil**.

Exemplo **Visão gerencial**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5397258336407/mceclip1.png)

**Passo 5.** Na rotina **FISA009**, preencha o campo da **conta contábil** informada na **visão gerencial** e os  campos abaixo:

* **CST**- Informe o **CST** de Receita. **CST's** permitidos: (**01, 02 ,03 ,04 ,05 ,06 ,07 ,08 ,09, 49 e 99**)
* **Período** - Informe  o período de apuração da **EFD Contribuições**, no formato MM/AAAA, onde MM corresponde ao mês e AAAA corresponde ao ano.
* **Alíquota de PIS** - Informe a alíquota de **PIS**, caso seja operação tributada
* **Alíquota de COFINS** - Informe  alíquota de **COFINS**, caso seja operação tributada
* **Tabela da Natureza de Receita** - Informe a natureza da receita quando houver receita não tributada, ao selecionar a tabela através da consulta padrão deste campo, automaticamente os campos  **Nat. Rec, Cod.Nat.Rec. Grp. Nat. Rec e Dt. Fim N.R.** serão preenchidos.

Os demais campos de valores do cabeçalho serão preenchidos automaticamente quando for realizada a integração com o **Módulo Contábil**, por este motivo estão desabilitados para edição. As informações desta seção correspondem ao **Registro I100**.

Após preenchimento do cabeçalho, deverá preencher os campos da seção **Cadastro Bloco I - Itens**

* **Tipo** - Neste campo devemos informar se o valor será **Receita** ou **Dedução**.
* **Bloco I** - Neste campo devemos selecionar o código de **Receita** ou **Dedução**, conforme especificado no campo **Tipo**. No caso de receita serão listados e validados os códigos da **Tabela 7.1.3**, se Dedução então serão listados e validados os códigos da **Tabela 7.1.4**.
* **Conta** - Aqui deverá ser informada a **conta contábil**, que será utilizada na geração dos **Registros I200 e I300**, e também para buscar os valores da **Visão Gerencial** no momento da **Integração Contábil.**
* **Compl** - Neste campo poderá ser informada uma descrição complementar, conforme necessidade.

O campo **Valor Reg**será preenchido automaticamente na integração com o **Módulo Contábil**, por este motivo está desabilitado para edição. As informações desta seção correspondem aos **Registros I200** e **I300**.

Segue o exemplo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5397300349975/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5397303221783/mceclip3.png)

Após isso realize a **Integração Contábil** através  das opções: **outras ações > integração contábil,** após a integração os sistema levará os valores na **Apuração**.  
  
**Passo 6.** Processe a **Apuração** com a pergunta **Instituição Financeira = SIM**

**Passo 7.** Gere o **Arquivo txt** com a pergunta **Atividade Preponderante = 3**, e a pergunta **Indicador Bloco I,** preenchida conforme classificação do contribuinte.

Importante ressaltar que o cadastro da estrutura do **Bloco I**, será feito manualmente, bem como o relacionamento com as **contas contábeis**, por isso é importante revisar o cadastro e movimentação contábil antes de processar a **Apuração** e gerar o **Arquivo texto**.
