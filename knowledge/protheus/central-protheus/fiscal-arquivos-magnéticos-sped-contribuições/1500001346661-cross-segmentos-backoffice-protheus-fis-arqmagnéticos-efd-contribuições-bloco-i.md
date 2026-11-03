---
article_id: 1500001346661
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: f05481f464b87f7ab125945ff16bf6543553b761237117494860febb2e24b537
fetched_at: '2026-06-28T22:42:05.336860+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  Bloco I Como gerar os Registros  I100, I200, I300
type: support-article
updated_at: '2022-08-31T12:53:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001346661-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Bloco-I-Como-gerar-os-Registros-I100-I200-I300
---

**Dúvida**EFD Contribuições Bloco I Como gerar os Registros I100, I200, I300 pela Contabilidade.  
  
**Ambiente**Microsiga Protheus – Fiscal – A partir da versão 12.1.17  
  
**Solução**Para realizar a configuração do **BLOCO I**, pela contabilidade realize os seguintes passos;

1. Acesse o **configurador** e configure o parâmetro **MV\_INTBLCI** =4;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001343742/mceclip0.png)

2. Acesse o modulo da **Contabilidade Gerencial** e realize o cadastro do **calendário** **Contábil.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100242794/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100242854/mceclip2.png)

3. Realize o cadastro das **moedas contábeis;**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001406681/mceclip3.png)**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001406701/mceclip4.png)**

4. Realize a amarração, **moedas x calendários**;

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001344322/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001344482/mceclip6.png)

5. No **módulo contábil** realizar **lançamentos contábeis;**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001344722/mceclip7.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100243154/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100243194/mceclip9.png)

6. Para o cadastro do bloco I, é necessário importar os códigos de receitas e deduções, que são disponibilizados pela Receita Federal através de arquivo textos;

Para este procedimento precisamos importar os códigos de Receita da tabela **7.1.3**, e para as Deduções os códigos da tabela **7.1.4**. Importante lembrar que estas tabelas possuem diversos grupos em função do segmento do contribuinte, então qual os grupos que deverão ser importados dependerá da atividade exercida pelo contribuinte;

É importante lembrar que os arquivos baixados deverão ser renomeados conforme o padrão estabelecido, arquivos da tabela 7.1.3 devem ser renomeados para **TABELA713GRZZZ.TXT** e os arquivos da tabela 7.1.4 renomeados para **TABELA714GRZZZ.TXT,** onde ZZZ corresponde ao grupo da tabela, por exemplo:

Ao baixar arquivo da tabela 7.1.3 do grupo 100, o arquivo ficará com o nome **TABELA713GR100.TXT**, do grupo 200 **TABELA713GR200.TXT** e assim sucessivamente;

![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102418813/mceclip25.png)

7. Para realizar a importação basta acessar a rotina **Importação Códigos EFD,** e depois selecionar as opções **3-Rec Inst.Fin,** para importar o arquivo com códigos de **receita da tabela 7.1.3**, ou opção **4-Ded. Inst.Fin,** para importar o arquivo com códigos de **deduções da tabela 7.1.4**, conforme imagem abaixo;

![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001407901/mceclip24.png)

8- Acesse a opção Outras Ações, **importar TXT**;

![mceclip26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100244714/mceclip26.png)

9. Depois de importar o arquivo TXT. Acesse a rotina de **apuração da EFD Contribuições** e inclua os lançamentos do **bloco I;**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001345042/mceclip10.png)**

**![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001345122/mceclip11.png)**

Registro cadastrado.

**![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001407121/mceclip12.png)**

10. Realize a **integração** com **contábil;**

**![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001407161/mceclip13.png)**

**![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100243554/mceclip14.png)**

**![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102418133/mceclip15.png)**

**![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001345222/mceclip16.png)**

**![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102418193/mceclip17.png)**

11. Veja que os valores foram preenchidos conforme movimentação das **contas contábeis**;

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001407301/mceclip18.png)

12. Processar **apuração da EFD Contribuições;**

**![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100243654/mceclip19.png)**

**![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001407441/mceclip20.png)**

13. Gerar o arquivo **Efd Contribuições;**

**![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102418353/mceclip21.png)**

**![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001407461/mceclip22.png)**

14. Registro **bloco I** gerado com sucesso;

**![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001345482/mceclip23.png)**

Para geração do Bloco I, será necessário a gravação das tabelas abaixo:

CL5 – Bloco I Consolidado   
CL6 – Bloco I Detalhado   
CKT – Receita PIS/COF Não Tributada

**Documentação de apoio:**

<https://tdn.totvs.com/display/public/PROT/FIS0093_BLOCO_I_CONTABIL_EFD_CONTRIBUICOES>
