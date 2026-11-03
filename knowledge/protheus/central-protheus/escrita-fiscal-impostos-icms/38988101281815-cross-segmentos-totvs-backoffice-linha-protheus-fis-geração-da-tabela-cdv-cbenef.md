---
article_id: 38988101281815
category: Escrita Fiscal - Impostos - ICMS
content_hash: 9a9da71918316e82ddedd6cec54cf8afca21a9be17c59dda8f2ef2ff7bf24b7e
fetched_at: '2026-06-28T22:39:25.931593+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Geração da tabela
  CDV "cBenef" para alimentar a tag cBenef para o estado do SP
type: support-article
updated_at: '2026-03-27T19:30:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38988101281815-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-da-tabela-CDV-cBenef-para-alimentar-a-tag-cBenef-para-o-estado-do-SP
---

**Dúvida**  
Geração da tabela CDV "cBenef" para alimentar a tag cBenef para o estado do SP  
  
**Ambiente**  
Protheus a partir 12.1.33  
  
**Solução**

O tratamento da tag cbenef para o estado de SP devera seguir orientação abaixo:

A TAG **cBenef é** validada pela **UF do emitente**, sendo assim para **UF de transmissão de nota**

Para gerar a tabela **CDV** realize os seguintes passos:

1. Configure os parâmetros;

* **MV\_ESTADO = SP**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988101265047)

* **MV\_GIAEFD = F**

![](https://totvssuporte.zendesk.com/attachments/token/IyfXFYRoPtEAKNiI1rFhSLgdk/?name=image.png)  
  
2. No site  <https://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>  ainda não foi disponibilizado para o estado de SP a tabela 5.2.

Com isso, nesse momento ainda não é possível importar a tabela via compatibilizador U\_IMPSPED, pois o próprio Fisco ainda não disponibilizou o arquivo para download.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988101265815)

Porém, é possível cadastrar os códigos manualmente na rotina FISA156 - Códigos de Valores Declaratórios.

Primeiro deverá acessar o portal da fazenda de SP e baixar a Tabela CST x cBenef - Excel.  
<https://portal.fazenda.sp.gov.br/servicos/nfe/Paginas/cBenef.aspx>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988101268119)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988113238167)

Acesse a rotina FISA156 - - Códigos de Valores Declaratórios e realize a configuração manualmente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988113239063)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988113239831)

Obs: Preencher o campo **Data Inicio** com uma data por exemplo, inicio do mês/ano**.**  
  
**Após concluir será gravado os códigos na sua tabela CDY**

Para fazer amarração na rotina "Itens X Cod.val.declaratórios" (FISA140)

Agora deve acessar a rotina FISA140

3. Criar a **amarração** na rotina **FISA140 - Prod. x Cod.V.Decl.;**

**Informar:**

* Produto
* CFOP da operação a ser aplicado aquele código
* Cod. Val. Decl (Tabela 5.2 da receita federal)
* CST
* Código de Reflexo conforme a sua necessidade

Exemplo:

