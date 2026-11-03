---
article_id: 8366020475543
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 54d986218a05b680bd708cadfbaa4e4a425182252f5eb0853694b80aae9cfe8b
fetched_at: '2026-06-28T22:42:03.658537+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - SPEDFISCAL -
  Como gerar o campo 23 e 24 do registro C100 no arquivo txt?
type: support-article
updated_at: '2022-11-11T15:21:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8366020475543-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Como-gerar-o-campo-23-e-24-do-registro-C100-no-arquivo-txt
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:07:20** **min****Dúvida**Como gerar o **campo 23 e 24** do **Registro C100** no arquivo txt do **Sped Fiscal**?  
  
**Ambiente**TOTVS Backoffice (**Linha Protheus**) - A partir da versão **12.1.25**  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos, para calcular o **ICMS ST** configure conforme abaixo:   
  
1. Cadastro de Produto:

**Solid. Saída (B1\_PICMRET)** - informe o **MVA** do produto para saída;  
**Solid. Entr. (B1\_PICMENT)** - informe o **MVA** do produto para entrada.

2. Cadastro de Cliente:

**Tipo (A1\_TIPO)** = Este campo têm relação com o parâmetro **MV\_TPSOLCF**, onde são informados os **tipos de cliente/fornecedores** que possuem cálculo de **ICMS Solidário**.

3. Cadastro de TES:

**Mkp ICM Comp. (F4\_MKPCMP)** = Não;

**Marg. Solid. (F4\_MKPSOL)** = Configuração.

**Crd.ICMS ST (F4\_CREDST)** = Diferente de 04 (Documentação oficial referente a este ponto abaixo)

<https://tdn.totvs.com/pages/releaseview.action?pageId=354473133>

4. Parâmetros:

**MV\_TPSOLCF** - Indica quais os tipos de cliente devem ser considerados para cálculo do **ICMS-ST**. Lembrando que é realizado o vínculo com o campo **Tipo (A1\_TIPO)**.  
  
**MV\_MKPICPT** - Indica se há margem de lucro nas operações de venda para o consumidor final.  
  
Para operações **interestaduais**, verifique os parâmetros **MV\_STUFS, MV\_SUBTRIB** e **MV\_STUF** (Deve ser preenchido com a **UF**).

Verifique como está os parâmetros abaixo, é importante que eles estejam preenchidos para gerar o valor do **ICMS ST**:  
   
**MV\_STUF**=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO

**MV\_STUFS**=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO

**MV\_SUBTRIB** = preenchido com **estado + inscrição estadual** (todos os estados que possuírem inscrição estadual para recolhimento do **ICMS ST**

5. Verifique as pergunta da *Wizard:*

![pag1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8365847923479/pag1.png)

Documentação sobre o Credito ICMS ST:

<https://tdn.totvs.com/pages/releaseview.action?pageId=142812281>

Caso ainda não esteja apresentando o valor nos campos mencionados, favor informar no parâmetro **MV\_CFERES** com a **CFOP** utilizada no seu processo.

E dessa forma, será gerada com sucesso no arquivo txt com o campo 23 buscando o valor do campo **FT\_BASERET** e campo 24 buscando o conteúdo do campo **FT\_ICMSRET** pela tabela SFT, alimentando os outros registros filhos:

![pag2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8365879312407/pag2.png)
