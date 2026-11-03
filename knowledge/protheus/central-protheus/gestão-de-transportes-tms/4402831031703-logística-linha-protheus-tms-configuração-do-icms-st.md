---
article_id: 4402831031703
category: Gestão de Transportes (TMS)
content_hash: fc5c4c212e163f03076945951058a8157a2772396313f2d5df7f98aa988577fb
fetched_at: '2026-06-28T22:45:27.565168+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Configuração do ICMS ST
type: support-article
updated_at: '2026-03-20T16:50:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402831031703-Log%C3%ADstica-Linha-Protheus-TMS-Configura%C3%A7%C3%A3o-do-ICMS-ST
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26020275834903)*** Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como configurar o cálculo do **ICMS** de Substituição Tributária no **CT-e** do tipo normal ou no **CT-e** complementar de imposto?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
A **Substituição Tributária** é quando a responsabilidade pelo **ICMS** devido em relação às operações ou prestações de serviços é atribuída à outro contribuinte.  
  
Para que um **CT-e** do tipo **normal** seja gerado com **ICMS** **ST**, configure conforme abaixo:  
  
**1. Cadastro** **Cliente:**  
1.1. Acesse **Atualizações / Cadastro / Clientes - MATA030.**  
1.2. Na aba **Cadastrais**, campo **Tipo** **- A1\_TIPO:** o conteúdo deste campo esta associado ao parâmetro **MV\_TPSOLCF** onde são informados os tipos de cliente/fornecedores que possuem cálculo de **ICMS** **Solidário**. E, para que o calculo do **ICMS ST** seja realizado, é imprescindível que o campo **Tipo - A1\_TIPO** do cliente tomador de serviço esteja como **Solidário.**  
  
Parâmetro: **MV\_TPSOLCF -** Indica quais os tipos de cliente devem ser considerados para cálculo do **ICMS ST**. Lembrando que é realizado o vínculo com o campo **Tipo - A1\_TIPO.**  
  
**2. Produto de Cálculo:**  
2.1. Acesse **Atualizações / Cadastro / Produtos - MATA010.**  
2.2. Na aba **Impostos**, informar um percentual fictício de 0,01 no campo **Solid. Saída - B1\_PICMRET** apenas para possibilitar o calculo do **ICMS ST**.  
  
**3. Cadastro TES**  
3.1. Acesse **Atualizações / Cadastro / Tipos de Entrada e Saída - MATA080.**  
3.2. Informar os seguintes campos:  
  
Na aba **Adm/fin/custo:**  
**Crd. ICMS ST - F4\_CREDST** = **2 - Retido ST**  
  
Na aba **Impostos**:  
**Calcula ICMS - F4\_ICM = N - Não**  
**L. FISC. ICMS - F4\_LFICM = O - Outros**  
**Agrega Valor - F4\_AGREG = I - ICMS+Merc**  
**Agrega Solid - F4\_INCSOL = D - Deduz Retido**  
**Sit. Trib. ICM - F4\_SITTRIB = 60**  
**Mkp ICM Comp - F4\_MKPCMP = 2 - Não**  
**ICMS s/ST - F4\_ICMSST = 1 - Sim**  
**LF ICMS-ST - F4\_LFICMST = Não**  
**Marg. Solid.  - F4\_MKPSOL = 1 - Nunca**  
  
Referente à seleção dos valores de impostos para a geração do **XML** do **CT-e** é necessário verificar os seguintes parâmetros:

* **MV\_CTEVPRE** - Determina qual valor será utilizado na *tag* **Total da Prestação** **<vTPRest>**, onde:
  + **.T.** = Valor sem impostos **-** **DT6\_VALFRE;**
  + **.F.** = Valor com impostos **- DT6\_VALTOT**.
* **MV\_CTEVFRE -** Determina valor a ser utilizado do componente de frete na *tag* **<vComp>**, onde:
  + **.T.** = Valor sem Imposto - **DT8\_VALPAS**;
  + **.F.** = Valor com Imposto - **DT8\_VALTOT**;

Na impressão da **DACTE**, a *tag* **<vTPRest>** é apresentada no campo **Valor Total da Prestação do Serviço**, e a tag **<vComp>** é apresentada no campo **Valor do componente**.  
  
