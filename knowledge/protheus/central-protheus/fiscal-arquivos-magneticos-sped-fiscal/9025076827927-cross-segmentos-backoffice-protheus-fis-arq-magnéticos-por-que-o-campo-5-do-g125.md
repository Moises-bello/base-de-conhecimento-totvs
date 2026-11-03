---
article_id: 9025076827927
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e4acb553f769cee550ca3661a6b15eb6be516304dbee64b741c183b2d7ff03ea
fetched_at: '2026-06-28T22:42:00.980153+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Por que o campo
  5 do G125 gera com valor zerado no Sped Fiscal?
type: support-article
updated_at: '2022-09-21T11:07:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9025076827927-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Por-que-o-campo-5-do-G125-gera-com-valor-zerado-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:04:00 min**

**Dúvida**Por que o campo **5 do G125** gera zerado no **Sped Fiscal** gerando o erro de validação?

**Para os tipos de movimentação iguais a "SI", "IM", "IA", "CI" ou "MC", pelo menos um dos campos VL\_IMOB\_ICMS\_OP, VL\_IMOB\_ICMS\_ST, VL\_IMOB\_ICMS\_FRT ou VL\_IMOB\_ICMS\_DIF deve ser maior que Zero.**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – A partir da versão 12  
  
**Solução**

Para identificar o motivo pelo qual o campo **05 - VL\_IMOB\_ICMS\_OP** do registro **G125 - Movimentação do bem ou Componente** está sendo gerado com valor zerado é preciso realizar as verificações abaixo:

**1.** O fornecedor dos **CIAPs** que estão zerados **(campo F9\_FORNECE)** é optante pelo **Simples Nacional ?** Essa verificação pode ser feita na tabela **SA2 - Fornecedores**, campo **Opt Simp Nac - A2\_SIMPNAC**  
  
Se sim, (**campo Opt Simp Nac - A2\_SIMPNAC = 1)** existe a seguinte tratativa: Para os bens adquiridos de fornecedores **Optantes pelo Simples Naciona**l, os valores com o **Tipo de Movimentação  SI** saem zerados no **Bloco G**, pois quando há somente a incidência de **ICMS Próprio** na operação não há o direito  de apropriação deste credito.   
  
Abaixo, segue trecho da validação do código fonte quanto à este cenário:  
  
**Else nTotD1FT := IIf(SA2->A2\_SIMPNAC == '1' .And. SF9->F9\_VALICMS == SD1->D1\_ICMSCOM ,0,SD1->D1\_VALICM) //05-VL\_IMOB\_ICMS\_OP >**  
  
Dessa forma, quando a aquisição do bem for feita de um fornecedor **Optante pelo Simples Nacional**,  o no cadastro de **TES** utilizado para escriturar o documento fiscal o campo **L.FIS. CIAP -** **F4\_CIAP = "Não"**, pois dessa forma, não será gerado **CIAP** para o bem em questão.  
  
Caso, o campo **Simp Nac - A2\_SIMPNAC** tenha sido preenchido equivocadamente como 1, ou seja, se o fornecedor **não** for **Optante do Simples Nacional**, altere o campo para **Não** e gere novamente o **Sped Fiscal**

**2.** O bem em questão é referente a um complemento campo **D1\_TIPO = C?**

**3.** O campo **ICMS Próprio - F9\_VALICMP** está preenchido? Para gerar valor no campo **5 do registro G125** esse campo na tabela **SF9 - Manutenção CIAP** precisa estar devidamente preenchido com valor.   
  
Quando o parâmetro **MV\_F9SKPNF = F** e o campo **F9\_ROTINA = MATA103** esse campo é preenchido automaticamente, conforme valor de **ICMS** da **nota fiscal de entrada.**  
  
Quando o **CIAP** é inserido manualmente via rotina **Manutenção CIAP (MATA905**), o parâmetro **MV\_F9SKPNF** precisa estar configurado = **T** para que o campo **ICMS Próprio - F9\_VALICMP** seja habilitado para preenchimento.  
  
**4.** Verifique se o campo **F9\_SIMPNAC=1.** O campo em questão foi criado recentemente e tem a seguinte tratativa:

Quando criado o campo **F9\_SIMPNAC**, o mesmo será preenchido de forma automática na funcionalidade **Apropriar da rotina MATA906 - Estorno do CIAP**, conforme regras a seguir, executada na primeira apropriação realizada após criação do campo:

![](https://tdn.totvs.com/download/attachments/657538746/image2021-12-29_14-24-51.png?version=1&modificationDate=1640798692233&api=v2)

**A - Bem inserido através de Documento de Entrada:**  
O sistema irá buscar no **Documento de Entrada** correspondente a informação constante no campo **F1\_SIMPNAC**, para identificar se o Fornecedor na ocasião de lançamento do **Documento Fiscal de Entrada** estava configurado como **Simples Nacional (F1\_SIMPNAC = "1-Sim")**, preenchendo o campo **F9\_SIMPNAC = "1 - Sim**" caso **F1\_SIMPNAC = "1 - Sim"** ou caso contrário preencherá o campo **F9\_SIMPNAC = '2 - Não'**.  
  
**B - Caso não localize o Documento de Entrada** correspondente, geralmente inclusão direta na rotina **MATA905 - Manutenção do CIAP,** irá buscar a informação no campo **A2\_SIMPNAC** do **Cadastro de Fornecedor**, preenchendo o campo **F9\_SIMPNAC = "1 - Sim"** caso **A2\_SIMPNAC = "1 - Sim',** caso contrário preencherá o campo **F9\_SIMPNAC = '2 - Não'**.

Importante: É muito importante e extrema atenção quando o bem foi incluído pela **Tabela de Manutenção CIAP**, inclusão pelo **Ativo Fixo** ou **Integração entre sistemas.**

Para estes casos o sistema irá considerar a informação do campo **A2\_SIMPNAC** do **Cadastro do Fornecedor,** e isto não quer dizer que quando foi realizada a aquisição do bem esta informação era daquele momento.

Por este motivo, será possível a alteração do campo **F9\_SIMPNAC** diretamente através da rotina **MATA905 - Manutenção do CIAP.**

Dessa forma, caso o fornecedor não seja de fato **optante pelo simples nacional**, altere o conteúdo do campo **F9\_SIMPNAC de 1 para 2**,  e realize novo teste.