**Vídeo didático no canal How To da Totvs no Youtube:** [*https://www.youtube.com/watch?v=WOUvZLBvRUU*](https://www.youtube.com/watch?v=WOUvZLBvRUU)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988101270679)

Após concluir, ir no MATA410 Pedido de venda e realizar inclusão do pedido de venda.

Depois que colocar o cliente, produto, quantidade e valor unitário e total, coloque a tes devidamente configurada e ir em Outras ações, Planilha, Aba lançamento de apuração e clicar em valor declaratório.

Neste momento vai aparecer as informações para tag cbenef

![Exibindo image.png](https://chat.google.com/api/get_attachment_url?url_type=FIFE_URL&content_type=image%2Fpng&attachment_token=AOo0EEVQzxbtfBFDVECjxvjornVn3irr79BSxBWk5Xtwe2hzvv%2By4AYPK3s6l7uhfUwFU3fdLf51DcxGLzPOetgM0S8fxAsPEO4AX5rSdEkDWpZnc3nikhQQwlGJiOpiVY2RUN2daAsedJ2sw41hLDcRCYhJm8UwFTuRrYSRES1xcYHznuskPWq8PNYHU3fTaSS5wveSpp5ydBtNt7guSZfJaqe%2F%2BkE59yfbLc0gqpo75WKz06DKirLX0FsBHU2hfsAu9ud7V3e7Cyrqa7F4ecU2Ct52TFqKCeqdh024abyN1fWWQoA%2BdQyNX2fuHAmevrWyIgKxw8EpqMX3gxVrowhMqcznUb%2FhduJY0EQw2e8cf8SLs%2BZ8DnqCO8kDuxiK5GYNt%2FVp4ASWb%2B%2FNRelwcJ09g7K9Xc%2BAdp%2F7mrp%2ByAaYbZjRWert0q4Qf0wFRh9A%2BBI9poxa8LLLhldtcy2oBZv5e1UjAEJ4YvRA2PfuACafRTo4gsTyUbUIYXWe6ATJP7YW2RotxOX2sO3dqknJMqCJH05%2BirYwMM8tTtcV%2B3abMYLA0s%2BpS5zHh3Pp2ER2tI3sWHvtQ7q5ChRFzWs67JaAlQ%3D%3D&allow_caching=true&sz=w1919-h877-rw&auditContext=forDisplay)

**ATENÇÃO**

Somente será gravada a tabela CDV após emissão da nota fiscal.

É desta tabela que a montagem do XML vai buscar para gerar a tabela para gerar a tag cBenef

## **Caso a tes esteja como:**

Calcula ICMS=Não e o Livro de ICMS estiver como OUTROS ou ISENTO, o código reflexo deve estar desta forma:

**Vídeo didático no canal How To da Totvs no Youtube:**

[*https://www.youtube.com/watch?v=1NGqosady-4&t=9s*](https://www.youtube.com/watch?v=1NGqosady-4&t=9s)

[*https://www.youtube.com/watch?v=\_frSFU\_mm2A&t=26s*](https://www.youtube.com/watch?v=_frSFU_mm2A&t=26s)

* Para Calcula ICMS= Não e Livro de ICMS = ISENTO

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38988101272599)

* Para Calcula ICMS= Não e Livro de ICMS = OUTROS

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38988101273495)

**Nos casos de redução de base de ICMS como fazer a amarração do código de reflexo:**

Documentação para configurar a redução de base do ICMS:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342473--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Redu%C3%A7%C3%A3o-de-Base-de-C%C3%A1lculo-de-ICMS>

Cadastro TES:

Calc. ICMS (F4\_ICM) = S

%Red.do ICMS (F4\_BASEICM) "TES" ou %Red.do ICMS (F7\_BASEICM) "Exceção fiscal" = Informe o valor a ser calculado do ICMS próprio. No padrão, este valor é apresentado na coluna Tributada do Livro Fiscal.

Livro Fiscal ICMS (F4\_LFICM) = ISENTO/ OUTROS. Selecione uma das opções para informar onde será destacado o restante da operação Valor total da NF menos percentual informado no campo F4\_BASEICM.

Material de Consumo (F4\_CONSUMO)=NÃO

Exemplo:

%Red.do ICMS (F4\_BASEICM) ou %Red.do ICMS (F7\_BASEICM)= 60;

Livro Fiscal ICMS (F4\_LFICM) = ISENTO

Material de Consumo (F4\_CONSUMO) = NÃO

O valor do ICMS será dividido entre as colunas Tributado(60%) e Isento(40%)

%Red.do ICMS (F4\_BASEICM) ou %Red.do ICMS (F7\_BASEICM)= 60;

Livro Fiscal ICMS (F4\_LFICM) = OUTROS

Material de Consumo (F4\_CONSUMO) = NÃO

O valor do ICMS será dividido entre as colunas Tributado(60%) e Outros(40%)

**Vídeo didático no canal How To da Totvs no Youtube:**[*https://www.youtube.com/watch?v=J\_2XSvhVe5I*](https://www.youtube.com/watch?v=J_2XSvhVe5I)

O código de reflexo deixe desta forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988113243671)

**Nos casos de ICMS Diferido**

Diferimento

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418030442775-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Diferimento-de-ICMS?source=search>

**Vídeo didático no canal How To da Totvs no Youtube:**[*https://www.youtube.com/watch?v=0rYNnvJTgCc*](https://www.youtube.com/watch?v=0rYNnvJTgCc)

Deixe seu código de reflexo desta forma:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988113244439)

**DICA**

Existe uma forma de tratar a FISA140 em vez de código de produto, poderá tratar via grupo de tributação.

Para tratar por grupo de tributação existe o parametro MV\_MTCLF3K

* MV\_MTCLF3K= 0 tratará por código de produto
* MV\_MTCLF3K= 1 tratará por grupo de tributação

Segue documentação:

<https://tdn.totvs.com/pages/releaseview.action?pageId=520651465>

**Exemplo:**

Se seu produto tem o grupo tributário amarrado como 001

E seu cliente o grupo tributário estiver em branco

A regra da FISA140 deve ter somente o grupo de produto informado = 001 e grupo de cliente em branco

Agora se seu produto tem o grupo tributário amarrado como 001

E seu cliente o grupo tributário estiver AAA

A regra da FISA140 deve ter somente o grupo de produto informado = 001 e grupo de cliente= AAA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38988113244823)

**IMPORTANTE:**

Se a informação estiver gerada CDV e mesmo assim não gera as informações no XML ou causando rejeição de transmissão,  **orientamos abrir um chamado com a equipe do TSS (nota fiscal eletrônica) para auxiliar.**