Para que um **CT-e complementar de imposto** seja gerado com **ICMS ST**, configure conforme abaixo:  
  
1. No Cadastro de **Tipos de Entrada e Saída - MATA080** e configure os seguintes campos:

Na aba **Adm/fin/custo:**  
**Crd. ICMS ST - F4\_CREDST = 2 - Retido ST**

Na aba**Impostos:**  
**Credita ICMS - F4\_CREDICM = N - Não**  
**Calcula ICMS - F4\_ICM = N - Não**  
**L. FISC. ICMS - F4\_LFICM = Z - ICMS Zerado**  
**Agrega Valor - F4\_AGREG = S - Sim**  
**Agrega Solid - F4\_INCSOL = N - Não**  
**Sit. Trib. ICM - F4\_SITTRIB = 60**  
**Mkp ICM Comp - F4\_MKPCMP = 2 - Não**  
**ICMS s/ST - F4\_ICMSST = 1 - Sim**  
**LF ICMS-ST - F4\_LFICMST = Não**  
**Marg. Solid.  - F4\_MKPSOL = 1 - Nunca**  
**Fórmula - F4\_FORMULA** = Amarrar uma fórmula com conteúdo texto = "Complemento" para que o Sistema não destaque o **ICMS** normal nos livros, apenas o **ICMS** retido.  
  
Caso o **CT-e** seja gerado com a alíquota de **ICMS** incorreta, então, será necessário validar os seguintes parâmetros:

* **MV\_ALIQICM** - Define as alíquotas de **ICMS** que podem serutilizadas pelo Sistema;
* **MV\_NORTE** - Relação de UFs pertencentes as regiões norte e nordeste que trabalham com operações interestaduais aplicando alíquota do **ICMS** em 7%;
* **MV\_FRETEST** - Define as alíquotas internas de **ICMS** de cada estado a serem utilizadas na geração do Conhecimento de frete;
* **MV\_ICMPAD** - Define a alíquota de **ICMS** aplicada em operações de transporte dentro do estado de onde a transportadora está localizada fisicamente;
* **MV\_ESTICM** - Define as alíquotas internas para os estados destinos para o cálculo do **Difal**, cálculo do **ICMS ST** e cálculo do diferencial de alíquota. Exemplo de Preenchimento: **MV\_ESTICM** = SP18;
* **MV\_ESTADO** - Sigla do estado de onde a transportadora está localizada fisicamente para efeito de cálculo de **ICMS** - 7, 12 ou 18%.

**Glossário**  
**CT-e** - Conhecimento de Transporte Eletrônico  
**COFINS** - Contribuição para o Financiamento da Seguridade Social  
**DACTE** - Documento Auxiliar do Conhecimento de Transporte Eletrônico  
**ICMS**- Imposto sobre Circulação de Mercadorias e Serviços  
**PIS** - Programa de Integração Social  
**ST** - Substituição Tributária  
**TES** - Tipos de Entrada e Saída  
**XML** - Extensible Markup Language  
  
**Saiba mais:**  
Para criar uma fórmula com o conteúdo texto, acesse - [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Inclusão de Fórmula para exibir na Mensagem na Nota Fiscal de Saída.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037464333-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Inclus%C3%A3o-de-F%C3%B3rmula-para-exibir-na-Mensagem-na-Nota-Fiscal-de-Sa%C3%ADda?source=search)  
Para deduzir o **ICMS ST** da base de cálculo do **PIS** e **COFINS,** acesse - [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Dedução do ICMS ST da base do PIS e COFINS.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026414952-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Dedu%C3%A7%C3%A3o-do-ICMS-ST-da-base-do-PIS-e-COFINS)  
Parametrização do **ICMS ST** via **Configurador de Tributos** - [CFGTRIB - ICMS-ST - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/releaseview.action?pageId=899211761) e [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular o ICMS ST?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17802352397591-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-ICMS-ST)  
Vídeo de capacitação do **ICMS ST** via **Configurador de Tributos** - [How To | MP - SIGAFIS - ICMS ST - Configurador de tributos](https://www.youtube.com/watch?v=bkRZBP3YhIQ)
